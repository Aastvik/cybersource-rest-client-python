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


class RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider(object):
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
        'accurint': 'RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderAccurint',
        'credilink': 'RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderCredilink',
        'ekata': 'RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata',
        'emailage': 'RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEmailage',
        'perseuss': 'RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderPerseuss',
        'signifyd': 'RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifyd',
        'targus': 'RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderTargus'
    }

    attribute_map = {
        'accurint': 'accurint',
        'credilink': 'credilink',
        'ekata': 'ekata',
        'emailage': 'emailage',
        'perseuss': 'perseuss',
        'signifyd': 'signifyd',
        'targus': 'targus'
    }

    def __init__(self, accurint=None, credilink=None, ekata=None, emailage=None, perseuss=None, signifyd=None, targus=None):
        """
        RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider - a model defined in Swagger
        """

        self._accurint = None
        self._credilink = None
        self._ekata = None
        self._emailage = None
        self._perseuss = None
        self._signifyd = None
        self._targus = None

        if accurint is not None:
          self.accurint = accurint
        if credilink is not None:
          self.credilink = credilink
        if ekata is not None:
          self.ekata = ekata
        if emailage is not None:
          self.emailage = emailage
        if perseuss is not None:
          self.perseuss = perseuss
        if signifyd is not None:
          self.signifyd = signifyd
        if targus is not None:
          self.targus = targus

    @property
    def accurint(self):
        """
        Gets the accurint of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.

        :return: The accurint of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.
        :rtype: RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderAccurint
        """
        return self._accurint

    @accurint.setter
    def accurint(self, accurint):
        """
        Sets the accurint of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.

        :param accurint: The accurint of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.
        :type: RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderAccurint
        """

        self._accurint = accurint

    @property
    def credilink(self):
        """
        Gets the credilink of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.

        :return: The credilink of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.
        :rtype: RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderCredilink
        """
        return self._credilink

    @credilink.setter
    def credilink(self, credilink):
        """
        Sets the credilink of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.

        :param credilink: The credilink of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.
        :type: RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderCredilink
        """

        self._credilink = credilink

    @property
    def ekata(self):
        """
        Gets the ekata of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.

        :return: The ekata of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.
        :rtype: RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata
        """
        return self._ekata

    @ekata.setter
    def ekata(self, ekata):
        """
        Sets the ekata of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.

        :param ekata: The ekata of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.
        :type: RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEkata
        """

        self._ekata = ekata

    @property
    def emailage(self):
        """
        Gets the emailage of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.

        :return: The emailage of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.
        :rtype: RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEmailage
        """
        return self._emailage

    @emailage.setter
    def emailage(self, emailage):
        """
        Sets the emailage of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.

        :param emailage: The emailage of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.
        :type: RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderEmailage
        """

        self._emailage = emailage

    @property
    def perseuss(self):
        """
        Gets the perseuss of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.

        :return: The perseuss of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.
        :rtype: RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderPerseuss
        """
        return self._perseuss

    @perseuss.setter
    def perseuss(self, perseuss):
        """
        Sets the perseuss of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.

        :param perseuss: The perseuss of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.
        :type: RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderPerseuss
        """

        self._perseuss = perseuss

    @property
    def signifyd(self):
        """
        Gets the signifyd of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.

        :return: The signifyd of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.
        :rtype: RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifyd
        """
        return self._signifyd

    @signifyd.setter
    def signifyd(self, signifyd):
        """
        Sets the signifyd of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.

        :param signifyd: The signifyd of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.
        :type: RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderSignifyd
        """

        self._signifyd = signifyd

    @property
    def targus(self):
        """
        Gets the targus of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.

        :return: The targus of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.
        :rtype: RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderTargus
        """
        return self._targus

    @targus.setter
    def targus(self, targus):
        """
        Sets the targus of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.

        :param targus: The targus of this RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider.
        :type: RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProviderTargus
        """

        self._targus = targus

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
        if not isinstance(other, RiskProductsDecisionManagerConfigurationInformationConfigurationsThirdpartyProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
