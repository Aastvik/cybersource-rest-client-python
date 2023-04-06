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


class BatchesApi(object):
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



    def get_batch_report(self, batch_id, **kwargs):
        """
        Retrieve a Batch Report
        **Get Batch Report**<br>This resource accepts a batch id and returns: - The batch status. - The total number of accepted, rejected, updated records. - The total number of card association responses. - The billable quantities of:   - New Account Numbers (NAN)   - New Expiry Dates (NED)   - Account Closures (ACL)   - Contact Card Holders (CCH) - Source record information including token ids, masked card number, expiration dates & card type. - Response record information including response code, reason, token ids, masked card number, expiration dates & card type. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_batch_report(batch_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str batch_id: Unique identification number assigned to the submitted request. (required)
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_batch_report` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_batch_report_with_http_info(batch_id, **kwargs)
        else:
            (data) = self.get_batch_report_with_http_info(batch_id, **kwargs)
            return data

    def get_batch_report_with_http_info(self, batch_id, **kwargs):
        """
        Retrieve a Batch Report
        **Get Batch Report**<br>This resource accepts a batch id and returns: - The batch status. - The total number of accepted, rejected, updated records. - The total number of card association responses. - The billable quantities of:   - New Account Numbers (NAN)   - New Expiry Dates (NED)   - Account Closures (ACL)   - Contact Card Holders (CCH) - Source record information including token ids, masked card number, expiration dates & card type. - Response record information including response code, reason, token ids, masked card number, expiration dates & card type. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_batch_report_with_http_info(batch_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str batch_id: Unique identification number assigned to the submitted request. (required)
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['batch_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_batch_report" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'batch_id' is set
        if ('batch_id' not in params) or (params['batch_id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `batch_id` when calling `get_batch_report`")
            raise ValueError("Missing the required parameter `batch_id` when calling `get_batch_report`")

        if 'batch_id' in params and params['batch_id'] > 32:
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `batch_id` when calling `get_batch_report`, must be a value less than or equal to `32`")
            raise ValueError("Invalid value for parameter `batch_id` when calling `get_batch_report`, must be a value less than or equal to `32`")
        if 'batch_id' in params and params['batch_id'] < 16:
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `batch_id` when calling `get_batch_report`, must be a value greater than or equal to `16`")
            raise ValueError("Invalid value for parameter `batch_id` when calling `get_batch_report`, must be a value greater than or equal to `16`")

        collection_formats = {}

        path_params = {}
        if 'batch_id' in params:
            path_params['batchId'] = params['batch_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'GET' in ('POST'):
            body_params = '{}'
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/accountupdater/v1/batches/{batchId}/report', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse20014',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_batch_status(self, batch_id, **kwargs):
        """
        Retrieve a Batch Status
        **Get Batch Status**<br>This resource accepts a batch id and returns: - The batch status. - The total number of accepted, rejected, updated records. - The total number of card association responses. - The billable quantities of:   - New Account Numbers (NAN)   - New Expiry Dates (NED)   - Account Closures (ACL)   - Contact Card Holders (CCH) 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_batch_status(batch_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str batch_id: Unique identification number assigned to the submitted request. (required)
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_batch_status` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_batch_status_with_http_info(batch_id, **kwargs)
        else:
            (data) = self.get_batch_status_with_http_info(batch_id, **kwargs)
            return data

    def get_batch_status_with_http_info(self, batch_id, **kwargs):
        """
        Retrieve a Batch Status
        **Get Batch Status**<br>This resource accepts a batch id and returns: - The batch status. - The total number of accepted, rejected, updated records. - The total number of card association responses. - The billable quantities of:   - New Account Numbers (NAN)   - New Expiry Dates (NED)   - Account Closures (ACL)   - Contact Card Holders (CCH) 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_batch_status_with_http_info(batch_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str batch_id: Unique identification number assigned to the submitted request. (required)
        :return: InlineResponse20013
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['batch_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_batch_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'batch_id' is set
        if ('batch_id' not in params) or (params['batch_id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `batch_id` when calling `get_batch_status`")
            raise ValueError("Missing the required parameter `batch_id` when calling `get_batch_status`")

        if 'batch_id' in params and params['batch_id'] > 32:
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `batch_id` when calling `get_batch_status`, must be a value less than or equal to `32`")
            raise ValueError("Invalid value for parameter `batch_id` when calling `get_batch_status`, must be a value less than or equal to `32`")
        if 'batch_id' in params and params['batch_id'] < 16:
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `batch_id` when calling `get_batch_status`, must be a value greater than or equal to `16`")
            raise ValueError("Invalid value for parameter `batch_id` when calling `get_batch_status`, must be a value greater than or equal to `16`")

        collection_formats = {}

        path_params = {}
        if 'batch_id' in params:
            path_params['batchId'] = params['batch_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'GET' in ('POST'):
            body_params = '{}'
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/accountupdater/v1/batches/{batchId}/status', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse20013',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_batches_list(self, **kwargs):
        """
        List Batches
        **List Batches**<br>This resource accepts a optional date range, record offset and limit, returning a paginated response of batches containing: - The batch id. - The batch status. - The batch created / modified dates. - The total number of accepted, rejected, updated records. - The total number of card association responses. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_batches_list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: Starting record in zero-based dataset that should be returned as the first object in the array.
        :param int limit: The maximum number that can be returned in the array starting from the offset record in zero-based dataset.
        :param str from_date: ISO-8601 format: yyyyMMddTHHmmssZ
        :param str to_date: ISO-8601 format: yyyyMMddTHHmmssZ
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_batches_list` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_batches_list_with_http_info(**kwargs)
        else:
            (data) = self.get_batches_list_with_http_info(**kwargs)
            return data

    def get_batches_list_with_http_info(self, **kwargs):
        """
        List Batches
        **List Batches**<br>This resource accepts a optional date range, record offset and limit, returning a paginated response of batches containing: - The batch id. - The batch status. - The batch created / modified dates. - The total number of accepted, rejected, updated records. - The total number of card association responses. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_batches_list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: Starting record in zero-based dataset that should be returned as the first object in the array.
        :param int limit: The maximum number that can be returned in the array starting from the offset record in zero-based dataset.
        :param str from_date: ISO-8601 format: yyyyMMddTHHmmssZ
        :param str to_date: ISO-8601 format: yyyyMMddTHHmmssZ
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'from_date', 'to_date']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_batches_list" % key
                )
            params[key] = val
        del params['kwargs']

        if 'offset' in params and params['offset'] < 0:
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `offset` when calling `get_batches_list`, must be a value greater than or equal to `0`")
            raise ValueError("Invalid value for parameter `offset` when calling `get_batches_list`, must be a value greater than or equal to `0`")
        if 'limit' in params and params['limit'] > 500:
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `limit` when calling `get_batches_list`, must be a value less than or equal to `500`")
            raise ValueError("Invalid value for parameter `limit` when calling `get_batches_list`, must be a value less than or equal to `500`")
        if 'limit' in params and params['limit'] < 1:
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Invalid value for parameter `limit` when calling `get_batches_list`, must be a value greater than or equal to `1`")
            raise ValueError("Invalid value for parameter `limit` when calling `get_batches_list`, must be a value greater than or equal to `1`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'from_date' in params:
            query_params.append(('fromDate', params['from_date']))
        if 'to_date' in params:
            query_params.append(('toDate', params['to_date']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'GET' in ('POST'):
            body_params = '{}'
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/accountupdater/v1/batches', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse20012',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_batch(self, body, **kwargs):
        """
        Create a Batch
        **Create a Batch**<br>This resource accepts TMS tokens ids of a Customer, Payment Instrument or Instrument Identifier. <br> The card numbers for the supplied tokens ids are then sent to the relevant card associations to check for updates.<br>The following type of batches can be submitted: -  **oneOff** batch containing tokens id for Visa or MasterCard card numbers. - **amexRegistration** batch containing tokens id for Amex card numbers.  A batch id will be returned on a successful response which can be used to get the batch status and the batch report. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_batch(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Body body: (required)
        :return: InlineResponse2022
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `post_batch` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_batch_with_http_info(body, **kwargs)
        else:
            (data) = self.post_batch_with_http_info(body, **kwargs)
            return data

    def post_batch_with_http_info(self, body, **kwargs):
        """
        Create a Batch
        **Create a Batch**<br>This resource accepts TMS tokens ids of a Customer, Payment Instrument or Instrument Identifier. <br> The card numbers for the supplied tokens ids are then sent to the relevant card associations to check for updates.<br>The following type of batches can be submitted: -  **oneOff** batch containing tokens id for Visa or MasterCard card numbers. - **amexRegistration** batch containing tokens id for Amex card numbers.  A batch id will be returned on a successful response which can be used to get the batch status and the batch report. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_batch_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Body body: (required)
        :return: InlineResponse2022
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_batch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `body` when calling `post_batch`")
            raise ValueError("Missing the required parameter `body` when calling `post_batch`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/accountupdater/v1/batches', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse2022',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
