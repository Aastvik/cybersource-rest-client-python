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


class Ptsv2paymentreferencesPaymentInformation(object):
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
        'card': 'Ptsv2paymentreferencesPaymentInformationCard',
        'bank': 'Ptsv2paymentreferencesPaymentInformationBank',
        'e_wallet': 'Ptsv2paymentreferencesPaymentInformationEWallet',
        'options': 'Ptsv2paymentreferencesPaymentInformationOptions',
        'payment_type': 'Ptsv2paymentsPaymentInformationPaymentType'
    }

    attribute_map = {
        'card': 'card',
        'bank': 'bank',
        'e_wallet': 'eWallet',
        'options': 'options',
        'payment_type': 'paymentType'
    }

    def __init__(self, card=None, bank=None, e_wallet=None, options=None, payment_type=None):
        """
        Ptsv2paymentreferencesPaymentInformation - a model defined in Swagger
        """

        self._card = None
        self._bank = None
        self._e_wallet = None
        self._options = None
        self._payment_type = None

        if card is not None:
          self.card = card
        if bank is not None:
          self.bank = bank
        if e_wallet is not None:
          self.e_wallet = e_wallet
        if options is not None:
          self.options = options
        if payment_type is not None:
          self.payment_type = payment_type

    @property
    def card(self):
        """
        Gets the card of this Ptsv2paymentreferencesPaymentInformation.

        :return: The card of this Ptsv2paymentreferencesPaymentInformation.
        :rtype: Ptsv2paymentreferencesPaymentInformationCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this Ptsv2paymentreferencesPaymentInformation.

        :param card: The card of this Ptsv2paymentreferencesPaymentInformation.
        :type: Ptsv2paymentreferencesPaymentInformationCard
        """

        self._card = card

    @property
    def bank(self):
        """
        Gets the bank of this Ptsv2paymentreferencesPaymentInformation.

        :return: The bank of this Ptsv2paymentreferencesPaymentInformation.
        :rtype: Ptsv2paymentreferencesPaymentInformationBank
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """
        Sets the bank of this Ptsv2paymentreferencesPaymentInformation.

        :param bank: The bank of this Ptsv2paymentreferencesPaymentInformation.
        :type: Ptsv2paymentreferencesPaymentInformationBank
        """

        self._bank = bank

    @property
    def e_wallet(self):
        """
        Gets the e_wallet of this Ptsv2paymentreferencesPaymentInformation.

        :return: The e_wallet of this Ptsv2paymentreferencesPaymentInformation.
        :rtype: Ptsv2paymentreferencesPaymentInformationEWallet
        """
        return self._e_wallet

    @e_wallet.setter
    def e_wallet(self, e_wallet):
        """
        Sets the e_wallet of this Ptsv2paymentreferencesPaymentInformation.

        :param e_wallet: The e_wallet of this Ptsv2paymentreferencesPaymentInformation.
        :type: Ptsv2paymentreferencesPaymentInformationEWallet
        """

        self._e_wallet = e_wallet

    @property
    def options(self):
        """
        Gets the options of this Ptsv2paymentreferencesPaymentInformation.

        :return: The options of this Ptsv2paymentreferencesPaymentInformation.
        :rtype: Ptsv2paymentreferencesPaymentInformationOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this Ptsv2paymentreferencesPaymentInformation.

        :param options: The options of this Ptsv2paymentreferencesPaymentInformation.
        :type: Ptsv2paymentreferencesPaymentInformationOptions
        """

        self._options = options

    @property
    def payment_type(self):
        """
        Gets the payment_type of this Ptsv2paymentreferencesPaymentInformation.

        :return: The payment_type of this Ptsv2paymentreferencesPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationPaymentType
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """
        Sets the payment_type of this Ptsv2paymentreferencesPaymentInformation.

        :param payment_type: The payment_type of this Ptsv2paymentreferencesPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationPaymentType
        """

        self._payment_type = payment_type

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
        if not isinstance(other, Ptsv2paymentreferencesPaymentInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
