# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CreateBillingAgreement(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'agreement_information': 'Ptsv2billingagreementsAgreementInformation',
        'client_reference_information': 'Ptsv2billingagreementsClientReferenceInformation',
        'aggregator_information': 'Ptsv2billingagreementsAggregatorInformation',
        'consumer_authentication_information': 'Ptsv2billingagreementsConsumerAuthenticationInformation',
        'device_information': 'Ptsv2billingagreementsDeviceInformation',
        'installment_information': 'Ptsv2billingagreementsInstallmentInformation',
        'merchant_information': 'Ptsv2billingagreementsMerchantInformation',
        'order_information': 'Ptsv2billingagreementsOrderInformation',
        'payment_information': 'Ptsv2billingagreementsPaymentInformation',
        'processing_information': 'Ptsv2billingagreementsProcessingInformation',
        'buyer_information': 'Ptsv2billingagreementsBuyerInformation'
    }

    attribute_map = {
        'agreement_information': 'agreementInformation',
        'client_reference_information': 'clientReferenceInformation',
        'aggregator_information': 'aggregatorInformation',
        'consumer_authentication_information': 'consumerAuthenticationInformation',
        'device_information': 'deviceInformation',
        'installment_information': 'installmentInformation',
        'merchant_information': 'merchantInformation',
        'order_information': 'orderInformation',
        'payment_information': 'paymentInformation',
        'processing_information': 'processingInformation',
        'buyer_information': 'buyerInformation'
    }

    def __init__(self, agreement_information=None, client_reference_information=None, aggregator_information=None, consumer_authentication_information=None, device_information=None, installment_information=None, merchant_information=None, order_information=None, payment_information=None, processing_information=None, buyer_information=None):
        """
        CreateBillingAgreement - a model defined in Swagger
        """

        self._agreement_information = None
        self._client_reference_information = None
        self._aggregator_information = None
        self._consumer_authentication_information = None
        self._device_information = None
        self._installment_information = None
        self._merchant_information = None
        self._order_information = None
        self._payment_information = None
        self._processing_information = None
        self._buyer_information = None

        if agreement_information is not None:
          self.agreement_information = agreement_information
        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if aggregator_information is not None:
          self.aggregator_information = aggregator_information
        if consumer_authentication_information is not None:
          self.consumer_authentication_information = consumer_authentication_information
        if device_information is not None:
          self.device_information = device_information
        if installment_information is not None:
          self.installment_information = installment_information
        if merchant_information is not None:
          self.merchant_information = merchant_information
        if order_information is not None:
          self.order_information = order_information
        if payment_information is not None:
          self.payment_information = payment_information
        if processing_information is not None:
          self.processing_information = processing_information
        if buyer_information is not None:
          self.buyer_information = buyer_information

    @property
    def agreement_information(self):
        """
        Gets the agreement_information of this CreateBillingAgreement.

        :return: The agreement_information of this CreateBillingAgreement.
        :rtype: Ptsv2billingagreementsAgreementInformation
        """
        return self._agreement_information

    @agreement_information.setter
    def agreement_information(self, agreement_information):
        """
        Sets the agreement_information of this CreateBillingAgreement.

        :param agreement_information: The agreement_information of this CreateBillingAgreement.
        :type: Ptsv2billingagreementsAgreementInformation
        """

        self._agreement_information = agreement_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this CreateBillingAgreement.

        :return: The client_reference_information of this CreateBillingAgreement.
        :rtype: Ptsv2billingagreementsClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this CreateBillingAgreement.

        :param client_reference_information: The client_reference_information of this CreateBillingAgreement.
        :type: Ptsv2billingagreementsClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def aggregator_information(self):
        """
        Gets the aggregator_information of this CreateBillingAgreement.

        :return: The aggregator_information of this CreateBillingAgreement.
        :rtype: Ptsv2billingagreementsAggregatorInformation
        """
        return self._aggregator_information

    @aggregator_information.setter
    def aggregator_information(self, aggregator_information):
        """
        Sets the aggregator_information of this CreateBillingAgreement.

        :param aggregator_information: The aggregator_information of this CreateBillingAgreement.
        :type: Ptsv2billingagreementsAggregatorInformation
        """

        self._aggregator_information = aggregator_information

    @property
    def consumer_authentication_information(self):
        """
        Gets the consumer_authentication_information of this CreateBillingAgreement.

        :return: The consumer_authentication_information of this CreateBillingAgreement.
        :rtype: Ptsv2billingagreementsConsumerAuthenticationInformation
        """
        return self._consumer_authentication_information

    @consumer_authentication_information.setter
    def consumer_authentication_information(self, consumer_authentication_information):
        """
        Sets the consumer_authentication_information of this CreateBillingAgreement.

        :param consumer_authentication_information: The consumer_authentication_information of this CreateBillingAgreement.
        :type: Ptsv2billingagreementsConsumerAuthenticationInformation
        """

        self._consumer_authentication_information = consumer_authentication_information

    @property
    def device_information(self):
        """
        Gets the device_information of this CreateBillingAgreement.

        :return: The device_information of this CreateBillingAgreement.
        :rtype: Ptsv2billingagreementsDeviceInformation
        """
        return self._device_information

    @device_information.setter
    def device_information(self, device_information):
        """
        Sets the device_information of this CreateBillingAgreement.

        :param device_information: The device_information of this CreateBillingAgreement.
        :type: Ptsv2billingagreementsDeviceInformation
        """

        self._device_information = device_information

    @property
    def installment_information(self):
        """
        Gets the installment_information of this CreateBillingAgreement.

        :return: The installment_information of this CreateBillingAgreement.
        :rtype: Ptsv2billingagreementsInstallmentInformation
        """
        return self._installment_information

    @installment_information.setter
    def installment_information(self, installment_information):
        """
        Sets the installment_information of this CreateBillingAgreement.

        :param installment_information: The installment_information of this CreateBillingAgreement.
        :type: Ptsv2billingagreementsInstallmentInformation
        """

        self._installment_information = installment_information

    @property
    def merchant_information(self):
        """
        Gets the merchant_information of this CreateBillingAgreement.

        :return: The merchant_information of this CreateBillingAgreement.
        :rtype: Ptsv2billingagreementsMerchantInformation
        """
        return self._merchant_information

    @merchant_information.setter
    def merchant_information(self, merchant_information):
        """
        Sets the merchant_information of this CreateBillingAgreement.

        :param merchant_information: The merchant_information of this CreateBillingAgreement.
        :type: Ptsv2billingagreementsMerchantInformation
        """

        self._merchant_information = merchant_information

    @property
    def order_information(self):
        """
        Gets the order_information of this CreateBillingAgreement.

        :return: The order_information of this CreateBillingAgreement.
        :rtype: Ptsv2billingagreementsOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this CreateBillingAgreement.

        :param order_information: The order_information of this CreateBillingAgreement.
        :type: Ptsv2billingagreementsOrderInformation
        """

        self._order_information = order_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this CreateBillingAgreement.

        :return: The payment_information of this CreateBillingAgreement.
        :rtype: Ptsv2billingagreementsPaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this CreateBillingAgreement.

        :param payment_information: The payment_information of this CreateBillingAgreement.
        :type: Ptsv2billingagreementsPaymentInformation
        """

        self._payment_information = payment_information

    @property
    def processing_information(self):
        """
        Gets the processing_information of this CreateBillingAgreement.

        :return: The processing_information of this CreateBillingAgreement.
        :rtype: Ptsv2billingagreementsProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this CreateBillingAgreement.

        :param processing_information: The processing_information of this CreateBillingAgreement.
        :type: Ptsv2billingagreementsProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def buyer_information(self):
        """
        Gets the buyer_information of this CreateBillingAgreement.

        :return: The buyer_information of this CreateBillingAgreement.
        :rtype: Ptsv2billingagreementsBuyerInformation
        """
        return self._buyer_information

    @buyer_information.setter
    def buyer_information(self, buyer_information):
        """
        Sets the buyer_information of this CreateBillingAgreement.

        :param buyer_information: The buyer_information of this CreateBillingAgreement.
        :type: Ptsv2billingagreementsBuyerInformation
        """

        self._buyer_information = buyer_information

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CreateBillingAgreement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
