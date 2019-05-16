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
from CyberSource.apis.credit_api import CreditApi


class TestCreditApi(unittest.TestCase):
    """ CreditApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.credit_api.CreditApi()

    def tearDown(self):
        pass

    def test_create_credit(self):
        """
        Test case for create_credit

        Process a Credit
        """
        pass


if __name__ == '__main__':
    unittest.main()
