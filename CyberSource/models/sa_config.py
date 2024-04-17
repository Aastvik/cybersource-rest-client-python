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


class SAConfig(object):
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
        'parent_profile_id': 'str',
        'contact_information': 'SAConfigContactInformation',
        'notifications': 'SAConfigNotifications',
        'service': 'SAConfigService',
        'payment_methods': 'SAConfigPaymentMethods',
        'checkout': 'SAConfigCheckout',
        'payment_types': 'SAConfigPaymentTypes'
    }

    attribute_map = {
        'parent_profile_id': 'parentProfileId',
        'contact_information': 'contactInformation',
        'notifications': 'notifications',
        'service': 'service',
        'payment_methods': 'paymentMethods',
        'checkout': 'checkout',
        'payment_types': 'paymentTypes'
    }

    def __init__(self, parent_profile_id=None, contact_information=None, notifications=None, service=None, payment_methods=None, checkout=None, payment_types=None):
        """
        SAConfig - a model defined in Swagger
        """

        self._parent_profile_id = None
        self._contact_information = None
        self._notifications = None
        self._service = None
        self._payment_methods = None
        self._checkout = None
        self._payment_types = None

        if parent_profile_id is not None:
          self.parent_profile_id = parent_profile_id
        if contact_information is not None:
          self.contact_information = contact_information
        if notifications is not None:
          self.notifications = notifications
        if service is not None:
          self.service = service
        if payment_methods is not None:
          self.payment_methods = payment_methods
        if checkout is not None:
          self.checkout = checkout
        if payment_types is not None:
          self.payment_types = payment_types

    @property
    def parent_profile_id(self):
        """
        Gets the parent_profile_id of this SAConfig.
        You can group Secure Acceptance profiles under parent profiles. By changing the parent profile, you can update all profiles underneath that parent. Specify the Parent Profile ID here.

        :return: The parent_profile_id of this SAConfig.
        :rtype: str
        """
        return self._parent_profile_id

    @parent_profile_id.setter
    def parent_profile_id(self, parent_profile_id):
        """
        Sets the parent_profile_id of this SAConfig.
        You can group Secure Acceptance profiles under parent profiles. By changing the parent profile, you can update all profiles underneath that parent. Specify the Parent Profile ID here.

        :param parent_profile_id: The parent_profile_id of this SAConfig.
        :type: str
        """

        self._parent_profile_id = parent_profile_id

    @property
    def contact_information(self):
        """
        Gets the contact_information of this SAConfig.

        :return: The contact_information of this SAConfig.
        :rtype: SAConfigContactInformation
        """
        return self._contact_information

    @contact_information.setter
    def contact_information(self, contact_information):
        """
        Sets the contact_information of this SAConfig.

        :param contact_information: The contact_information of this SAConfig.
        :type: SAConfigContactInformation
        """

        self._contact_information = contact_information

    @property
    def notifications(self):
        """
        Gets the notifications of this SAConfig.

        :return: The notifications of this SAConfig.
        :rtype: SAConfigNotifications
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """
        Sets the notifications of this SAConfig.

        :param notifications: The notifications of this SAConfig.
        :type: SAConfigNotifications
        """

        self._notifications = notifications

    @property
    def service(self):
        """
        Gets the service of this SAConfig.

        :return: The service of this SAConfig.
        :rtype: SAConfigService
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this SAConfig.

        :param service: The service of this SAConfig.
        :type: SAConfigService
        """

        self._service = service

    @property
    def payment_methods(self):
        """
        Gets the payment_methods of this SAConfig.

        :return: The payment_methods of this SAConfig.
        :rtype: SAConfigPaymentMethods
        """
        return self._payment_methods

    @payment_methods.setter
    def payment_methods(self, payment_methods):
        """
        Sets the payment_methods of this SAConfig.

        :param payment_methods: The payment_methods of this SAConfig.
        :type: SAConfigPaymentMethods
        """

        self._payment_methods = payment_methods

    @property
    def checkout(self):
        """
        Gets the checkout of this SAConfig.

        :return: The checkout of this SAConfig.
        :rtype: SAConfigCheckout
        """
        return self._checkout

    @checkout.setter
    def checkout(self, checkout):
        """
        Sets the checkout of this SAConfig.

        :param checkout: The checkout of this SAConfig.
        :type: SAConfigCheckout
        """

        self._checkout = checkout

    @property
    def payment_types(self):
        """
        Gets the payment_types of this SAConfig.

        :return: The payment_types of this SAConfig.
        :rtype: SAConfigPaymentTypes
        """
        return self._payment_types

    @payment_types.setter
    def payment_types(self, payment_types):
        """
        Sets the payment_types of this SAConfig.

        :param payment_types: The payment_types of this SAConfig.
        :type: SAConfigPaymentTypes
        """

        self._payment_types = payment_types

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
        if not isinstance(other, SAConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
