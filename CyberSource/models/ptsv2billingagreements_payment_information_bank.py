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


class Ptsv2billingagreementsPaymentInformationBank(object):
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
        'account': 'Ptsv2billingagreementsPaymentInformationBankAccount',
        'iban': 'str',
        'swift_code': 'str',
        'scheme': 'str'
    }

    attribute_map = {
        'account': 'account',
        'iban': 'iban',
        'swift_code': 'swiftCode',
        'scheme': 'scheme'
    }

    def __init__(self, account=None, iban=None, swift_code=None, scheme=None):
        """
        Ptsv2billingagreementsPaymentInformationBank - a model defined in Swagger
        """

        self._account = None
        self._iban = None
        self._swift_code = None
        self._scheme = None

        if account is not None:
          self.account = account
        if iban is not None:
          self.iban = iban
        if swift_code is not None:
          self.swift_code = swift_code
        if scheme is not None:
          self.scheme = scheme

    @property
    def account(self):
        """
        Gets the account of this Ptsv2billingagreementsPaymentInformationBank.

        :return: The account of this Ptsv2billingagreementsPaymentInformationBank.
        :rtype: Ptsv2billingagreementsPaymentInformationBankAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this Ptsv2billingagreementsPaymentInformationBank.

        :param account: The account of this Ptsv2billingagreementsPaymentInformationBank.
        :type: Ptsv2billingagreementsPaymentInformationBankAccount
        """

        self._account = account

    @property
    def iban(self):
        """
        Gets the iban of this Ptsv2billingagreementsPaymentInformationBank.
        International Bank Account Number (IBAN). #### SEPA Required for mandates services 

        :return: The iban of this Ptsv2billingagreementsPaymentInformationBank.
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """
        Sets the iban of this Ptsv2billingagreementsPaymentInformationBank.
        International Bank Account Number (IBAN). #### SEPA Required for mandates services 

        :param iban: The iban of this Ptsv2billingagreementsPaymentInformationBank.
        :type: str
        """

        self._iban = iban

    @property
    def swift_code(self):
        """
        Gets the swift_code of this Ptsv2billingagreementsPaymentInformationBank.
        Bank's SWIFT code. You can use this field only when scoring a direct debit transaction. #### BACS Required for mandates services 

        :return: The swift_code of this Ptsv2billingagreementsPaymentInformationBank.
        :rtype: str
        """
        return self._swift_code

    @swift_code.setter
    def swift_code(self, swift_code):
        """
        Sets the swift_code of this Ptsv2billingagreementsPaymentInformationBank.
        Bank's SWIFT code. You can use this field only when scoring a direct debit transaction. #### BACS Required for mandates services 

        :param swift_code: The swift_code of this Ptsv2billingagreementsPaymentInformationBank.
        :type: str
        """

        self._swift_code = swift_code

    @property
    def scheme(self):
        """
        Gets the scheme of this Ptsv2billingagreementsPaymentInformationBank.
        The scheme that sets the rules for the direct debit process. Possible values:   - SEPA   - BACS #### SEPA/BACS Required for mandates services 

        :return: The scheme of this Ptsv2billingagreementsPaymentInformationBank.
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """
        Sets the scheme of this Ptsv2billingagreementsPaymentInformationBank.
        The scheme that sets the rules for the direct debit process. Possible values:   - SEPA   - BACS #### SEPA/BACS Required for mandates services 

        :param scheme: The scheme of this Ptsv2billingagreementsPaymentInformationBank.
        :type: str
        """

        self._scheme = scheme

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
        if not isinstance(other, Ptsv2billingagreementsPaymentInformationBank):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
