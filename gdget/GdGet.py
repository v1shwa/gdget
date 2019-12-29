#!/usr/bin/env python
# -*- coding: utf8 -*-

import cgi
import sys
import re
from tqdm import tqdm
import requests


class GdError(Exception):
    """Raised When the Google drive is invalid 
    or  non-downloadable ( native gdrive format like doc, sheet etc.)
    """


class GdGet:
    """Class to download Google drive Links"""

    def __init__(self, options):
        self.options = options
        self.session = requests.Session()

    def _save_to_file(self, response, filename):
        """Save content of <Requests> object to file

        Arguments:
            response {requests.models.Response} -- Requests to stream data to file
            filename {string} -- filename to save to

        Returns:
            string -- filename if success
        """
        total_size = int(response.headers.get("content-length", 0))
        pbar = tqdm(
            initial=0,
            total=total_size,
            unit="B",
            unit_scale=True,
            desc=filename,
            disable=self.options.quiet,
        )
        with open(filename, "wb") as file_handler:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file_handler.write(chunk)
                    pbar.update(1024)
        return filename

    def parse_drive_url(self, url):
        """Parses Google Drive link & return URL ID

        Arguments:
            url {string} -- Google Drive url or ID

        Returns:
            string -- URL ID

        Raises:
            GdError -- If the google drive link is not valid/parse-able.
        """
        if url.startswith("http") and "drive.google.com" not in url:
            raise GdError("Not a valid Google drive link. Please check the url & try again.")

        try:
            if "id=" in url:
                url_id = re.search(r"id=([^&]*)", url).group(1)
            elif "file/d" in url:
                url_id = re.search(r"file/d/([^/]*)", url).group(1)
            else:
                # defaults to thinking url_id as url
                url_id = url
        except AttributeError:
            raise GdError(
                "Couldn't parse the given google drive link. Please try it in the browser & enter the final url you see in the address bar post all redirects."
            )

        return url_id

    def _parse_file_name(self, header):
        """Parse <Requests> headers for file.

        If user specified a custom filename, that will be returned instead
        of parsing the header.

        Arguments:
            header {dict} -- Content-dispositon header

        Returns:
            str -- Filename
        """
        if self.options.output_document:
            return self.options.output_document
        _, params = cgi.parse_header(header)
        return params["filename"]

    def _confirm_download(self, url_id):
        # Get confirmation key from cookies
        cookies = requests.utils.dict_from_cookiejar(self.session.cookies)
        try:
            conf_key = next(
                val for key, val in cookies.items() if key.startswith("download_warning_")
            )
        except StopIteration:
            raise GdError(
                "Unable to download. Native google drive files such as docs, ppts etc. can't be downloaded."
            )
        # stream the data instead of loading everything onto RAM
        url = "https://docs.google.com/uc?export=download&confirm=%s&id=%s" % (
            conf_key,
            url_id,
        )
        response = self.session.get(url, stream=True)
        return self._save_to_file(response, self._parse_file_name(response.headers["Content-Disposition"]))

    def download(self, url_id):
        response = self.session.get("https://docs.google.com/uc?export=download&id=%s" % url_id)
        # small text-based files are available on single call
        try:
            title = self._save_to_file(
                response, self._parse_file_name(response.headers["Content-Disposition"])
            )
        except KeyError:
            # need confirmation for other files
            title = self._confirm_download(url_id)
        return title

    def run(self):
        if self.options.URL is None:
            sys.exit("GdGet: Missing Google Drive URL/ID")

        try:
            url_id = self.parse_drive_url(self.options.URL)
            if not self.options.quiet:
                sys.stdout.write("Connecting to https://drive.google.com/file/%s\n" % url_id)
            title = self.download(url_id)
        except GdError as e:
            sys.exit("GdGet: [ERROR] " + str(e))

        return title
