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


class Ptsv2payoutsSenderInformation(object):
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
        'reference_number': 'str',
        'account': 'Ptsv2payoutsSenderInformationAccount',
        'first_name': 'str',
        'middle_initial': 'str',
        'last_name': 'str',
        'name': 'str',
        'address1': 'str',
        'locality': 'str',
        'administrative_area': 'str',
        'country_code': 'str',
        'postal_code': 'str',
        'phone_number': 'str',
        'date_of_birth': 'str',
        'vat_registration_number': 'str'
    }

    attribute_map = {
        'reference_number': 'referenceNumber',
        'account': 'account',
        'first_name': 'firstName',
        'middle_initial': 'middleInitial',
        'last_name': 'lastName',
        'name': 'name',
        'address1': 'address1',
        'locality': 'locality',
        'administrative_area': 'administrativeArea',
        'country_code': 'countryCode',
        'postal_code': 'postalCode',
        'phone_number': 'phoneNumber',
        'date_of_birth': 'dateOfBirth',
        'vat_registration_number': 'vatRegistrationNumber'
    }

    def __init__(self, reference_number=None, account=None, first_name=None, middle_initial=None, last_name=None, name=None, address1=None, locality=None, administrative_area=None, country_code=None, postal_code=None, phone_number=None, date_of_birth=None, vat_registration_number=None):
        """
        Ptsv2payoutsSenderInformation - a model defined in Swagger
        """

        self._reference_number = None
        self._account = None
        self._first_name = None
        self._middle_initial = None
        self._last_name = None
        self._name = None
        self._address1 = None
        self._locality = None
        self._administrative_area = None
        self._country_code = None
        self._postal_code = None
        self._phone_number = None
        self._date_of_birth = None
        self._vat_registration_number = None

        if reference_number is not None:
          self.reference_number = reference_number
        if account is not None:
          self.account = account
        if first_name is not None:
          self.first_name = first_name
        if middle_initial is not None:
          self.middle_initial = middle_initial
        if last_name is not None:
          self.last_name = last_name
        if name is not None:
          self.name = name
        if address1 is not None:
          self.address1 = address1
        if locality is not None:
          self.locality = locality
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if country_code is not None:
          self.country_code = country_code
        if postal_code is not None:
          self.postal_code = postal_code
        if phone_number is not None:
          self.phone_number = phone_number
        if date_of_birth is not None:
          self.date_of_birth = date_of_birth
        if vat_registration_number is not None:
          self.vat_registration_number = vat_registration_number

    @property
    def reference_number(self):
        """
        Gets the reference_number of this Ptsv2payoutsSenderInformation.
        Reference number generated by you that uniquely identifies the sender.

        :return: The reference_number of this Ptsv2payoutsSenderInformation.
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """
        Sets the reference_number of this Ptsv2payoutsSenderInformation.
        Reference number generated by you that uniquely identifies the sender.

        :param reference_number: The reference_number of this Ptsv2payoutsSenderInformation.
        :type: str
        """
        if reference_number is not None and len(reference_number) > 19:
            raise ValueError("Invalid value for `reference_number`, length must be less than or equal to `19`")

        self._reference_number = reference_number

    @property
    def account(self):
        """
        Gets the account of this Ptsv2payoutsSenderInformation.

        :return: The account of this Ptsv2payoutsSenderInformation.
        :rtype: Ptsv2payoutsSenderInformationAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this Ptsv2payoutsSenderInformation.

        :param account: The account of this Ptsv2payoutsSenderInformation.
        :type: Ptsv2payoutsSenderInformationAccount
        """

        self._account = account

    @property
    def first_name(self):
        """
        Gets the first_name of this Ptsv2payoutsSenderInformation.
        First name of sender (Optional). * CTV (14) * Paymentech (30) 

        :return: The first_name of this Ptsv2payoutsSenderInformation.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Ptsv2payoutsSenderInformation.
        First name of sender (Optional). * CTV (14) * Paymentech (30) 

        :param first_name: The first_name of this Ptsv2payoutsSenderInformation.
        :type: str
        """
        if first_name is not None and len(first_name) > 35:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `35`")

        self._first_name = first_name

    @property
    def middle_initial(self):
        """
        Gets the middle_initial of this Ptsv2payoutsSenderInformation.
        Recipient middle initial (Optional). 

        :return: The middle_initial of this Ptsv2payoutsSenderInformation.
        :rtype: str
        """
        return self._middle_initial

    @middle_initial.setter
    def middle_initial(self, middle_initial):
        """
        Sets the middle_initial of this Ptsv2payoutsSenderInformation.
        Recipient middle initial (Optional). 

        :param middle_initial: The middle_initial of this Ptsv2payoutsSenderInformation.
        :type: str
        """
        if middle_initial is not None and len(middle_initial) > 1:
            raise ValueError("Invalid value for `middle_initial`, length must be less than or equal to `1`")

        self._middle_initial = middle_initial

    @property
    def last_name(self):
        """
        Gets the last_name of this Ptsv2payoutsSenderInformation.
        Recipient last name (Optional). * CTV (14) * Paymentech (30) 

        :return: The last_name of this Ptsv2payoutsSenderInformation.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Ptsv2payoutsSenderInformation.
        Recipient last name (Optional). * CTV (14) * Paymentech (30) 

        :param last_name: The last_name of this Ptsv2payoutsSenderInformation.
        :type: str
        """
        if last_name is not None and len(last_name) > 35:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `35`")

        self._last_name = last_name

    @property
    def name(self):
        """
        Gets the name of this Ptsv2payoutsSenderInformation.
        Name of sender.  **Funds Disbursement**  This value is the name of the originator sending the funds disbursement. * CTV, Paymentech (30) 

        :return: The name of this Ptsv2payoutsSenderInformation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Ptsv2payoutsSenderInformation.
        Name of sender.  **Funds Disbursement**  This value is the name of the originator sending the funds disbursement. * CTV, Paymentech (30) 

        :param name: The name of this Ptsv2payoutsSenderInformation.
        :type: str
        """
        if name is not None and len(name) > 24:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `24`")

        self._name = name

    @property
    def address1(self):
        """
        Gets the address1 of this Ptsv2payoutsSenderInformation.
        Street address of sender.  **Funds Disbursement**  This value is the address of the originator sending the funds disbursement. 

        :return: The address1 of this Ptsv2payoutsSenderInformation.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this Ptsv2payoutsSenderInformation.
        Street address of sender.  **Funds Disbursement**  This value is the address of the originator sending the funds disbursement. 

        :param address1: The address1 of this Ptsv2payoutsSenderInformation.
        :type: str
        """
        if address1 is not None and len(address1) > 50:
            raise ValueError("Invalid value for `address1`, length must be less than or equal to `50`")

        self._address1 = address1

    @property
    def locality(self):
        """
        Gets the locality of this Ptsv2payoutsSenderInformation.
        City of sender.  **Funds Disbursement**  This value is the city of the originator sending the funds disbursement. 

        :return: The locality of this Ptsv2payoutsSenderInformation.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Ptsv2payoutsSenderInformation.
        City of sender.  **Funds Disbursement**  This value is the city of the originator sending the funds disbursement. 

        :param locality: The locality of this Ptsv2payoutsSenderInformation.
        :type: str
        """
        if locality is not None and len(locality) > 25:
            raise ValueError("Invalid value for `locality`, length must be less than or equal to `25`")

        self._locality = locality

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this Ptsv2payoutsSenderInformation.
        Sender’s state. Use the State, Province, and Territory Codes for the United States and Canada. 

        :return: The administrative_area of this Ptsv2payoutsSenderInformation.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this Ptsv2payoutsSenderInformation.
        Sender’s state. Use the State, Province, and Territory Codes for the United States and Canada. 

        :param administrative_area: The administrative_area of this Ptsv2payoutsSenderInformation.
        :type: str
        """
        if administrative_area is not None and len(administrative_area) > 2:
            raise ValueError("Invalid value for `administrative_area`, length must be less than or equal to `2`")

        self._administrative_area = administrative_area

    @property
    def country_code(self):
        """
        Gets the country_code of this Ptsv2payoutsSenderInformation.
        Country of sender. Use the ISO Standard Country Codes. * CTV (3) 

        :return: The country_code of this Ptsv2payoutsSenderInformation.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this Ptsv2payoutsSenderInformation.
        Country of sender. Use the ISO Standard Country Codes. * CTV (3) 

        :param country_code: The country_code of this Ptsv2payoutsSenderInformation.
        :type: str
        """
        if country_code is not None and len(country_code) > 2:
            raise ValueError("Invalid value for `country_code`, length must be less than or equal to `2`")

        self._country_code = country_code

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Ptsv2payoutsSenderInformation.
        Sender’s postal code. Required only for FDCCompass.

        :return: The postal_code of this Ptsv2payoutsSenderInformation.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Ptsv2payoutsSenderInformation.
        Sender’s postal code. Required only for FDCCompass.

        :param postal_code: The postal_code of this Ptsv2payoutsSenderInformation.
        :type: str
        """
        if postal_code is not None and len(postal_code) > 10:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `10`")

        self._postal_code = postal_code

    @property
    def phone_number(self):
        """
        Gets the phone_number of this Ptsv2payoutsSenderInformation.
        Sender’s phone number. Required only for FDCCompass.

        :return: The phone_number of this Ptsv2payoutsSenderInformation.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this Ptsv2payoutsSenderInformation.
        Sender’s phone number. Required only for FDCCompass.

        :param phone_number: The phone_number of this Ptsv2payoutsSenderInformation.
        :type: str
        """
        if phone_number is not None and len(phone_number) > 20:
            raise ValueError("Invalid value for `phone_number`, length must be less than or equal to `20`")

        self._phone_number = phone_number

    @property
    def date_of_birth(self):
        """
        Gets the date_of_birth of this Ptsv2payoutsSenderInformation.
        Sender’s date of birth in YYYYMMDD format. Required only for FDCCompass.

        :return: The date_of_birth of this Ptsv2payoutsSenderInformation.
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """
        Sets the date_of_birth of this Ptsv2payoutsSenderInformation.
        Sender’s date of birth in YYYYMMDD format. Required only for FDCCompass.

        :param date_of_birth: The date_of_birth of this Ptsv2payoutsSenderInformation.
        :type: str
        """
        if date_of_birth is not None and len(date_of_birth) > 8:
            raise ValueError("Invalid value for `date_of_birth`, length must be less than or equal to `8`")
        if date_of_birth is not None and len(date_of_birth) < 8:
            raise ValueError("Invalid value for `date_of_birth`, length must be greater than or equal to `8`")

        self._date_of_birth = date_of_birth

    @property
    def vat_registration_number(self):
        """
        Gets the vat_registration_number of this Ptsv2payoutsSenderInformation.
        Customer's government-assigned tax identification number. 

        :return: The vat_registration_number of this Ptsv2payoutsSenderInformation.
        :rtype: str
        """
        return self._vat_registration_number

    @vat_registration_number.setter
    def vat_registration_number(self, vat_registration_number):
        """
        Sets the vat_registration_number of this Ptsv2payoutsSenderInformation.
        Customer's government-assigned tax identification number. 

        :param vat_registration_number: The vat_registration_number of this Ptsv2payoutsSenderInformation.
        :type: str
        """
        if vat_registration_number is not None and len(vat_registration_number) > 13:
            raise ValueError("Invalid value for `vat_registration_number`, length must be less than or equal to `13`")

        self._vat_registration_number = vat_registration_number

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
        if not isinstance(other, Ptsv2payoutsSenderInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
