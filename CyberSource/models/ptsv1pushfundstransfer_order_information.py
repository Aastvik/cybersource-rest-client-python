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


class Ptsv1pushfundstransferOrderInformation(object):
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
        'amount_details': 'Ptsv1pushfundstransferOrderInformationAmountDetails',
        'is_cryptocurrency_purchase': 'str',
        'surcharge': 'Ptsv1pushfundstransferOrderInformationSurcharge'
    }

    attribute_map = {
        'amount_details': 'amountDetails',
        'is_cryptocurrency_purchase': 'isCryptocurrencyPurchase',
        'surcharge': 'surcharge'
    }

    def __init__(self, amount_details=None, is_cryptocurrency_purchase=None, surcharge=None):
        """
        Ptsv1pushfundstransferOrderInformation - a model defined in Swagger
        """

        self._amount_details = None
        self._is_cryptocurrency_purchase = None
        self._surcharge = None

        self.amount_details = amount_details
        if is_cryptocurrency_purchase is not None:
          self.is_cryptocurrency_purchase = is_cryptocurrency_purchase
        if surcharge is not None:
          self.surcharge = surcharge

    @property
    def amount_details(self):
        """
        Gets the amount_details of this Ptsv1pushfundstransferOrderInformation.

        :return: The amount_details of this Ptsv1pushfundstransferOrderInformation.
        :rtype: Ptsv1pushfundstransferOrderInformationAmountDetails
        """
        return self._amount_details

    @amount_details.setter
    def amount_details(self, amount_details):
        """
        Sets the amount_details of this Ptsv1pushfundstransferOrderInformation.

        :param amount_details: The amount_details of this Ptsv1pushfundstransferOrderInformation.
        :type: Ptsv1pushfundstransferOrderInformationAmountDetails
        """
        if amount_details is None:
            raise ValueError("Invalid value for `amount_details`, must not be `None`")

        self._amount_details = amount_details

    @property
    def is_cryptocurrency_purchase(self):
        """
        Gets the is_cryptocurrency_purchase of this Ptsv1pushfundstransferOrderInformation.
        This indicates that the funds transfer is for a crypto currency transaction. Optional Y/y, true N/n, false 

        :return: The is_cryptocurrency_purchase of this Ptsv1pushfundstransferOrderInformation.
        :rtype: str
        """
        return self._is_cryptocurrency_purchase

    @is_cryptocurrency_purchase.setter
    def is_cryptocurrency_purchase(self, is_cryptocurrency_purchase):
        """
        Sets the is_cryptocurrency_purchase of this Ptsv1pushfundstransferOrderInformation.
        This indicates that the funds transfer is for a crypto currency transaction. Optional Y/y, true N/n, false 

        :param is_cryptocurrency_purchase: The is_cryptocurrency_purchase of this Ptsv1pushfundstransferOrderInformation.
        :type: str
        """

        self._is_cryptocurrency_purchase = is_cryptocurrency_purchase

    @property
    def surcharge(self):
        """
        Gets the surcharge of this Ptsv1pushfundstransferOrderInformation.

        :return: The surcharge of this Ptsv1pushfundstransferOrderInformation.
        :rtype: Ptsv1pushfundstransferOrderInformationSurcharge
        """
        return self._surcharge

    @surcharge.setter
    def surcharge(self, surcharge):
        """
        Sets the surcharge of this Ptsv1pushfundstransferOrderInformation.

        :param surcharge: The surcharge of this Ptsv1pushfundstransferOrderInformation.
        :type: Ptsv1pushfundstransferOrderInformationSurcharge
        """

        self._surcharge = surcharge

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
        if not isinstance(other, Ptsv1pushfundstransferOrderInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
