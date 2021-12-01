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


class Ptsv2payoutsProcessingInformation(object):
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
        'network_routing_order': 'str',
        'commerce_indicator': 'str',
        'reconciliation_id': 'str',
        'payouts_options': 'Ptsv2payoutsProcessingInformationPayoutsOptions',
        'transaction_reason': 'str',
        'purpose_of_payment': 'str'
    }

    attribute_map = {
        'business_application_id': 'businessApplicationId',
        'network_routing_order': 'networkRoutingOrder',
        'commerce_indicator': 'commerceIndicator',
        'reconciliation_id': 'reconciliationId',
        'payouts_options': 'payoutsOptions',
        'transaction_reason': 'transactionReason',
        'purpose_of_payment': 'purposeOfPayment'
    }

    def __init__(self, business_application_id=None, network_routing_order=None, commerce_indicator=None, reconciliation_id=None, payouts_options=None, transaction_reason=None, purpose_of_payment=None):
        """
        Ptsv2payoutsProcessingInformation - a model defined in Swagger
        """

        self._business_application_id = None
        self._network_routing_order = None
        self._commerce_indicator = None
        self._reconciliation_id = None
        self._payouts_options = None
        self._transaction_reason = None
        self._purpose_of_payment = None

        if business_application_id is not None:
          self.business_application_id = business_application_id
        if network_routing_order is not None:
          self.network_routing_order = network_routing_order
        if commerce_indicator is not None:
          self.commerce_indicator = commerce_indicator
        if reconciliation_id is not None:
          self.reconciliation_id = reconciliation_id
        if payouts_options is not None:
          self.payouts_options = payouts_options
        if transaction_reason is not None:
          self.transaction_reason = transaction_reason
        if purpose_of_payment is not None:
          self.purpose_of_payment = purpose_of_payment

    @property
    def business_application_id(self):
        """
        Gets the business_application_id of this Ptsv2payoutsProcessingInformation.
        Payouts transaction type.  Applicable Processors: FDC Compass, Paymentech, CtV  Possible values:  **Credit Card Bill Payment**   - **CP**: credit card bill payment  **Funds Disbursement**   - **FD**: funds disbursement  - **GD**: government disbursement  - **MD**: merchant disbursement  **Money Transfer**   - **AA**: account to account. Sender and receiver are same person.  - **PP**: person to person. Sender and receiver are different.  **Prepaid Load**   - **TU**: top up 

        :return: The business_application_id of this Ptsv2payoutsProcessingInformation.
        :rtype: str
        """
        return self._business_application_id

    @business_application_id.setter
    def business_application_id(self, business_application_id):
        """
        Sets the business_application_id of this Ptsv2payoutsProcessingInformation.
        Payouts transaction type.  Applicable Processors: FDC Compass, Paymentech, CtV  Possible values:  **Credit Card Bill Payment**   - **CP**: credit card bill payment  **Funds Disbursement**   - **FD**: funds disbursement  - **GD**: government disbursement  - **MD**: merchant disbursement  **Money Transfer**   - **AA**: account to account. Sender and receiver are same person.  - **PP**: person to person. Sender and receiver are different.  **Prepaid Load**   - **TU**: top up 

        :param business_application_id: The business_application_id of this Ptsv2payoutsProcessingInformation.
        :type: str
        """

        self._business_application_id = business_application_id

    @property
    def network_routing_order(self):
        """
        Gets the network_routing_order of this Ptsv2payoutsProcessingInformation.
        This field is optionally used by Push Payments Gateway participants (merchants and acquirers) to get the attributes for specified networks only. The networks specified in this field must be a subset of the information provided during program enrollment. Refer to Sharing Group Code/Network Routing Order. Note: Supported only in US for domestic transactions involving Push Payments Gateway Service.  VisaNet checks to determine if there are issuer routing preferences for any of the networks specified by the network routing order. If an issuer preference exists for one of the specified debit networks, VisaNet makes a routing selection based on the issuer’s preference.  If an issuer preference exists for more than one of the specified debit networks, or if no issuer preference exists, VisaNet makes a selection based on the acquirer’s routing priorities.   For details, see the `network_order` field description in [BIN Lookup Service Using the SCMP API.](http://apps.cybersource.com/library/documentation/BIN_Lookup/BIN_Lookup_SCMP_API/html/) 

        :return: The network_routing_order of this Ptsv2payoutsProcessingInformation.
        :rtype: str
        """
        return self._network_routing_order

    @network_routing_order.setter
    def network_routing_order(self, network_routing_order):
        """
        Sets the network_routing_order of this Ptsv2payoutsProcessingInformation.
        This field is optionally used by Push Payments Gateway participants (merchants and acquirers) to get the attributes for specified networks only. The networks specified in this field must be a subset of the information provided during program enrollment. Refer to Sharing Group Code/Network Routing Order. Note: Supported only in US for domestic transactions involving Push Payments Gateway Service.  VisaNet checks to determine if there are issuer routing preferences for any of the networks specified by the network routing order. If an issuer preference exists for one of the specified debit networks, VisaNet makes a routing selection based on the issuer’s preference.  If an issuer preference exists for more than one of the specified debit networks, or if no issuer preference exists, VisaNet makes a selection based on the acquirer’s routing priorities.   For details, see the `network_order` field description in [BIN Lookup Service Using the SCMP API.](http://apps.cybersource.com/library/documentation/BIN_Lookup/BIN_Lookup_SCMP_API/html/) 

        :param network_routing_order: The network_routing_order of this Ptsv2payoutsProcessingInformation.
        :type: str
        """

        self._network_routing_order = network_routing_order

    @property
    def commerce_indicator(self):
        """
        Gets the commerce_indicator of this Ptsv2payoutsProcessingInformation.
        Type of transaction.  Value for an OCT transaction: - `internet`  For details, see the `e_commerce_indicator` field description in [Payouts Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/payouts_SCMP/html/) 

        :return: The commerce_indicator of this Ptsv2payoutsProcessingInformation.
        :rtype: str
        """
        return self._commerce_indicator

    @commerce_indicator.setter
    def commerce_indicator(self, commerce_indicator):
        """
        Sets the commerce_indicator of this Ptsv2payoutsProcessingInformation.
        Type of transaction.  Value for an OCT transaction: - `internet`  For details, see the `e_commerce_indicator` field description in [Payouts Using the SCMP API.](http://apps.cybersource.com/library/documentation/dev_guides/payouts_SCMP/html/) 

        :param commerce_indicator: The commerce_indicator of this Ptsv2payoutsProcessingInformation.
        :type: str
        """

        self._commerce_indicator = commerce_indicator

    @property
    def reconciliation_id(self):
        """
        Gets the reconciliation_id of this Ptsv2payoutsProcessingInformation.
        Please check with Cybersource customer support to see if your merchant account is configured correctly so you can include this field in your request. * For Payouts: max length for FDCCompass is String (22). 

        :return: The reconciliation_id of this Ptsv2payoutsProcessingInformation.
        :rtype: str
        """
        return self._reconciliation_id

    @reconciliation_id.setter
    def reconciliation_id(self, reconciliation_id):
        """
        Sets the reconciliation_id of this Ptsv2payoutsProcessingInformation.
        Please check with Cybersource customer support to see if your merchant account is configured correctly so you can include this field in your request. * For Payouts: max length for FDCCompass is String (22). 

        :param reconciliation_id: The reconciliation_id of this Ptsv2payoutsProcessingInformation.
        :type: str
        """

        self._reconciliation_id = reconciliation_id

    @property
    def payouts_options(self):
        """
        Gets the payouts_options of this Ptsv2payoutsProcessingInformation.

        :return: The payouts_options of this Ptsv2payoutsProcessingInformation.
        :rtype: Ptsv2payoutsProcessingInformationPayoutsOptions
        """
        return self._payouts_options

    @payouts_options.setter
    def payouts_options(self, payouts_options):
        """
        Sets the payouts_options of this Ptsv2payoutsProcessingInformation.

        :param payouts_options: The payouts_options of this Ptsv2payoutsProcessingInformation.
        :type: Ptsv2payoutsProcessingInformationPayoutsOptions
        """

        self._payouts_options = payouts_options

    @property
    def transaction_reason(self):
        """
        Gets the transaction_reason of this Ptsv2payoutsProcessingInformation.
        Transaction reason code. 

        :return: The transaction_reason of this Ptsv2payoutsProcessingInformation.
        :rtype: str
        """
        return self._transaction_reason

    @transaction_reason.setter
    def transaction_reason(self, transaction_reason):
        """
        Sets the transaction_reason of this Ptsv2payoutsProcessingInformation.
        Transaction reason code. 

        :param transaction_reason: The transaction_reason of this Ptsv2payoutsProcessingInformation.
        :type: str
        """

        self._transaction_reason = transaction_reason

    @property
    def purpose_of_payment(self):
        """
        Gets the purpose_of_payment of this Ptsv2payoutsProcessingInformation.
        This will send purpose of funds code for original credit transactions (OCTs). 

        :return: The purpose_of_payment of this Ptsv2payoutsProcessingInformation.
        :rtype: str
        """
        return self._purpose_of_payment

    @purpose_of_payment.setter
    def purpose_of_payment(self, purpose_of_payment):
        """
        Sets the purpose_of_payment of this Ptsv2payoutsProcessingInformation.
        This will send purpose of funds code for original credit transactions (OCTs). 

        :param purpose_of_payment: The purpose_of_payment of this Ptsv2payoutsProcessingInformation.
        :type: str
        """

        self._purpose_of_payment = purpose_of_payment

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
        if not isinstance(other, Ptsv2payoutsProcessingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
