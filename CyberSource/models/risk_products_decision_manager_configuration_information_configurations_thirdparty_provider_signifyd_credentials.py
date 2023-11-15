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


class RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials(object):
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
        'team_id': 'str',
        'api_key': 'str',
        'secret_keyid': 'str',
        'secret_key': 'str'
    }

    attribute_map = {
        'team_id': 'teamId',
        'api_key': 'apiKey',
        'secret_keyid': 'secretKeyid',
        'secret_key': 'secretKey'
    }

    def __init__(self, team_id=None, api_key=None, secret_keyid=None, secret_key=None):
        """
        RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials - a model defined in Swagger
        """

        self._team_id = None
        self._api_key = None
        self._secret_keyid = None
        self._secret_key = None

        if team_id is not None:
          self.team_id = team_id
        if api_key is not None:
          self.api_key = api_key
        if secret_keyid is not None:
          self.secret_keyid = secret_keyid
        if secret_key is not None:
          self.secret_key = secret_key

    @property
    def team_id(self):
        """
        Gets the team_id of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials.

        :return: The team_id of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials.

        :param team_id: The team_id of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials.
        :type: str
        """

        self._team_id = team_id

    @property
    def api_key(self):
        """
        Gets the api_key of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials.

        :return: The api_key of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """
        Sets the api_key of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials.

        :param api_key: The api_key of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials.
        :type: str
        """

        self._api_key = api_key

    @property
    def secret_keyid(self):
        """
        Gets the secret_keyid of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials.

        :return: The secret_keyid of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials.
        :rtype: str
        """
        return self._secret_keyid

    @secret_keyid.setter
    def secret_keyid(self, secret_keyid):
        """
        Sets the secret_keyid of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials.

        :param secret_keyid: The secret_keyid of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials.
        :type: str
        """

        self._secret_keyid = secret_keyid

    @property
    def secret_key(self):
        """
        Gets the secret_key of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials.

        :return: The secret_key of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """
        Sets the secret_key of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials.

        :param secret_key: The secret_key of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials.
        :type: str
        """

        self._secret_key = secret_key

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
        if not isinstance(other, RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifydCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
