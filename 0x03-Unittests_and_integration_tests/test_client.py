#!/usr/bin/env python3
"""Module containing  unit test for client package"""
from unittest import TestCase
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch
from unittest.mock import PropertyMock
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError
from parameterized import parameterized_class


class TestGithubOrgClient(TestCase):
    """"Class that defines attributes to test client.GithubOrgClient class"""

    @parameterized.expand([("google"), ("abc")])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock):
        """Method to test if GithubOrgClient.org returns the correct value"""

        client = GithubOrgClient(org_name)
        res = client.org

        self.assertEqual(res, mock.return_value)
        mock.assert_called_once

    def test_public_repos_url(self):
        """Method to test GithubOrgClient._public_repos_url function"""

        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock,
                          return_value={"repos_url": "Test value"}
                          ) as mock:
            test_json = {"repos_url": "Test value"}
            client = GithubOrgClient(test_json.get("repos_url"))
            res = client._public_repos_url

            self.assertEqual(res, mock.return_value.get("repos_url"))
            mock.assert_called_once

    @patch("client.get_json", return_value=[{"name": "Test value"}])
    def test_public_repos(self, mock):
        """Method to test GithubOrgClient.public_rep function"""

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/"
                          ) as pub:
            client = GithubOrgClient("Test value")
            res = client.public_repos()

            self.assertEqual(res, ["Test value"])
            mock.assert_called_once
            pub.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)])
    def test_has_license(self, repo, license_key, ret):
        """Method to test GithubOrgClient.has_license function"""

        client = GithubOrgClient("Test value")
        res = client.has_license(repo, license_key)
        self.assertEqual(ret, res)


@parameterized_class(("org_payload", "repos_payload", "expected_repos",
                     "apache2_repos"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(TestCase):
    """Class that defines attributes to test client.GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Method to prepare test fixture"""

        cls.get_patcher = patch('requests.get', side_effect=HTTPError)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Method called after test method has been called"""

        cls.get_patcher.stop()

    def test_public_repos(self):
        """Method to test GithubOrgClient.public_repos function"""

        res = GithubOrgClient("Test value")
        self.assertTrue(res)
