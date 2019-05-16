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


class InlineResponse200PaymentBatchSummaries(object):
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
        'currency_code': 'str',
        'payment_sub_type_description': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'sales_count': 'int',
        'sales_amount': 'str',
        'credit_count': 'int',
        'credit_amount': 'str',
        'account_name': 'str',
        'account_id': 'str',
        'merchant_id': 'str',
        'merchant_name': 'str'
    }

    attribute_map = {
        'currency_code': 'currencyCode',
        'payment_sub_type_description': 'paymentSubTypeDescription',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'sales_count': 'salesCount',
        'sales_amount': 'salesAmount',
        'credit_count': 'creditCount',
        'credit_amount': 'creditAmount',
        'account_name': 'accountName',
        'account_id': 'accountId',
        'merchant_id': 'merchantId',
        'merchant_name': 'merchantName'
    }

    def __init__(self, currency_code=None, payment_sub_type_description=None, start_time=None, end_time=None, sales_count=None, sales_amount=None, credit_count=None, credit_amount=None, account_name=None, account_id=None, merchant_id=None, merchant_name=None):
        """
        InlineResponse200PaymentBatchSummaries - a model defined in Swagger
        """

        self._currency_code = None
        self._payment_sub_type_description = None
        self._start_time = None
        self._end_time = None
        self._sales_count = None
        self._sales_amount = None
        self._credit_count = None
        self._credit_amount = None
        self._account_name = None
        self._account_id = None
        self._merchant_id = None
        self._merchant_name = None

        if currency_code is not None:
          self.currency_code = currency_code
        if payment_sub_type_description is not None:
          self.payment_sub_type_description = payment_sub_type_description
        if start_time is not None:
          self.start_time = start_time
        if end_time is not None:
          self.end_time = end_time
        if sales_count is not None:
          self.sales_count = sales_count
        if sales_amount is not None:
          self.sales_amount = sales_amount
        if credit_count is not None:
          self.credit_count = credit_count
        if credit_amount is not None:
          self.credit_amount = credit_amount
        if account_name is not None:
          self.account_name = account_name
        if account_id is not None:
          self.account_id = account_id
        if merchant_id is not None:
          self.merchant_id = merchant_id
        if merchant_name is not None:
          self.merchant_name = merchant_name

    @property
    def currency_code(self):
        """
        Gets the currency_code of this InlineResponse200PaymentBatchSummaries.

        :return: The currency_code of this InlineResponse200PaymentBatchSummaries.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this InlineResponse200PaymentBatchSummaries.

        :param currency_code: The currency_code of this InlineResponse200PaymentBatchSummaries.
        :type: str
        """

        self._currency_code = currency_code

    @property
    def payment_sub_type_description(self):
        """
        Gets the payment_sub_type_description of this InlineResponse200PaymentBatchSummaries.

        :return: The payment_sub_type_description of this InlineResponse200PaymentBatchSummaries.
        :rtype: str
        """
        return self._payment_sub_type_description

    @payment_sub_type_description.setter
    def payment_sub_type_description(self, payment_sub_type_description):
        """
        Sets the payment_sub_type_description of this InlineResponse200PaymentBatchSummaries.

        :param payment_sub_type_description: The payment_sub_type_description of this InlineResponse200PaymentBatchSummaries.
        :type: str
        """

        self._payment_sub_type_description = payment_sub_type_description

    @property
    def start_time(self):
        """
        Gets the start_time of this InlineResponse200PaymentBatchSummaries.

        :return: The start_time of this InlineResponse200PaymentBatchSummaries.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this InlineResponse200PaymentBatchSummaries.

        :param start_time: The start_time of this InlineResponse200PaymentBatchSummaries.
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this InlineResponse200PaymentBatchSummaries.

        :return: The end_time of this InlineResponse200PaymentBatchSummaries.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this InlineResponse200PaymentBatchSummaries.

        :param end_time: The end_time of this InlineResponse200PaymentBatchSummaries.
        :type: datetime
        """

        self._end_time = end_time

    @property
    def sales_count(self):
        """
        Gets the sales_count of this InlineResponse200PaymentBatchSummaries.

        :return: The sales_count of this InlineResponse200PaymentBatchSummaries.
        :rtype: int
        """
        return self._sales_count

    @sales_count.setter
    def sales_count(self, sales_count):
        """
        Sets the sales_count of this InlineResponse200PaymentBatchSummaries.

        :param sales_count: The sales_count of this InlineResponse200PaymentBatchSummaries.
        :type: int
        """

        self._sales_count = sales_count

    @property
    def sales_amount(self):
        """
        Gets the sales_amount of this InlineResponse200PaymentBatchSummaries.

        :return: The sales_amount of this InlineResponse200PaymentBatchSummaries.
        :rtype: str
        """
        return self._sales_amount

    @sales_amount.setter
    def sales_amount(self, sales_amount):
        """
        Sets the sales_amount of this InlineResponse200PaymentBatchSummaries.

        :param sales_amount: The sales_amount of this InlineResponse200PaymentBatchSummaries.
        :type: str
        """

        self._sales_amount = sales_amount

    @property
    def credit_count(self):
        """
        Gets the credit_count of this InlineResponse200PaymentBatchSummaries.

        :return: The credit_count of this InlineResponse200PaymentBatchSummaries.
        :rtype: int
        """
        return self._credit_count

    @credit_count.setter
    def credit_count(self, credit_count):
        """
        Sets the credit_count of this InlineResponse200PaymentBatchSummaries.

        :param credit_count: The credit_count of this InlineResponse200PaymentBatchSummaries.
        :type: int
        """

        self._credit_count = credit_count

    @property
    def credit_amount(self):
        """
        Gets the credit_amount of this InlineResponse200PaymentBatchSummaries.

        :return: The credit_amount of this InlineResponse200PaymentBatchSummaries.
        :rtype: str
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        """
        Sets the credit_amount of this InlineResponse200PaymentBatchSummaries.

        :param credit_amount: The credit_amount of this InlineResponse200PaymentBatchSummaries.
        :type: str
        """

        self._credit_amount = credit_amount

    @property
    def account_name(self):
        """
        Gets the account_name of this InlineResponse200PaymentBatchSummaries.

        :return: The account_name of this InlineResponse200PaymentBatchSummaries.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """
        Sets the account_name of this InlineResponse200PaymentBatchSummaries.

        :param account_name: The account_name of this InlineResponse200PaymentBatchSummaries.
        :type: str
        """

        self._account_name = account_name

    @property
    def account_id(self):
        """
        Gets the account_id of this InlineResponse200PaymentBatchSummaries.

        :return: The account_id of this InlineResponse200PaymentBatchSummaries.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this InlineResponse200PaymentBatchSummaries.

        :param account_id: The account_id of this InlineResponse200PaymentBatchSummaries.
        :type: str
        """

        self._account_id = account_id

    @property
    def merchant_id(self):
        """
        Gets the merchant_id of this InlineResponse200PaymentBatchSummaries.

        :return: The merchant_id of this InlineResponse200PaymentBatchSummaries.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """
        Sets the merchant_id of this InlineResponse200PaymentBatchSummaries.

        :param merchant_id: The merchant_id of this InlineResponse200PaymentBatchSummaries.
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def merchant_name(self):
        """
        Gets the merchant_name of this InlineResponse200PaymentBatchSummaries.

        :return: The merchant_name of this InlineResponse200PaymentBatchSummaries.
        :rtype: str
        """
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, merchant_name):
        """
        Sets the merchant_name of this InlineResponse200PaymentBatchSummaries.

        :param merchant_name: The merchant_name of this InlineResponse200PaymentBatchSummaries.
        :type: str
        """

        self._merchant_name = merchant_name

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
        if not isinstance(other, InlineResponse200PaymentBatchSummaries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
