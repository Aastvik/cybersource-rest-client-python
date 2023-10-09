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


class KeyManagementApi(object):
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



    def search_keys(self, **kwargs):
        """
        Search Keys
        Search one or more Keys
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search_keys(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: This allows you to specify the page offset from the resulting list resultset you want the records to be returned
        :param int limit: This allows you to specify the total number of records to be returned off the resulting list resultset
        :param str sort: This allows you to specify a comma separated list of fields in the order which the resulting list resultset must be sorted.
        :param list[str] organization_ids: List of Orgaization Ids to search. The maximum size of the organization Ids list is 1. The maximum length of Organization Id is 30.
        :param list[str] key_ids: List of Key Ids to search. The maximum size of the Key Ids list is 1
        :param list[str] key_types: Key Type, Possible values -  certificate, password, pgp and scmp_api. When Key Type is provided atleast one more filter needs to be provided
        :param datetime expiration_start_date: Expiry Filter Start Date. When Expiration Date filter is provided, atleast one more filter needs to be provided
        :param datetime expiration_end_date: Expiry Filter End Date. When Expiration Date filter is provided, atleast one more filter needs to be provided
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `search_keys` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.search_keys_with_http_info(**kwargs)
        else:
            (data) = self.search_keys_with_http_info(**kwargs)
            return data

    def search_keys_with_http_info(self, **kwargs):
        """
        Search Keys
        Search one or more Keys
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search_keys_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: This allows you to specify the page offset from the resulting list resultset you want the records to be returned
        :param int limit: This allows you to specify the total number of records to be returned off the resulting list resultset
        :param str sort: This allows you to specify a comma separated list of fields in the order which the resulting list resultset must be sorted.
        :param list[str] organization_ids: List of Orgaization Ids to search. The maximum size of the organization Ids list is 1. The maximum length of Organization Id is 30.
        :param list[str] key_ids: List of Key Ids to search. The maximum size of the Key Ids list is 1
        :param list[str] key_types: Key Type, Possible values -  certificate, password, pgp and scmp_api. When Key Type is provided atleast one more filter needs to be provided
        :param datetime expiration_start_date: Expiry Filter Start Date. When Expiration Date filter is provided, atleast one more filter needs to be provided
        :param datetime expiration_end_date: Expiry Filter End Date. When Expiration Date filter is provided, atleast one more filter needs to be provided
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'sort', 'organization_ids', 'key_ids', 'key_types', 'expiration_start_date', 'expiration_end_date']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_keys" % key
                )
            params[key] = val
        del params['kwargs']

        if 'expiration_start_date' in params and not re.search('yyyy-mm-dd', params['expiration_start_date']):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `expiration_start_date` when calling `search_keys`, must conform to the pattern `/yyyy-mm-dd/`")
            raise ValueError("Invalid value for parameter `expiration_start_date` when calling `search_keys`, must conform to the pattern `/yyyy-mm-dd/`")
        if 'expiration_end_date' in params and not re.search('yyyy-mm-dd', params['expiration_end_date']):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `expiration_end_date` when calling `search_keys`, must conform to the pattern `/yyyy-mm-dd/`")
            raise ValueError("Invalid value for parameter `expiration_end_date` when calling `search_keys`, must conform to the pattern `/yyyy-mm-dd/`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
        if 'organization_ids' in params:
            query_params.append(('organizationIds', params['organization_ids']))
            collection_formats['organizationIds'] = 'csv'
        if 'key_ids' in params:
            query_params.append(('keyIds', params['key_ids']))
            collection_formats['keyIds'] = 'csv'
        if 'key_types' in params:
            query_params.append(('keyTypes', params['key_types']))
            collection_formats['keyTypes'] = 'csv'
        if 'expiration_start_date' in params:
            query_params.append(('expirationStartDate', params['expiration_start_date']))
        if 'expiration_end_date' in params:
            query_params.append(('expirationEndDate', params['expiration_end_date']))

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

        return self.api_client.call_api(f'/kms/v2/keys', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse2001',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
