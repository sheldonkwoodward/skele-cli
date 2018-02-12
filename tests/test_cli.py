from subprocess import PIPE, Popen as popen
from unittest import TestCase

from skele import __version__ as version


class TestHelp(TestCase):
    def test_returns_usage_information(self):
        output = popen(['skele', '-h'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)

        output = popen(['skele', '--help'], stdout=PIPE).communicate()[0]
        self.assertTrue('Usage:' in output)


class TestVersion(TestCase):
    def test_returns_version_information(self):
        output = popen(['skele', '--version'], stdout=PIPE).communicate()[0]
        self.assertEqual(output.strip(), version)
