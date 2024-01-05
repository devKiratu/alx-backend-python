#!/usr/bin/env python3
"""
Defines unit tests for the utils module
"""
from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    unit tests for the method utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        tests access_nested_map method behaves as expected
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        tests whether the method access_nested_map raises KeyError exceptions
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    unit tests class for the utils.get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        test that utils.get_json returns the expected result
        """
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload

            response = get_json(test_url)
            self.assertDictEqual(response, test_payload)
            mock_get.assert_called_once_with(test_url)


if __name__ == '__main__':
    unittest.main()
