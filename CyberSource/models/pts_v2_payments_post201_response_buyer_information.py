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


class PtsV2PaymentsPost201ResponseBuyerInformation(object):
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
        'merchant_customer_id': 'str',
        'date_of_birth': 'str',
        'vat_registration_number': 'str',
        'personal_identification': 'list[Ptsv2paymentsBuyerInformationPersonalIdentification]',
        'tax_id': 'str',
        'login_id': 'str'
    }

    attribute_map = {
        'merchant_customer_id': 'merchantCustomerId',
        'date_of_birth': 'dateOfBirth',
        'vat_registration_number': 'vatRegistrationNumber',
        'personal_identification': 'personalIdentification',
        'tax_id': 'taxId',
        'login_id': 'loginId'
    }

    def __init__(self, merchant_customer_id=None, date_of_birth=None, vat_registration_number=None, personal_identification=None, tax_id=None, login_id=None):
        """
        PtsV2PaymentsPost201ResponseBuyerInformation - a model defined in Swagger
        """

        self._merchant_customer_id = None
        self._date_of_birth = None
        self._vat_registration_number = None
        self._personal_identification = None
        self._tax_id = None
        self._login_id = None

        if merchant_customer_id is not None:
          self.merchant_customer_id = merchant_customer_id
        if date_of_birth is not None:
          self.date_of_birth = date_of_birth
        if vat_registration_number is not None:
          self.vat_registration_number = vat_registration_number
        if personal_identification is not None:
          self.personal_identification = personal_identification
        if tax_id is not None:
          self.tax_id = tax_id
        if login_id is not None:
          self.login_id = login_id

    @property
    def merchant_customer_id(self):
        """
        Gets the merchant_customer_id of this PtsV2PaymentsPost201ResponseBuyerInformation.
        Your identifier for the customer.  When a subscription or customer profile is being created, the maximum length for this field for most processors is 30. Otherwise, the maximum length is 100.  #### Comercio Latino For recurring payments in Mexico, the value is the customer's contract number. Note Before you request the authorization, you must inform the issuer of the customer contract numbers that will be used for recurring transactions.  #### Worldpay VAP For a follow-on credit with Worldpay VAP, CyberSource checks the following locations, in the order given, for a customer account ID value and uses the first value it finds: 1. `customer_account_id` value in the follow-on credit request 2. Customer account ID value that was used for the capture that is being credited 3. Customer account ID value that was used for the original authorization If a customer account ID value cannot be found in any of these locations, then no value is used.  For processor-specific information, see the `customer_account_id` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :return: The merchant_customer_id of this PtsV2PaymentsPost201ResponseBuyerInformation.
        :rtype: str
        """
        return self._merchant_customer_id

    @merchant_customer_id.setter
    def merchant_customer_id(self, merchant_customer_id):
        """
        Sets the merchant_customer_id of this PtsV2PaymentsPost201ResponseBuyerInformation.
        Your identifier for the customer.  When a subscription or customer profile is being created, the maximum length for this field for most processors is 30. Otherwise, the maximum length is 100.  #### Comercio Latino For recurring payments in Mexico, the value is the customer's contract number. Note Before you request the authorization, you must inform the issuer of the customer contract numbers that will be used for recurring transactions.  #### Worldpay VAP For a follow-on credit with Worldpay VAP, CyberSource checks the following locations, in the order given, for a customer account ID value and uses the first value it finds: 1. `customer_account_id` value in the follow-on credit request 2. Customer account ID value that was used for the capture that is being credited 3. Customer account ID value that was used for the original authorization If a customer account ID value cannot be found in any of these locations, then no value is used.  For processor-specific information, see the `customer_account_id` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html) 

        :param merchant_customer_id: The merchant_customer_id of this PtsV2PaymentsPost201ResponseBuyerInformation.
        :type: str
        """

        self._merchant_customer_id = merchant_customer_id

    @property
    def date_of_birth(self):
        """
        Gets the date_of_birth of this PtsV2PaymentsPost201ResponseBuyerInformation.
        Recipient's date of birth. **Format**: `YYYYMMDD`.  This field is a `pass-through`, which means that CyberSource ensures that the value is eight numeric characters but otherwise does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  For more details, see `recipient_date_of_birth` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The date_of_birth of this PtsV2PaymentsPost201ResponseBuyerInformation.
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """
        Sets the date_of_birth of this PtsV2PaymentsPost201ResponseBuyerInformation.
        Recipient's date of birth. **Format**: `YYYYMMDD`.  This field is a `pass-through`, which means that CyberSource ensures that the value is eight numeric characters but otherwise does not verify the value or modify it in any way before sending it to the processor. If the field is not required for the transaction, CyberSource does not forward it to the processor.  For more details, see `recipient_date_of_birth` field description in the [Credit Card Services Using the SCMP API Guide.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param date_of_birth: The date_of_birth of this PtsV2PaymentsPost201ResponseBuyerInformation.
        :type: str
        """

        self._date_of_birth = date_of_birth

    @property
    def vat_registration_number(self):
        """
        Gets the vat_registration_number of this PtsV2PaymentsPost201ResponseBuyerInformation.
        Customer's government-assigned tax identification number.  #### Tax Calculation Optional for international and value added taxes only. Not applicable to U.S. and Canadian taxes.  For processor-specific information, see the purchaser_vat_registration_number field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :return: The vat_registration_number of this PtsV2PaymentsPost201ResponseBuyerInformation.
        :rtype: str
        """
        return self._vat_registration_number

    @vat_registration_number.setter
    def vat_registration_number(self, vat_registration_number):
        """
        Sets the vat_registration_number of this PtsV2PaymentsPost201ResponseBuyerInformation.
        Customer's government-assigned tax identification number.  #### Tax Calculation Optional for international and value added taxes only. Not applicable to U.S. and Canadian taxes.  For processor-specific information, see the purchaser_vat_registration_number field in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :param vat_registration_number: The vat_registration_number of this PtsV2PaymentsPost201ResponseBuyerInformation.
        :type: str
        """

        self._vat_registration_number = vat_registration_number

    @property
    def personal_identification(self):
        """
        Gets the personal_identification of this PtsV2PaymentsPost201ResponseBuyerInformation.

        :return: The personal_identification of this PtsV2PaymentsPost201ResponseBuyerInformation.
        :rtype: list[Ptsv2paymentsBuyerInformationPersonalIdentification]
        """
        return self._personal_identification

    @personal_identification.setter
    def personal_identification(self, personal_identification):
        """
        Sets the personal_identification of this PtsV2PaymentsPost201ResponseBuyerInformation.

        :param personal_identification: The personal_identification of this PtsV2PaymentsPost201ResponseBuyerInformation.
        :type: list[Ptsv2paymentsBuyerInformationPersonalIdentification]
        """

        self._personal_identification = personal_identification

    @property
    def tax_id(self):
        """
        Gets the tax_id of this PtsV2PaymentsPost201ResponseBuyerInformation.
        The description for this field is not available.

        :return: The tax_id of this PtsV2PaymentsPost201ResponseBuyerInformation.
        :rtype: str
        """
        return self._tax_id

    @tax_id.setter
    def tax_id(self, tax_id):
        """
        Sets the tax_id of this PtsV2PaymentsPost201ResponseBuyerInformation.
        The description for this field is not available.

        :param tax_id: The tax_id of this PtsV2PaymentsPost201ResponseBuyerInformation.
        :type: str
        """

        self._tax_id = tax_id

    @property
    def login_id(self):
        """
        Gets the login_id of this PtsV2PaymentsPost201ResponseBuyerInformation.
        The buyer's Alipay login Id, the id might be an email or mobile number. The id is partially masked for privacy. cao***@126.com  or 186***22156 

        :return: The login_id of this PtsV2PaymentsPost201ResponseBuyerInformation.
        :rtype: str
        """
        return self._login_id

    @login_id.setter
    def login_id(self, login_id):
        """
        Sets the login_id of this PtsV2PaymentsPost201ResponseBuyerInformation.
        The buyer's Alipay login Id, the id might be an email or mobile number. The id is partially masked for privacy. cao***@126.com  or 186***22156 

        :param login_id: The login_id of this PtsV2PaymentsPost201ResponseBuyerInformation.
        :type: str
        """

        self._login_id = login_id

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseBuyerInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
