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


class TransactionBatchesApi(object):
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


    def get_transaction_batch_details(self, transaction_batch_id, **kwargs):
        """
        Filters batch response. 
        Filters batch response. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_transaction_batch_details(transaction_batch_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str transaction_batch_id: Transaction Batch Id, this is unique. (required)
        :param date upload_date: Date in which the original batch file was uploaded. Date must be in ISO-8601 format.
        :param str status: Allows you to filter by rejected response. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_transaction_batch_details_with_http_info(transaction_batch_id, **kwargs)
        else:
            (data) = self.get_transaction_batch_details_with_http_info(transaction_batch_id, **kwargs)
            return data

    def get_transaction_batch_details_with_http_info(self, transaction_batch_id, **kwargs):
        """
        Filters batch response. 
        Filters batch response. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_transaction_batch_details_with_http_info(transaction_batch_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str transaction_batch_id: Transaction Batch Id, this is unique. (required)
        :param date upload_date: Date in which the original batch file was uploaded. Date must be in ISO-8601 format.
        :param str status: Allows you to filter by rejected response. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transaction_batch_id', 'upload_date', 'status']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transaction_batch_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'transaction_batch_id' is set
        if ('transaction_batch_id' not in params) or (params['transaction_batch_id'] is None):
            raise ValueError("Missing the required parameter `transaction_batch_id` when calling `get_transaction_batch_details`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'transaction_batch_id' in params:
            query_params.append(('transactionBatchId', params['transaction_batch_id']))
        if 'upload_date' in params:
            query_params.append(('uploadDate', params['upload_date']))
        if 'status' in params:
            query_params.append(('status', params['status']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/vnd.cybersource.map-csv'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/pts/v1/transaction-batch-details', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_transaction_batch_id(self, id, **kwargs):
        """
        Get individual batch file
        Provide the search range
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_transaction_batch_id(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The batch id assigned for the template. (required)
        :return: PtsV1TransactionBatchesIdGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_transaction_batch_id_with_http_info(id, **kwargs)
        else:
            (data) = self.get_transaction_batch_id_with_http_info(id, **kwargs)
            return data

    def get_transaction_batch_id_with_http_info(self, id, **kwargs):
        """
        Get individual batch file
        Provide the search range
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_transaction_batch_id_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The batch id assigned for the template. (required)
        :return: PtsV1TransactionBatchesIdGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transaction_batch_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_transaction_batch_id`")


        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/pts/v1/transaction-batches/' + id, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PtsV1TransactionBatchesIdGet200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_transaction_batches(self, start_time, end_time, **kwargs):
        """
        Get a list of batch files
        Provide the search range
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_transaction_batches(start_time, end_time, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime start_time: Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZZ  (required)
        :param datetime end_time: Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZZ  (required)
        :return: PtsV1TransactionBatchesGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_transaction_batches_with_http_info(start_time, end_time, **kwargs)
        else:
            (data) = self.get_transaction_batches_with_http_info(start_time, end_time, **kwargs)
            return data

    def get_transaction_batches_with_http_info(self, start_time, end_time, **kwargs):
        """
        Get a list of batch files
        Provide the search range
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_transaction_batches_with_http_info(start_time, end_time, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param datetime start_time: Valid report Start Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZZ  (required)
        :param datetime end_time: Valid report End Time in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd'T'HH:mm:ss.SSSZZ  (required)
        :return: PtsV1TransactionBatchesGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_time', 'end_time']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transaction_batches" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start_time' is set
        if ('start_time' not in params) or (params['start_time'] is None):
            raise ValueError("Missing the required parameter `start_time` when calling `get_transaction_batches`")
        # verify the required parameter 'end_time' is set
        if ('end_time' not in params) or (params['end_time'] is None):
            raise ValueError("Missing the required parameter `end_time` when calling `get_transaction_batches`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/pts/v1/transaction-batches', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PtsV1TransactionBatchesGet200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
