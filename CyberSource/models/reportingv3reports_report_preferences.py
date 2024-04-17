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


class Reportingv3reportsReportPreferences(object):
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
        'signed_amounts': 'bool',
        'field_name_convention': 'str'
    }

    attribute_map = {
        'signed_amounts': 'signedAmounts',
        'field_name_convention': 'fieldNameConvention'
    }

    def __init__(self, signed_amounts=None, field_name_convention=None):
        """
        Reportingv3reportsReportPreferences - a model defined in Swagger
        """

        self._signed_amounts = None
        self._field_name_convention = None

        if signed_amounts is not None:
          self.signed_amounts = signed_amounts
        if field_name_convention is not None:
          self.field_name_convention = field_name_convention

    @property
    def signed_amounts(self):
        """
        Gets the signed_amounts of this Reportingv3reportsReportPreferences.
        Indicator to determine whether negative sign infront of amount for all refunded transaction

        :return: The signed_amounts of this Reportingv3reportsReportPreferences.
        :rtype: bool
        """
        return self._signed_amounts

    @signed_amounts.setter
    def signed_amounts(self, signed_amounts):
        """
        Sets the signed_amounts of this Reportingv3reportsReportPreferences.
        Indicator to determine whether negative sign infront of amount for all refunded transaction

        :param signed_amounts: The signed_amounts of this Reportingv3reportsReportPreferences.
        :type: bool
        """

        self._signed_amounts = signed_amounts

    @property
    def field_name_convention(self):
        """
        Gets the field_name_convention of this Reportingv3reportsReportPreferences.
        Specify the field naming convention to be followed in reports (applicable to only csv report formats)  Valid values: - SOAPI - SCMP 

        :return: The field_name_convention of this Reportingv3reportsReportPreferences.
        :rtype: str
        """
        return self._field_name_convention

    @field_name_convention.setter
    def field_name_convention(self, field_name_convention):
        """
        Sets the field_name_convention of this Reportingv3reportsReportPreferences.
        Specify the field naming convention to be followed in reports (applicable to only csv report formats)  Valid values: - SOAPI - SCMP 

        :param field_name_convention: The field_name_convention of this Reportingv3reportsReportPreferences.
        :type: str
        """

        self._field_name_convention = field_name_convention

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
        if not isinstance(other, Reportingv3reportsReportPreferences):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
