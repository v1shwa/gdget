
from subprocess import PIPE, Popen as popen
import unittest
import os.path
import warnings

class TestGdGet(unittest.TestCase):
    def setUp(self):
        try:
            warnings.simplefilter("ignore", ResourceWarning)
        except NameError:
            pass

    def test_by_id(self):
        output = popen(['gdget', '1sOlEsawO0_YwM4KjKHX_sLB8vijMpcP0'], stdout=PIPE, stderr=PIPE).stderr.read()
        self.assertTrue('blur.txt' in str(output) and os.path.isfile('blur.txt'))

    def test_by_url_1(self):
        output = popen(['gdget', 'https://drive.google.com/file/d/1sOlEsawO0_YwM4KjKHX_sLB8vijMpcP0/view?usp=sharing'], stdout=PIPE, stderr=PIPE).stderr.read()
        self.assertTrue('blur.txt' in str(output) and os.path.isfile('blur.txt'))

    def test_by_url_2(self):
        output = popen(['gdget', 'https://drive.google.com/uc?id=1sOlEsawO0_YwM4KjKHX_sLB8vijMpcP0&export=download'], stdout=PIPE, stderr=PIPE).stderr.read()
        self.assertTrue('blur.txt' in str(output) and os.path.isfile('blur.txt'))

    def test_by_url_3(self):
        output = popen(['gdget', 'https://drive.google.com/uc?export=download&confirm=gege&id=1sOlEsawO0_YwM4KjKHX_sLB8vijMpcP0'], stdout=PIPE, stderr=PIPE).stderr.read()
        self.assertTrue('blur.txt' in str(output) and os.path.isfile('blur.txt'))

    def test_output_flag(self):
        output = popen(['gdget', 'https://drive.google.com/file/d/1sOlEsawO0_YwM4KjKHX_sLB8vijMpcP0/view?usp=sharing','-O','testing_output_flag.txt'], stdout=PIPE, stderr=PIPE).stderr.read()
        self.assertTrue('testing_output_flag.txt' in str(output) and os.path.isfile('testing_output_flag.txt'))

    def test_invalid_doc(self):
        output = popen(['gdget', 'https://drive.google.com/file/d/0BwNnXVsA1pABbDB6LTQwU3l5NW8/view?usp=sharing'], stdout=PIPE, stderr=PIPE).stderr.read()
        self.assertTrue('Unable to download' in str(output))

    def test_invalid_url(self):
        output = popen(['gdget', 'https://google.com'], stdout=PIPE, stderr=PIPE).stderr.read()
        self.assertTrue('Not a valid Google drive link' in str(output))

if __name__ == '__main__':
    unittest.main()