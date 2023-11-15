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


class CommerceSolutionsProductsAccountUpdaterConfigurationInformationConfigurationsVisa(object):
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
        'merchant_id': 'str',
        'segment_id': 'str',
        'active': 'bool'
    }

    attribute_map = {
        'merchant_id': 'merchantId',
        'segment_id': 'segmentId',
        'active': 'active'
    }

    def __init__(self, merchant_id=None, segment_id=None, active=None):
        """
        CommerceSolutionsProductsAccountUpdaterConfigurationInformationConfigurationsVisa - a model defined in Swagger
        """

        self._merchant_id = None
        self._segment_id = None
        self._active = None

        self.merchant_id = merchant_id
        self.segment_id = segment_id
        if active is not None:
          self.active = active

    @property
    def merchant_id(self):
        """
        Gets the merchant_id of this CommerceSolutionsProductsAccountUpdaterConfigurationInformationConfigurationsVisa.
        Visa merchant identified number

        :return: The merchant_id of this CommerceSolutionsProductsAccountUpdaterConfigurationInformationConfigurationsVisa.
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """
        Sets the merchant_id of this CommerceSolutionsProductsAccountUpdaterConfigurationInformationConfigurationsVisa.
        Visa merchant identified number

        :param merchant_id: The merchant_id of this CommerceSolutionsProductsAccountUpdaterConfigurationInformationConfigurationsVisa.
        :type: str
        """
        if merchant_id is None:
            raise ValueError("Invalid value for `merchant_id`, must not be `None`")

        self._merchant_id = merchant_id

    @property
    def segment_id(self):
        """
        Gets the segment_id of this CommerceSolutionsProductsAccountUpdaterConfigurationInformationConfigurationsVisa.
        Visa assigned segment ID for each group of merchants participating in VAU.

        :return: The segment_id of this CommerceSolutionsProductsAccountUpdaterConfigurationInformationConfigurationsVisa.
        :rtype: str
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id):
        """
        Sets the segment_id of this CommerceSolutionsProductsAccountUpdaterConfigurationInformationConfigurationsVisa.
        Visa assigned segment ID for each group of merchants participating in VAU.

        :param segment_id: The segment_id of this CommerceSolutionsProductsAccountUpdaterConfigurationInformationConfigurationsVisa.
        :type: str
        """
        if segment_id is None:
            raise ValueError("Invalid value for `segment_id`, must not be `None`")

        self._segment_id = segment_id

    @property
    def active(self):
        """
        Gets the active of this CommerceSolutionsProductsAccountUpdaterConfigurationInformationConfigurationsVisa.

        :return: The active of this CommerceSolutionsProductsAccountUpdaterConfigurationInformationConfigurationsVisa.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this CommerceSolutionsProductsAccountUpdaterConfigurationInformationConfigurationsVisa.

        :param active: The active of this CommerceSolutionsProductsAccountUpdaterConfigurationInformationConfigurationsVisa.
        :type: bool
        """

        self._active = active

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
        if not isinstance(other, CommerceSolutionsProductsAccountUpdaterConfigurationInformationConfigurationsVisa):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
