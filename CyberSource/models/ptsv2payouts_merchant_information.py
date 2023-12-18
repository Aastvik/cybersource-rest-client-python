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


class Ptsv2payoutsMerchantInformation(object):
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
        'category_code': 'int',
        'submit_local_date_time': 'str',
        'vat_registration_number': 'str',
        'merchant_descriptor': 'Ptsv2payoutsMerchantInformationMerchantDescriptor'
    }

    attribute_map = {
        'category_code': 'categoryCode',
        'submit_local_date_time': 'submitLocalDateTime',
        'vat_registration_number': 'vatRegistrationNumber',
        'merchant_descriptor': 'merchantDescriptor'
    }

    def __init__(self, category_code=None, submit_local_date_time=None, vat_registration_number=None, merchant_descriptor=None):
        """
        Ptsv2payoutsMerchantInformation - a model defined in Swagger
        """

        self._category_code = None
        self._submit_local_date_time = None
        self._vat_registration_number = None
        self._merchant_descriptor = None

        if category_code is not None:
          self.category_code = category_code
        if submit_local_date_time is not None:
          self.submit_local_date_time = submit_local_date_time
        if vat_registration_number is not None:
          self.vat_registration_number = vat_registration_number
        if merchant_descriptor is not None:
          self.merchant_descriptor = merchant_descriptor

    @property
    def category_code(self):
        """
        Gets the category_code of this Ptsv2payoutsMerchantInformation.
        The value for this field is a four-digit number that the payment card industry uses to classify merchants into market segments. A payment card company assigned one or more of these values to your business when you started accepting the payment card company's cards. When you do not include this field in your request, CyberSource uses the value in your CyberSource account.  For processor-specific information, see the `merchant_category_code` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  #### CyberSource through VisaNet The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP01 TCR4 - Position: 150-153 - Field: Merchant Category Code 

        :return: The category_code of this Ptsv2payoutsMerchantInformation.
        :rtype: int
        """
        return self._category_code

    @category_code.setter
    def category_code(self, category_code):
        """
        Sets the category_code of this Ptsv2payoutsMerchantInformation.
        The value for this field is a four-digit number that the payment card industry uses to classify merchants into market segments. A payment card company assigned one or more of these values to your business when you started accepting the payment card company's cards. When you do not include this field in your request, CyberSource uses the value in your CyberSource account.  For processor-specific information, see the `merchant_category_code` field description in [Credit Card Services Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html)  #### CyberSource through VisaNet The value for this field corresponds to the following data in the TC 33 capture file5: - Record: CP01 TCR4 - Position: 150-153 - Field: Merchant Category Code 

        :param category_code: The category_code of this Ptsv2payoutsMerchantInformation.
        :type: int
        """

        self._category_code = category_code

    @property
    def submit_local_date_time(self):
        """
        Gets the submit_local_date_time of this Ptsv2payoutsMerchantInformation.
        Time that the transaction was submitted in local time. The time is in hhmmss format. 

        :return: The submit_local_date_time of this Ptsv2payoutsMerchantInformation.
        :rtype: str
        """
        return self._submit_local_date_time

    @submit_local_date_time.setter
    def submit_local_date_time(self, submit_local_date_time):
        """
        Sets the submit_local_date_time of this Ptsv2payoutsMerchantInformation.
        Time that the transaction was submitted in local time. The time is in hhmmss format. 

        :param submit_local_date_time: The submit_local_date_time of this Ptsv2payoutsMerchantInformation.
        :type: str
        """

        self._submit_local_date_time = submit_local_date_time

    @property
    def vat_registration_number(self):
        """
        Gets the vat_registration_number of this Ptsv2payoutsMerchantInformation.
        Your government-assigned tax identification number.  #### Tax Calculation Required field for value added tax only. Not applicable to U.S. and Canadian taxes.  #### CyberSource through VisaNet For CtV processors, the maximum length is 20.  For other processor-specific information, see the `merchant_vat_registration_number` field description in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :return: The vat_registration_number of this Ptsv2payoutsMerchantInformation.
        :rtype: str
        """
        return self._vat_registration_number

    @vat_registration_number.setter
    def vat_registration_number(self, vat_registration_number):
        """
        Sets the vat_registration_number of this Ptsv2payoutsMerchantInformation.
        Your government-assigned tax identification number.  #### Tax Calculation Required field for value added tax only. Not applicable to U.S. and Canadian taxes.  #### CyberSource through VisaNet For CtV processors, the maximum length is 20.  For other processor-specific information, see the `merchant_vat_registration_number` field description in [Level II and Level III Processing Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/Level_2_3_SCMP_API/html) 

        :param vat_registration_number: The vat_registration_number of this Ptsv2payoutsMerchantInformation.
        :type: str
        """

        self._vat_registration_number = vat_registration_number

    @property
    def merchant_descriptor(self):
        """
        Gets the merchant_descriptor of this Ptsv2payoutsMerchantInformation.

        :return: The merchant_descriptor of this Ptsv2payoutsMerchantInformation.
        :rtype: Ptsv2payoutsMerchantInformationMerchantDescriptor
        """
        return self._merchant_descriptor

    @merchant_descriptor.setter
    def merchant_descriptor(self, merchant_descriptor):
        """
        Sets the merchant_descriptor of this Ptsv2payoutsMerchantInformation.

        :param merchant_descriptor: The merchant_descriptor of this Ptsv2payoutsMerchantInformation.
        :type: Ptsv2payoutsMerchantInformationMerchantDescriptor
        """

        self._merchant_descriptor = merchant_descriptor

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
        if not isinstance(other, Ptsv2payoutsMerchantInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
