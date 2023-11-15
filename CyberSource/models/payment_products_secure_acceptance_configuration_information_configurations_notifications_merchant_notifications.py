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


class PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications(object):
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
        'backoffice_post_enabled': 'bool',
        'backoffice_email_address': 'str',
        'backoffice_email_enabled': 'bool',
        'backoffice_post_url': 'str',
        'card_number_format': 'str'
    }

    attribute_map = {
        'backoffice_post_enabled': 'backofficePostEnabled',
        'backoffice_email_address': 'backofficeEmailAddress',
        'backoffice_email_enabled': 'backofficeEmailEnabled',
        'backoffice_post_url': 'backofficePostUrl',
        'card_number_format': 'cardNumberFormat'
    }

    def __init__(self, backoffice_post_enabled=None, backoffice_email_address=None, backoffice_email_enabled=None, backoffice_post_url=None, card_number_format=None):
        """
        PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications - a model defined in Swagger
        """

        self._backoffice_post_enabled = None
        self._backoffice_email_address = None
        self._backoffice_email_enabled = None
        self._backoffice_post_url = None
        self._card_number_format = None

        if backoffice_post_enabled is not None:
          self.backoffice_post_enabled = backoffice_post_enabled
        if backoffice_email_address is not None:
          self.backoffice_email_address = backoffice_email_address
        if backoffice_email_enabled is not None:
          self.backoffice_email_enabled = backoffice_email_enabled
        if backoffice_post_url is not None:
          self.backoffice_post_url = backoffice_post_url
        if card_number_format is not None:
          self.card_number_format = card_number_format

    @property
    def backoffice_post_enabled(self):
        """
        Gets the backoffice_post_enabled of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        Enables Webhook transaction confirmation messages sent to URL defined in backofficePostUrl. Usually enabled by web developers integrating to Secure Acceptance.

        :return: The backoffice_post_enabled of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        :rtype: bool
        """
        return self._backoffice_post_enabled

    @backoffice_post_enabled.setter
    def backoffice_post_enabled(self, backoffice_post_enabled):
        """
        Sets the backoffice_post_enabled of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        Enables Webhook transaction confirmation messages sent to URL defined in backofficePostUrl. Usually enabled by web developers integrating to Secure Acceptance.

        :param backoffice_post_enabled: The backoffice_post_enabled of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        :type: bool
        """

        self._backoffice_post_enabled = backoffice_post_enabled

    @property
    def backoffice_email_address(self):
        """
        Gets the backoffice_email_address of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        Email address to receive transaction confirmation messages.

        :return: The backoffice_email_address of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        :rtype: str
        """
        return self._backoffice_email_address

    @backoffice_email_address.setter
    def backoffice_email_address(self, backoffice_email_address):
        """
        Sets the backoffice_email_address of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        Email address to receive transaction confirmation messages.

        :param backoffice_email_address: The backoffice_email_address of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        :type: str
        """

        self._backoffice_email_address = backoffice_email_address

    @property
    def backoffice_email_enabled(self):
        """
        Gets the backoffice_email_enabled of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        Enables email transaction confirmation messages, sent to the address specified in backofficeEmailAddress.

        :return: The backoffice_email_enabled of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        :rtype: bool
        """
        return self._backoffice_email_enabled

    @backoffice_email_enabled.setter
    def backoffice_email_enabled(self, backoffice_email_enabled):
        """
        Sets the backoffice_email_enabled of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        Enables email transaction confirmation messages, sent to the address specified in backofficeEmailAddress.

        :param backoffice_email_enabled: The backoffice_email_enabled of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        :type: bool
        """

        self._backoffice_email_enabled = backoffice_email_enabled

    @property
    def backoffice_post_url(self):
        """
        Gets the backoffice_post_url of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        Webhook URL to which transaction confirmation is sent. Usually completed by the web developers integrating to Secure Acceptance.

        :return: The backoffice_post_url of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        :rtype: str
        """
        return self._backoffice_post_url

    @backoffice_post_url.setter
    def backoffice_post_url(self, backoffice_post_url):
        """
        Sets the backoffice_post_url of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        Webhook URL to which transaction confirmation is sent. Usually completed by the web developers integrating to Secure Acceptance.

        :param backoffice_post_url: The backoffice_post_url of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        :type: str
        """

        self._backoffice_post_url = backoffice_post_url

    @property
    def card_number_format(self):
        """
        Gets the card_number_format of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        Format in which the card number should be masked in the notifications.   Valid values: `1` - Display first 6 digits only (e.g. \"444433**********\")  `2` - Display last four digits only (e.g. \"************1111\")  `3` - Display First six and last four digits (e.g. \"444433******1111\") 

        :return: The card_number_format of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        :rtype: str
        """
        return self._card_number_format

    @card_number_format.setter
    def card_number_format(self, card_number_format):
        """
        Sets the card_number_format of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        Format in which the card number should be masked in the notifications.   Valid values: `1` - Display first 6 digits only (e.g. \"444433**********\")  `2` - Display last four digits only (e.g. \"************1111\")  `3` - Display First six and last four digits (e.g. \"444433******1111\") 

        :param card_number_format: The card_number_format of this PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications.
        :type: str
        """

        self._card_number_format = card_number_format

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
        if not isinstance(other, PaymentProductsSecureAcceptanceConfigurationInformationConfigurationsNotificationsMerchantNotifications):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
