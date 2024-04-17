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


class PtsV2PaymentsPost201ResponseRiskInformationProcessorResults(object):
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
        'fraud_decision': 'str',
        'fraud_decision_reason': 'str'
    }

    attribute_map = {
        'fraud_decision': 'fraudDecision',
        'fraud_decision_reason': 'fraudDecisionReason'
    }

    def __init__(self, fraud_decision=None, fraud_decision_reason=None):
        """
        PtsV2PaymentsPost201ResponseRiskInformationProcessorResults - a model defined in Swagger
        """

        self._fraud_decision = None
        self._fraud_decision_reason = None

        if fraud_decision is not None:
          self.fraud_decision = fraud_decision
        if fraud_decision_reason is not None:
          self.fraud_decision_reason = fraud_decision_reason

    @property
    def fraud_decision(self):
        """
        Gets the fraud_decision of this PtsV2PaymentsPost201ResponseRiskInformationProcessorResults.
        Type of filter. Possible values: - ACCEPT - PENDING - DENY - REPORT 

        :return: The fraud_decision of this PtsV2PaymentsPost201ResponseRiskInformationProcessorResults.
        :rtype: str
        """
        return self._fraud_decision

    @fraud_decision.setter
    def fraud_decision(self, fraud_decision):
        """
        Sets the fraud_decision of this PtsV2PaymentsPost201ResponseRiskInformationProcessorResults.
        Type of filter. Possible values: - ACCEPT - PENDING - DENY - REPORT 

        :param fraud_decision: The fraud_decision of this PtsV2PaymentsPost201ResponseRiskInformationProcessorResults.
        :type: str
        """

        self._fraud_decision = fraud_decision

    @property
    def fraud_decision_reason(self):
        """
        Gets the fraud_decision_reason of this PtsV2PaymentsPost201ResponseRiskInformationProcessorResults.
        possible values - AVS_NO_MATCH - AVS_PARTIAL_MATCH - AVS_UNAVAILABLE_OR_UNSUPPORTED - CARD_SECURITY_CODE_MISMATCH - MAXIMUM_TRANSACTION_AMOUNT - UNCONFIRMED_ADDRESS - COUNTRY_MONITOR - LARGE_ORDER_NUMBER - BILLING_OR_SHIPPING_ADDRESS_MISMATCH - RISKY_ZIP_CODE - SUSPECTED_FREIGHT_FORWARDER_CHECK - TOTAL_PURCHASE_PRICE_MINIMUM - IP_ADDRESS_VELOCITY - RISKY_EMAIL_ADDRESS_DOMAIN_CHECK - RISKY_BANK_IDENTIFICATION_NUMBER_CHECK, RISKY_IP_ADDRESS_RANGE - PAYPAL_FRAUD_MODEL 

        :return: The fraud_decision_reason of this PtsV2PaymentsPost201ResponseRiskInformationProcessorResults.
        :rtype: str
        """
        return self._fraud_decision_reason

    @fraud_decision_reason.setter
    def fraud_decision_reason(self, fraud_decision_reason):
        """
        Sets the fraud_decision_reason of this PtsV2PaymentsPost201ResponseRiskInformationProcessorResults.
        possible values - AVS_NO_MATCH - AVS_PARTIAL_MATCH - AVS_UNAVAILABLE_OR_UNSUPPORTED - CARD_SECURITY_CODE_MISMATCH - MAXIMUM_TRANSACTION_AMOUNT - UNCONFIRMED_ADDRESS - COUNTRY_MONITOR - LARGE_ORDER_NUMBER - BILLING_OR_SHIPPING_ADDRESS_MISMATCH - RISKY_ZIP_CODE - SUSPECTED_FREIGHT_FORWARDER_CHECK - TOTAL_PURCHASE_PRICE_MINIMUM - IP_ADDRESS_VELOCITY - RISKY_EMAIL_ADDRESS_DOMAIN_CHECK - RISKY_BANK_IDENTIFICATION_NUMBER_CHECK, RISKY_IP_ADDRESS_RANGE - PAYPAL_FRAUD_MODEL 

        :param fraud_decision_reason: The fraud_decision_reason of this PtsV2PaymentsPost201ResponseRiskInformationProcessorResults.
        :type: str
        """

        self._fraud_decision_reason = fraud_decision_reason

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseRiskInformationProcessorResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
