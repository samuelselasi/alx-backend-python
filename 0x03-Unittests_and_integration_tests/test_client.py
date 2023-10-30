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
from unittest.mock import Mock


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


@parameterized_class([{"org_payload": TEST_PAYLOAD[0][0],
                       "repos_payload": TEST_PAYLOAD[0][1],
                       "expected_repos": TEST_PAYLOAD[0][2],
                       "apache2_repos": TEST_PAYLOAD[0][3]}])
class TestIntegrationGithubOrgClient(TestCase):
    """Class that defines attributes to test client.GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Method to prepare test fixture"""

        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload}

        def get_payload(url):
            """Function that handles urls"""

            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self):
        """Method to test GithubOrgClient.public_repos function"""

        self.assertEqual(GithubOrgClient("google").public_repos(),
                         self.expected_repos)

    @classmethod
    def tearDownClass(cls):
        """Method called after test method has been called"""

        cls.get_patcher.stop()
