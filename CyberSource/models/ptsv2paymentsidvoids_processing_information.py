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


class Ptsv2paymentsidvoidsProcessingInformation(object):
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
        'action_list': 'list[str]'
    }

    attribute_map = {
        'action_list': 'actionList'
    }

    def __init__(self, action_list=None):
        """
        Ptsv2paymentsidvoidsProcessingInformation - a model defined in Swagger
        """

        self._action_list = None

        if action_list is not None:
          self.action_list = action_list

    @property
    def action_list(self):
        """
        Gets the action_list of this Ptsv2paymentsidvoidsProcessingInformation.
        Array of actions (one or more) to be included in the void to invoke bundled services along with void. Possible values: - `AP_CANCEL`: Use this when Alternative Payment Void service is requested. 

        :return: The action_list of this Ptsv2paymentsidvoidsProcessingInformation.
        :rtype: list[str]
        """
        return self._action_list

    @action_list.setter
    def action_list(self, action_list):
        """
        Sets the action_list of this Ptsv2paymentsidvoidsProcessingInformation.
        Array of actions (one or more) to be included in the void to invoke bundled services along with void. Possible values: - `AP_CANCEL`: Use this when Alternative Payment Void service is requested. 

        :param action_list: The action_list of this Ptsv2paymentsidvoidsProcessingInformation.
        :type: list[str]
        """

        self._action_list = action_list

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
        if not isinstance(other, Ptsv2paymentsidvoidsProcessingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
