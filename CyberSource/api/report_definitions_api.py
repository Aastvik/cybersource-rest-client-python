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


class ReportDefinitionsApi(object):
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



    def get_resource_info_by_report_definition(self, report_definition_name, **kwargs):
        """
        Get Report Definition
        View the attributes of an individual report type. For a list of values for reportDefinitionName, see the [Reporting Developer Guide](https://www.cybersource.com/developers/documentation/reporting_and_reconciliation/) 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_resource_info_by_report_definition(report_definition_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str report_definition_name: Name of the Report definition to retrieve (required)
        :param str subscription_type: The subscription type for which report definition is required. By default the type will be CUSTOM. Valid Values: - CLASSIC - CUSTOM - STANDARD 
        :param str report_mime_type: The format for which the report definition is required. By default the value will be CSV. Valid Values: - application/xml - text/csv 
        :param str organization_id: Valid Organization Id
        :return: ReportingV3ReportDefinitionsNameGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_resource_info_by_report_definition` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_resource_info_by_report_definition_with_http_info(report_definition_name, **kwargs)
        else:
            (data) = self.get_resource_info_by_report_definition_with_http_info(report_definition_name, **kwargs)
            return data

    def get_resource_info_by_report_definition_with_http_info(self, report_definition_name, **kwargs):
        """
        Get Report Definition
        View the attributes of an individual report type. For a list of values for reportDefinitionName, see the [Reporting Developer Guide](https://www.cybersource.com/developers/documentation/reporting_and_reconciliation/) 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_resource_info_by_report_definition_with_http_info(report_definition_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str report_definition_name: Name of the Report definition to retrieve (required)
        :param str subscription_type: The subscription type for which report definition is required. By default the type will be CUSTOM. Valid Values: - CLASSIC - CUSTOM - STANDARD 
        :param str report_mime_type: The format for which the report definition is required. By default the value will be CSV. Valid Values: - application/xml - text/csv 
        :param str organization_id: Valid Organization Id
        :return: ReportingV3ReportDefinitionsNameGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['report_definition_name', 'subscription_type', 'report_mime_type', 'organization_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resource_info_by_report_definition" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'report_definition_name' is set
        if ('report_definition_name' not in params) or (params['report_definition_name'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `report_definition_name` when calling `get_resource_info_by_report_definition`")
            raise ValueError("Missing the required parameter `report_definition_name` when calling `get_resource_info_by_report_definition`")

        if 'organization_id' in params and len(params['organization_id']) > 32:
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `organization_id` when calling `get_resource_info_by_report_definition`, length must be less than or equal to `32`")
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_resource_info_by_report_definition`, length must be less than or equal to `32`")
        if 'organization_id' in params and len(params['organization_id']) < 1:
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `organization_id` when calling `get_resource_info_by_report_definition`, length must be greater than or equal to `1`")
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_resource_info_by_report_definition`, length must be greater than or equal to `1`")
        if 'organization_id' in params and not re.search('[a-zA-Z0-9-_]+', params['organization_id']):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `organization_id` when calling `get_resource_info_by_report_definition`, must conform to the pattern `/[a-zA-Z0-9-_]+/`")
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_resource_info_by_report_definition`, must conform to the pattern `/[a-zA-Z0-9-_]+/`")

        collection_formats = {}

        path_params = {}
        if 'report_definition_name' in params:
            path_params['reportDefinitionName'] = params['report_definition_name']
            reportDefinitionName=report_definition_name

        query_params = []
        if 'subscription_type' in params:
            query_params.append(('subscriptionType', params['subscription_type']))
        if 'report_mime_type' in params:
            query_params.append(('reportMimeType', params['report_mime_type']))
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'GET' in ('POST'):
            body_params = '{}'
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/reporting/v3/report-definitions/{reportDefinitionName}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ReportingV3ReportDefinitionsNameGet200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_resource_v2_info(self, **kwargs):
        """
        Get Reporting Resource Information
        View a list of supported reports and their attributes before subscribing to them. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_resource_v2_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str subscription_type: Valid Values: - CLASSIC - CUSTOM - STANDARD 
        :param str organization_id: Valid Organization Id
        :return: ReportingV3ReportDefinitionsGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_resource_v2_info` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_resource_v2_info_with_http_info(**kwargs)
        else:
            (data) = self.get_resource_v2_info_with_http_info(**kwargs)
            return data

    def get_resource_v2_info_with_http_info(self, **kwargs):
        """
        Get Reporting Resource Information
        View a list of supported reports and their attributes before subscribing to them. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_resource_v2_info_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str subscription_type: Valid Values: - CLASSIC - CUSTOM - STANDARD 
        :param str organization_id: Valid Organization Id
        :return: ReportingV3ReportDefinitionsGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_type', 'organization_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_resource_v2_info" % key
                )
            params[key] = val
        del params['kwargs']

        if 'organization_id' in params and len(params['organization_id']) > 32:
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `organization_id` when calling `get_resource_v2_info`, length must be less than or equal to `32`")
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_resource_v2_info`, length must be less than or equal to `32`")
        if 'organization_id' in params and len(params['organization_id']) < 1:
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `organization_id` when calling `get_resource_v2_info`, length must be greater than or equal to `1`")
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_resource_v2_info`, length must be greater than or equal to `1`")
        if 'organization_id' in params and not re.search('[a-zA-Z0-9-_]+', params['organization_id']):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `organization_id` when calling `get_resource_v2_info`, must conform to the pattern `/[a-zA-Z0-9-_]+/`")
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_resource_v2_info`, must conform to the pattern `/[a-zA-Z0-9-_]+/`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'subscription_type' in params:
            query_params.append(('subscriptionType', params['subscription_type']))
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'GET' in ('POST'):
            body_params = '{}'
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/reporting/v3/report-definitions', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ReportingV3ReportDefinitionsGet200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
