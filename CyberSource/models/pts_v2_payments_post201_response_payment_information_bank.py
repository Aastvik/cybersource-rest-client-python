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


class PtsV2PaymentsPost201ResponsePaymentInformationBank(object):
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
        'account': 'PtsV2PaymentsPost201ResponsePaymentInformationBankAccount',
        'corrected_routing_number': 'str'
    }

    attribute_map = {
        'account': 'account',
        'corrected_routing_number': 'correctedRoutingNumber'
    }

    def __init__(self, account=None, corrected_routing_number=None):
        """
        PtsV2PaymentsPost201ResponsePaymentInformationBank - a model defined in Swagger
        """

        self._account = None
        self._corrected_routing_number = None

        if account is not None:
          self.account = account
        if corrected_routing_number is not None:
          self.corrected_routing_number = corrected_routing_number

    @property
    def account(self):
        """
        Gets the account of this PtsV2PaymentsPost201ResponsePaymentInformationBank.

        :return: The account of this PtsV2PaymentsPost201ResponsePaymentInformationBank.
        :rtype: PtsV2PaymentsPost201ResponsePaymentInformationBankAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this PtsV2PaymentsPost201ResponsePaymentInformationBank.

        :param account: The account of this PtsV2PaymentsPost201ResponsePaymentInformationBank.
        :type: PtsV2PaymentsPost201ResponsePaymentInformationBankAccount
        """

        self._account = account

    @property
    def corrected_routing_number(self):
        """
        Gets the corrected_routing_number of this PtsV2PaymentsPost201ResponsePaymentInformationBank.
        The description for this field is not available.

        :return: The corrected_routing_number of this PtsV2PaymentsPost201ResponsePaymentInformationBank.
        :rtype: str
        """
        return self._corrected_routing_number

    @corrected_routing_number.setter
    def corrected_routing_number(self, corrected_routing_number):
        """
        Sets the corrected_routing_number of this PtsV2PaymentsPost201ResponsePaymentInformationBank.
        The description for this field is not available.

        :param corrected_routing_number: The corrected_routing_number of this PtsV2PaymentsPost201ResponsePaymentInformationBank.
        :type: str
        """
        if corrected_routing_number is not None and len(corrected_routing_number) > 9:
            raise ValueError("Invalid value for `corrected_routing_number`, length must be less than or equal to `9`")

        self._corrected_routing_number = corrected_routing_number

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
        if not isinstance(other, PtsV2PaymentsPost201ResponsePaymentInformationBank):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
