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


class SAConfigPaymentTypesCardTypes(object):
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
        'discover': 'SAConfigPaymentTypesCardTypesDiscover',
        'amex': 'SAConfigPaymentTypesCardTypesDiscover',
        'master_card': 'SAConfigPaymentTypesCardTypesDiscover',
        'visa': 'SAConfigPaymentTypesCardTypesDiscover'
    }

    attribute_map = {
        'discover': 'discover',
        'amex': 'amex',
        'master_card': 'masterCard',
        'visa': 'visa'
    }

    def __init__(self, discover=None, amex=None, master_card=None, visa=None):
        """
        SAConfigPaymentTypesCardTypes - a model defined in Swagger
        """

        self._discover = None
        self._amex = None
        self._master_card = None
        self._visa = None

        if discover is not None:
          self.discover = discover
        if amex is not None:
          self.amex = amex
        if master_card is not None:
          self.master_card = master_card
        if visa is not None:
          self.visa = visa

    @property
    def discover(self):
        """
        Gets the discover of this SAConfigPaymentTypesCardTypes.

        :return: The discover of this SAConfigPaymentTypesCardTypes.
        :rtype: SAConfigPaymentTypesCardTypesDiscover
        """
        return self._discover

    @discover.setter
    def discover(self, discover):
        """
        Sets the discover of this SAConfigPaymentTypesCardTypes.

        :param discover: The discover of this SAConfigPaymentTypesCardTypes.
        :type: SAConfigPaymentTypesCardTypesDiscover
        """

        self._discover = discover

    @property
    def amex(self):
        """
        Gets the amex of this SAConfigPaymentTypesCardTypes.

        :return: The amex of this SAConfigPaymentTypesCardTypes.
        :rtype: SAConfigPaymentTypesCardTypesDiscover
        """
        return self._amex

    @amex.setter
    def amex(self, amex):
        """
        Sets the amex of this SAConfigPaymentTypesCardTypes.

        :param amex: The amex of this SAConfigPaymentTypesCardTypes.
        :type: SAConfigPaymentTypesCardTypesDiscover
        """

        self._amex = amex

    @property
    def master_card(self):
        """
        Gets the master_card of this SAConfigPaymentTypesCardTypes.

        :return: The master_card of this SAConfigPaymentTypesCardTypes.
        :rtype: SAConfigPaymentTypesCardTypesDiscover
        """
        return self._master_card

    @master_card.setter
    def master_card(self, master_card):
        """
        Sets the master_card of this SAConfigPaymentTypesCardTypes.

        :param master_card: The master_card of this SAConfigPaymentTypesCardTypes.
        :type: SAConfigPaymentTypesCardTypesDiscover
        """

        self._master_card = master_card

    @property
    def visa(self):
        """
        Gets the visa of this SAConfigPaymentTypesCardTypes.

        :return: The visa of this SAConfigPaymentTypesCardTypes.
        :rtype: SAConfigPaymentTypesCardTypesDiscover
        """
        return self._visa

    @visa.setter
    def visa(self, visa):
        """
        Sets the visa of this SAConfigPaymentTypesCardTypes.

        :param visa: The visa of this SAConfigPaymentTypesCardTypes.
        :type: SAConfigPaymentTypesCardTypesDiscover
        """

        self._visa = visa

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
        if not isinstance(other, SAConfigPaymentTypesCardTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
