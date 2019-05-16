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


class Ptsv2paymentsidrefundsOrderInformation(object):
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
        'amount_details': 'Ptsv2paymentsidcapturesOrderInformationAmountDetails',
        'bill_to': 'Ptsv2paymentsidcapturesOrderInformationBillTo',
        'ship_to': 'Ptsv2paymentsidcapturesOrderInformationShipTo',
        'line_items': 'list[Ptsv2paymentsidrefundsOrderInformationLineItems]',
        'invoice_details': 'Ptsv2paymentsidcapturesOrderInformationInvoiceDetails',
        'shipping_details': 'Ptsv2paymentsidcapturesOrderInformationShippingDetails'
    }

    attribute_map = {
        'amount_details': 'amountDetails',
        'bill_to': 'billTo',
        'ship_to': 'shipTo',
        'line_items': 'lineItems',
        'invoice_details': 'invoiceDetails',
        'shipping_details': 'shippingDetails'
    }

    def __init__(self, amount_details=None, bill_to=None, ship_to=None, line_items=None, invoice_details=None, shipping_details=None):
        """
        Ptsv2paymentsidrefundsOrderInformation - a model defined in Swagger
        """

        self._amount_details = None
        self._bill_to = None
        self._ship_to = None
        self._line_items = None
        self._invoice_details = None
        self._shipping_details = None

        if amount_details is not None:
          self.amount_details = amount_details
        if bill_to is not None:
          self.bill_to = bill_to
        if ship_to is not None:
          self.ship_to = ship_to
        if line_items is not None:
          self.line_items = line_items
        if invoice_details is not None:
          self.invoice_details = invoice_details
        if shipping_details is not None:
          self.shipping_details = shipping_details

    @property
    def amount_details(self):
        """
        Gets the amount_details of this Ptsv2paymentsidrefundsOrderInformation.

        :return: The amount_details of this Ptsv2paymentsidrefundsOrderInformation.
        :rtype: Ptsv2paymentsidcapturesOrderInformationAmountDetails
        """
        return self._amount_details

    @amount_details.setter
    def amount_details(self, amount_details):
        """
        Sets the amount_details of this Ptsv2paymentsidrefundsOrderInformation.

        :param amount_details: The amount_details of this Ptsv2paymentsidrefundsOrderInformation.
        :type: Ptsv2paymentsidcapturesOrderInformationAmountDetails
        """

        self._amount_details = amount_details

    @property
    def bill_to(self):
        """
        Gets the bill_to of this Ptsv2paymentsidrefundsOrderInformation.

        :return: The bill_to of this Ptsv2paymentsidrefundsOrderInformation.
        :rtype: Ptsv2paymentsidcapturesOrderInformationBillTo
        """
        return self._bill_to

    @bill_to.setter
    def bill_to(self, bill_to):
        """
        Sets the bill_to of this Ptsv2paymentsidrefundsOrderInformation.

        :param bill_to: The bill_to of this Ptsv2paymentsidrefundsOrderInformation.
        :type: Ptsv2paymentsidcapturesOrderInformationBillTo
        """

        self._bill_to = bill_to

    @property
    def ship_to(self):
        """
        Gets the ship_to of this Ptsv2paymentsidrefundsOrderInformation.

        :return: The ship_to of this Ptsv2paymentsidrefundsOrderInformation.
        :rtype: Ptsv2paymentsidcapturesOrderInformationShipTo
        """
        return self._ship_to

    @ship_to.setter
    def ship_to(self, ship_to):
        """
        Sets the ship_to of this Ptsv2paymentsidrefundsOrderInformation.

        :param ship_to: The ship_to of this Ptsv2paymentsidrefundsOrderInformation.
        :type: Ptsv2paymentsidcapturesOrderInformationShipTo
        """

        self._ship_to = ship_to

    @property
    def line_items(self):
        """
        Gets the line_items of this Ptsv2paymentsidrefundsOrderInformation.

        :return: The line_items of this Ptsv2paymentsidrefundsOrderInformation.
        :rtype: list[Ptsv2paymentsidrefundsOrderInformationLineItems]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """
        Sets the line_items of this Ptsv2paymentsidrefundsOrderInformation.

        :param line_items: The line_items of this Ptsv2paymentsidrefundsOrderInformation.
        :type: list[Ptsv2paymentsidrefundsOrderInformationLineItems]
        """

        self._line_items = line_items

    @property
    def invoice_details(self):
        """
        Gets the invoice_details of this Ptsv2paymentsidrefundsOrderInformation.

        :return: The invoice_details of this Ptsv2paymentsidrefundsOrderInformation.
        :rtype: Ptsv2paymentsidcapturesOrderInformationInvoiceDetails
        """
        return self._invoice_details

    @invoice_details.setter
    def invoice_details(self, invoice_details):
        """
        Sets the invoice_details of this Ptsv2paymentsidrefundsOrderInformation.

        :param invoice_details: The invoice_details of this Ptsv2paymentsidrefundsOrderInformation.
        :type: Ptsv2paymentsidcapturesOrderInformationInvoiceDetails
        """

        self._invoice_details = invoice_details

    @property
    def shipping_details(self):
        """
        Gets the shipping_details of this Ptsv2paymentsidrefundsOrderInformation.

        :return: The shipping_details of this Ptsv2paymentsidrefundsOrderInformation.
        :rtype: Ptsv2paymentsidcapturesOrderInformationShippingDetails
        """
        return self._shipping_details

    @shipping_details.setter
    def shipping_details(self, shipping_details):
        """
        Sets the shipping_details of this Ptsv2paymentsidrefundsOrderInformation.

        :param shipping_details: The shipping_details of this Ptsv2paymentsidrefundsOrderInformation.
        :type: Ptsv2paymentsidcapturesOrderInformationShippingDetails
        """

        self._shipping_details = shipping_details

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
        if not isinstance(other, Ptsv2paymentsidrefundsOrderInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
