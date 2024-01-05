#!/usr/bin/env python3
"""
Defines unit tests for the utils module
"""
from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
import os
from utils import access_nested_map, get_json, memoize


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


class TestMemoize(unittest.TestCase):
    """
    unit tests class for the utlis.memoize function/decorator
    """
    def test_memoize(self):
        """
        tests that utils.memoize works correctly
        """
        class TestClass:
            """
            test class that makes use of the memoize decorator
            """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42
            test_class = TestClass()
            case_1 = test_class.a_property
            case_2 = test_class.a_property

            mock_a_method.assert_called_once()
            self.assertEqual(case_1, 42)
            self.assertEqual(case_2, 42)


if __name__ == '__main__':
    unittest.main()
