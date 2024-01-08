#!/usr/bin/env python3
"""
Defines unit tests for the client module
"""
import unittest
from unittest.mock import Mock, patch, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
org_payload, repos_payload, expected_repos, apache2_repos = TEST_PAYLOAD[0]


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

    # TODO: implement this - task 6
    # @patch('utils.requests.get')
    # def test_public_repos(self, mock_get):
    #     """
    #     unit-test GithubOrgClient.public_repos method
    #     """
    #     github_client = GithubOrgClient('google')
    #     payload1 = {
    #         'repos_url': 'https://api.github.com/orgs/google/repos'
    #     }
    #     payload = [
    #         {'name': 'repo1'}
    #         ]
    #     mock_get.return_value.json.return_value = payload

    #     with patch('client.GithubOrgClient._public_repos_url',
    #                new_callable=PropertyMock) as mock__public_repos_url:
    #         mock__public_repos_url.return_value = payload1['repos_url']

    #         self.assertEqual(github_client._public_repos_url,
    #                          payload1['repos_url'])
    #         mock__public_repos_url.assert_called_once()

    #     repos = github_client.public_repos()
    #     self.assertEqual(repos, [])
    #     mock_get.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        unit-test GithubOrgClient.has_license method
        """
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


@parameterized_class(('org', 'repos', 'expected_repos', 'apache2_repos'), [
    (org_payload, repos_payload, expected_repos, apache2_repos)
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    test the GithubOrgClient.public_repos method in an integration test
    """
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get', side_effect=cls.get_payload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    @staticmethod
    def get_payload(url):
        """
        returns mock data
        """
        data = {
            'https://api.github.com/orgs/google': org_payload,
            'https://api.github.com/orgs/google/repos': repos_payload,
        }
        if url in data:
            return MagicMock(json=lambda: data[url])

    def test_public_repos(self):
        """
        test the GithubOrgClient.public_repos method in an integration test
        """
        github_client = GithubOrgClient('google')

        result = github_client.public_repos()
        self.assertEqual(result, expected_repos)

    def test_public_repos_with_license(self):
        """
        test the public_repos with the argument license="apache-2.0"
        """
        github_client = GithubOrgClient('google')
        result = github_client.public_repos(license="apache-2.0")
        self.assertEqual(result, apache2_repos)


if __name__ == "__main__":
    unittest.main()
