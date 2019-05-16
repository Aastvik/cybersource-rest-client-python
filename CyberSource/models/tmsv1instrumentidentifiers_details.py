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


class Tmsv1instrumentidentifiersDetails(object):
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
        'name': 'str',
        'location': 'str'
    }

    attribute_map = {
        'name': 'name',
        'location': 'location'
    }

    def __init__(self, name=None, location=None):
        """
        Tmsv1instrumentidentifiersDetails - a model defined in Swagger
        """

        self._name = None
        self._location = None

        if name is not None:
          self.name = name
        if location is not None:
          self.location = location

    @property
    def name(self):
        """
        Gets the name of this Tmsv1instrumentidentifiersDetails.
        The name of the field that threw the error.

        :return: The name of this Tmsv1instrumentidentifiersDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Tmsv1instrumentidentifiersDetails.
        The name of the field that threw the error.

        :param name: The name of this Tmsv1instrumentidentifiersDetails.
        :type: str
        """

        self._name = name

    @property
    def location(self):
        """
        Gets the location of this Tmsv1instrumentidentifiersDetails.
        The location of the field that threw the error.

        :return: The location of this Tmsv1instrumentidentifiersDetails.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this Tmsv1instrumentidentifiersDetails.
        The location of the field that threw the error.

        :param location: The location of this Tmsv1instrumentidentifiersDetails.
        :type: str
        """

        self._location = location

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
        if not isinstance(other, Tmsv1instrumentidentifiersDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
