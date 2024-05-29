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
class InvoicesApi(object):
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



    def create_invoice(self, create_invoice_request, **kwargs):
        """
        Create a New Invoice
        The invoicing product enables you to bill any customer with an email address and accept digital payments securely from any connected device. You can either use the system generated email or use the invoice payment link in your own communication. You can add discounts and taxes for the entire invoice or for each line item. To customize the invoice to match your brand see [Invoice Settings](https://developer.cybersource.com/api-reference-assets/index.html#invoicing_invoice-settings_update-invoice-settings). The invoice payment page uses Unified Checkout to process the payments.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_invoice(create_invoice_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateInvoiceRequest create_invoice_request: (required)
        :return: InvoicingV2InvoicesPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `create_invoice` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_invoice_with_http_info(create_invoice_request, **kwargs)
        else:
            (data) = self.create_invoice_with_http_info(create_invoice_request, **kwargs)
            return data

    def create_invoice_with_http_info(self, create_invoice_request, **kwargs):
        """
        Create a New Invoice
        The invoicing product enables you to bill any customer with an email address and accept digital payments securely from any connected device. You can either use the system generated email or use the invoice payment link in your own communication. You can add discounts and taxes for the entire invoice or for each line item. To customize the invoice to match your brand see [Invoice Settings](https://developer.cybersource.com/api-reference-assets/index.html#invoicing_invoice-settings_update-invoice-settings). The invoice payment page uses Unified Checkout to process the payments.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_invoice_with_http_info(create_invoice_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateInvoiceRequest create_invoice_request: (required)
        :return: InvoicingV2InvoicesPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_invoice_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_invoice_request' is set
        if ('create_invoice_request' not in params) or (params['create_invoice_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `create_invoice_request` when calling `create_invoice`")
            raise ValueError("Missing the required parameter `create_invoice_request` when calling `create_invoice`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_invoice_request' in params:
            body_params = params['create_invoice_request']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'create_invoice_request', self.api_client.mconfig.run_environment)
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json', 'application/hal+json', 'application/json;charset=utf-8', 'application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/invoicing/v2/invoices', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InvoicingV2InvoicesPost201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_all_invoices(self, offset, limit, **kwargs):
        """
        Get a List of Invoices
        Provides a (filtered) list of invoices that have been created in your account. You can filter the list based on Invoice Status by setting the status query parameter to one of DRAFT, CREATED, SENT, PARTIAL, PAID or CANCELED.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_invoices(offset, limit, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: Page offset number. (required)
        :param int limit: Maximum number of items you would like returned. (required)
        :param str status: The status of the invoice.  Possible values:   - DRAFT   - CREATED   - SENT   - PARTIAL   - PAID   - CANCELED   - PENDING 
        :return: InvoicingV2InvoicesAllGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_all_invoices` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_invoices_with_http_info(offset, limit, **kwargs)
        else:
            (data) = self.get_all_invoices_with_http_info(offset, limit, **kwargs)
            return data

    def get_all_invoices_with_http_info(self, offset, limit, **kwargs):
        """
        Get a List of Invoices
        Provides a (filtered) list of invoices that have been created in your account. You can filter the list based on Invoice Status by setting the status query parameter to one of DRAFT, CREATED, SENT, PARTIAL, PAID or CANCELED.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_invoices_with_http_info(offset, limit, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: Page offset number. (required)
        :param int limit: Maximum number of items you would like returned. (required)
        :param str status: The status of the invoice.  Possible values:   - DRAFT   - CREATED   - SENT   - PARTIAL   - PAID   - CANCELED   - PENDING 
        :return: InvoicingV2InvoicesAllGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit', 'status']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_invoices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'offset' is set
        if ('offset' not in params) or (params['offset'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `offset` when calling `get_all_invoices`")
            raise ValueError("Missing the required parameter `offset` when calling `get_all_invoices`")
        # verify the required parameter 'limit' is set
        if ('limit' not in params) or (params['limit'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `limit` when calling `get_all_invoices`")
            raise ValueError("Missing the required parameter `limit` when calling `get_all_invoices`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'status' in params:
            query_params.append(('status', params['status']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'GET' in ('POST'):
            body_params = '{}'
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json', 'application/hal+json', 'application/json;charset=utf-8', 'application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/invoicing/v2/invoices', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InvoicingV2InvoicesAllGet200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_invoice(self, id, **kwargs):
        """
        Get Invoice Details
        You can retrieve details of a specific invoice. This can be used to check the Invoice status and get a list of invoice payments in the invoice history section of the response. For each payment transaction you can use the Transaction Details API to get more details on the payment transaction.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_invoice(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The invoice number. (required)
        :return: InvoicingV2InvoicesGet200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_invoice` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_invoice_with_http_info(id, **kwargs)
        else:
            (data) = self.get_invoice_with_http_info(id, **kwargs)
            return data

    def get_invoice_with_http_info(self, id, **kwargs):
        """
        Get Invoice Details
        You can retrieve details of a specific invoice. This can be used to check the Invoice status and get a list of invoice payments in the invoice history section of the response. For each payment transaction you can use the Transaction Details API to get more details on the payment transaction.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_invoice_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The invoice number. (required)
        :return: InvoicingV2InvoicesGet200Response
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
                    " to method get_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `id` when calling `get_invoice`")
            raise ValueError("Missing the required parameter `id` when calling `get_invoice`")


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
        if 'GET' in ('POST'):
            body_params = '{}'
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json', 'application/hal+json', 'application/json;charset=utf-8', 'application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/invoicing/v2/invoices/{id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InvoicingV2InvoicesGet200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def perform_cancel_action(self, id, **kwargs):
        """
        Cancel an Invoice
        You can cancel an invoice if no payment is made to it. You cannot cancel partially or fully paid invoices.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.perform_cancel_action(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The invoice number. (required)
        :return: InvoicingV2InvoicesPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `perform_cancel_action` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.perform_cancel_action_with_http_info(id, **kwargs)
        else:
            (data) = self.perform_cancel_action_with_http_info(id, **kwargs)
            return data

    def perform_cancel_action_with_http_info(self, id, **kwargs):
        """
        Cancel an Invoice
        You can cancel an invoice if no payment is made to it. You cannot cancel partially or fully paid invoices.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.perform_cancel_action_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The invoice number. (required)
        :return: InvoicingV2InvoicesPost201Response
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
                    " to method perform_cancel_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `id` when calling `perform_cancel_action`")
            raise ValueError("Missing the required parameter `id` when calling `perform_cancel_action`")


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
        if 'POST' in ('POST'):
            body_params = '{}'
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json', 'application/hal+json', 'application/json;charset=utf-8', 'application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/invoicing/v2/invoices/{id}/cancelation', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InvoicingV2InvoicesPost201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def perform_send_action(self, id, **kwargs):
        """
        Send an Invoice
        You can send an invoice in draft or created state or resend a sent or partially paid invoice. Fully paid or canceled invoices cannot be resent.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.perform_send_action(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The invoice number. (required)
        :return: InvoicingV2InvoicesPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `perform_send_action` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.perform_send_action_with_http_info(id, **kwargs)
        else:
            (data) = self.perform_send_action_with_http_info(id, **kwargs)
            return data

    def perform_send_action_with_http_info(self, id, **kwargs):
        """
        Send an Invoice
        You can send an invoice in draft or created state or resend a sent or partially paid invoice. Fully paid or canceled invoices cannot be resent.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.perform_send_action_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The invoice number. (required)
        :return: InvoicingV2InvoicesPost201Response
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
                    " to method perform_send_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `id` when calling `perform_send_action`")
            raise ValueError("Missing the required parameter `id` when calling `perform_send_action`")


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
        if 'POST' in ('POST'):
            body_params = '{}'
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json', 'application/hal+json', 'application/json;charset=utf-8', 'application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/invoicing/v2/invoices/{id}/delivery', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InvoicingV2InvoicesPost201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_invoice(self, id, update_invoice_request, **kwargs):
        """
        Update an Invoice
        You can update all information except the invoice number till any payment is received for an invoice. Invoices that are partially or fully paid or cancelled cannot be updated.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_invoice(id, update_invoice_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The invoice number. (required)
        :param UpdateInvoiceRequest update_invoice_request: Updating the invoice does not resend the invoice automatically. You must resend the invoice separately. (required)
        :return: InvoicingV2InvoicesPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `update_invoice` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_invoice_with_http_info(id, update_invoice_request, **kwargs)
        else:
            (data) = self.update_invoice_with_http_info(id, update_invoice_request, **kwargs)
            return data

    def update_invoice_with_http_info(self, id, update_invoice_request, **kwargs):
        """
        Update an Invoice
        You can update all information except the invoice number till any payment is received for an invoice. Invoices that are partially or fully paid or cancelled cannot be updated.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_invoice_with_http_info(id, update_invoice_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: The invoice number. (required)
        :param UpdateInvoiceRequest update_invoice_request: Updating the invoice does not resend the invoice automatically. You must resend the invoice separately. (required)
        :return: InvoicingV2InvoicesPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'update_invoice_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `id` when calling `update_invoice`")
            raise ValueError("Missing the required parameter `id` when calling `update_invoice`")
        # verify the required parameter 'update_invoice_request' is set
        if ('update_invoice_request' not in params) or (params['update_invoice_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `update_invoice_request` when calling `update_invoice`")
            raise ValueError("Missing the required parameter `update_invoice_request` when calling `update_invoice`")


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
        if 'update_invoice_request' in params:
            body_params = params['update_invoice_request']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'update_invoice_request', self.api_client.mconfig.run_environment)
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json', 'application/hal+json', 'application/json;charset=utf-8', 'application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/invoicing/v2/invoices/{id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InvoicingV2InvoicesPost201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
