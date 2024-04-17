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


class Ptsv2paymentsidrefundsMerchantInformation(object):
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
        'merchant_descriptor': 'Ptsv2paymentsMerchantInformationMerchantDescriptor',
        'category_code': 'int',
        'vat_registration_number': 'str',
        'card_acceptor_reference_number': 'str',
        'tax_id': 'str'
    }

    attribute_map = {
        'merchant_descriptor': 'merchantDescriptor',
        'category_code': 'categoryCode',
        'vat_registration_number': 'vatRegistrationNumber',
        'card_acceptor_reference_number': 'cardAcceptorReferenceNumber',
        'tax_id': 'taxId'
    }

    def __init__(self, merchant_descriptor=None, category_code=None, vat_registration_number=None, card_acceptor_reference_number=None, tax_id=None):
        """
        Ptsv2paymentsidrefundsMerchantInformation - a model defined in Swagger
        """

        self._merchant_descriptor = None
        self._category_code = None
        self._vat_registration_number = None
        self._card_acceptor_reference_number = None
        self._tax_id = None

        if merchant_descriptor is not None:
          self.merchant_descriptor = merchant_descriptor
        if category_code is not None:
          self.category_code = category_code
        if vat_registration_number is not None:
          self.vat_registration_number = vat_registration_number
        if card_acceptor_reference_number is not None:
          self.card_acceptor_reference_number = card_acceptor_reference_number
        if tax_id is not None:
          self.tax_id = tax_id

    @property
    def merchant_descriptor(self):
        """
        Gets the merchant_descriptor of this Ptsv2paymentsidrefundsMerchantInformation.

        :return: The merchant_descriptor of this Ptsv2paymentsidrefundsMerchantInformation.
        :rtype: Ptsv2paymentsMerchantInformationMerchantDescriptor
        """
        return self._merchant_descriptor

    @merchant_descriptor.setter
    def merchant_descriptor(self, merchant_descriptor):
        """
        Sets the merchant_descriptor of this Ptsv2paymentsidrefundsMerchantInformation.

        :param merchant_descriptor: The merchant_descriptor of this Ptsv2paymentsidrefundsMerchantInformation.
        :type: Ptsv2paymentsMerchantInformationMerchantDescriptor
        """

        self._merchant_descriptor = merchant_descriptor

    @property
    def category_code(self):
        """
        Gets the category_code of this Ptsv2paymentsidrefundsMerchantInformation.
        The value for this field is a four-digit number that the payment card industry uses to classify merchants into market segments. A payment card company assigned one or more of these values to your business when you started accepting the payment card company's cards. When you do not include this field in your request, CyberSource uses the value in your CyberSource account.  For processor-specific information, see the `merchant_category_code` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  #### CyberSource through VisaNet The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP01 TCR4 - Position: 150-153 - Field: Merchant Category Code 

        :return: The category_code of this Ptsv2paymentsidrefundsMerchantInformation.
        :rtype: int
        """
        return self._category_code

    @category_code.setter
    def category_code(self, category_code):
        """
        Sets the category_code of this Ptsv2paymentsidrefundsMerchantInformation.
        The value for this field is a four-digit number that the payment card industry uses to classify merchants into market segments. A payment card company assigned one or more of these values to your business when you started accepting the payment card company's cards. When you do not include this field in your request, CyberSource uses the value in your CyberSource account.  For processor-specific information, see the `merchant_category_code` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  #### CyberSource through VisaNet The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP01 TCR4 - Position: 150-153 - Field: Merchant Category Code 

        :param category_code: The category_code of this Ptsv2paymentsidrefundsMerchantInformation.
        :type: int
        """

        self._category_code = category_code

    @property
    def vat_registration_number(self):
        """
        Gets the vat_registration_number of this Ptsv2paymentsidrefundsMerchantInformation.
        Your government-assigned tax identification number.  #### Tax Calculation Required field for value added tax only. Not applicable to U.S. and Canadian taxes.  #### CyberSource through VisaNet For CtV processors, the maximum length is 20.  For other processor-specific information, see the `merchant_vat_registration_number` field description in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :return: The vat_registration_number of this Ptsv2paymentsidrefundsMerchantInformation.
        :rtype: str
        """
        return self._vat_registration_number

    @vat_registration_number.setter
    def vat_registration_number(self, vat_registration_number):
        """
        Sets the vat_registration_number of this Ptsv2paymentsidrefundsMerchantInformation.
        Your government-assigned tax identification number.  #### Tax Calculation Required field for value added tax only. Not applicable to U.S. and Canadian taxes.  #### CyberSource through VisaNet For CtV processors, the maximum length is 20.  For other processor-specific information, see the `merchant_vat_registration_number` field description in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :param vat_registration_number: The vat_registration_number of this Ptsv2paymentsidrefundsMerchantInformation.
        :type: str
        """

        self._vat_registration_number = vat_registration_number

    @property
    def card_acceptor_reference_number(self):
        """
        Gets the card_acceptor_reference_number of this Ptsv2paymentsidrefundsMerchantInformation.
        Reference number that facilitates card acceptor/corporation communication and record keeping.  For processor-specific information, see the `card_acceptor_ref_number` field description in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :return: The card_acceptor_reference_number of this Ptsv2paymentsidrefundsMerchantInformation.
        :rtype: str
        """
        return self._card_acceptor_reference_number

    @card_acceptor_reference_number.setter
    def card_acceptor_reference_number(self, card_acceptor_reference_number):
        """
        Sets the card_acceptor_reference_number of this Ptsv2paymentsidrefundsMerchantInformation.
        Reference number that facilitates card acceptor/corporation communication and record keeping.  For processor-specific information, see the `card_acceptor_ref_number` field description in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :param card_acceptor_reference_number: The card_acceptor_reference_number of this Ptsv2paymentsidrefundsMerchantInformation.
        :type: str
        """

        self._card_acceptor_reference_number = card_acceptor_reference_number

    @property
    def tax_id(self):
        """
        Gets the tax_id of this Ptsv2paymentsidrefundsMerchantInformation.
        Your Cadastro Nacional da Pessoa Jurídica (CNPJ) number.  This field is supported only for BNDES transactions on CyberSource through VisaNet.  The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP07 TCR6 - Position: 40-59 - Field: BNDES Reference Field 1  For details, see `bill_merchant_tax_id` field description in the [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The tax_id of this Ptsv2paymentsidrefundsMerchantInformation.
        :rtype: str
        """
        return self._tax_id

    @tax_id.setter
    def tax_id(self, tax_id):
        """
        Sets the tax_id of this Ptsv2paymentsidrefundsMerchantInformation.
        Your Cadastro Nacional da Pessoa Jurídica (CNPJ) number.  This field is supported only for BNDES transactions on CyberSource through VisaNet.  The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP07 TCR6 - Position: 40-59 - Field: BNDES Reference Field 1  For details, see `bill_merchant_tax_id` field description in the [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param tax_id: The tax_id of this Ptsv2paymentsidrefundsMerchantInformation.
        :type: str
        """

        self._tax_id = tax_id

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
        if not isinstance(other, Ptsv2paymentsidrefundsMerchantInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
