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


class Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator(object):
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
        'type': 'str',
        'credential_stored_on_file': 'bool',
        'stored_credential_used': 'bool',
        'merchant_initiated_transaction': 'Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction'
    }

    attribute_map = {
        'type': 'type',
        'credential_stored_on_file': 'credentialStoredOnFile',
        'stored_credential_used': 'storedCredentialUsed',
        'merchant_initiated_transaction': 'merchantInitiatedTransaction'
    }

    def __init__(self, type=None, credential_stored_on_file=None, stored_credential_used=None, merchant_initiated_transaction=None):
        """
        Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator - a model defined in Swagger
        """

        self._type = None
        self._credential_stored_on_file = None
        self._stored_credential_used = None
        self._merchant_initiated_transaction = None

        if type is not None:
          self.type = type
        if credential_stored_on_file is not None:
          self.credential_stored_on_file = credential_stored_on_file
        if stored_credential_used is not None:
          self.stored_credential_used = stored_credential_used
        if merchant_initiated_transaction is not None:
          self.merchant_initiated_transaction = merchant_initiated_transaction

    @property
    def type(self):
        """
        Gets the type of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator.
        This field indicates whether the transaction is a merchant-initiated transaction or customer-initiated transaction.  Valid values: - **customer** - **merchant** 

        :return: The type of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator.
        This field indicates whether the transaction is a merchant-initiated transaction or customer-initiated transaction.  Valid values: - **customer** - **merchant** 

        :param type: The type of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator.
        :type: str
        """

        self._type = type

    @property
    def credential_stored_on_file(self):
        """
        Gets the credential_stored_on_file of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator.
        Indicates to the issuing bank two things: - The merchant has received consent from the cardholder to store their card details on file - The merchant wants the issuing bank to check out the card details before the merchant initiates their first transaction for this cardholder. The purpose of the merchant-initiated transaction is to ensure that the cardholder's credentials are valid (that the card is not stolen or has restrictions) and that the card details are good to be stored on the merchant's file for future transactions.  Valid values: - `true` means merchant will use this transaction to store payment credentials for follow-up merchant-initiated transactions. - `false` means merchant will not use this transaction to store payment credentials for follow-up merchant-initiated transactions.  For details, see `subsequent_auth_first` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  **NOTE:** The value for this field does not correspond to any data in the TC 33 capture file5.  This field is supported only for Visa transactions on CyberSource through VisaNet. 

        :return: The credential_stored_on_file of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator.
        :rtype: bool
        """
        return self._credential_stored_on_file

    @credential_stored_on_file.setter
    def credential_stored_on_file(self, credential_stored_on_file):
        """
        Sets the credential_stored_on_file of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator.
        Indicates to the issuing bank two things: - The merchant has received consent from the cardholder to store their card details on file - The merchant wants the issuing bank to check out the card details before the merchant initiates their first transaction for this cardholder. The purpose of the merchant-initiated transaction is to ensure that the cardholder's credentials are valid (that the card is not stolen or has restrictions) and that the card details are good to be stored on the merchant's file for future transactions.  Valid values: - `true` means merchant will use this transaction to store payment credentials for follow-up merchant-initiated transactions. - `false` means merchant will not use this transaction to store payment credentials for follow-up merchant-initiated transactions.  For details, see `subsequent_auth_first` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  **NOTE:** The value for this field does not correspond to any data in the TC 33 capture file5.  This field is supported only for Visa transactions on CyberSource through VisaNet. 

        :param credential_stored_on_file: The credential_stored_on_file of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator.
        :type: bool
        """

        self._credential_stored_on_file = credential_stored_on_file

    @property
    def stored_credential_used(self):
        """
        Gets the stored_credential_used of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator.
        Indicates to an issuing bank whether a merchant-initiated transaction came from a card that was already stored on file.  Possible values: - **true** means the merchant-initiated transaction came from a card that was already stored on file. - **false**  means the merchant-initiated transaction came from a card that was not stored on file. 

        :return: The stored_credential_used of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator.
        :rtype: bool
        """
        return self._stored_credential_used

    @stored_credential_used.setter
    def stored_credential_used(self, stored_credential_used):
        """
        Sets the stored_credential_used of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator.
        Indicates to an issuing bank whether a merchant-initiated transaction came from a card that was already stored on file.  Possible values: - **true** means the merchant-initiated transaction came from a card that was already stored on file. - **false**  means the merchant-initiated transaction came from a card that was not stored on file. 

        :param stored_credential_used: The stored_credential_used of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator.
        :type: bool
        """

        self._stored_credential_used = stored_credential_used

    @property
    def merchant_initiated_transaction(self):
        """
        Gets the merchant_initiated_transaction of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator.

        :return: The merchant_initiated_transaction of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator.
        :rtype: Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction
        """
        return self._merchant_initiated_transaction

    @merchant_initiated_transaction.setter
    def merchant_initiated_transaction(self, merchant_initiated_transaction):
        """
        Sets the merchant_initiated_transaction of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator.

        :param merchant_initiated_transaction: The merchant_initiated_transaction of this Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator.
        :type: Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiatorMerchantInitiatedTransaction
        """

        self._merchant_initiated_transaction = merchant_initiated_transaction

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
        if not isinstance(other, Ptsv2paymentsProcessingInformationAuthorizationOptionsInitiator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
