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


class Riskv1authenticationsetupsTokenInformation(object):
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
        'transient_token': 'str',
        'jti': 'str'
    }

    attribute_map = {
        'transient_token': 'transientToken',
        'jti': 'jti'
    }

    def __init__(self, transient_token=None, jti=None):
        """
        Riskv1authenticationsetupsTokenInformation - a model defined in Swagger
        """

        self._transient_token = None
        self._jti = None

        if transient_token is not None:
          self.transient_token = transient_token
        if jti is not None:
          self.jti = jti

    @property
    def transient_token(self):
        """
        Gets the transient_token of this Riskv1authenticationsetupsTokenInformation.
        A temporary ID that represents the customer's payment data (which is securely stored in Visa Data Centers). Flex Microform generates this ID and sets it to expire within 15 minutes from when the ID is generated or until the first payment authorization is carried out (whichever occurs first).  Valid value for the ID is a 64-character, alphanumeric string.  Example: 1D08M4YB968R1F7YVL4TBBKYVNRIR02VZFH9CBYSQIJJXORPI1NK5C98D7F6EB53 

        :return: The transient_token of this Riskv1authenticationsetupsTokenInformation.
        :rtype: str
        """
        return self._transient_token

    @transient_token.setter
    def transient_token(self, transient_token):
        """
        Sets the transient_token of this Riskv1authenticationsetupsTokenInformation.
        A temporary ID that represents the customer's payment data (which is securely stored in Visa Data Centers). Flex Microform generates this ID and sets it to expire within 15 minutes from when the ID is generated or until the first payment authorization is carried out (whichever occurs first).  Valid value for the ID is a 64-character, alphanumeric string.  Example: 1D08M4YB968R1F7YVL4TBBKYVNRIR02VZFH9CBYSQIJJXORPI1NK5C98D7F6EB53 

        :param transient_token: The transient_token of this Riskv1authenticationsetupsTokenInformation.
        :type: str
        """

        self._transient_token = transient_token

    @property
    def jti(self):
        """
        Gets the jti of this Riskv1authenticationsetupsTokenInformation.
        TMS Transient Token, 64 hexadecimal id value representing captured payment credentials (including Sensitive Authentication Data, e.g. CVV). 

        :return: The jti of this Riskv1authenticationsetupsTokenInformation.
        :rtype: str
        """
        return self._jti

    @jti.setter
    def jti(self, jti):
        """
        Sets the jti of this Riskv1authenticationsetupsTokenInformation.
        TMS Transient Token, 64 hexadecimal id value representing captured payment credentials (including Sensitive Authentication Data, e.g. CVV). 

        :param jti: The jti of this Riskv1authenticationsetupsTokenInformation.
        :type: str
        """

        self._jti = jti

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
        if not isinstance(other, Riskv1authenticationsetupsTokenInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
