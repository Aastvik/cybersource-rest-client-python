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


class PtsV2ModifyBillingAgreementPost201ResponsePaymentInformation(object):
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
        'e_wallet': 'PtsV2ModifyBillingAgreementPost201ResponsePaymentInformationEWallet',
        'bank': 'PtsV2ModifyBillingAgreementPost201ResponsePaymentInformationBank'
    }

    attribute_map = {
        'e_wallet': 'eWallet',
        'bank': 'bank'
    }

    def __init__(self, e_wallet=None, bank=None):
        """
        PtsV2ModifyBillingAgreementPost201ResponsePaymentInformation - a model defined in Swagger
        """

        self._e_wallet = None
        self._bank = None

        if e_wallet is not None:
          self.e_wallet = e_wallet
        if bank is not None:
          self.bank = bank

    @property
    def e_wallet(self):
        """
        Gets the e_wallet of this PtsV2ModifyBillingAgreementPost201ResponsePaymentInformation.

        :return: The e_wallet of this PtsV2ModifyBillingAgreementPost201ResponsePaymentInformation.
        :rtype: PtsV2ModifyBillingAgreementPost201ResponsePaymentInformationEWallet
        """
        return self._e_wallet

    @e_wallet.setter
    def e_wallet(self, e_wallet):
        """
        Sets the e_wallet of this PtsV2ModifyBillingAgreementPost201ResponsePaymentInformation.

        :param e_wallet: The e_wallet of this PtsV2ModifyBillingAgreementPost201ResponsePaymentInformation.
        :type: PtsV2ModifyBillingAgreementPost201ResponsePaymentInformationEWallet
        """

        self._e_wallet = e_wallet

    @property
    def bank(self):
        """
        Gets the bank of this PtsV2ModifyBillingAgreementPost201ResponsePaymentInformation.

        :return: The bank of this PtsV2ModifyBillingAgreementPost201ResponsePaymentInformation.
        :rtype: PtsV2ModifyBillingAgreementPost201ResponsePaymentInformationBank
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """
        Sets the bank of this PtsV2ModifyBillingAgreementPost201ResponsePaymentInformation.

        :param bank: The bank of this PtsV2ModifyBillingAgreementPost201ResponsePaymentInformation.
        :type: PtsV2ModifyBillingAgreementPost201ResponsePaymentInformationBank
        """

        self._bank = bank

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
        if not isinstance(other, PtsV2ModifyBillingAgreementPost201ResponsePaymentInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
