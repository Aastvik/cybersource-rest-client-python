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


class Ptsv1pushfundstransferOrderInformationAmountDetails(object):
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
        'total_amount': 'str',
        'currency': 'str'
    }

    attribute_map = {
        'total_amount': 'totalAmount',
        'currency': 'currency'
    }

    def __init__(self, total_amount=None, currency=None):
        """
        Ptsv1pushfundstransferOrderInformationAmountDetails - a model defined in Swagger
        """

        self._total_amount = None
        self._currency = None

        self.total_amount = total_amount
        self.currency = currency

    @property
    def total_amount(self):
        """
        Gets the total_amount of this Ptsv1pushfundstransferOrderInformationAmountDetails.
        Grand total for the order. This value cannot be negative. You can include a decimal point (.), but no other special characters. CyberSource truncates the amount to the correct number of decimal places.  The disbursement amount. Numeric integer, 1-999999999999. The decimal point is implied based on the relevant currency exponent. For example, a US Dollar $53 amount is a value of 5300.  Processor Amount Ranges: Visa Platform Connect: .01-9999999999.99  Mastercard Send: 1-9999999999.99  FDC Compass: .01- 9999999999.99  Chase Paymentech: .01-9999999999.99 

        :return: The total_amount of this Ptsv1pushfundstransferOrderInformationAmountDetails.
        :rtype: str
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """
        Sets the total_amount of this Ptsv1pushfundstransferOrderInformationAmountDetails.
        Grand total for the order. This value cannot be negative. You can include a decimal point (.), but no other special characters. CyberSource truncates the amount to the correct number of decimal places.  The disbursement amount. Numeric integer, 1-999999999999. The decimal point is implied based on the relevant currency exponent. For example, a US Dollar $53 amount is a value of 5300.  Processor Amount Ranges: Visa Platform Connect: .01-9999999999.99  Mastercard Send: 1-9999999999.99  FDC Compass: .01- 9999999999.99  Chase Paymentech: .01-9999999999.99 

        :param total_amount: The total_amount of this Ptsv1pushfundstransferOrderInformationAmountDetails.
        :type: str
        """
        if total_amount is None:
            raise ValueError("Invalid value for `total_amount`, must not be `None`")

        self._total_amount = total_amount

    @property
    def currency(self):
        """
        Gets the currency of this Ptsv1pushfundstransferOrderInformationAmountDetails.
        Use a 3-character alpha currency code for currency of the sender.  ISO standard currencies: http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf  Currency must be supported by the processor. 

        :return: The currency of this Ptsv1pushfundstransferOrderInformationAmountDetails.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Ptsv1pushfundstransferOrderInformationAmountDetails.
        Use a 3-character alpha currency code for currency of the sender.  ISO standard currencies: http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf  Currency must be supported by the processor. 

        :param currency: The currency of this Ptsv1pushfundstransferOrderInformationAmountDetails.
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")

        self._currency = currency

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
        if not isinstance(other, Ptsv1pushfundstransferOrderInformationAmountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
