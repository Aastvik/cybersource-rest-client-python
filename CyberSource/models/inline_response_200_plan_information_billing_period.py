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


class InlineResponse200PlanInformationBillingPeriod(object):
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
        'length': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'length': 'length',
        'unit': 'unit'
    }

    def __init__(self, length=None, unit=None):
        """
        InlineResponse200PlanInformationBillingPeriod - a model defined in Swagger
        """

        self._length = None
        self._unit = None

        if length is not None:
          self.length = length
        if unit is not None:
          self.unit = unit

    @property
    def length(self):
        """
        Gets the length of this InlineResponse200PlanInformationBillingPeriod.
        Example: - If length=1 & unit=month then charge every month - If length=7 & unit=day then charge every 7th day 

        :return: The length of this InlineResponse200PlanInformationBillingPeriod.
        :rtype: str
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Sets the length of this InlineResponse200PlanInformationBillingPeriod.
        Example: - If length=1 & unit=month then charge every month - If length=7 & unit=day then charge every 7th day 

        :param length: The length of this InlineResponse200PlanInformationBillingPeriod.
        :type: str
        """

        self._length = length

    @property
    def unit(self):
        """
        Gets the unit of this InlineResponse200PlanInformationBillingPeriod.
        Calendar unit values.   possible values:   - `D` - day   - `M` - month   - `W` - week   - `Y` - year 

        :return: The unit of this InlineResponse200PlanInformationBillingPeriod.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this InlineResponse200PlanInformationBillingPeriod.
        Calendar unit values.   possible values:   - `D` - day   - `M` - month   - `W` - week   - `Y` - year 

        :param unit: The unit of this InlineResponse200PlanInformationBillingPeriod.
        :type: str
        """

        self._unit = unit

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
        if not isinstance(other, InlineResponse200PlanInformationBillingPeriod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
