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


class PaymentsProductsECheckSubscriptionInformation(object):
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
        'enabled': 'bool',
        'self_serviceability': 'str',
        'mode': 'list[str]'
    }

    attribute_map = {
        'enabled': 'enabled',
        'self_serviceability': 'selfServiceability',
        'mode': 'mode'
    }

    def __init__(self, enabled=None, self_serviceability='NOT_SELF_SERVICEABLE', mode=None):
        """
        PaymentsProductsECheckSubscriptionInformation - a model defined in Swagger
        """

        self._enabled = None
        self._self_serviceability = None
        self._mode = None

        if enabled is not None:
          self.enabled = enabled
        if self_serviceability is not None:
          self.self_serviceability = self_serviceability
        if mode is not None:
          self.mode = mode

    @property
    def enabled(self):
        """
        Gets the enabled of this PaymentsProductsECheckSubscriptionInformation.

        :return: The enabled of this PaymentsProductsECheckSubscriptionInformation.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this PaymentsProductsECheckSubscriptionInformation.

        :param enabled: The enabled of this PaymentsProductsECheckSubscriptionInformation.
        :type: bool
        """

        self._enabled = enabled

    @property
    def self_serviceability(self):
        """
        Gets the self_serviceability of this PaymentsProductsECheckSubscriptionInformation.
        Indicates if the organization can enable this product using self service.

        :return: The self_serviceability of this PaymentsProductsECheckSubscriptionInformation.
        :rtype: str
        """
        return self._self_serviceability

    @self_serviceability.setter
    def self_serviceability(self, self_serviceability):
        """
        Sets the self_serviceability of this PaymentsProductsECheckSubscriptionInformation.
        Indicates if the organization can enable this product using self service.

        :param self_serviceability: The self_serviceability of this PaymentsProductsECheckSubscriptionInformation.
        :type: str
        """
        allowed_values = ["SELF_SERVICEABLE", "NOT_SELF_SERVICEABLE", "SELF_SERVICE_ONLY"]
        if self_serviceability not in allowed_values:
            raise ValueError(
                "Invalid value for `self_serviceability` ({0}), must be one of {1}"
                .format(self_serviceability, allowed_values)
            )

        self._self_serviceability = self_serviceability

    @property
    def mode(self):
        """
        Gets the mode of this PaymentsProductsECheckSubscriptionInformation.
        Indicates what mode the product is expected to behave at boarding and transaction flows. Ex, Acquirer/Gateway/Other.

        :return: The mode of this PaymentsProductsECheckSubscriptionInformation.
        :rtype: list[str]
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this PaymentsProductsECheckSubscriptionInformation.
        Indicates what mode the product is expected to behave at boarding and transaction flows. Ex, Acquirer/Gateway/Other.

        :param mode: The mode of this PaymentsProductsECheckSubscriptionInformation.
        :type: list[str]
        """

        self._mode = mode

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
        if not isinstance(other, PaymentsProductsECheckSubscriptionInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
