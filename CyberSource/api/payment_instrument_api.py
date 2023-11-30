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
class PaymentInstrumentApi(object):
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



    def delete_payment_instrument(self, payment_instrument_id, **kwargs):
        """
        Delete a Payment Instrument
        |  |  |  | | --- | --- | --- | |**Standalone Payment Instruments**<br>A Payment Instrument represents tokenized payment information such as expiration date, billing address & card type.<br>A Payment Instrument token does not store the card number. A Payment Instrument is associated with an [Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier) that represents either a payment card number, or in the case of an ACH bank account, the routing and account number.<br>**Standalone Payment Instruments do not belong to a [Customer](#token-management_customer_create-a-customer).**|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Deleting a Payment Instrument**<br>Your system can use this API to delete an existing Payment Instrument.<br>Any Instrument Identifiers representing the card number will also be deleted if they are not associated with any other Payment Instruments. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_payment_instrument(payment_instrument_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str payment_instrument_id: The Id of a payment instrument. (required)
        :param str profile_id: The Id of a profile containing user specific TMS configuration.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `delete_payment_instrument` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_payment_instrument_with_http_info(payment_instrument_id, **kwargs)
        else:
            (data) = self.delete_payment_instrument_with_http_info(payment_instrument_id, **kwargs)
            return data

    def delete_payment_instrument_with_http_info(self, payment_instrument_id, **kwargs):
        """
        Delete a Payment Instrument
        |  |  |  | | --- | --- | --- | |**Standalone Payment Instruments**<br>A Payment Instrument represents tokenized payment information such as expiration date, billing address & card type.<br>A Payment Instrument token does not store the card number. A Payment Instrument is associated with an [Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier) that represents either a payment card number, or in the case of an ACH bank account, the routing and account number.<br>**Standalone Payment Instruments do not belong to a [Customer](#token-management_customer_create-a-customer).**|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Deleting a Payment Instrument**<br>Your system can use this API to delete an existing Payment Instrument.<br>Any Instrument Identifiers representing the card number will also be deleted if they are not associated with any other Payment Instruments. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_payment_instrument_with_http_info(payment_instrument_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str payment_instrument_id: The Id of a payment instrument. (required)
        :param str profile_id: The Id of a profile containing user specific TMS configuration.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_instrument_id', 'profile_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_payment_instrument" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_instrument_id' is set
        if ('payment_instrument_id' not in params) or (params['payment_instrument_id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `payment_instrument_id` when calling `delete_payment_instrument`")
            raise ValueError("Missing the required parameter `payment_instrument_id` when calling `delete_payment_instrument`")


        collection_formats = {}

        path_params = {}
        if 'payment_instrument_id' in params:
            path_params['paymentInstrumentId'] = params['payment_instrument_id']
            paymentInstrumentId=payment_instrument_id

        query_params = []

        header_params = {}
        if 'profile_id' in params:
            header_params['profile-id'] = params['profile_id']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'DELETE' in ('POST'):
            body_params = '{}'
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/tms/v1/paymentinstruments/{paymentInstrumentId}', 'DELETE',
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

    def get_payment_instrument(self, payment_instrument_id, **kwargs):
        """
        Retrieve a Payment Instrument
        |  |  |  | | --- | --- | --- | |**Standalone Payment Instruments**<br>A Payment Instrument represents tokenized payment information such as expiration date, billing address & card type.<br>A Payment Instrument token does not store the card number. A Payment Instrument is associated with an [Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier) that represents either a payment card number, or in the case of an ACH bank account, the routing and account number.<br>**Standalone Payment Instruments do not belong to a [Customer](#token-management_customer_create-a-customer).**|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Retrieving a Payment Instrument**<br>Your system can use this API to retrieve an existing Payment Instrument.<br>To perform a payment with a particular Payment Instrument simply specify the [Payment Instrument Id in the payments request](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-using-tokens_authorization-with-customer-payment-instrument-and-shipping-address-token-id_liveconsole-tab-request-body). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_payment_instrument(payment_instrument_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str payment_instrument_id: The Id of a payment instrument. (required)
        :param str profile_id: The Id of a profile containing user specific TMS configuration.
        :return: Tmsv2customersEmbeddedDefaultPaymentInstrument
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `get_payment_instrument` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_payment_instrument_with_http_info(payment_instrument_id, **kwargs)
        else:
            (data) = self.get_payment_instrument_with_http_info(payment_instrument_id, **kwargs)
            return data

    def get_payment_instrument_with_http_info(self, payment_instrument_id, **kwargs):
        """
        Retrieve a Payment Instrument
        |  |  |  | | --- | --- | --- | |**Standalone Payment Instruments**<br>A Payment Instrument represents tokenized payment information such as expiration date, billing address & card type.<br>A Payment Instrument token does not store the card number. A Payment Instrument is associated with an [Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier) that represents either a payment card number, or in the case of an ACH bank account, the routing and account number.<br>**Standalone Payment Instruments do not belong to a [Customer](#token-management_customer_create-a-customer).**|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Retrieving a Payment Instrument**<br>Your system can use this API to retrieve an existing Payment Instrument.<br>To perform a payment with a particular Payment Instrument simply specify the [Payment Instrument Id in the payments request](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-using-tokens_authorization-with-customer-payment-instrument-and-shipping-address-token-id_liveconsole-tab-request-body). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_payment_instrument_with_http_info(payment_instrument_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str payment_instrument_id: The Id of a payment instrument. (required)
        :param str profile_id: The Id of a profile containing user specific TMS configuration.
        :return: Tmsv2customersEmbeddedDefaultPaymentInstrument
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_instrument_id', 'profile_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payment_instrument" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_instrument_id' is set
        if ('payment_instrument_id' not in params) or (params['payment_instrument_id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `payment_instrument_id` when calling `get_payment_instrument`")
            raise ValueError("Missing the required parameter `payment_instrument_id` when calling `get_payment_instrument`")


        collection_formats = {}

        path_params = {}
        if 'payment_instrument_id' in params:
            path_params['paymentInstrumentId'] = params['payment_instrument_id']
            paymentInstrumentId=payment_instrument_id

        query_params = []

        header_params = {}
        if 'profile_id' in params:
            header_params['profile-id'] = params['profile_id']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'GET' in ('POST'):
            body_params = '{}'
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/tms/v1/paymentinstruments/{paymentInstrumentId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Tmsv2customersEmbeddedDefaultPaymentInstrument',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def patch_payment_instrument(self, payment_instrument_id, patch_payment_instrument_request, **kwargs):
        """
        Update a Payment Instrument
        |  |  |  | | --- | --- | --- | |**Standalone Payment Instruments**<br>A Payment Instrument represents tokenized payment information such as expiration date, billing address & card type.<br>A Payment Instrument token does not store the card number. A Payment Instrument is associated with an [Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier) that represents either a payment card number, or in the case of an ACH bank account, the routing and account number.<br>**Standalone Payment Instruments do not belong to a [Customer](#token-management_customer_create-a-customer).**|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Updating a Payment Instrument**<br>Your system can use this API to update an existing Payment Instrument. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_payment_instrument(payment_instrument_id, patch_payment_instrument_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str payment_instrument_id: The Id of a payment instrument. (required)
        :param PatchPaymentInstrumentRequest patch_payment_instrument_request: (required)
        :param str profile_id: The Id of a profile containing user specific TMS configuration.
        :param str if_match: Contains an ETag value from a GET request to make the request conditional.
        :return: Tmsv2customersEmbeddedDefaultPaymentInstrument
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `patch_payment_instrument` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.patch_payment_instrument_with_http_info(payment_instrument_id, patch_payment_instrument_request, **kwargs)
        else:
            (data) = self.patch_payment_instrument_with_http_info(payment_instrument_id, patch_payment_instrument_request, **kwargs)
            return data

    def patch_payment_instrument_with_http_info(self, payment_instrument_id, patch_payment_instrument_request, **kwargs):
        """
        Update a Payment Instrument
        |  |  |  | | --- | --- | --- | |**Standalone Payment Instruments**<br>A Payment Instrument represents tokenized payment information such as expiration date, billing address & card type.<br>A Payment Instrument token does not store the card number. A Payment Instrument is associated with an [Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier) that represents either a payment card number, or in the case of an ACH bank account, the routing and account number.<br>**Standalone Payment Instruments do not belong to a [Customer](#token-management_customer_create-a-customer).**|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Updating a Payment Instrument**<br>Your system can use this API to update an existing Payment Instrument. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.patch_payment_instrument_with_http_info(payment_instrument_id, patch_payment_instrument_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str payment_instrument_id: The Id of a payment instrument. (required)
        :param PatchPaymentInstrumentRequest patch_payment_instrument_request: (required)
        :param str profile_id: The Id of a profile containing user specific TMS configuration.
        :param str if_match: Contains an ETag value from a GET request to make the request conditional.
        :return: Tmsv2customersEmbeddedDefaultPaymentInstrument
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_instrument_id', 'patch_payment_instrument_request', 'profile_id', 'if_match']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_payment_instrument" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_instrument_id' is set
        if ('payment_instrument_id' not in params) or (params['payment_instrument_id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `payment_instrument_id` when calling `patch_payment_instrument`")
            raise ValueError("Missing the required parameter `payment_instrument_id` when calling `patch_payment_instrument`")
        # verify the required parameter 'patch_payment_instrument_request' is set
        if ('patch_payment_instrument_request' not in params) or (params['patch_payment_instrument_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `patch_payment_instrument_request` when calling `patch_payment_instrument`")
            raise ValueError("Missing the required parameter `patch_payment_instrument_request` when calling `patch_payment_instrument`")


        collection_formats = {}

        path_params = {}
        if 'payment_instrument_id' in params:
            path_params['paymentInstrumentId'] = params['payment_instrument_id']
            paymentInstrumentId=payment_instrument_id

        query_params = []

        header_params = {}
        if 'profile_id' in params:
            header_params['profile-id'] = params['profile_id']
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'patch_payment_instrument_request' in params:
            body_params = params['patch_payment_instrument_request']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'patch_payment_instrument_request', self.api_client.mconfig.run_environment)
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/tms/v1/paymentinstruments/{paymentInstrumentId}', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Tmsv2customersEmbeddedDefaultPaymentInstrument',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_payment_instrument(self, post_payment_instrument_request, **kwargs):
        """
        Create a Payment Instrument
        |  |  |  | | --- | --- | --- | |**Standalone Payment Instruments**<br>A Payment Instrument represents tokenized payment information such as expiration date, billing address & card type.<br>A Payment Instrument token does not store the card number. A Payment Instrument is associated with an [Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier) that represents either a payment card number, or in the case of an ACH bank account, the routing and account number.<br>**Standalone Payment Instruments do not belong to a [Customer](#token-management_customer_create-a-customer).**<br><br>**Creating a Payment Instrument**<br>It is recommended you [create a Payment Instrument via a Payment Authorization](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-with-token-create_authorization-with-customer-token-creation_liveconsole-tab-request-body), this can be for a zero amount.<br>In Europe: You should perform Payer Authentication alongside the Authorization.|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Payment Network Tokens**<br>Network tokens perform better than regular card numbers and they are not necessarily invalidated when a cardholder loses their card, or it expires.<br>A Payment Network Token will be automatically created and used in future payments if you are enabled for the service.<br>A Payment Network Token can also be [provisioned for an existing Instrument Identifier](#token-management_instrument-identifier_enroll-an-instrument-identifier-for-payment-network-token).<br>For more information about Payment Network Tokens see the Developer Guide.<br><br>**Payments with Payment Instruments**<br>To perform a payment with a particular Payment Instrument specify the [Payment Instrument in the payment request](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-using-tokens_authorization-with-customer-payment-instrument-and-shipping-address-token-id_liveconsole-tab-request-body). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_payment_instrument(post_payment_instrument_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PostPaymentInstrumentRequest post_payment_instrument_request: (required)
        :param str profile_id: The Id of a profile containing user specific TMS configuration.
        :return: Tmsv2customersEmbeddedDefaultPaymentInstrument
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `post_payment_instrument` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_payment_instrument_with_http_info(post_payment_instrument_request, **kwargs)
        else:
            (data) = self.post_payment_instrument_with_http_info(post_payment_instrument_request, **kwargs)
            return data

    def post_payment_instrument_with_http_info(self, post_payment_instrument_request, **kwargs):
        """
        Create a Payment Instrument
        |  |  |  | | --- | --- | --- | |**Standalone Payment Instruments**<br>A Payment Instrument represents tokenized payment information such as expiration date, billing address & card type.<br>A Payment Instrument token does not store the card number. A Payment Instrument is associated with an [Instrument Identifier](#token-management_instrument-identifier_create-an-instrument-identifier) that represents either a payment card number, or in the case of an ACH bank account, the routing and account number.<br>**Standalone Payment Instruments do not belong to a [Customer](#token-management_customer_create-a-customer).**<br><br>**Creating a Payment Instrument**<br>It is recommended you [create a Payment Instrument via a Payment Authorization](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-with-token-create_authorization-with-customer-token-creation_liveconsole-tab-request-body), this can be for a zero amount.<br>In Europe: You should perform Payer Authentication alongside the Authorization.|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|**Payment Network Tokens**<br>Network tokens perform better than regular card numbers and they are not necessarily invalidated when a cardholder loses their card, or it expires.<br>A Payment Network Token will be automatically created and used in future payments if you are enabled for the service.<br>A Payment Network Token can also be [provisioned for an existing Instrument Identifier](#token-management_instrument-identifier_enroll-an-instrument-identifier-for-payment-network-token).<br>For more information about Payment Network Tokens see the Developer Guide.<br><br>**Payments with Payment Instruments**<br>To perform a payment with a particular Payment Instrument specify the [Payment Instrument in the payment request](#payments_payments_process-a-payment_samplerequests-dropdown_authorization-using-tokens_authorization-with-customer-payment-instrument-and-shipping-address-token-id_liveconsole-tab-request-body). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_payment_instrument_with_http_info(post_payment_instrument_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param PostPaymentInstrumentRequest post_payment_instrument_request: (required)
        :param str profile_id: The Id of a profile containing user specific TMS configuration.
        :return: Tmsv2customersEmbeddedDefaultPaymentInstrument
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['post_payment_instrument_request', 'profile_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_payment_instrument" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_payment_instrument_request' is set
        if ('post_payment_instrument_request' not in params) or (params['post_payment_instrument_request'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `post_payment_instrument_request` when calling `post_payment_instrument`")
            raise ValueError("Missing the required parameter `post_payment_instrument_request` when calling `post_payment_instrument`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'profile_id' in params:
            header_params['profile-id'] = params['profile_id']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'post_payment_instrument_request' in params:
            body_params = params['post_payment_instrument_request']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'post_payment_instrument_request', self.api_client.mconfig.run_environment)
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/tms/v1/paymentinstruments', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Tmsv2customersEmbeddedDefaultPaymentInstrument',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
