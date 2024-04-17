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


class Ptsv2paymentsOrderInformationAmountDetailsOrder(object):
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
        'total_amount': 'str',
        'currency': 'str',
        'sub_total_amount': 'str',
        'handling_amount': 'str',
        'shipping_amount': 'str',
        'shipping_discount_amount': 'str',
        'tax_amount': 'str',
        'insurance_amount': 'str',
        'gift_wrap_amount': 'str'
    }

    attribute_map = {
        'total_amount': 'totalAmount',
        'currency': 'currency',
        'sub_total_amount': 'subTotalAmount',
        'handling_amount': 'handlingAmount',
        'shipping_amount': 'shippingAmount',
        'shipping_discount_amount': 'shippingDiscountAmount',
        'tax_amount': 'taxAmount',
        'insurance_amount': 'insuranceAmount',
        'gift_wrap_amount': 'giftWrapAmount'
    }

    def __init__(self, total_amount=None, currency=None, sub_total_amount=None, handling_amount=None, shipping_amount=None, shipping_discount_amount=None, tax_amount=None, insurance_amount=None, gift_wrap_amount=None):
        """
        Ptsv2paymentsOrderInformationAmountDetailsOrder - a model defined in Swagger
        """

        self._total_amount = None
        self._currency = None
        self._sub_total_amount = None
        self._handling_amount = None
        self._shipping_amount = None
        self._shipping_discount_amount = None
        self._tax_amount = None
        self._insurance_amount = None
        self._gift_wrap_amount = None

        if total_amount is not None:
          self.total_amount = total_amount
        if currency is not None:
          self.currency = currency
        if sub_total_amount is not None:
          self.sub_total_amount = sub_total_amount
        if handling_amount is not None:
          self.handling_amount = handling_amount
        if shipping_amount is not None:
          self.shipping_amount = shipping_amount
        if shipping_discount_amount is not None:
          self.shipping_discount_amount = shipping_discount_amount
        if tax_amount is not None:
          self.tax_amount = tax_amount
        if insurance_amount is not None:
          self.insurance_amount = insurance_amount
        if gift_wrap_amount is not None:
          self.gift_wrap_amount = gift_wrap_amount

    @property
    def total_amount(self):
        """
        Gets the total_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Grand total for the order. This value cannot be negative. You can include a decimal point (.), but you cannot include any other special characters. CyberSource truncates the amount to the correct number of decimal places 

        :return: The total_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :rtype: str
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """
        Sets the total_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Grand total for the order. This value cannot be negative. You can include a decimal point (.), but you cannot include any other special characters. CyberSource truncates the amount to the correct number of decimal places 

        :param total_amount: The total_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :type: str
        """

        self._total_amount = total_amount

    @property
    def currency(self):
        """
        Gets the currency of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Currency used for the order 

        :return: The currency of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Currency used for the order 

        :param currency: The currency of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :type: str
        """

        self._currency = currency

    @property
    def sub_total_amount(self):
        """
        Gets the sub_total_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Shipping discount amount for the transaction. If this amount has changed since the initial sessions request, you must include the new value in the order request. You must also include all additional amount fields that apply to the order and ensure the total amount equals the purchaseTotals_grandTotalAmount value. 

        :return: The sub_total_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :rtype: str
        """
        return self._sub_total_amount

    @sub_total_amount.setter
    def sub_total_amount(self, sub_total_amount):
        """
        Sets the sub_total_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Shipping discount amount for the transaction. If this amount has changed since the initial sessions request, you must include the new value in the order request. You must also include all additional amount fields that apply to the order and ensure the total amount equals the purchaseTotals_grandTotalAmount value. 

        :param sub_total_amount: The sub_total_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :type: str
        """

        self._sub_total_amount = sub_total_amount

    @property
    def handling_amount(self):
        """
        Gets the handling_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Aggregate handling charges for the transaction. If this amount has changed since the initial sessions request, you must include the new value in the order request. You must also include all additional amount fields that apply to the order and ensure the total amount equals the purchaseTotals_grandTotalAmount value. 

        :return: The handling_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :rtype: str
        """
        return self._handling_amount

    @handling_amount.setter
    def handling_amount(self, handling_amount):
        """
        Sets the handling_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Aggregate handling charges for the transaction. If this amount has changed since the initial sessions request, you must include the new value in the order request. You must also include all additional amount fields that apply to the order and ensure the total amount equals the purchaseTotals_grandTotalAmount value. 

        :param handling_amount: The handling_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :type: str
        """

        self._handling_amount = handling_amount

    @property
    def shipping_amount(self):
        """
        Gets the shipping_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Aggregate shipping charges for the transaction If this amount has changed since the initial sessions request, you must include the new value in the order request. You must also include all additional amount fields that apply to the order and ensure the total amount equals the purchaseTotals_grandTotalAmount value. 

        :return: The shipping_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :rtype: str
        """
        return self._shipping_amount

    @shipping_amount.setter
    def shipping_amount(self, shipping_amount):
        """
        Sets the shipping_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Aggregate shipping charges for the transaction If this amount has changed since the initial sessions request, you must include the new value in the order request. You must also include all additional amount fields that apply to the order and ensure the total amount equals the purchaseTotals_grandTotalAmount value. 

        :param shipping_amount: The shipping_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :type: str
        """

        self._shipping_amount = shipping_amount

    @property
    def shipping_discount_amount(self):
        """
        Gets the shipping_discount_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Shipping discount amount for the transaction. If this amount has changed since the initial sessions request, you must include the new value in the order request. You must also include all additional amount fields that apply to the order and ensure the total amount equals the purchaseTotals_grandTotalAmount value. 

        :return: The shipping_discount_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :rtype: str
        """
        return self._shipping_discount_amount

    @shipping_discount_amount.setter
    def shipping_discount_amount(self, shipping_discount_amount):
        """
        Sets the shipping_discount_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Shipping discount amount for the transaction. If this amount has changed since the initial sessions request, you must include the new value in the order request. You must also include all additional amount fields that apply to the order and ensure the total amount equals the purchaseTotals_grandTotalAmount value. 

        :param shipping_discount_amount: The shipping_discount_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :type: str
        """

        self._shipping_discount_amount = shipping_discount_amount

    @property
    def tax_amount(self):
        """
        Gets the tax_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Total tax amount. When the purchaseTotals_ taxAmount and ap_subtotalAmount fields are included in the request, do not include the tax amount as part of the subtotal amount calculation.  

        :return: The tax_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :rtype: str
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """
        Sets the tax_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Total tax amount. When the purchaseTotals_ taxAmount and ap_subtotalAmount fields are included in the request, do not include the tax amount as part of the subtotal amount calculation.  

        :param tax_amount: The tax_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :type: str
        """

        self._tax_amount = tax_amount

    @property
    def insurance_amount(self):
        """
        Gets the insurance_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Amount being charged for the insurance fee. Only supported when the payment_method is set to paypal. 

        :return: The insurance_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :rtype: str
        """
        return self._insurance_amount

    @insurance_amount.setter
    def insurance_amount(self, insurance_amount):
        """
        Sets the insurance_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Amount being charged for the insurance fee. Only supported when the payment_method is set to paypal. 

        :param insurance_amount: The insurance_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :type: str
        """

        self._insurance_amount = insurance_amount

    @property
    def gift_wrap_amount(self):
        """
        Gets the gift_wrap_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Amount being charged as gift wrap fee.            

        :return: The gift_wrap_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :rtype: str
        """
        return self._gift_wrap_amount

    @gift_wrap_amount.setter
    def gift_wrap_amount(self, gift_wrap_amount):
        """
        Sets the gift_wrap_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        Amount being charged as gift wrap fee.            

        :param gift_wrap_amount: The gift_wrap_amount of this Ptsv2paymentsOrderInformationAmountDetailsOrder.
        :type: str
        """

        self._gift_wrap_amount = gift_wrap_amount

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
        if not isinstance(other, Ptsv2paymentsOrderInformationAmountDetailsOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
