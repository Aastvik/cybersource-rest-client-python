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
class TaxesApi(object):
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



    def calculate_tax(self, tax_request, **kwargs):
        """
        Calculate Taxes
        The tax calculation service provides real-time sales tax and VAT calculations for orders placed with your business worldwide.  It enhances your ability to conduct business globally and enables you to avoid the risk and complexity of managing online tax calculation.  The service supports product-based tax rules and exemptions for goods and services.  The tax rates are updated twice a month and calculations include sub-level detail (rates per taxing jurisdiction, names and types of jurisdictions). Implementation guidance, list of supported countries, and information on tax reporting are in the [Tax User Guide](https://developer.cybersource.com/docs/cybs/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-overview.html). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.calculate_tax(tax_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TaxRequest tax_request: (required)
        :return: VasV2PaymentsPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `calculate_tax` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.calculate_tax_with_http_info(tax_request, **kwargs)
        else:
            (data) = self.calculate_tax_with_http_info(tax_request, **kwargs)
            return data

    def calculate_tax_with_http_info(self, tax_request, **kwargs):
        """
        Calculate Taxes
        The tax calculation service provides real-time sales tax and VAT calculations for orders placed with your business worldwide.  It enhances your ability to conduct business globally and enables you to avoid the risk and complexity of managing online tax calculation.  The service supports product-based tax rules and exemptions for goods and services.  The tax rates are updated twice a month and calculations include sub-level detail (rates per taxing jurisdiction, names and types of jurisdictions). Implementation guidance, list of supported countries, and information on tax reporting are in the [Tax User Guide](https://developer.cybersource.com/docs/cybs/en-us/tax-calculation/developer/all/rest/tax-calculation/tax-overview.html). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.calculate_tax_with_http_info(tax_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TaxRequest tax_request: (required)
        :return: VasV2PaymentsPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tax_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method calculate_tax" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tax_request' is set
        if ('tax_request' not in params) or (params['tax_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `tax_request` when calling `calculate_tax`")
            raise ValueError("Missing the required parameter `tax_request` when calling `calculate_tax`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tax_request' in params:
            body_params = params['tax_request']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'tax_request', self.api_client.mconfig.run_environment)
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/vas/v2/tax', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='VasV2PaymentsPost201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def void_tax(self, void_tax_request, id, **kwargs):
        """
        Void Taxes
        Pass the Tax Request ID in the PATCH request to void the committed tax calculation.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.void_tax(void_tax_request, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VoidTaxRequest void_tax_request: (required)
        :param str id: The tax ID returned from a previous request. (required)
        :return: VasV2TaxVoid200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `void_tax` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.void_tax_with_http_info(void_tax_request, id, **kwargs)
        else:
            (data) = self.void_tax_with_http_info(void_tax_request, id, **kwargs)
            return data

    def void_tax_with_http_info(self, void_tax_request, id, **kwargs):
        """
        Void Taxes
        Pass the Tax Request ID in the PATCH request to void the committed tax calculation.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.void_tax_with_http_info(void_tax_request, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param VoidTaxRequest void_tax_request: (required)
        :param str id: The tax ID returned from a previous request. (required)
        :return: VasV2TaxVoid200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['void_tax_request', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method void_tax" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'void_tax_request' is set
        if ('void_tax_request' not in params) or (params['void_tax_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `void_tax_request` when calling `void_tax`")
            raise ValueError("Missing the required parameter `void_tax_request` when calling `void_tax`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `id` when calling `void_tax`")
            raise ValueError("Missing the required parameter `id` when calling `void_tax`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']
            id=id

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'void_tax_request' in params:
            body_params = params['void_tax_request']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'void_tax_request', self.api_client.mconfig.run_environment)
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/vas/v2/tax/{id}', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='VasV2TaxVoid200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
