# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient
import CyberSource.logging.log_factory as LogFactory

from ..utilities.tracking.sdk_tracker import SdkTracker
class SymmetricKeyManagementApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """
	
    def __init__(self, merchant_config, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client
        self.api_client.set_configuration(merchant_config)
        self.logger = LogFactory.setup_logger(self.__class__.__name__, self.api_client.mconfig.log_config)



    def create_v2_shared_secret_keys(self, create_shared_secret_keys_request, **kwargs):
        """
        Create Shared-Secret Keys
        Create one or more Shared-Secret Keys 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_v2_shared_secret_keys(create_shared_secret_keys_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateSharedSecretKeysRequest create_shared_secret_keys_request: (required)
        :return: KmsV2KeysSymPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `create_v2_shared_secret_keys` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_v2_shared_secret_keys_with_http_info(create_shared_secret_keys_request, **kwargs)
        else:
            (data) = self.create_v2_shared_secret_keys_with_http_info(create_shared_secret_keys_request, **kwargs)
            return data

    def create_v2_shared_secret_keys_with_http_info(self, create_shared_secret_keys_request, **kwargs):
        """
        Create Shared-Secret Keys
        Create one or more Shared-Secret Keys 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_v2_shared_secret_keys_with_http_info(create_shared_secret_keys_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateSharedSecretKeysRequest create_shared_secret_keys_request: (required)
        :return: KmsV2KeysSymPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_shared_secret_keys_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_v2_shared_secret_keys" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_shared_secret_keys_request' is set
        if ('create_shared_secret_keys_request' not in params) or (params['create_shared_secret_keys_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `create_shared_secret_keys_request` when calling `create_v2_shared_secret_keys`")
            raise ValueError("Missing the required parameter `create_shared_secret_keys_request` when calling `create_v2_shared_secret_keys`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_shared_secret_keys_request' in params:
            body_params = params['create_shared_secret_keys_request']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'create_shared_secret_keys_request', self.api_client.mconfig.run_environment)
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/kms/v2/keys-sym', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='KmsV2KeysSymPost201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def create_v2_shared_secret_keys_verifi(self, v_ic_domain, create_shared_secret_keys_verifi_request, **kwargs):
        """
        Create Shared-Secret Keys as per verifi spec
        Create one or more Shared-Secret Keys as per Verifi spec with 32 chars, store digest algo during key generation. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_v2_shared_secret_keys_verifi(v_ic_domain, create_shared_secret_keys_verifi_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str v_ic_domain: domain (required)
        :param CreateSharedSecretKeysVerifiRequest create_shared_secret_keys_verifi_request: (required)
        :return: KmsV2KeysSymPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `create_v2_shared_secret_keys_verifi` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_v2_shared_secret_keys_verifi_with_http_info(v_ic_domain, create_shared_secret_keys_verifi_request, **kwargs)
        else:
            (data) = self.create_v2_shared_secret_keys_verifi_with_http_info(v_ic_domain, create_shared_secret_keys_verifi_request, **kwargs)
            return data

    def create_v2_shared_secret_keys_verifi_with_http_info(self, v_ic_domain, create_shared_secret_keys_verifi_request, **kwargs):
        """
        Create Shared-Secret Keys as per verifi spec
        Create one or more Shared-Secret Keys as per Verifi spec with 32 chars, store digest algo during key generation. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_v2_shared_secret_keys_verifi_with_http_info(v_ic_domain, create_shared_secret_keys_verifi_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str v_ic_domain: domain (required)
        :param CreateSharedSecretKeysVerifiRequest create_shared_secret_keys_verifi_request: (required)
        :return: KmsV2KeysSymPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['v_ic_domain', 'create_shared_secret_keys_verifi_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_v2_shared_secret_keys_verifi" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'v_ic_domain' is set
        if ('v_ic_domain' not in params) or (params['v_ic_domain'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `v_ic_domain` when calling `create_v2_shared_secret_keys_verifi`")
            raise ValueError("Missing the required parameter `v_ic_domain` when calling `create_v2_shared_secret_keys_verifi`")
        # verify the required parameter 'create_shared_secret_keys_verifi_request' is set
        if ('create_shared_secret_keys_verifi_request' not in params) or (params['create_shared_secret_keys_verifi_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `create_shared_secret_keys_verifi_request` when calling `create_v2_shared_secret_keys_verifi`")
            raise ValueError("Missing the required parameter `create_shared_secret_keys_verifi_request` when calling `create_v2_shared_secret_keys_verifi`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'v_ic_domain' in params:
            header_params['v-ic-domain'] = params['v_ic_domain']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_shared_secret_keys_verifi_request' in params:
            body_params = params['create_shared_secret_keys_verifi_request']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'create_shared_secret_keys_verifi_request', self.api_client.mconfig.run_environment)
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/kms/v2/keys-sym/verifi', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='KmsV2KeysSymPost201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_bulk_symmetric_keys(self, delete_bulk_symmetric_keys_request, **kwargs):
        """
        Delete one or more Symmetric keys
        'Delete one or more Symmetric keys' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_bulk_symmetric_keys(delete_bulk_symmetric_keys_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DeleteBulkSymmetricKeysRequest delete_bulk_symmetric_keys_request: (required)
        :return: KmsV2KeysSymDeletesPost200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `delete_bulk_symmetric_keys` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_bulk_symmetric_keys_with_http_info(delete_bulk_symmetric_keys_request, **kwargs)
        else:
            (data) = self.delete_bulk_symmetric_keys_with_http_info(delete_bulk_symmetric_keys_request, **kwargs)
            return data

    def delete_bulk_symmetric_keys_with_http_info(self, delete_bulk_symmetric_keys_request, **kwargs):
        """
        Delete one or more Symmetric keys
        'Delete one or more Symmetric keys' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_bulk_symmetric_keys_with_http_info(delete_bulk_symmetric_keys_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DeleteBulkSymmetricKeysRequest delete_bulk_symmetric_keys_request: (required)
        :return: KmsV2KeysSymDeletesPost200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['delete_bulk_symmetric_keys_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_bulk_symmetric_keys" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'delete_bulk_symmetric_keys_request' is set
        if ('delete_bulk_symmetric_keys_request' not in params) or (params['delete_bulk_symmetric_keys_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `delete_bulk_symmetric_keys_request` when calling `delete_bulk_symmetric_keys`")
            raise ValueError("Missing the required parameter `delete_bulk_symmetric_keys_request` when calling `delete_bulk_symmetric_keys`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'delete_bulk_symmetric_keys_request' in params:
            body_params = params['delete_bulk_symmetric_keys_request']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'delete_bulk_symmetric_keys_request', self.api_client.mconfig.run_environment)
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/kms/v2/keys-sym/deletes', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='KmsV2KeysSymDeletesPost200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_key_details(self, key_id, **kwargs):
        """
        Retrieves shared secret key details
        Retrieves keys details by providing the key id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_key_details(key_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str key_id: Key ID.  (required)
        :return: KmsV2KeysSymGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_key_details` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_key_details_with_http_info(key_id, **kwargs)
        else:
            (data) = self.get_key_details_with_http_info(key_id, **kwargs)
            return data

    def get_key_details_with_http_info(self, key_id, **kwargs):
        """
        Retrieves shared secret key details
        Retrieves keys details by providing the key id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_key_details_with_http_info(key_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str key_id: Key ID.  (required)
        :return: KmsV2KeysSymGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['key_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_key_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'key_id' is set
        if ('key_id' not in params) or (params['key_id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `key_id` when calling `get_key_details`")
            raise ValueError("Missing the required parameter `key_id` when calling `get_key_details`")


        collection_formats = {}

        path_params = {}
        if 'key_id' in params:
            path_params['keyId'] = params['key_id']
            keyId=key_id

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'GET' in ('POST'):
            body_params = '{}'
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/kms/v2/keys-sym/{keyId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='KmsV2KeysSymGet200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
