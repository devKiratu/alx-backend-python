#!/usr/bin/env python3
"""
Defines unit tests for the client module
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    unittests for the GithubOrgClient class
    """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_org(self, org_name):
        """
        tests that GithubOrgClient.org returns the correct value
        """
        with patch('utils.requests.get') as mock_get:
            github_client = GithubOrgClient(org_name)
            url = github_client.ORG_URL.format(org=org_name)

            github_client.org()

            mock_get.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()
