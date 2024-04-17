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


class ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges(object):
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
        'merchant_reference_number': 'str',
        'transaction_reference_number': 'str',
        'time': 'datetime',
        'code': 'str',
        'account_type': 'str',
        'routing_number': 'str',
        'account_number': 'str',
        'consumer_name': 'str'
    }

    attribute_map = {
        'merchant_reference_number': 'merchantReferenceNumber',
        'transaction_reference_number': 'transactionReferenceNumber',
        'time': 'time',
        'code': 'code',
        'account_type': 'accountType',
        'routing_number': 'routingNumber',
        'account_number': 'accountNumber',
        'consumer_name': 'consumerName'
    }

    def __init__(self, merchant_reference_number=None, transaction_reference_number=None, time=None, code=None, account_type=None, routing_number=None, account_number=None, consumer_name=None):
        """
        ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges - a model defined in Swagger
        """

        self._merchant_reference_number = None
        self._transaction_reference_number = None
        self._time = None
        self._code = None
        self._account_type = None
        self._routing_number = None
        self._account_number = None
        self._consumer_name = None

        if merchant_reference_number is not None:
          self.merchant_reference_number = merchant_reference_number
        if transaction_reference_number is not None:
          self.transaction_reference_number = transaction_reference_number
        if time is not None:
          self.time = time
        if code is not None:
          self.code = code
        if account_type is not None:
          self.account_type = account_type
        if routing_number is not None:
          self.routing_number = routing_number
        if account_number is not None:
          self.account_number = account_number
        if consumer_name is not None:
          self.consumer_name = consumer_name

    @property
    def merchant_reference_number(self):
        """
        Gets the merchant_reference_number of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        Merchant Reference Number

        :return: The merchant_reference_number of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        :rtype: str
        """
        return self._merchant_reference_number

    @merchant_reference_number.setter
    def merchant_reference_number(self, merchant_reference_number):
        """
        Sets the merchant_reference_number of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        Merchant Reference Number

        :param merchant_reference_number: The merchant_reference_number of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        :type: str
        """

        self._merchant_reference_number = merchant_reference_number

    @property
    def transaction_reference_number(self):
        """
        Gets the transaction_reference_number of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        Transaction Reference Number

        :return: The transaction_reference_number of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        :rtype: str
        """
        return self._transaction_reference_number

    @transaction_reference_number.setter
    def transaction_reference_number(self, transaction_reference_number):
        """
        Sets the transaction_reference_number of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        Transaction Reference Number

        :param transaction_reference_number: The transaction_reference_number of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        :type: str
        """

        self._transaction_reference_number = transaction_reference_number

    @property
    def time(self):
        """
        Gets the time of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        Notification Of Change Date(ISO 8601 Extended)

        :return: The time of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        Notification Of Change Date(ISO 8601 Extended)

        :param time: The time of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        :type: datetime
        """

        self._time = time

    @property
    def code(self):
        """
        Gets the code of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        Merchant Reference Number

        :return: The code of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        Merchant Reference Number

        :param code: The code of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        :type: str
        """

        self._code = code

    @property
    def account_type(self):
        """
        Gets the account_type of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        Account Type

        :return: The account_type of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """
        Sets the account_type of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        Account Type

        :param account_type: The account_type of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        :type: str
        """

        self._account_type = account_type

    @property
    def routing_number(self):
        """
        Gets the routing_number of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        Routing Number

        :return: The routing_number of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        :rtype: str
        """
        return self._routing_number

    @routing_number.setter
    def routing_number(self, routing_number):
        """
        Sets the routing_number of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        Routing Number

        :param routing_number: The routing_number of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        :type: str
        """

        self._routing_number = routing_number

    @property
    def account_number(self):
        """
        Gets the account_number of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        Account Number

        :return: The account_number of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """
        Sets the account_number of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        Account Number

        :param account_number: The account_number of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        :type: str
        """

        self._account_number = account_number

    @property
    def consumer_name(self):
        """
        Gets the consumer_name of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        Consumer Name

        :return: The consumer_name of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        :rtype: str
        """
        return self._consumer_name

    @consumer_name.setter
    def consumer_name(self, consumer_name):
        """
        Sets the consumer_name of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        Consumer Name

        :param consumer_name: The consumer_name of this ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges.
        :type: str
        """

        self._consumer_name = consumer_name

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
        if not isinstance(other, ReportingV3NotificationofChangesGet200ResponseNotificationOfChanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
