#!/usr/bin/env python3
"""Module containing  unit test for client package"""
from unittest import TestCase
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch
from unittest.mock import PropertyMock


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
