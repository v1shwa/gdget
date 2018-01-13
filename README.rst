GdGet
=====

A simple command line utility to download Google Drive public URLs
effortlessly.

Installation
~~~~~~~~~~~~

.. code:: bash

    pip install gdget

Usage
~~~~~

-  Download using google drive url

.. code:: bash

    gdget https://drive.google.com/file/d/1rcZ42siSqpLlVx2LRR_xjD7uJA8twKEa/view

-  Download using Google drive ID

.. code:: bash

    gdget 1rcZ42siSqpLlVx2LRR_xjD7uJA8twKEa

Requirements
~~~~~~~~~~~~

-  Python >=2.6 & >=3.4 (does not support 3.3)
-  requests
-  tqdm
-  pytest (optional, to run tests)

License
~~~~~~~

`The MIT License`_

.. _The MIT License: ./LICENSE