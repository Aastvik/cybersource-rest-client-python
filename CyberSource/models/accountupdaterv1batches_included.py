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


class Accountupdaterv1batchesIncluded(object):
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
        'tokens': 'list[Accountupdaterv1batchesIncludedTokens]'
    }

    attribute_map = {
        'tokens': 'tokens'
    }

    def __init__(self, tokens=None):
        """
        Accountupdaterv1batchesIncluded - a model defined in Swagger
        """

        self._tokens = None

        if tokens is not None:
          self.tokens = tokens

    @property
    def tokens(self):
        """
        Gets the tokens of this Accountupdaterv1batchesIncluded.

        :return: The tokens of this Accountupdaterv1batchesIncluded.
        :rtype: list[Accountupdaterv1batchesIncludedTokens]
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """
        Sets the tokens of this Accountupdaterv1batchesIncluded.

        :param tokens: The tokens of this Accountupdaterv1batchesIncluded.
        :type: list[Accountupdaterv1batchesIncludedTokens]
        """

        self._tokens = tokens

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
        if not isinstance(other, Accountupdaterv1batchesIncluded):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
