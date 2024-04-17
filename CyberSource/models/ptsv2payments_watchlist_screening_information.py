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


class Ptsv2paymentsWatchlistScreeningInformation(object):
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
        'address_operator': 'str',
        'weights': 'Ptsv2paymentsWatchlistScreeningInformationWeights',
        'sanction_lists': 'list[str]',
        'proceed_on_match': 'bool'
    }

    attribute_map = {
        'address_operator': 'addressOperator',
        'weights': 'weights',
        'sanction_lists': 'sanctionLists',
        'proceed_on_match': 'proceedOnMatch'
    }

    def __init__(self, address_operator=None, weights=None, sanction_lists=None, proceed_on_match=None):
        """
        Ptsv2paymentsWatchlistScreeningInformation - a model defined in Swagger
        """

        self._address_operator = None
        self._weights = None
        self._sanction_lists = None
        self._proceed_on_match = None

        if address_operator is not None:
          self.address_operator = address_operator
        if weights is not None:
          self.weights = weights
        if sanction_lists is not None:
          self.sanction_lists = sanction_lists
        if proceed_on_match is not None:
          self.proceed_on_match = proceed_on_match

    @property
    def address_operator(self):
        """
        Gets the address_operator of this Ptsv2paymentsWatchlistScreeningInformation.
        Parts of the customer's information that must match with an entry in the DPL (denied parties list) before a match occurs. This field can contain one of the following values: - AND: (default) The customer's name or company and the customer's address must appear in the database. - OR: The customer's name must appear in the database. - IGNORE: You want the service to detect a match only of the customer's name or company but not of the address. 

        :return: The address_operator of this Ptsv2paymentsWatchlistScreeningInformation.
        :rtype: str
        """
        return self._address_operator

    @address_operator.setter
    def address_operator(self, address_operator):
        """
        Sets the address_operator of this Ptsv2paymentsWatchlistScreeningInformation.
        Parts of the customer's information that must match with an entry in the DPL (denied parties list) before a match occurs. This field can contain one of the following values: - AND: (default) The customer's name or company and the customer's address must appear in the database. - OR: The customer's name must appear in the database. - IGNORE: You want the service to detect a match only of the customer's name or company but not of the address. 

        :param address_operator: The address_operator of this Ptsv2paymentsWatchlistScreeningInformation.
        :type: str
        """

        self._address_operator = address_operator

    @property
    def weights(self):
        """
        Gets the weights of this Ptsv2paymentsWatchlistScreeningInformation.

        :return: The weights of this Ptsv2paymentsWatchlistScreeningInformation.
        :rtype: Ptsv2paymentsWatchlistScreeningInformationWeights
        """
        return self._weights

    @weights.setter
    def weights(self, weights):
        """
        Sets the weights of this Ptsv2paymentsWatchlistScreeningInformation.

        :param weights: The weights of this Ptsv2paymentsWatchlistScreeningInformation.
        :type: Ptsv2paymentsWatchlistScreeningInformationWeights
        """

        self._weights = weights

    @property
    def sanction_lists(self):
        """
        Gets the sanction_lists of this Ptsv2paymentsWatchlistScreeningInformation.
        Use this field to specify which list(s) you want checked with the request. The reply will include the list name as well as the response data. To check against multiple lists, enter multiple list codes separated by a caret (^). For more information, see \"Restricted and Denied Parties List,\" page 68. 

        :return: The sanction_lists of this Ptsv2paymentsWatchlistScreeningInformation.
        :rtype: list[str]
        """
        return self._sanction_lists

    @sanction_lists.setter
    def sanction_lists(self, sanction_lists):
        """
        Sets the sanction_lists of this Ptsv2paymentsWatchlistScreeningInformation.
        Use this field to specify which list(s) you want checked with the request. The reply will include the list name as well as the response data. To check against multiple lists, enter multiple list codes separated by a caret (^). For more information, see \"Restricted and Denied Parties List,\" page 68. 

        :param sanction_lists: The sanction_lists of this Ptsv2paymentsWatchlistScreeningInformation.
        :type: list[str]
        """

        self._sanction_lists = sanction_lists

    @property
    def proceed_on_match(self):
        """
        Gets the proceed_on_match of this Ptsv2paymentsWatchlistScreeningInformation.
        Indicates whether the transaction should proceed if there is a match. Possible values: - `true`: Transaction proceeds even when match is found in the Denied Parties List. The match is noted in the response. - `false`: Normal watchlist screening behavior occurs. (Transaction stops if a match to DPL occurs. Transaction proceeds if no match.) 

        :return: The proceed_on_match of this Ptsv2paymentsWatchlistScreeningInformation.
        :rtype: bool
        """
        return self._proceed_on_match

    @proceed_on_match.setter
    def proceed_on_match(self, proceed_on_match):
        """
        Sets the proceed_on_match of this Ptsv2paymentsWatchlistScreeningInformation.
        Indicates whether the transaction should proceed if there is a match. Possible values: - `true`: Transaction proceeds even when match is found in the Denied Parties List. The match is noted in the response. - `false`: Normal watchlist screening behavior occurs. (Transaction stops if a match to DPL occurs. Transaction proceeds if no match.) 

        :param proceed_on_match: The proceed_on_match of this Ptsv2paymentsWatchlistScreeningInformation.
        :type: bool
        """

        self._proceed_on_match = proceed_on_match

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
        if not isinstance(other, Ptsv2paymentsWatchlistScreeningInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
