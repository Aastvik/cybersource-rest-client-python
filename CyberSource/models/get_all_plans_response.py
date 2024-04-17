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


class GetAllPlansResponse(object):
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
        'links': 'GetAllPlansResponseLinks',
        'submit_time_utc': 'str',
        'total_count': 'int',
        'plans': 'list[GetAllPlansResponsePlans]'
    }

    attribute_map = {
        'links': '_links',
        'submit_time_utc': 'submitTimeUtc',
        'total_count': 'totalCount',
        'plans': 'plans'
    }

    def __init__(self, links=None, submit_time_utc=None, total_count=None, plans=None):
        """
        GetAllPlansResponse - a model defined in Swagger
        """

        self._links = None
        self._submit_time_utc = None
        self._total_count = None
        self._plans = None

        if links is not None:
          self.links = links
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if total_count is not None:
          self.total_count = total_count
        if plans is not None:
          self.plans = plans

    @property
    def links(self):
        """
        Gets the links of this GetAllPlansResponse.

        :return: The links of this GetAllPlansResponse.
        :rtype: GetAllPlansResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this GetAllPlansResponse.

        :param links: The links of this GetAllPlansResponse.
        :type: GetAllPlansResponseLinks
        """

        self._links = links

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this GetAllPlansResponse.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :return: The submit_time_utc of this GetAllPlansResponse.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this GetAllPlansResponse.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :param submit_time_utc: The submit_time_utc of this GetAllPlansResponse.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

    @property
    def total_count(self):
        """
        Gets the total_count of this GetAllPlansResponse.
        total number of plans created

        :return: The total_count of this GetAllPlansResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this GetAllPlansResponse.
        total number of plans created

        :param total_count: The total_count of this GetAllPlansResponse.
        :type: int
        """

        self._total_count = total_count

    @property
    def plans(self):
        """
        Gets the plans of this GetAllPlansResponse.

        :return: The plans of this GetAllPlansResponse.
        :rtype: list[GetAllPlansResponsePlans]
        """
        return self._plans

    @plans.setter
    def plans(self, plans):
        """
        Sets the plans of this GetAllPlansResponse.

        :param plans: The plans of this GetAllPlansResponse.
        :type: list[GetAllPlansResponsePlans]
        """

        self._plans = plans

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
        if not isinstance(other, GetAllPlansResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
