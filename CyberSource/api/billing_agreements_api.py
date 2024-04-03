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
class BillingAgreementsApi(object):
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



    def billing_agreements_de_registration(self, modify_billing_agreement, id, **kwargs):
        """
        Modify a Billing Agreement
        #### Standing Instruction: Standing Instruction with or without Token.  #### Revoke Mandate: When you revoke a mandate, any pending direct debits linked to that mandate are canceled. No notifications are sent. When you revoke a mandate with no pending direct debits, the Bacs scheme or customer's bank notify you of any subsequent direct debit events. When you revoke a mandate, you cannot send a direct debit request using the mandate ID. Customer payments cannot be made against a revoked mandate. You can revoke a mandate when the customer:   - Requests that you revoke the mandate.   - Closes their account with you. Possible revoke mandate status values -   - Revoked—the revoke mandate request was successfully processed.   - Failed—the revoke mandate request was not accepted.  #### Update Mandate: In most cases, the account details of an existing mandate cannot be updated in the Bacs schema, except by creating a new mandate. However, some very limited customer information, like name and address, can be updated to the mandate without needing to revoke it first  #### Mandate Status: After the customer signs the mandate, request that the mandate status service verify the mandate status. Possible mandate status values:   - Active—the mandate is successfully created. A direct debit can be sent for this mandate ID.   - Pending—a pending mandate means the mandate is not yet signed.   - Failed—the customer did not authenticate.   - Expired—the deadline to create the mandate passed.   - Revoked—the mandate is cancelled.  #### Paypal Billing Agreement:  A billing agreement is set up between PayPal and your customer. When you collect the details of a customer's billing agreement, you are able to bill that customer without requiring an authorization for each payment.  You can bill the customer at the same time you process their PayPal Express checkout order, which simplifies your business processes. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billing_agreements_de_registration(modify_billing_agreement, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ModifyBillingAgreement modify_billing_agreement: (required)
        :param str id: ID for de-registration or cancellation of Billing Agreement (required)
        :return: PtsV2ModifyBillingAgreementPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `billing_agreements_de_registration` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.billing_agreements_de_registration_with_http_info(modify_billing_agreement, id, **kwargs)
        else:
            (data) = self.billing_agreements_de_registration_with_http_info(modify_billing_agreement, id, **kwargs)
            return data

    def billing_agreements_de_registration_with_http_info(self, modify_billing_agreement, id, **kwargs):
        """
        Modify a Billing Agreement
        #### Standing Instruction: Standing Instruction with or without Token.  #### Revoke Mandate: When you revoke a mandate, any pending direct debits linked to that mandate are canceled. No notifications are sent. When you revoke a mandate with no pending direct debits, the Bacs scheme or customer's bank notify you of any subsequent direct debit events. When you revoke a mandate, you cannot send a direct debit request using the mandate ID. Customer payments cannot be made against a revoked mandate. You can revoke a mandate when the customer:   - Requests that you revoke the mandate.   - Closes their account with you. Possible revoke mandate status values -   - Revoked—the revoke mandate request was successfully processed.   - Failed—the revoke mandate request was not accepted.  #### Update Mandate: In most cases, the account details of an existing mandate cannot be updated in the Bacs schema, except by creating a new mandate. However, some very limited customer information, like name and address, can be updated to the mandate without needing to revoke it first  #### Mandate Status: After the customer signs the mandate, request that the mandate status service verify the mandate status. Possible mandate status values:   - Active—the mandate is successfully created. A direct debit can be sent for this mandate ID.   - Pending—a pending mandate means the mandate is not yet signed.   - Failed—the customer did not authenticate.   - Expired—the deadline to create the mandate passed.   - Revoked—the mandate is cancelled.  #### Paypal Billing Agreement:  A billing agreement is set up between PayPal and your customer. When you collect the details of a customer's billing agreement, you are able to bill that customer without requiring an authorization for each payment.  You can bill the customer at the same time you process their PayPal Express checkout order, which simplifies your business processes. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billing_agreements_de_registration_with_http_info(modify_billing_agreement, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ModifyBillingAgreement modify_billing_agreement: (required)
        :param str id: ID for de-registration or cancellation of Billing Agreement (required)
        :return: PtsV2ModifyBillingAgreementPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['modify_billing_agreement', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method billing_agreements_de_registration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'modify_billing_agreement' is set
        if ('modify_billing_agreement' not in params) or (params['modify_billing_agreement'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `modify_billing_agreement` when calling `billing_agreements_de_registration`")
            raise ValueError("Missing the required parameter `modify_billing_agreement` when calling `billing_agreements_de_registration`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `id` when calling `billing_agreements_de_registration`")
            raise ValueError("Missing the required parameter `id` when calling `billing_agreements_de_registration`")


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
        if 'modify_billing_agreement' in params:
            body_params = params['modify_billing_agreement']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'modify_billing_agreement', self.api_client.mconfig.run_environment)
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/pts/v2/billing-agreements/{id}', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PtsV2ModifyBillingAgreementPost201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def billing_agreements_intimation(self, intimate_billing_agreement, id, **kwargs):
        """
        Standing Instruction intimation
        Standing Instruction with or without Token.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billing_agreements_intimation(intimate_billing_agreement, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param IntimateBillingAgreement intimate_billing_agreement: (required)
        :param str id: ID for intimation of Billing Agreement (required)
        :return: PtsV2CreditsPost201Response1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `billing_agreements_intimation` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.billing_agreements_intimation_with_http_info(intimate_billing_agreement, id, **kwargs)
        else:
            (data) = self.billing_agreements_intimation_with_http_info(intimate_billing_agreement, id, **kwargs)
            return data

    def billing_agreements_intimation_with_http_info(self, intimate_billing_agreement, id, **kwargs):
        """
        Standing Instruction intimation
        Standing Instruction with or without Token.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billing_agreements_intimation_with_http_info(intimate_billing_agreement, id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param IntimateBillingAgreement intimate_billing_agreement: (required)
        :param str id: ID for intimation of Billing Agreement (required)
        :return: PtsV2CreditsPost201Response1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['intimate_billing_agreement', 'id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method billing_agreements_intimation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'intimate_billing_agreement' is set
        if ('intimate_billing_agreement' not in params) or (params['intimate_billing_agreement'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `intimate_billing_agreement` when calling `billing_agreements_intimation`")
            raise ValueError("Missing the required parameter `intimate_billing_agreement` when calling `billing_agreements_intimation`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `id` when calling `billing_agreements_intimation`")
            raise ValueError("Missing the required parameter `id` when calling `billing_agreements_intimation`")


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
        if 'intimate_billing_agreement' in params:
            body_params = params['intimate_billing_agreement']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'intimate_billing_agreement', self.api_client.mconfig.run_environment)
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/pts/v2/billing-agreements/{id}/intimations', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PtsV2CreditsPost201Response1',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def billing_agreements_registration(self, create_billing_agreement, **kwargs):
        """
        Create a Billing Agreement
        #### Standing Instruction: Standing Instruction with or without Token. Transaction amount in case First payment is coming along with registration. Only 2 decimal places allowed  #### Create Mandate: You can create a mandate through the direct debit mandate flow. Possible create mandate status values:   - Pending—the create mandate request was successfully processed.   - Failed—the create mandate request was not accepted.  #### Import Mandate: In the Bacs scheme, a mandate is created with a status of active. Direct debit collections can be made against it immediately. You can import a mandate to the CyberSource database when:   - You have existing customers with signed, active mandates   - You manage mandates outside of CyberSource.  When you import an existing mandate to the CyberSource database, provide a unique value for the mandate ID or the request results in an error. If an import mandate request is not accepted, the import mandate status value is failed. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billing_agreements_registration(create_billing_agreement, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateBillingAgreement create_billing_agreement: (required)
        :return: PtsV2CreateBillingAgreementPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        if self.api_client.mconfig.log_config.enable_log:
            self.logger.info("CALL TO METHOD `billing_agreements_registration` STARTED")

        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.billing_agreements_registration_with_http_info(create_billing_agreement, **kwargs)
        else:
            (data) = self.billing_agreements_registration_with_http_info(create_billing_agreement, **kwargs)
            return data

    def billing_agreements_registration_with_http_info(self, create_billing_agreement, **kwargs):
        """
        Create a Billing Agreement
        #### Standing Instruction: Standing Instruction with or without Token. Transaction amount in case First payment is coming along with registration. Only 2 decimal places allowed  #### Create Mandate: You can create a mandate through the direct debit mandate flow. Possible create mandate status values:   - Pending—the create mandate request was successfully processed.   - Failed—the create mandate request was not accepted.  #### Import Mandate: In the Bacs scheme, a mandate is created with a status of active. Direct debit collections can be made against it immediately. You can import a mandate to the CyberSource database when:   - You have existing customers with signed, active mandates   - You manage mandates outside of CyberSource.  When you import an existing mandate to the CyberSource database, provide a unique value for the mandate ID or the request results in an error. If an import mandate request is not accepted, the import mandate status value is failed. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.billing_agreements_registration_with_http_info(create_billing_agreement, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateBillingAgreement create_billing_agreement: (required)
        :return: PtsV2CreateBillingAgreementPost201Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_billing_agreement']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method billing_agreements_registration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_billing_agreement' is set
        if ('create_billing_agreement' not in params) or (params['create_billing_agreement'] is None):
            if self.api_client.mconfig.log_config.enable_log:
                self.logger.error("InvalidArgumentException : Missing the required parameter `create_billing_agreement` when calling `billing_agreements_registration`")
            raise ValueError("Missing the required parameter `create_billing_agreement` when calling `billing_agreements_registration`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_billing_agreement' in params:
            body_params = params['create_billing_agreement']
        
            sdkTracker = SdkTracker()
            body_params = sdkTracker.insert_developer_id_tracker(body_params, 'create_billing_agreement', self.api_client.mconfig.run_environment)
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/hal+json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(f'/pts/v2/billing-agreements', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PtsV2CreateBillingAgreementPost201Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
