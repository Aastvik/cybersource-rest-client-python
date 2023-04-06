# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import CyberSource
from CyberSource.rest import ApiException
from CyberSource.apis.subscriptions_api import SubscriptionsApi


class TestSubscriptionsApi(unittest.TestCase):
    """ SubscriptionsApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.subscriptions_api.SubscriptionsApi()

    def tearDown(self):
        pass

    def test_activate_subscription(self):
        """
        Test case for activate_subscription

        Activate a Subscription
        """
        pass

    def test_cancel_subscription(self):
        """
        Test case for cancel_subscription

        Cancel a Subscription
        """
        pass

    def test_create_subscription(self):
        """
        Test case for create_subscription

        Create a Subscription
        """
        pass

    def test_get_all_subscriptions(self):
        """
        Test case for get_all_subscriptions

        Get a List of Subscriptions
        """
        pass

    def test_get_subscription(self):
        """
        Test case for get_subscription

        Get a Subscription
        """
        pass

    def test_get_subscription_code(self):
        """
        Test case for get_subscription_code

        Get a Subscription Code
        """
        pass

    def test_suspend_subscription(self):
        """
        Test case for suspend_subscription

        Suspend a Subscription
        """
        pass

    def test_update_subscription(self):
        """
        Test case for update_subscription

        Update a Subscription
        """
        pass


if __name__ == '__main__':
    unittest.main()
