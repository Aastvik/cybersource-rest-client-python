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


class SAConfigContactInformation(object):
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
        'phone': 'str',
        'company_name': 'str',
        'email': 'str',
        'name': 'str'
    }

    attribute_map = {
        'phone': 'phone',
        'company_name': 'companyName',
        'email': 'email',
        'name': 'name'
    }

    def __init__(self, phone=None, company_name=None, email=None, name=None):
        """
        SAConfigContactInformation - a model defined in Swagger
        """

        self._phone = None
        self._company_name = None
        self._email = None
        self._name = None

        if phone is not None:
          self.phone = phone
        if company_name is not None:
          self.company_name = company_name
        if email is not None:
          self.email = email
        if name is not None:
          self.name = name

    @property
    def phone(self):
        """
        Gets the phone of this SAConfigContactInformation.

        :return: The phone of this SAConfigContactInformation.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this SAConfigContactInformation.

        :param phone: The phone of this SAConfigContactInformation.
        :type: str
        """

        self._phone = phone

    @property
    def company_name(self):
        """
        Gets the company_name of this SAConfigContactInformation.

        :return: The company_name of this SAConfigContactInformation.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this SAConfigContactInformation.

        :param company_name: The company_name of this SAConfigContactInformation.
        :type: str
        """

        self._company_name = company_name

    @property
    def email(self):
        """
        Gets the email of this SAConfigContactInformation.

        :return: The email of this SAConfigContactInformation.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this SAConfigContactInformation.

        :param email: The email of this SAConfigContactInformation.
        :type: str
        """

        self._email = email

    @property
    def name(self):
        """
        Gets the name of this SAConfigContactInformation.

        :return: The name of this SAConfigContactInformation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SAConfigContactInformation.

        :param name: The name of this SAConfigContactInformation.
        :type: str
        """

        self._name = name

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
        if not isinstance(other, SAConfigContactInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
