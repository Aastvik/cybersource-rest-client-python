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


class Ptsv2paymentsPaymentInformationSepa(object):
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
        'direct_debit': 'Ptsv2paymentsPaymentInformationSepaDirectDebit'
    }

    attribute_map = {
        'direct_debit': 'directDebit'
    }

    def __init__(self, direct_debit=None):
        """
        Ptsv2paymentsPaymentInformationSepa - a model defined in Swagger
        """

        self._direct_debit = None

        if direct_debit is not None:
          self.direct_debit = direct_debit

    @property
    def direct_debit(self):
        """
        Gets the direct_debit of this Ptsv2paymentsPaymentInformationSepa.

        :return: The direct_debit of this Ptsv2paymentsPaymentInformationSepa.
        :rtype: Ptsv2paymentsPaymentInformationSepaDirectDebit
        """
        return self._direct_debit

    @direct_debit.setter
    def direct_debit(self, direct_debit):
        """
        Sets the direct_debit of this Ptsv2paymentsPaymentInformationSepa.

        :param direct_debit: The direct_debit of this Ptsv2paymentsPaymentInformationSepa.
        :type: Ptsv2paymentsPaymentInformationSepaDirectDebit
        """

        self._direct_debit = direct_debit

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
        if not isinstance(other, Ptsv2paymentsPaymentInformationSepa):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
