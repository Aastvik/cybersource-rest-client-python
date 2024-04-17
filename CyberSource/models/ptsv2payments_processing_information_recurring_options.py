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


class Ptsv2paymentsProcessingInformationRecurringOptions(object):
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
        'loan_payment': 'bool',
        'first_recurring_payment': 'bool'
    }

    attribute_map = {
        'loan_payment': 'loanPayment',
        'first_recurring_payment': 'firstRecurringPayment'
    }

    def __init__(self, loan_payment=False, first_recurring_payment=False):
        """
        Ptsv2paymentsProcessingInformationRecurringOptions - a model defined in Swagger
        """

        self._loan_payment = None
        self._first_recurring_payment = None

        if loan_payment is not None:
          self.loan_payment = loan_payment
        if first_recurring_payment is not None:
          self.first_recurring_payment = first_recurring_payment

    @property
    def loan_payment(self):
        """
        Gets the loan_payment of this Ptsv2paymentsProcessingInformationRecurringOptions.
        Flag that indicates whether this is a payment towards an existing contractual loan.  Possible values: - `true`: Loan payment - `false`: (default) Not a loan payment  For processor-specific details, see `debt_indicator` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The loan_payment of this Ptsv2paymentsProcessingInformationRecurringOptions.
        :rtype: bool
        """
        return self._loan_payment

    @loan_payment.setter
    def loan_payment(self, loan_payment):
        """
        Sets the loan_payment of this Ptsv2paymentsProcessingInformationRecurringOptions.
        Flag that indicates whether this is a payment towards an existing contractual loan.  Possible values: - `true`: Loan payment - `false`: (default) Not a loan payment  For processor-specific details, see `debt_indicator` field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param loan_payment: The loan_payment of this Ptsv2paymentsProcessingInformationRecurringOptions.
        :type: bool
        """

        self._loan_payment = loan_payment

    @property
    def first_recurring_payment(self):
        """
        Gets the first_recurring_payment of this Ptsv2paymentsProcessingInformationRecurringOptions.
        Flag that indicates whether this transaction is the first in a series of recurring payments.  This field is supported only for **Atos**, **FDC Nashville Global**, and **OmniPay Direct**.  Possible values:  - `true` Indicates this is the first payment in a series of recurring payments  - `false` (default) Indicates this is not the first payment in a series of recurring payments.  For details, see `auth_first_recurring_payment` field description and \"Recurring Payments\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :return: The first_recurring_payment of this Ptsv2paymentsProcessingInformationRecurringOptions.
        :rtype: bool
        """
        return self._first_recurring_payment

    @first_recurring_payment.setter
    def first_recurring_payment(self, first_recurring_payment):
        """
        Sets the first_recurring_payment of this Ptsv2paymentsProcessingInformationRecurringOptions.
        Flag that indicates whether this transaction is the first in a series of recurring payments.  This field is supported only for **Atos**, **FDC Nashville Global**, and **OmniPay Direct**.  Possible values:  - `true` Indicates this is the first payment in a series of recurring payments  - `false` (default) Indicates this is not the first payment in a series of recurring payments.  For details, see `auth_first_recurring_payment` field description and \"Recurring Payments\" in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/) 

        :param first_recurring_payment: The first_recurring_payment of this Ptsv2paymentsProcessingInformationRecurringOptions.
        :type: bool
        """

        self._first_recurring_payment = first_recurring_payment

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
        if not isinstance(other, Ptsv2paymentsProcessingInformationRecurringOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
