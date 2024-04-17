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


class Ptsv2paymentsidcapturesAggregatorInformationSubMerchant(object):
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
        'name': 'str',
        'address1': 'str',
        'locality': 'str',
        'administrative_area': 'str',
        'postal_code': 'str',
        'country': 'str',
        'email': 'str',
        'phone_number': 'str',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'address1': 'address1',
        'locality': 'locality',
        'administrative_area': 'administrativeArea',
        'postal_code': 'postalCode',
        'country': 'country',
        'email': 'email',
        'phone_number': 'phoneNumber',
        'id': 'id'
    }

    def __init__(self, name=None, address1=None, locality=None, administrative_area=None, postal_code=None, country=None, email=None, phone_number=None, id=None):
        """
        Ptsv2paymentsidcapturesAggregatorInformationSubMerchant - a model defined in Swagger
        """

        self._name = None
        self._address1 = None
        self._locality = None
        self._administrative_area = None
        self._postal_code = None
        self._country = None
        self._email = None
        self._phone_number = None
        self._id = None

        if name is not None:
          self.name = name
        if address1 is not None:
          self.address1 = address1
        if locality is not None:
          self.locality = locality
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if postal_code is not None:
          self.postal_code = postal_code
        if country is not None:
          self.country = country
        if email is not None:
          self.email = email
        if phone_number is not None:
          self.phone_number = phone_number
        if id is not None:
          self.id = id

    @property
    def name(self):
        """
        Gets the name of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        Sub-merchant's business name.  #### American Express Direct The maximum length of the sub-merchant name depends on the length of the aggregator name. The combined length for both values must not exceed 36 characters.  #### CyberSource through VisaNet With American Express, the maximum length of the sub-merchant name depends on the length of the aggregator name. The combined length for both values must not exceed 36 characters. The value for this field does not map to the TC 33 capture file5.  #### FDC Compass This value must consist of uppercase characters.  #### FDC Nashville Global With Mastercard, the maximum length of the sub-merchant name depends on the length of the aggregator name: - If aggregator name length is 1 through 3, maximum sub-merchant name length is 21. - If aggregator name length is 4 through 7, maximum sub-merchant name length is 17. - If aggregator name length is 8 through 12, maximum sub-merchant name length is 12. 

        :return: The name of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        Sub-merchant's business name.  #### American Express Direct The maximum length of the sub-merchant name depends on the length of the aggregator name. The combined length for both values must not exceed 36 characters.  #### CyberSource through VisaNet With American Express, the maximum length of the sub-merchant name depends on the length of the aggregator name. The combined length for both values must not exceed 36 characters. The value for this field does not map to the TC 33 capture file5.  #### FDC Compass This value must consist of uppercase characters.  #### FDC Nashville Global With Mastercard, the maximum length of the sub-merchant name depends on the length of the aggregator name: - If aggregator name length is 1 through 3, maximum sub-merchant name length is 21. - If aggregator name length is 4 through 7, maximum sub-merchant name length is 17. - If aggregator name length is 8 through 12, maximum sub-merchant name length is 12. 

        :param name: The name of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :type: str
        """

        self._name = name

    @property
    def address1(self):
        """
        Gets the address1 of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        First line of the sub-merchant's street address.  For processor-specific details, see `submerchant_street` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### CyberSource through VisaNet The value for this field does not map to the TC 33 capture file5.  #### FDC Compass This value must consist of uppercase characters. 

        :return: The address1 of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        First line of the sub-merchant's street address.  For processor-specific details, see `submerchant_street` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### CyberSource through VisaNet The value for this field does not map to the TC 33 capture file5.  #### FDC Compass This value must consist of uppercase characters. 

        :param address1: The address1 of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :type: str
        """

        self._address1 = address1

    @property
    def locality(self):
        """
        Gets the locality of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        Sub-merchant's city.  For processor-specific details, see `submerchant_city` request field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### CyberSource through VisaNet The value for this field does not map to the TC 33 capture file5.  #### FDC Compass This value must consist of uppercase characters. 

        :return: The locality of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        Sub-merchant's city.  For processor-specific details, see `submerchant_city` request field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### CyberSource through VisaNet The value for this field does not map to the TC 33 capture file5.  #### FDC Compass This value must consist of uppercase characters. 

        :param locality: The locality of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :type: str
        """

        self._locality = locality

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        Sub-merchant's state or province.  For possible values and also aggregator support, see `submerchant_state` request field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### CyberSource through VisaNet The value for this field does not map to the TC 33 capture file5.  #### FDC Compass This value must consist of uppercase characters. 

        :return: The administrative_area of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        Sub-merchant's state or province.  For possible values and also aggregator support, see `submerchant_state` request field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### CyberSource through VisaNet The value for this field does not map to the TC 33 capture file5.  #### FDC Compass This value must consist of uppercase characters. 

        :param administrative_area: The administrative_area of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :type: str
        """

        self._administrative_area = administrative_area

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        Partial postal code for the sub-merchant's address.  For processor-specific details, see `submerchant_postal_code` request field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### CyberSource through VisaNet The value for this field does not map to the TC 33 capture file5.  #### FDC Compass This value must consist of uppercase characters. 

        :return: The postal_code of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        Partial postal code for the sub-merchant's address.  For processor-specific details, see `submerchant_postal_code` request field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  #### CyberSource through VisaNet The value for this field does not map to the TC 33 capture file5.  #### FDC Compass This value must consist of uppercase characters. 

        :param postal_code: The postal_code of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country(self):
        """
        Gets the country of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        Sub-merchant's country. Use the [ISO Standard Country Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf).  #### CyberSource through VisaNet The value for this field does not map to the TC 33 capture file.  #### FDC Compass This value must consist of uppercase characters.  For details, see the `submerchant_country` request-level field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The country of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        Sub-merchant's country. Use the [ISO Standard Country Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf).  #### CyberSource through VisaNet The value for this field does not map to the TC 33 capture file.  #### FDC Compass This value must consist of uppercase characters.  For details, see the `submerchant_country` request-level field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param country: The country of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :type: str
        """

        self._country = country

    @property
    def email(self):
        """
        Gets the email of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        Sub-merchant's email address.  **Maximum length for processors**   - American Express Direct: 40  - CyberSource through VisaNet: 40  - FDC Compass: 40  - FDC Nashville Global: 19  #### CyberSource through VisaNet With American Express, the value for this field corresponds to the following data in the TC 33 capture file: - Record: CP01 TCRB - Position: 25-64 - Field: American Express Seller E-mail Address  **Note** The TC 33 Capture file contains information about the purchases and refunds that a merchant submits to CyberSource. CyberSource through VisaNet creates the TC 33 Capture file at the end of the day and sends it to the merchant's acquirer, who uses this information to facilitate end-of-day clearing processing with payment card companies. 

        :return: The email of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        Sub-merchant's email address.  **Maximum length for processors**   - American Express Direct: 40  - CyberSource through VisaNet: 40  - FDC Compass: 40  - FDC Nashville Global: 19  #### CyberSource through VisaNet With American Express, the value for this field corresponds to the following data in the TC 33 capture file: - Record: CP01 TCRB - Position: 25-64 - Field: American Express Seller E-mail Address  **Note** The TC 33 Capture file contains information about the purchases and refunds that a merchant submits to CyberSource. CyberSource through VisaNet creates the TC 33 Capture file at the end of the day and sends it to the merchant's acquirer, who uses this information to facilitate end-of-day clearing processing with payment card companies. 

        :param email: The email of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :type: str
        """

        self._email = email

    @property
    def phone_number(self):
        """
        Gets the phone_number of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        Sub-merchant's telephone number.  **Maximum length for procesors**   - American Express Direct: 20  - CyberSource through VisaNet: 20  - FDC Compass: 13  - FDC Nashville Global: 10  #### CyberSource through VisaNet With American Express, the value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP01 TCRB - Position: 5-24 - Field: American Express Seller Telephone Number  **FDC Compass**\\ This value must consist of uppercase characters. Use one of these recommended formats:\\ `NNN-NNN-NNNN`\\ `NNN-AAAAAAA` 

        :return: The phone_number of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        Sub-merchant's telephone number.  **Maximum length for procesors**   - American Express Direct: 20  - CyberSource through VisaNet: 20  - FDC Compass: 13  - FDC Nashville Global: 10  #### CyberSource through VisaNet With American Express, the value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP01 TCRB - Position: 5-24 - Field: American Express Seller Telephone Number  **FDC Compass**\\ This value must consist of uppercase characters. Use one of these recommended formats:\\ `NNN-NNN-NNNN`\\ `NNN-AAAAAAA` 

        :param phone_number: The phone_number of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def id(self):
        """
        Gets the id of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        The ID you assigned to your sub-merchant. CyberSource through VisaNet: For American Express transaction, the value for this field corresponds to the following data in the TC 33 capture file: - Record: CP01 TCRB - Position: 65-84 - Field: American Express Seller ID For  Mastercard transactions, the value for this field corresponds to the following data in the TC 33 capture file: - Record: CP01 TCR6 - Position: 117-131 - Field: Mastercard Sub-Merchant ID FDC Compass: This value must consist of uppercase characters.  American Express Direct: String (20) CyberSource through VisaNet with American Express: String (20) CyberSource through VisaNet with Mastercard: String (15) FDC Compass: String (20) FDC Nashville Global: String (14) 

        :return: The id of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        The ID you assigned to your sub-merchant. CyberSource through VisaNet: For American Express transaction, the value for this field corresponds to the following data in the TC 33 capture file: - Record: CP01 TCRB - Position: 65-84 - Field: American Express Seller ID For  Mastercard transactions, the value for this field corresponds to the following data in the TC 33 capture file: - Record: CP01 TCR6 - Position: 117-131 - Field: Mastercard Sub-Merchant ID FDC Compass: This value must consist of uppercase characters.  American Express Direct: String (20) CyberSource through VisaNet with American Express: String (20) CyberSource through VisaNet with Mastercard: String (15) FDC Compass: String (20) FDC Nashville Global: String (14) 

        :param id: The id of this Ptsv2paymentsidcapturesAggregatorInformationSubMerchant.
        :type: str
        """

        self._id = id

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
        if not isinstance(other, Ptsv2paymentsidcapturesAggregatorInformationSubMerchant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
