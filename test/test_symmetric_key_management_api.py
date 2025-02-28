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
from CyberSource.apis.symmetric_key_management_api import SymmetricKeyManagementApi


class TestSymmetricKeyManagementApi(unittest.TestCase):
    """ SymmetricKeyManagementApi unit test stubs """

    def setUp(self):
        self.api = CyberSource.apis.symmetric_key_management_api.SymmetricKeyManagementApi()

    def tearDown(self):
        pass

    def test_create_v2_shared_secret_keys(self):
        """
        Test case for create_v2_shared_secret_keys

        Create Shared-Secret Keys
        """
        pass

    def test_create_v2_shared_secret_keys_verifi(self):
        """
        Test case for create_v2_shared_secret_keys_verifi

        Create Shared-Secret Keys as per verifi spec
        """
        pass

    def test_delete_bulk_symmetric_keys(self):
        """
        Test case for delete_bulk_symmetric_keys

        Delete one or more Symmetric keys
        """
        pass

    def test_get_key_details(self):
        """
        Test case for get_key_details

        Retrieves shared secret key details
        """
        pass


if __name__ == '__main__':
    unittest.main()
