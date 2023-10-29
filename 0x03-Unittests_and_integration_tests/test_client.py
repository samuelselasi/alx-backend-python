#!/usr/bin/env python3
"""Module containing  unit test for client package"""
from unittest import TestCase
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch


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
