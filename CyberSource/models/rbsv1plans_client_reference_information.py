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


class Rbsv1plansClientReferenceInformation(object):
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
        'comments': 'str',
        'partner': 'Riskv1decisionsClientReferenceInformationPartner',
        'application_name': 'str',
        'application_version': 'str',
        'application_user': 'str'
    }

    attribute_map = {
        'comments': 'comments',
        'partner': 'partner',
        'application_name': 'applicationName',
        'application_version': 'applicationVersion',
        'application_user': 'applicationUser'
    }

    def __init__(self, comments=None, partner=None, application_name=None, application_version=None, application_user=None):
        """
        Rbsv1plansClientReferenceInformation - a model defined in Swagger
        """

        self._comments = None
        self._partner = None
        self._application_name = None
        self._application_version = None
        self._application_user = None

        if comments is not None:
          self.comments = comments
        if partner is not None:
          self.partner = partner
        if application_name is not None:
          self.application_name = application_name
        if application_version is not None:
          self.application_version = application_version
        if application_user is not None:
          self.application_user = application_user

    @property
    def comments(self):
        """
        Gets the comments of this Rbsv1plansClientReferenceInformation.
        Brief description of the order or any comment you wish to add to the order. 

        :return: The comments of this Rbsv1plansClientReferenceInformation.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this Rbsv1plansClientReferenceInformation.
        Brief description of the order or any comment you wish to add to the order. 

        :param comments: The comments of this Rbsv1plansClientReferenceInformation.
        :type: str
        """

        self._comments = comments

    @property
    def partner(self):
        """
        Gets the partner of this Rbsv1plansClientReferenceInformation.

        :return: The partner of this Rbsv1plansClientReferenceInformation.
        :rtype: Riskv1decisionsClientReferenceInformationPartner
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """
        Sets the partner of this Rbsv1plansClientReferenceInformation.

        :param partner: The partner of this Rbsv1plansClientReferenceInformation.
        :type: Riskv1decisionsClientReferenceInformationPartner
        """

        self._partner = partner

    @property
    def application_name(self):
        """
        Gets the application_name of this Rbsv1plansClientReferenceInformation.
        The name of the Connection Method client (such as Virtual Terminal or SOAP Toolkit API) that the merchant uses to send a transaction request to CyberSource. 

        :return: The application_name of this Rbsv1plansClientReferenceInformation.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """
        Sets the application_name of this Rbsv1plansClientReferenceInformation.
        The name of the Connection Method client (such as Virtual Terminal or SOAP Toolkit API) that the merchant uses to send a transaction request to CyberSource. 

        :param application_name: The application_name of this Rbsv1plansClientReferenceInformation.
        :type: str
        """

        self._application_name = application_name

    @property
    def application_version(self):
        """
        Gets the application_version of this Rbsv1plansClientReferenceInformation.
        Version of the CyberSource application or integration used for a transaction. 

        :return: The application_version of this Rbsv1plansClientReferenceInformation.
        :rtype: str
        """
        return self._application_version

    @application_version.setter
    def application_version(self, application_version):
        """
        Sets the application_version of this Rbsv1plansClientReferenceInformation.
        Version of the CyberSource application or integration used for a transaction. 

        :param application_version: The application_version of this Rbsv1plansClientReferenceInformation.
        :type: str
        """

        self._application_version = application_version

    @property
    def application_user(self):
        """
        Gets the application_user of this Rbsv1plansClientReferenceInformation.
        The entity that is responsible for running the transaction and submitting the processing request to CyberSource. This could be a person, a system, or a connection method. 

        :return: The application_user of this Rbsv1plansClientReferenceInformation.
        :rtype: str
        """
        return self._application_user

    @application_user.setter
    def application_user(self, application_user):
        """
        Sets the application_user of this Rbsv1plansClientReferenceInformation.
        The entity that is responsible for running the transaction and submitting the processing request to CyberSource. This could be a person, a system, or a connection method. 

        :param application_user: The application_user of this Rbsv1plansClientReferenceInformation.
        :type: str
        """

        self._application_user = application_user

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
        if not isinstance(other, Rbsv1plansClientReferenceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
