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


class Boardingv1registrationsOrganizationInformationOwners(object):
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
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'birth_date': 'date',
        'is_primary': 'bool',
        'ssn': 'str',
        'passport_number': 'str',
        'passport_country': 'str',
        'job_title': 'str',
        'has_significant_responsability': 'bool',
        'ownership_percentage': 'float',
        'phone_number': 'str',
        'email': 'str',
        'address': 'Boardingv1registrationsOrganizationInformationBusinessInformationAddress'
    }

    attribute_map = {
        'first_name': 'firstName',
        'middle_name': 'middleName',
        'last_name': 'lastName',
        'birth_date': 'birthDate',
        'is_primary': 'isPrimary',
        'ssn': 'ssn',
        'passport_number': 'passportNumber',
        'passport_country': 'passportCountry',
        'job_title': 'jobTitle',
        'has_significant_responsability': 'hasSignificantResponsability',
        'ownership_percentage': 'ownershipPercentage',
        'phone_number': 'phoneNumber',
        'email': 'email',
        'address': 'address'
    }

    def __init__(self, first_name=None, middle_name=None, last_name=None, birth_date=None, is_primary=None, ssn=None, passport_number=None, passport_country=None, job_title=None, has_significant_responsability=None, ownership_percentage=None, phone_number=None, email=None, address=None):
        """
        Boardingv1registrationsOrganizationInformationOwners - a model defined in Swagger
        """

        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._birth_date = None
        self._is_primary = None
        self._ssn = None
        self._passport_number = None
        self._passport_country = None
        self._job_title = None
        self._has_significant_responsability = None
        self._ownership_percentage = None
        self._phone_number = None
        self._email = None
        self._address = None

        self.first_name = first_name
        if middle_name is not None:
          self.middle_name = middle_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.is_primary = is_primary
        if ssn is not None:
          self.ssn = ssn
        if passport_number is not None:
          self.passport_number = passport_number
        if passport_country is not None:
          self.passport_country = passport_country
        self.job_title = job_title
        self.has_significant_responsability = has_significant_responsability
        self.ownership_percentage = ownership_percentage
        self.phone_number = phone_number
        self.email = email
        self.address = address

    @property
    def first_name(self):
        """
        Gets the first_name of this Boardingv1registrationsOrganizationInformationOwners.

        :return: The first_name of this Boardingv1registrationsOrganizationInformationOwners.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Boardingv1registrationsOrganizationInformationOwners.

        :param first_name: The first_name of this Boardingv1registrationsOrganizationInformationOwners.
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")
        if first_name is not None and not re.search('[À-ÖØ-öø-ǿÀ-ÖØ-öø-ǿa-zA-Z().\\-_#,;\/\\\\@$:&amp;!?%«»€₣«»€₣ ]{1,}$', first_name):
            raise ValueError("Invalid value for `first_name`, must be a follow pattern or equal to `/[À-ÖØ-öø-ǿÀ-ÖØ-öø-ǿa-zA-Z().\\-_#,;\/\\\\@$:&amp;!?%«»€₣«»€₣ ]{1,}$/`")

        self._first_name = first_name

    @property
    def middle_name(self):
        """
        Gets the middle_name of this Boardingv1registrationsOrganizationInformationOwners.

        :return: The middle_name of this Boardingv1registrationsOrganizationInformationOwners.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """
        Sets the middle_name of this Boardingv1registrationsOrganizationInformationOwners.

        :param middle_name: The middle_name of this Boardingv1registrationsOrganizationInformationOwners.
        :type: str
        """
        if middle_name is not None and not re.search('[À-ÖØ-öø-ǿÀ-ÖØ-öø-ǿa-zA-Z().\\-_#,;\/\\\\@$:&amp;!?%«»€₣«»€₣ ]{1,}$', middle_name):
            raise ValueError("Invalid value for `middle_name`, must be a follow pattern or equal to `/[À-ÖØ-öø-ǿÀ-ÖØ-öø-ǿa-zA-Z().\\-_#,;\/\\\\@$:&amp;!?%«»€₣«»€₣ ]{1,}$/`")

        self._middle_name = middle_name

    @property
    def last_name(self):
        """
        Gets the last_name of this Boardingv1registrationsOrganizationInformationOwners.

        :return: The last_name of this Boardingv1registrationsOrganizationInformationOwners.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Boardingv1registrationsOrganizationInformationOwners.

        :param last_name: The last_name of this Boardingv1registrationsOrganizationInformationOwners.
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")
        if last_name is not None and not re.search('[À-ÖØ-öø-ǿÀ-ÖØ-öø-ǿa-zA-Z().\\-_#,;\/\\\\@$:&amp;!?%«»€₣«»€₣ ]{1,}$', last_name):
            raise ValueError("Invalid value for `last_name`, must be a follow pattern or equal to `/[À-ÖØ-öø-ǿÀ-ÖØ-öø-ǿa-zA-Z().\\-_#,;\/\\\\@$:&amp;!?%«»€₣«»€₣ ]{1,}$/`")

        self._last_name = last_name

    @property
    def birth_date(self):
        """
        Gets the birth_date of this Boardingv1registrationsOrganizationInformationOwners.
        `Format: YYYY-MM-DD` Example 2016-08-11 equals August 11, 2016 

        :return: The birth_date of this Boardingv1registrationsOrganizationInformationOwners.
        :rtype: date
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """
        Sets the birth_date of this Boardingv1registrationsOrganizationInformationOwners.
        `Format: YYYY-MM-DD` Example 2016-08-11 equals August 11, 2016 

        :param birth_date: The birth_date of this Boardingv1registrationsOrganizationInformationOwners.
        :type: date
        """
        if birth_date is None:
            raise ValueError("Invalid value for `birth_date`, must not be `None`")

        self._birth_date = birth_date

    @property
    def is_primary(self):
        """
        Gets the is_primary of this Boardingv1registrationsOrganizationInformationOwners.
        Determines whether the owner is the Primary owner of the organization

        :return: The is_primary of this Boardingv1registrationsOrganizationInformationOwners.
        :rtype: bool
        """
        return self._is_primary

    @is_primary.setter
    def is_primary(self, is_primary):
        """
        Sets the is_primary of this Boardingv1registrationsOrganizationInformationOwners.
        Determines whether the owner is the Primary owner of the organization

        :param is_primary: The is_primary of this Boardingv1registrationsOrganizationInformationOwners.
        :type: bool
        """
        if is_primary is None:
            raise ValueError("Invalid value for `is_primary`, must not be `None`")

        self._is_primary = is_primary

    @property
    def ssn(self):
        """
        Gets the ssn of this Boardingv1registrationsOrganizationInformationOwners.
        Social Security Number

        :return: The ssn of this Boardingv1registrationsOrganizationInformationOwners.
        :rtype: str
        """
        return self._ssn

    @ssn.setter
    def ssn(self, ssn):
        """
        Sets the ssn of this Boardingv1registrationsOrganizationInformationOwners.
        Social Security Number

        :param ssn: The ssn of this Boardingv1registrationsOrganizationInformationOwners.
        :type: str
        """
        if ssn is not None and not re.search('^\\d{3}-\\d{2}-\\d{4}$|^\\d{9,9}$', ssn):
            raise ValueError("Invalid value for `ssn`, must be a follow pattern or equal to `/^\\d{3}-\\d{2}-\\d{4}$|^\\d{9,9}$/`")

        self._ssn = ssn

    @property
    def passport_number(self):
        """
        Gets the passport_number of this Boardingv1registrationsOrganizationInformationOwners.
        Passport number

        :return: The passport_number of this Boardingv1registrationsOrganizationInformationOwners.
        :rtype: str
        """
        return self._passport_number

    @passport_number.setter
    def passport_number(self, passport_number):
        """
        Sets the passport_number of this Boardingv1registrationsOrganizationInformationOwners.
        Passport number

        :param passport_number: The passport_number of this Boardingv1registrationsOrganizationInformationOwners.
        :type: str
        """
        if passport_number is not None and not re.search('^(?!^0+$)[a-zA-Z0-9]{3,20}$', passport_number):
            raise ValueError("Invalid value for `passport_number`, must be a follow pattern or equal to `/^(?!^0+$)[a-zA-Z0-9]{3,20}$/`")

        self._passport_number = passport_number

    @property
    def passport_country(self):
        """
        Gets the passport_country of this Boardingv1registrationsOrganizationInformationOwners.

        :return: The passport_country of this Boardingv1registrationsOrganizationInformationOwners.
        :rtype: str
        """
        return self._passport_country

    @passport_country.setter
    def passport_country(self, passport_country):
        """
        Sets the passport_country of this Boardingv1registrationsOrganizationInformationOwners.

        :param passport_country: The passport_country of this Boardingv1registrationsOrganizationInformationOwners.
        :type: str
        """
        if passport_country is not None and not re.search('^[À-ÖØ-öø-ǿa-zA-Z0-9().\\-_#,;\/@$:!% ]{1,}$', passport_country):
            raise ValueError("Invalid value for `passport_country`, must be a follow pattern or equal to `/^[À-ÖØ-öø-ǿa-zA-Z0-9().\\-_#,;\/@$:!% ]{1,}$/`")

        self._passport_country = passport_country

    @property
    def job_title(self):
        """
        Gets the job_title of this Boardingv1registrationsOrganizationInformationOwners.

        :return: The job_title of this Boardingv1registrationsOrganizationInformationOwners.
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """
        Sets the job_title of this Boardingv1registrationsOrganizationInformationOwners.

        :param job_title: The job_title of this Boardingv1registrationsOrganizationInformationOwners.
        :type: str
        """
        if job_title is None:
            raise ValueError("Invalid value for `job_title`, must not be `None`")
        if job_title is not None and not re.search('^[À-ÖØ-öø-ǿa-zA-Z0-9().\\-_#,;\/@$:!% ]{1,}$', job_title):
            raise ValueError("Invalid value for `job_title`, must be a follow pattern or equal to `/^[À-ÖØ-öø-ǿa-zA-Z0-9().\\-_#,;\/@$:!% ]{1,}$/`")

        self._job_title = job_title

    @property
    def has_significant_responsability(self):
        """
        Gets the has_significant_responsability of this Boardingv1registrationsOrganizationInformationOwners.
        Determines whether owner has significant responsibility to control, manage or direct the company

        :return: The has_significant_responsability of this Boardingv1registrationsOrganizationInformationOwners.
        :rtype: bool
        """
        return self._has_significant_responsability

    @has_significant_responsability.setter
    def has_significant_responsability(self, has_significant_responsability):
        """
        Sets the has_significant_responsability of this Boardingv1registrationsOrganizationInformationOwners.
        Determines whether owner has significant responsibility to control, manage or direct the company

        :param has_significant_responsability: The has_significant_responsability of this Boardingv1registrationsOrganizationInformationOwners.
        :type: bool
        """
        if has_significant_responsability is None:
            raise ValueError("Invalid value for `has_significant_responsability`, must not be `None`")

        self._has_significant_responsability = has_significant_responsability

    @property
    def ownership_percentage(self):
        """
        Gets the ownership_percentage of this Boardingv1registrationsOrganizationInformationOwners.
        Determines the percentage of ownership this owner has. For the primary owner the percentage can be from 0-100; for other owners the percentage can be from 25-100 and the sum of ownership accross owners cannot exceed 100

        :return: The ownership_percentage of this Boardingv1registrationsOrganizationInformationOwners.
        :rtype: float
        """
        return self._ownership_percentage

    @ownership_percentage.setter
    def ownership_percentage(self, ownership_percentage):
        """
        Sets the ownership_percentage of this Boardingv1registrationsOrganizationInformationOwners.
        Determines the percentage of ownership this owner has. For the primary owner the percentage can be from 0-100; for other owners the percentage can be from 25-100 and the sum of ownership accross owners cannot exceed 100

        :param ownership_percentage: The ownership_percentage of this Boardingv1registrationsOrganizationInformationOwners.
        :type: float
        """
        if ownership_percentage is None:
            raise ValueError("Invalid value for `ownership_percentage`, must not be `None`")

        self._ownership_percentage = ownership_percentage

    @property
    def phone_number(self):
        """
        Gets the phone_number of this Boardingv1registrationsOrganizationInformationOwners.

        :return: The phone_number of this Boardingv1registrationsOrganizationInformationOwners.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this Boardingv1registrationsOrganizationInformationOwners.

        :param phone_number: The phone_number of this Boardingv1registrationsOrganizationInformationOwners.
        :type: str
        """
        if phone_number is None:
            raise ValueError("Invalid value for `phone_number`, must not be `None`")
        if phone_number is not None and not re.search('^[0-9a-zA-Z\\\\+\\\\-]+$', phone_number):
            raise ValueError("Invalid value for `phone_number`, must be a follow pattern or equal to `/^[0-9a-zA-Z\\\\+\\\\-]+$/`")

        self._phone_number = phone_number

    @property
    def email(self):
        """
        Gets the email of this Boardingv1registrationsOrganizationInformationOwners.

        :return: The email of this Boardingv1registrationsOrganizationInformationOwners.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Boardingv1registrationsOrganizationInformationOwners.

        :param email: The email of this Boardingv1registrationsOrganizationInformationOwners.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")
        if email is not None and not re.search('^([a-zA-Z0-9_\\-\\.]+)@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.)|(([a-zA-Z0-9\\-]+\\.)+))([a-zA-Z]{2,50}|[0-9]{1,3})(\\]?)$', email):
            raise ValueError("Invalid value for `email`, must be a follow pattern or equal to `/^([a-zA-Z0-9_\\-\\.]+)@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.)|(([a-zA-Z0-9\\-]+\\.)+))([a-zA-Z]{2,50}|[0-9]{1,3})(\\]?)$/`")

        self._email = email

    @property
    def address(self):
        """
        Gets the address of this Boardingv1registrationsOrganizationInformationOwners.

        :return: The address of this Boardingv1registrationsOrganizationInformationOwners.
        :rtype: Boardingv1registrationsOrganizationInformationBusinessInformationAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Boardingv1registrationsOrganizationInformationOwners.

        :param address: The address of this Boardingv1registrationsOrganizationInformationOwners.
        :type: Boardingv1registrationsOrganizationInformationBusinessInformationAddress
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")

        self._address = address

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
        if not isinstance(other, Boardingv1registrationsOrganizationInformationOwners):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
