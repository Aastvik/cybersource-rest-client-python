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
class PayoutsApi(object):
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



    def oct_create_payment(self, oct_create_payment_request, **kwargs):
        """
        Process a Payout
        Send funds from a selected funding source to a designated credit/debit card account or a prepaid card using an Original Credit Transaction (OCT). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.oct_create_payment(oct_create_payment_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param OctCreatePaymentRequest oct_create_payment_request: (required)
        :return: PtsV2PayoutsPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `oct_create_payment` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.oct_create_payment_with_http_info(oct_create_payment_request, **kwargs)
        else:
            (data) = self.oct_create_payment_with_http_info(oct_create_payment_request, **kwargs)
            return data

    def oct_create_payment_with_http_info(self, oct_create_payment_request, **kwargs):
        """
        Process a Payout
        Send funds from a selected funding source to a designated credit/debit card account or a prepaid card using an Original Credit Transaction (OCT). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.oct_create_payment_with_http_info(oct_create_payment_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param OctCreatePaymentRequest oct_create_payment_request: (required)
        :return: PtsV2PayoutsPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['oct_create_payment_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method oct_create_payment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'oct_create_payment_request' is set
        if ('oct_create_payment_request' not in params) or (params['oct_create_payment_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `oct_create_payment_request` when calling `oct_create_payment`")
            raise ValueError("Missing the required parameter `oct_create_payment_request` when calling `oct_create_payment`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'oct_create_payment_request' in params:
            body_params = params['oct_create_payment_request']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'oct_create_payment_request', self.api_client.mconfig.run_environment)
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/pts/v2/payouts', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PtsV2PayoutsPost201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
