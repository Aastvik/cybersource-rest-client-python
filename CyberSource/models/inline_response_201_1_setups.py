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


class InlineResponse2011Setups(object):
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
        'payments': 'InlineResponse2011SetupsPayments',
        'risk': 'InlineResponse2011SetupsRisk',
        'commerce_solutions': 'InlineResponse2011SetupsCommerceSolutions',
        'value_added_services': 'InlineResponse2011SetupsValueAddedServices'
    }

    attribute_map = {
        'payments': 'payments',
        'risk': 'risk',
        'commerce_solutions': 'commerceSolutions',
        'value_added_services': 'valueAddedServices'
    }

    def __init__(self, payments=None, risk=None, commerce_solutions=None, value_added_services=None):
        """
        InlineResponse2011Setups - a model defined in Swagger
        """

        self._payments = None
        self._risk = None
        self._commerce_solutions = None
        self._value_added_services = None

        if payments is not None:
          self.payments = payments
        if risk is not None:
          self.risk = risk
        if commerce_solutions is not None:
          self.commerce_solutions = commerce_solutions
        if value_added_services is not None:
          self.value_added_services = value_added_services

    @property
    def payments(self):
        """
        Gets the payments of this InlineResponse2011Setups.

        :return: The payments of this InlineResponse2011Setups.
        :rtype: InlineResponse2011SetupsPayments
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """
        Sets the payments of this InlineResponse2011Setups.

        :param payments: The payments of this InlineResponse2011Setups.
        :type: InlineResponse2011SetupsPayments
        """

        self._payments = payments

    @property
    def risk(self):
        """
        Gets the risk of this InlineResponse2011Setups.

        :return: The risk of this InlineResponse2011Setups.
        :rtype: InlineResponse2011SetupsRisk
        """
        return self._risk

    @risk.setter
    def risk(self, risk):
        """
        Sets the risk of this InlineResponse2011Setups.

        :param risk: The risk of this InlineResponse2011Setups.
        :type: InlineResponse2011SetupsRisk
        """

        self._risk = risk

    @property
    def commerce_solutions(self):
        """
        Gets the commerce_solutions of this InlineResponse2011Setups.

        :return: The commerce_solutions of this InlineResponse2011Setups.
        :rtype: InlineResponse2011SetupsCommerceSolutions
        """
        return self._commerce_solutions

    @commerce_solutions.setter
    def commerce_solutions(self, commerce_solutions):
        """
        Sets the commerce_solutions of this InlineResponse2011Setups.

        :param commerce_solutions: The commerce_solutions of this InlineResponse2011Setups.
        :type: InlineResponse2011SetupsCommerceSolutions
        """

        self._commerce_solutions = commerce_solutions

    @property
    def value_added_services(self):
        """
        Gets the value_added_services of this InlineResponse2011Setups.

        :return: The value_added_services of this InlineResponse2011Setups.
        :rtype: InlineResponse2011SetupsValueAddedServices
        """
        return self._value_added_services

    @value_added_services.setter
    def value_added_services(self, value_added_services):
        """
        Sets the value_added_services of this InlineResponse2011Setups.

        :param value_added_services: The value_added_services of this InlineResponse2011Setups.
        :type: InlineResponse2011SetupsValueAddedServices
        """

        self._value_added_services = value_added_services

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
        if not isinstance(other, InlineResponse2011Setups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
