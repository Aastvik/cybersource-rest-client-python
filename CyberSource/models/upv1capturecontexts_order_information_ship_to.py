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


class Upv1capturecontextsOrderInformationShipTo(object):
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
        'address1': 'str',
        'address2': 'str',
        'address3': 'str',
        'address4': 'str',
        'administrative_area': 'str',
        'building_number': 'str',
        'country': 'str',
        'district': 'str',
        'locality': 'str',
        'postal_code': 'str',
        'first_name': 'str',
        'last_name': 'str'
    }

    attribute_map = {
        'address1': 'address1',
        'address2': 'address2',
        'address3': 'address3',
        'address4': 'address4',
        'administrative_area': 'administrativeArea',
        'building_number': 'buildingNumber',
        'country': 'country',
        'district': 'district',
        'locality': 'locality',
        'postal_code': 'postalCode',
        'first_name': 'firstName',
        'last_name': 'lastName'
    }

    def __init__(self, address1=None, address2=None, address3=None, address4=None, administrative_area=None, building_number=None, country=None, district=None, locality=None, postal_code=None, first_name=None, last_name=None):
        """
        Upv1capturecontextsOrderInformationShipTo - a model defined in Swagger
        """

        self._address1 = None
        self._address2 = None
        self._address3 = None
        self._address4 = None
        self._administrative_area = None
        self._building_number = None
        self._country = None
        self._district = None
        self._locality = None
        self._postal_code = None
        self._first_name = None
        self._last_name = None

        if address1 is not None:
          self.address1 = address1
        if address2 is not None:
          self.address2 = address2
        if address3 is not None:
          self.address3 = address3
        if address4 is not None:
          self.address4 = address4
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if building_number is not None:
          self.building_number = building_number
        if country is not None:
          self.country = country
        if district is not None:
          self.district = district
        if locality is not None:
          self.locality = locality
        if postal_code is not None:
          self.postal_code = postal_code
        if first_name is not None:
          self.first_name = first_name
        if last_name is not None:
          self.last_name = last_name

    @property
    def address1(self):
        """
        Gets the address1 of this Upv1capturecontextsOrderInformationShipTo.
        First line of the shipping address. 

        :return: The address1 of this Upv1capturecontextsOrderInformationShipTo.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this Upv1capturecontextsOrderInformationShipTo.
        First line of the shipping address. 

        :param address1: The address1 of this Upv1capturecontextsOrderInformationShipTo.
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this Upv1capturecontextsOrderInformationShipTo.
        Second line of the shipping address. 

        :return: The address2 of this Upv1capturecontextsOrderInformationShipTo.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this Upv1capturecontextsOrderInformationShipTo.
        Second line of the shipping address. 

        :param address2: The address2 of this Upv1capturecontextsOrderInformationShipTo.
        :type: str
        """

        self._address2 = address2

    @property
    def address3(self):
        """
        Gets the address3 of this Upv1capturecontextsOrderInformationShipTo.
        Third line of the shipping address. 

        :return: The address3 of this Upv1capturecontextsOrderInformationShipTo.
        :rtype: str
        """
        return self._address3

    @address3.setter
    def address3(self, address3):
        """
        Sets the address3 of this Upv1capturecontextsOrderInformationShipTo.
        Third line of the shipping address. 

        :param address3: The address3 of this Upv1capturecontextsOrderInformationShipTo.
        :type: str
        """

        self._address3 = address3

    @property
    def address4(self):
        """
        Gets the address4 of this Upv1capturecontextsOrderInformationShipTo.
        Fourth line of the shipping address.

        :return: The address4 of this Upv1capturecontextsOrderInformationShipTo.
        :rtype: str
        """
        return self._address4

    @address4.setter
    def address4(self, address4):
        """
        Sets the address4 of this Upv1capturecontextsOrderInformationShipTo.
        Fourth line of the shipping address.

        :param address4: The address4 of this Upv1capturecontextsOrderInformationShipTo.
        :type: str
        """

        self._address4 = address4

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this Upv1capturecontextsOrderInformationShipTo.
        State or province of the shipping address.  Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf) 

        :return: The administrative_area of this Upv1capturecontextsOrderInformationShipTo.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this Upv1capturecontextsOrderInformationShipTo.
        State or province of the shipping address.  Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf) 

        :param administrative_area: The administrative_area of this Upv1capturecontextsOrderInformationShipTo.
        :type: str
        """

        self._administrative_area = administrative_area

    @property
    def building_number(self):
        """
        Gets the building_number of this Upv1capturecontextsOrderInformationShipTo.
        Building number in the street address. 

        :return: The building_number of this Upv1capturecontextsOrderInformationShipTo.
        :rtype: str
        """
        return self._building_number

    @building_number.setter
    def building_number(self, building_number):
        """
        Sets the building_number of this Upv1capturecontextsOrderInformationShipTo.
        Building number in the street address. 

        :param building_number: The building_number of this Upv1capturecontextsOrderInformationShipTo.
        :type: str
        """

        self._building_number = building_number

    @property
    def country(self):
        """
        Gets the country of this Upv1capturecontextsOrderInformationShipTo.
        Country of the shipping address.  Use the two-character [ISO Standard Country Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf) 

        :return: The country of this Upv1capturecontextsOrderInformationShipTo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Upv1capturecontextsOrderInformationShipTo.
        Country of the shipping address.  Use the two-character [ISO Standard Country Codes.](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf) 

        :param country: The country of this Upv1capturecontextsOrderInformationShipTo.
        :type: str
        """

        self._country = country

    @property
    def district(self):
        """
        Gets the district of this Upv1capturecontextsOrderInformationShipTo.
        Neighborhood, community, or region within a city or municipality.

        :return: The district of this Upv1capturecontextsOrderInformationShipTo.
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """
        Sets the district of this Upv1capturecontextsOrderInformationShipTo.
        Neighborhood, community, or region within a city or municipality.

        :param district: The district of this Upv1capturecontextsOrderInformationShipTo.
        :type: str
        """

        self._district = district

    @property
    def locality(self):
        """
        Gets the locality of this Upv1capturecontextsOrderInformationShipTo.
        City of the shipping address. 

        :return: The locality of this Upv1capturecontextsOrderInformationShipTo.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Upv1capturecontextsOrderInformationShipTo.
        City of the shipping address. 

        :param locality: The locality of this Upv1capturecontextsOrderInformationShipTo.
        :type: str
        """

        self._locality = locality

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Upv1capturecontextsOrderInformationShipTo.
        Postal code for the shipping address. The postal code must consist of 5 to 9 digits. 

        :return: The postal_code of this Upv1capturecontextsOrderInformationShipTo.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Upv1capturecontextsOrderInformationShipTo.
        Postal code for the shipping address. The postal code must consist of 5 to 9 digits. 

        :param postal_code: The postal_code of this Upv1capturecontextsOrderInformationShipTo.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def first_name(self):
        """
        Gets the first_name of this Upv1capturecontextsOrderInformationShipTo.
        First name of the recipient

        :return: The first_name of this Upv1capturecontextsOrderInformationShipTo.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Upv1capturecontextsOrderInformationShipTo.
        First name of the recipient

        :param first_name: The first_name of this Upv1capturecontextsOrderInformationShipTo.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this Upv1capturecontextsOrderInformationShipTo.
        Last name of the recipient.

        :return: The last_name of this Upv1capturecontextsOrderInformationShipTo.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Upv1capturecontextsOrderInformationShipTo.
        Last name of the recipient.

        :param last_name: The last_name of this Upv1capturecontextsOrderInformationShipTo.
        :type: str
        """

        self._last_name = last_name

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
        if not isinstance(other, Upv1capturecontextsOrderInformationShipTo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
