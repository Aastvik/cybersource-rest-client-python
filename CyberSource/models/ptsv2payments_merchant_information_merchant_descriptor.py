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


class Ptsv2paymentsMerchantInformationMerchantDescriptor(object):
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
        'alternate_name': 'str',
        'contact': 'str',
        'address1': 'str',
        'locality': 'str',
        'country': 'str',
        'postal_code': 'str',
        'administrative_area': 'str',
        'phone': 'str',
        'url': 'str',
        'country_of_origin': 'str',
        'customer_service_phone_number': 'str'
    }

    attribute_map = {
        'name': 'name',
        'alternate_name': 'alternateName',
        'contact': 'contact',
        'address1': 'address1',
        'locality': 'locality',
        'country': 'country',
        'postal_code': 'postalCode',
        'administrative_area': 'administrativeArea',
        'phone': 'phone',
        'url': 'url',
        'country_of_origin': 'countryOfOrigin',
        'customer_service_phone_number': 'customerServicePhoneNumber'
    }

    def __init__(self, name=None, alternate_name=None, contact=None, address1=None, locality=None, country=None, postal_code=None, administrative_area=None, phone=None, url=None, country_of_origin=None, customer_service_phone_number=None):
        """
        Ptsv2paymentsMerchantInformationMerchantDescriptor - a model defined in Swagger
        """

        self._name = None
        self._alternate_name = None
        self._contact = None
        self._address1 = None
        self._locality = None
        self._country = None
        self._postal_code = None
        self._administrative_area = None
        self._phone = None
        self._url = None
        self._country_of_origin = None
        self._customer_service_phone_number = None

        if name is not None:
          self.name = name
        if alternate_name is not None:
          self.alternate_name = alternate_name
        if contact is not None:
          self.contact = contact
        if address1 is not None:
          self.address1 = address1
        if locality is not None:
          self.locality = locality
        if country is not None:
          self.country = country
        if postal_code is not None:
          self.postal_code = postal_code
        if administrative_area is not None:
          self.administrative_area = administrative_area
        if phone is not None:
          self.phone = phone
        if url is not None:
          self.url = url
        if country_of_origin is not None:
          self.country_of_origin = country_of_origin
        if customer_service_phone_number is not None:
          self.customer_service_phone_number = customer_service_phone_number

    @property
    def name(self):
        """
        Gets the name of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        Your merchant name.  **Note** For Paymentech processor using Cybersource Payouts, the maximum data length is 22.  #### PIN debit Your business name. This name is displayed on the cardholder's statement. When you include more than one consecutive space, extra spaces are removed.  When you do not include this value in your PIN debit request, the merchant name from your account is used. **Important** This value must consist of English characters.  Optional field for PIN debit credit or PIN debit purchase requests.  #### Airline processing Your merchant name. This name is displayed on the cardholder's statement. When you include more than one consecutive space, extra spaces are removed.  **Note** Some airline fee programs may require the original ticket number (ticket identifier) or the ancillary service description in positions 13 through 23 of this field.  **Important** This value must consist of English characters.  Required for captures and credits. 

        :return: The name of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        Your merchant name.  **Note** For Paymentech processor using Cybersource Payouts, the maximum data length is 22.  #### PIN debit Your business name. This name is displayed on the cardholder's statement. When you include more than one consecutive space, extra spaces are removed.  When you do not include this value in your PIN debit request, the merchant name from your account is used. **Important** This value must consist of English characters.  Optional field for PIN debit credit or PIN debit purchase requests.  #### Airline processing Your merchant name. This name is displayed on the cardholder's statement. When you include more than one consecutive space, extra spaces are removed.  **Note** Some airline fee programs may require the original ticket number (ticket identifier) or the ancillary service description in positions 13 through 23 of this field.  **Important** This value must consist of English characters.  Required for captures and credits. 

        :param name: The name of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :type: str
        """

        self._name = name

    @property
    def alternate_name(self):
        """
        Gets the alternate_name of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        An alternate name for the merchant.  For the descriptions, used-by information, data types, and lengths for these fields, see the `merchant_descriptor_alternate` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)--> 

        :return: The alternate_name of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._alternate_name

    @alternate_name.setter
    def alternate_name(self, alternate_name):
        """
        Sets the alternate_name of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        An alternate name for the merchant.  For the descriptions, used-by information, data types, and lengths for these fields, see the `merchant_descriptor_alternate` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)--> 

        :param alternate_name: The alternate_name of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :type: str
        """

        self._alternate_name = alternate_name

    @property
    def contact(self):
        """
        Gets the contact of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        For the descriptions, used-by information, data types, and lengths for these fields, see `merchant_descriptor_contact` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)--> Contact information for the merchant.  **Note** These are the maximum data lengths for the following payment processors: - FDCCompass (13) - Paymentech (13) 

        :return: The contact of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """
        Sets the contact of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        For the descriptions, used-by information, data types, and lengths for these fields, see `merchant_descriptor_contact` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)--> Contact information for the merchant.  **Note** These are the maximum data lengths for the following payment processors: - FDCCompass (13) - Paymentech (13) 

        :param contact: The contact of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :type: str
        """

        self._contact = contact

    @property
    def address1(self):
        """
        Gets the address1 of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        First line of merchant's address. For the descriptions, used-by information, data types, and lengths for these fields, see `merchant_descriptor_street` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The address1 of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        First line of merchant's address. For the descriptions, used-by information, data types, and lengths for these fields, see `merchant_descriptor_street` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param address1: The address1 of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :type: str
        """

        self._address1 = address1

    @property
    def locality(self):
        """
        Gets the locality of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        Merchant's City.  #### PIN debit City for your business location. This value might be displayed on the cardholder's statement.  When you do not include this value in your PIN debit request, the merchant name from your account is used. **Important** This value must consist of English characters.  Optional field for PIN debit credit or PIN debit purchase requests. 

        :return: The locality of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        Merchant's City.  #### PIN debit City for your business location. This value might be displayed on the cardholder's statement.  When you do not include this value in your PIN debit request, the merchant name from your account is used. **Important** This value must consist of English characters.  Optional field for PIN debit credit or PIN debit purchase requests. 

        :param locality: The locality of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :type: str
        """

        self._locality = locality

    @property
    def country(self):
        """
        Gets the country of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        Merchant's country.  #### PIN debit Country code for your business location. Use the [ISO Standard Country Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf) This value might be displayed on the cardholder's statement.  When you do not include this value in your PIN debit request, the merchant name from your account is used. **Important** This value must consist of English characters. **Note** If your business is located in the U.S. or Canada and you include this field in a request, you must also include `merchantInformation.merchantDescriptor.administrativeArea`.  Optional field for PIN debit credit or PIN debit purchase. 

        :return: The country of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        Merchant's country.  #### PIN debit Country code for your business location. Use the [ISO Standard Country Codes](https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf) This value might be displayed on the cardholder's statement.  When you do not include this value in your PIN debit request, the merchant name from your account is used. **Important** This value must consist of English characters. **Note** If your business is located in the U.S. or Canada and you include this field in a request, you must also include `merchantInformation.merchantDescriptor.administrativeArea`.  Optional field for PIN debit credit or PIN debit purchase. 

        :param country: The country of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :type: str
        """

        self._country = country

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        Merchant's postal code.  #### PIN debit Postal code for your business location. This value might be displayed on the cardholder's statement.  If your business is domiciled in the U.S., you can use a 5-digit or 9-digit postal code. A 9-digit postal code must follow this format: [5 digits][dash][4 digits] Example: `12345-6789`  If your business is domiciled in Canada, you can use a 6-digit or 9-digit postal code. A 6-digit postal code must follow this format: [alpha][numeric][alpha][space] [numeric][alpha][numeric] Example: `A1B 2C3`  When you do not include this value in your PIN debit request, the merchant name from your account is used. **Important** This value must consist of English characters.  **Note** This field is supported only for businesses located in the U.S. or Canada. **Important** Mastercard requires a postal code for any country that uses postal codes. You can provide the postal code in your account or you can include this field in your request.  Optional field for PIN debit credit or PIN debit purchase. 

        :return: The postal_code of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        Merchant's postal code.  #### PIN debit Postal code for your business location. This value might be displayed on the cardholder's statement.  If your business is domiciled in the U.S., you can use a 5-digit or 9-digit postal code. A 9-digit postal code must follow this format: [5 digits][dash][4 digits] Example: `12345-6789`  If your business is domiciled in Canada, you can use a 6-digit or 9-digit postal code. A 6-digit postal code must follow this format: [alpha][numeric][alpha][space] [numeric][alpha][numeric] Example: `A1B 2C3`  When you do not include this value in your PIN debit request, the merchant name from your account is used. **Important** This value must consist of English characters.  **Note** This field is supported only for businesses located in the U.S. or Canada. **Important** Mastercard requires a postal code for any country that uses postal codes. You can provide the postal code in your account or you can include this field in your request.  Optional field for PIN debit credit or PIN debit purchase. 

        :param postal_code: The postal_code of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        The state where the merchant is located.  #### PIN debit State code or region code for your business. Use the Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf) This value might be displayed on the cardholder's statement.  When you do not include this value in your PIN debit request, the merchant name from your account is used. **Important** This value must consist of English characters.  **Note** This field is supported only for businesses located in the U.S. or Canada.  Optional field for PIN debit credit or PIN debit purchase. 

        :return: The administrative_area of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        The state where the merchant is located.  #### PIN debit State code or region code for your business. Use the Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf) This value might be displayed on the cardholder's statement.  When you do not include this value in your PIN debit request, the merchant name from your account is used. **Important** This value must consist of English characters.  **Note** This field is supported only for businesses located in the U.S. or Canada.  Optional field for PIN debit credit or PIN debit purchase. 

        :param administrative_area: The administrative_area of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :type: str
        """

        self._administrative_area = administrative_area

    @property
    def phone(self):
        """
        Gets the phone of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        Merchant phone as contact information for CNP transactions 

        :return: The phone of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        Merchant phone as contact information for CNP transactions 

        :param phone: The phone of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :type: str
        """

        self._phone = phone

    @property
    def url(self):
        """
        Gets the url of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        Address of company's website provided by merchant 

        :return: The url of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        Address of company's website provided by merchant 

        :param url: The url of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :type: str
        """

        self._url = url

    @property
    def country_of_origin(self):
        """
        Gets the country_of_origin of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        #### Visa Platform Connect This field will indicate merchant country of origin 

        :return: The country_of_origin of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._country_of_origin

    @country_of_origin.setter
    def country_of_origin(self, country_of_origin):
        """
        Sets the country_of_origin of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        #### Visa Platform Connect This field will indicate merchant country of origin 

        :param country_of_origin: The country_of_origin of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :type: str
        """

        self._country_of_origin = country_of_origin

    @property
    def customer_service_phone_number(self):
        """
        Gets the customer_service_phone_number of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        #### Visa Platform Connect Indicates customer service phone number of Merchant. 

        :return: The customer_service_phone_number of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :rtype: str
        """
        return self._customer_service_phone_number

    @customer_service_phone_number.setter
    def customer_service_phone_number(self, customer_service_phone_number):
        """
        Sets the customer_service_phone_number of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        #### Visa Platform Connect Indicates customer service phone number of Merchant. 

        :param customer_service_phone_number: The customer_service_phone_number of this Ptsv2paymentsMerchantInformationMerchantDescriptor.
        :type: str
        """

        self._customer_service_phone_number = customer_service_phone_number

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
        if not isinstance(other, Ptsv2paymentsMerchantInformationMerchantDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
