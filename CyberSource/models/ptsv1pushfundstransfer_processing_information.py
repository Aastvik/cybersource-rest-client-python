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


class Ptsv1pushfundstransferProcessingInformation(object):
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
        'business_application_id': 'str',
        'commerce_indicator': 'str',
        'network_routing_order': 'str',
        'payouts_options': 'Ptsv1pushfundstransferProcessingInformationPayoutsOptions',
        'purpose_of_payment': 'str',
        'reconciliation_id': 'str',
        'recurring_options': 'Ptsv1pushfundstransferProcessingInformationRecurringOptions',
        'transaction_reason': 'str'
    }

    attribute_map = {
        'business_application_id': 'businessApplicationId',
        'commerce_indicator': 'commerceIndicator',
        'network_routing_order': 'networkRoutingOrder',
        'payouts_options': 'payoutsOptions',
        'purpose_of_payment': 'purposeOfPayment',
        'reconciliation_id': 'reconciliationId',
        'recurring_options': 'recurringOptions',
        'transaction_reason': 'transactionReason'
    }

    def __init__(self, business_application_id=None, commerce_indicator=None, network_routing_order=None, payouts_options=None, purpose_of_payment=None, reconciliation_id=None, recurring_options=None, transaction_reason=None):
        """
        Ptsv1pushfundstransferProcessingInformation - a model defined in Swagger
        """

        self._business_application_id = None
        self._commerce_indicator = None
        self._network_routing_order = None
        self._payouts_options = None
        self._purpose_of_payment = None
        self._reconciliation_id = None
        self._recurring_options = None
        self._transaction_reason = None

        if business_application_id is not None:
          self.business_application_id = business_application_id
        self.commerce_indicator = commerce_indicator
        if network_routing_order is not None:
          self.network_routing_order = network_routing_order
        if payouts_options is not None:
          self.payouts_options = payouts_options
        if purpose_of_payment is not None:
          self.purpose_of_payment = purpose_of_payment
        if reconciliation_id is not None:
          self.reconciliation_id = reconciliation_id
        if recurring_options is not None:
          self.recurring_options = recurring_options
        if transaction_reason is not None:
          self.transaction_reason = transaction_reason

    @property
    def business_application_id(self):
        """
        Gets the business_application_id of this Ptsv1pushfundstransferProcessingInformation.
         Payouts transaction type. Required for Mastercard Send.  Valid Values- Visa Platform Connect: - `AA`: Account to account. - `CP`: Card bill payment - `FD`: Funds disbursement (general) - `GD`: Government disbursement - `MD`: Merchant disbursement (acquirers or aggregators settling to merchants). - `PP`: Person to person. - `TU`: Top-up for enhanced prepaid loads.   Mastercard Send: - `BB`: Business to business. - `BD`: Business Disbursement - `CP`: Card bill payment - `GD`: Government disbursement - `MD`: Merchant disbursement (acquirers or aggregators settling to merchants). - `OG`: Online gambling payout.   Chase Paymentech Solutions: - `AA`: Account to account. - `FD`: Funds disbursement (general) - `MD`: Merchant disbursement (acquirers or aggregators settling to merchants). - `PP`: Person to person.   FDC Compass: - `BB`: Business to business. - `BI`: Bank-initiated money transfer. - `FD`: Funds disbursement (general) - `GD`: Government disbursement - `GP`: Gambling Payment - `LO`: Loyalty Offers - `MD`: Merchant disbursement (acquirers or aggregators settling to merchants). - `MI`: Merchant initated money transfer - `OG`: Online gambling payout. - `PD`: Payroll pension disbursement. - `PP`: Person to person. - `WT`: Wallet transfer. 

        :return: The business_application_id of this Ptsv1pushfundstransferProcessingInformation.
        :rtype: str
        """
        return self._business_application_id

    @business_application_id.setter
    def business_application_id(self, business_application_id):
        """
        Sets the business_application_id of this Ptsv1pushfundstransferProcessingInformation.
         Payouts transaction type. Required for Mastercard Send.  Valid Values- Visa Platform Connect: - `AA`: Account to account. - `CP`: Card bill payment - `FD`: Funds disbursement (general) - `GD`: Government disbursement - `MD`: Merchant disbursement (acquirers or aggregators settling to merchants). - `PP`: Person to person. - `TU`: Top-up for enhanced prepaid loads.   Mastercard Send: - `BB`: Business to business. - `BD`: Business Disbursement - `CP`: Card bill payment - `GD`: Government disbursement - `MD`: Merchant disbursement (acquirers or aggregators settling to merchants). - `OG`: Online gambling payout.   Chase Paymentech Solutions: - `AA`: Account to account. - `FD`: Funds disbursement (general) - `MD`: Merchant disbursement (acquirers or aggregators settling to merchants). - `PP`: Person to person.   FDC Compass: - `BB`: Business to business. - `BI`: Bank-initiated money transfer. - `FD`: Funds disbursement (general) - `GD`: Government disbursement - `GP`: Gambling Payment - `LO`: Loyalty Offers - `MD`: Merchant disbursement (acquirers or aggregators settling to merchants). - `MI`: Merchant initated money transfer - `OG`: Online gambling payout. - `PD`: Payroll pension disbursement. - `PP`: Person to person. - `WT`: Wallet transfer. 

        :param business_application_id: The business_application_id of this Ptsv1pushfundstransferProcessingInformation.
        :type: str
        """

        self._business_application_id = business_application_id

    @property
    def commerce_indicator(self):
        """
        Gets the commerce_indicator of this Ptsv1pushfundstransferProcessingInformation.
        Type of transaction.  Value for an OCT transaction: internet  For details, see the e_commerce_indicator field description in Payouts Using the SCMP API. 

        :return: The commerce_indicator of this Ptsv1pushfundstransferProcessingInformation.
        :rtype: str
        """
        return self._commerce_indicator

    @commerce_indicator.setter
    def commerce_indicator(self, commerce_indicator):
        """
        Sets the commerce_indicator of this Ptsv1pushfundstransferProcessingInformation.
        Type of transaction.  Value for an OCT transaction: internet  For details, see the e_commerce_indicator field description in Payouts Using the SCMP API. 

        :param commerce_indicator: The commerce_indicator of this Ptsv1pushfundstransferProcessingInformation.
        :type: str
        """
        if commerce_indicator is None:
            raise ValueError("Invalid value for `commerce_indicator`, must not be `None`")

        self._commerce_indicator = commerce_indicator

    @property
    def network_routing_order(self):
        """
        Gets the network_routing_order of this Ptsv1pushfundstransferProcessingInformation.
        Visa Platform Connect This field is optionally used by Push Payments Gateway participants (merchants and acquirers) to get the attributes for specified networks only. The networks specified in this field must be a subset of the information provided during program enrollment. Refer to Sharing Group Code/Network Routing Order. Note: Supported only in US for domestic transactions involving Push Payments Gateway Service.  VisaNet checks to determine if there are issuer routing preferences for any of the networks specified by the network routing order. If an issuer preference exists for one of the specified debit networks, VisaNet makes a routing selection based on the issuer's preference. If an issuer preference exists for more than one of the specified debit networks, or if no issuer preference exists, VisaNet makes a selection based on the acquirer's routing priorities.  For details, see the network_order field description in BIN Lookup Service Using the SCMP API. 

        :return: The network_routing_order of this Ptsv1pushfundstransferProcessingInformation.
        :rtype: str
        """
        return self._network_routing_order

    @network_routing_order.setter
    def network_routing_order(self, network_routing_order):
        """
        Sets the network_routing_order of this Ptsv1pushfundstransferProcessingInformation.
        Visa Platform Connect This field is optionally used by Push Payments Gateway participants (merchants and acquirers) to get the attributes for specified networks only. The networks specified in this field must be a subset of the information provided during program enrollment. Refer to Sharing Group Code/Network Routing Order. Note: Supported only in US for domestic transactions involving Push Payments Gateway Service.  VisaNet checks to determine if there are issuer routing preferences for any of the networks specified by the network routing order. If an issuer preference exists for one of the specified debit networks, VisaNet makes a routing selection based on the issuer's preference. If an issuer preference exists for more than one of the specified debit networks, or if no issuer preference exists, VisaNet makes a selection based on the acquirer's routing priorities.  For details, see the network_order field description in BIN Lookup Service Using the SCMP API. 

        :param network_routing_order: The network_routing_order of this Ptsv1pushfundstransferProcessingInformation.
        :type: str
        """

        self._network_routing_order = network_routing_order

    @property
    def payouts_options(self):
        """
        Gets the payouts_options of this Ptsv1pushfundstransferProcessingInformation.

        :return: The payouts_options of this Ptsv1pushfundstransferProcessingInformation.
        :rtype: Ptsv1pushfundstransferProcessingInformationPayoutsOptions
        """
        return self._payouts_options

    @payouts_options.setter
    def payouts_options(self, payouts_options):
        """
        Sets the payouts_options of this Ptsv1pushfundstransferProcessingInformation.

        :param payouts_options: The payouts_options of this Ptsv1pushfundstransferProcessingInformation.
        :type: Ptsv1pushfundstransferProcessingInformationPayoutsOptions
        """

        self._payouts_options = payouts_options

    @property
    def purpose_of_payment(self):
        """
        Gets the purpose_of_payment of this Ptsv1pushfundstransferProcessingInformation.
        This will send purpose of funds code for original credit transactions (OCTs).  Visa Platform Connect (VPC) This will send purpose of transaction code for original credit transactions (OCTs). Purpose of Payment codes are defined by the recipient issuer's country and vary by country.  Mastercard Send: - `00`: Family Support - `01`: Regular Labor Transfers (expatriates), - `02`: Travel & Tourism - `03`: Education - `04`: Hospitalization & Medical Treatment, - `05`: Emergency Need - `06`: Savings - `07`: Gifts - `08`: Other - `09`: Salary - `10`: Crowd lending - `11`: Crypto currency - `12`: Refund to original card - `13`: Refund to new card 

        :return: The purpose_of_payment of this Ptsv1pushfundstransferProcessingInformation.
        :rtype: str
        """
        return self._purpose_of_payment

    @purpose_of_payment.setter
    def purpose_of_payment(self, purpose_of_payment):
        """
        Sets the purpose_of_payment of this Ptsv1pushfundstransferProcessingInformation.
        This will send purpose of funds code for original credit transactions (OCTs).  Visa Platform Connect (VPC) This will send purpose of transaction code for original credit transactions (OCTs). Purpose of Payment codes are defined by the recipient issuer's country and vary by country.  Mastercard Send: - `00`: Family Support - `01`: Regular Labor Transfers (expatriates), - `02`: Travel & Tourism - `03`: Education - `04`: Hospitalization & Medical Treatment, - `05`: Emergency Need - `06`: Savings - `07`: Gifts - `08`: Other - `09`: Salary - `10`: Crowd lending - `11`: Crypto currency - `12`: Refund to original card - `13`: Refund to new card 

        :param purpose_of_payment: The purpose_of_payment of this Ptsv1pushfundstransferProcessingInformation.
        :type: str
        """

        self._purpose_of_payment = purpose_of_payment

    @property
    def reconciliation_id(self):
        """
        Gets the reconciliation_id of this Ptsv1pushfundstransferProcessingInformation.
        Please check with Cybersource customer support to see if your merchant account is configured correctly so you can include this field in your request.  For Payouts: max length for FDCCompass is String (22). 

        :return: The reconciliation_id of this Ptsv1pushfundstransferProcessingInformation.
        :rtype: str
        """
        return self._reconciliation_id

    @reconciliation_id.setter
    def reconciliation_id(self, reconciliation_id):
        """
        Sets the reconciliation_id of this Ptsv1pushfundstransferProcessingInformation.
        Please check with Cybersource customer support to see if your merchant account is configured correctly so you can include this field in your request.  For Payouts: max length for FDCCompass is String (22). 

        :param reconciliation_id: The reconciliation_id of this Ptsv1pushfundstransferProcessingInformation.
        :type: str
        """

        self._reconciliation_id = reconciliation_id

    @property
    def recurring_options(self):
        """
        Gets the recurring_options of this Ptsv1pushfundstransferProcessingInformation.

        :return: The recurring_options of this Ptsv1pushfundstransferProcessingInformation.
        :rtype: Ptsv1pushfundstransferProcessingInformationRecurringOptions
        """
        return self._recurring_options

    @recurring_options.setter
    def recurring_options(self, recurring_options):
        """
        Sets the recurring_options of this Ptsv1pushfundstransferProcessingInformation.

        :param recurring_options: The recurring_options of this Ptsv1pushfundstransferProcessingInformation.
        :type: Ptsv1pushfundstransferProcessingInformationRecurringOptions
        """

        self._recurring_options = recurring_options

    @property
    def transaction_reason(self):
        """
        Gets the transaction_reason of this Ptsv1pushfundstransferProcessingInformation.
        Transaction reason code.  This field applies only to Visa Platform Connect 

        :return: The transaction_reason of this Ptsv1pushfundstransferProcessingInformation.
        :rtype: str
        """
        return self._transaction_reason

    @transaction_reason.setter
    def transaction_reason(self, transaction_reason):
        """
        Sets the transaction_reason of this Ptsv1pushfundstransferProcessingInformation.
        Transaction reason code.  This field applies only to Visa Platform Connect 

        :param transaction_reason: The transaction_reason of this Ptsv1pushfundstransferProcessingInformation.
        :type: str
        """

        self._transaction_reason = transaction_reason

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
        if not isinstance(other, Ptsv1pushfundstransferProcessingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
