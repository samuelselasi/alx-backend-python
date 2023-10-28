#!/usr/bin/env python3
"""Module containing  unit test for utils package"""
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """Class that defines attributes to test functions"""

    @parameterized.expand([({"a": 1}, ("a",), 1), ({"a": {
        "b": 2}}, ("a",), {"b": 2}), ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, res):
        """Method to test that access_nested_map returns the right result"""

        self.assertEqual(access_nested_map(nested_map, path), res)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self,  nested_map, path):
        """Method to test that access_nested_map handles errors correctly"""

        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(err.exception.args[0], path[-1])
