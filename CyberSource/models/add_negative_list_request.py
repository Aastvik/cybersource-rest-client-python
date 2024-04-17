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


class AddNegativeListRequest(object):
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
        'order_information': 'Riskv1liststypeentriesOrderInformation',
        'payment_information': 'Riskv1liststypeentriesPaymentInformation',
        'client_reference_information': 'Riskv1liststypeentriesClientReferenceInformation',
        'device_information': 'Riskv1liststypeentriesDeviceInformation',
        'risk_information': 'Riskv1liststypeentriesRiskInformation',
        'buyer_information': 'Riskv1liststypeentriesBuyerInformation'
    }

    attribute_map = {
        'order_information': 'orderInformation',
        'payment_information': 'paymentInformation',
        'client_reference_information': 'clientReferenceInformation',
        'device_information': 'deviceInformation',
        'risk_information': 'riskInformation',
        'buyer_information': 'buyerInformation'
    }

    def __init__(self, order_information=None, payment_information=None, client_reference_information=None, device_information=None, risk_information=None, buyer_information=None):
        """
        AddNegativeListRequest - a model defined in Swagger
        """

        self._order_information = None
        self._payment_information = None
        self._client_reference_information = None
        self._device_information = None
        self._risk_information = None
        self._buyer_information = None

        if order_information is not None:
          self.order_information = order_information
        if payment_information is not None:
          self.payment_information = payment_information
        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if device_information is not None:
          self.device_information = device_information
        if risk_information is not None:
          self.risk_information = risk_information
        if buyer_information is not None:
          self.buyer_information = buyer_information

    @property
    def order_information(self):
        """
        Gets the order_information of this AddNegativeListRequest.

        :return: The order_information of this AddNegativeListRequest.
        :rtype: Riskv1liststypeentriesOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this AddNegativeListRequest.

        :param order_information: The order_information of this AddNegativeListRequest.
        :type: Riskv1liststypeentriesOrderInformation
        """

        self._order_information = order_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this AddNegativeListRequest.

        :return: The payment_information of this AddNegativeListRequest.
        :rtype: Riskv1liststypeentriesPaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this AddNegativeListRequest.

        :param payment_information: The payment_information of this AddNegativeListRequest.
        :type: Riskv1liststypeentriesPaymentInformation
        """

        self._payment_information = payment_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this AddNegativeListRequest.

        :return: The client_reference_information of this AddNegativeListRequest.
        :rtype: Riskv1liststypeentriesClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this AddNegativeListRequest.

        :param client_reference_information: The client_reference_information of this AddNegativeListRequest.
        :type: Riskv1liststypeentriesClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def device_information(self):
        """
        Gets the device_information of this AddNegativeListRequest.

        :return: The device_information of this AddNegativeListRequest.
        :rtype: Riskv1liststypeentriesDeviceInformation
        """
        return self._device_information

    @device_information.setter
    def device_information(self, device_information):
        """
        Sets the device_information of this AddNegativeListRequest.

        :param device_information: The device_information of this AddNegativeListRequest.
        :type: Riskv1liststypeentriesDeviceInformation
        """

        self._device_information = device_information

    @property
    def risk_information(self):
        """
        Gets the risk_information of this AddNegativeListRequest.

        :return: The risk_information of this AddNegativeListRequest.
        :rtype: Riskv1liststypeentriesRiskInformation
        """
        return self._risk_information

    @risk_information.setter
    def risk_information(self, risk_information):
        """
        Sets the risk_information of this AddNegativeListRequest.

        :param risk_information: The risk_information of this AddNegativeListRequest.
        :type: Riskv1liststypeentriesRiskInformation
        """

        self._risk_information = risk_information

    @property
    def buyer_information(self):
        """
        Gets the buyer_information of this AddNegativeListRequest.

        :return: The buyer_information of this AddNegativeListRequest.
        :rtype: Riskv1liststypeentriesBuyerInformation
        """
        return self._buyer_information

    @buyer_information.setter
    def buyer_information(self, buyer_information):
        """
        Sets the buyer_information of this AddNegativeListRequest.

        :param buyer_information: The buyer_information of this AddNegativeListRequest.
        :type: Riskv1liststypeentriesBuyerInformation
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
        if not isinstance(other, AddNegativeListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
