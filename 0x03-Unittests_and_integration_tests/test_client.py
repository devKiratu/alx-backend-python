#!/usr/bin/env python3
"""
Defines unit tests for the client module
"""
import unittest
from unittest.mock import Mock, patch, PropertyMock
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

    @parameterized.expand([('google')])
    def test_public_repos_url(self, org_name):
        """
        unit-test GithubOrgClient._public_repos_url method
        """
        with patch('utils.requests.get') as mock_get:
            github_client = GithubOrgClient(org_name)
            payload = {
                'repos_url': 'https://api.github.com/orgs/google/repos'
            }
            mock_get.return_value.json.return_value = payload

            self.assertEqual(github_client._public_repos_url,
                             payload['repos_url'])


if __name__ == "__main__":
    unittest.main()
