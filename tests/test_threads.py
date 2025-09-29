import unittest

from nexgenomics import threads

class TestThreads(unittest.TestCase):

    def test_ping(self):
        p = threads.ping()
        self.assertEqual (p["api"], "v0")
        self.assertEqual (p["host"], "nexgenomics.ai")

    def test_new(self):
        p = threads.new(title="AbCdE")
        print (p)



