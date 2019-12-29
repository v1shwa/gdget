from subprocess import PIPE, Popen as popen
import unittest
import os.path


class TestGdGet(unittest.TestCase):
    def get_command_output(self, command):
        p = popen(command, stdout=PIPE, stderr=PIPE)
        p.wait()
        (_out, err) = p.communicate()
        return err

    def test_by_id(self):
        output = self.get_command_output(["gdget", "1sOlEsawO0_YwM4KjKHX_sLB8vijMpcP0"])
        self.assertTrue("blur.txt" in str(output) and os.path.isfile("blur.txt"))

    def test_by_url_1(self):
        output = self.get_command_output(
            [
                "gdget",
                "https://drive.google.com/file/d/1sOlEsawO0_YwM4KjKHX_sLB8vijMpcP0/view?usp=sharing",
            ]
        )
        self.assertTrue("blur.txt" in str(output) and os.path.isfile("blur.txt"))

    def test_by_url_2(self):
        output = self.get_command_output(
            [
                "gdget",
                "https://drive.google.com/uc?id=1sOlEsawO0_YwM4KjKHX_sLB8vijMpcP0&export=download",
            ]
        )
        self.assertTrue("blur.txt" in str(output) and os.path.isfile("blur.txt"))

    def test_by_url_3(self):
        output = self.get_command_output(
            [
                "gdget",
                "https://drive.google.com/uc?export=download&confirm=gege&id=1sOlEsawO0_YwM4KjKHX_sLB8vijMpcP0",
            ]
        )
        self.assertTrue("blur.txt" in str(output) and os.path.isfile("blur.txt"))

    def test_output_flag(self):
        output = self.get_command_output(
            [
                "gdget",
                "https://drive.google.com/file/d/1sOlEsawO0_YwM4KjKHX_sLB8vijMpcP0/view?usp=sharing",
                "-O",
                "testing_output_flag.txt",
            ]
        )
        self.assertTrue(
            "testing_output_flag.txt" in str(output)
            and os.path.isfile("testing_output_flag.txt")
        )

    def test_invalid_doc(self):
        output = self.get_command_output(
            [
                "gdget",
                "https://drive.google.com/file/d/0BwNnXVsA1pABbDB6LTQwU3l5NW8/view?usp=sharing",
            ]
        )
        self.assertTrue("Unable to download" in str(output))

    def test_invalid_url(self):
        output = self.get_command_output(["gdget", "https://google.com"])
        self.assertTrue("Not a valid Google drive link" in str(output))


if __name__ == "__main__":
    unittest.main()
