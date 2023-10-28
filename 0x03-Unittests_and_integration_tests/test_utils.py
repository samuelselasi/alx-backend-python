#!/usr/bin/env python3
"""Module containing  unit test for utils package"""
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from unittest.mock import patch
from utils import memoize


class TestAccessNestedMap(TestCase):
    """Class that defines attributes to test utils.access_nested_map func"""

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


class TestGetJson(TestCase):
    """Class that defines attributes to test utils.get_json function"""

    @parameterized.expand([("http://example.com", {
        "payload": True}), ("http://holberton.io", {"payload": False})])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock):
        """Method to test that utils.get_json returns the expected result"""

        mock.return_value = test_payload
        res = get_json(test_url)
        self.assertEqual(res, test_payload)


class TestMemoize(TestCase):
    """Class that defines attributes to test utils.memoize function"""

    def test_memoize(self):
        """Method that using test memorize to check if func is called twice"""

        class TestClass:
            """Class that defines attributes to test memoize"""

            def a_method(self):
                """Method that returns an instance of memoize class"""

                return 42

            @memoize
            def a_property(self):
                """Method that defines a property instance of memoize"""

                return self.a_method()

        with patch.object(TestClass, "a_method") as mock:
            test = TestClass()
            test.a_property
            test.a_property
            mock.assert_called_once
