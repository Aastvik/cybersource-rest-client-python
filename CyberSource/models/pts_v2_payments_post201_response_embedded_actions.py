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


class PtsV2PaymentsPost201ResponseEmbeddedActions(object):
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
        'capture': 'PtsV2PaymentsPost201ResponseEmbeddedActionsCAPTURE',
        'decision': 'PtsV2PaymentsPost201ResponseEmbeddedActionsDECISION',
        'consumer_authentication': 'PtsV2PaymentsPost201ResponseEmbeddedActionsCONSUMERAUTHENTICATION',
        'validate_consumer_authentication': 'PtsV2PaymentsPost201ResponseEmbeddedActionsCONSUMERAUTHENTICATION',
        'watchlist_screening': 'PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING'
    }

    attribute_map = {
        'capture': 'CAPTURE',
        'decision': 'DECISION',
        'consumer_authentication': 'CONSUMER_AUTHENTICATION',
        'validate_consumer_authentication': 'VALIDATE_CONSUMER_AUTHENTICATION',
        'watchlist_screening': 'WATCHLIST_SCREENING'
    }

    def __init__(self, capture=None, decision=None, consumer_authentication=None, validate_consumer_authentication=None, watchlist_screening=None):
        """
        PtsV2PaymentsPost201ResponseEmbeddedActions - a model defined in Swagger
        """

        self._capture = None
        self._decision = None
        self._consumer_authentication = None
        self._validate_consumer_authentication = None
        self._watchlist_screening = None

        if capture is not None:
          self.capture = capture
        if decision is not None:
          self.decision = decision
        if consumer_authentication is not None:
          self.consumer_authentication = consumer_authentication
        if validate_consumer_authentication is not None:
          self.validate_consumer_authentication = validate_consumer_authentication
        if watchlist_screening is not None:
          self.watchlist_screening = watchlist_screening

    @property
    def capture(self):
        """
        Gets the capture of this PtsV2PaymentsPost201ResponseEmbeddedActions.

        :return: The capture of this PtsV2PaymentsPost201ResponseEmbeddedActions.
        :rtype: PtsV2PaymentsPost201ResponseEmbeddedActionsCAPTURE
        """
        return self._capture

    @capture.setter
    def capture(self, capture):
        """
        Sets the capture of this PtsV2PaymentsPost201ResponseEmbeddedActions.

        :param capture: The capture of this PtsV2PaymentsPost201ResponseEmbeddedActions.
        :type: PtsV2PaymentsPost201ResponseEmbeddedActionsCAPTURE
        """

        self._capture = capture

    @property
    def decision(self):
        """
        Gets the decision of this PtsV2PaymentsPost201ResponseEmbeddedActions.

        :return: The decision of this PtsV2PaymentsPost201ResponseEmbeddedActions.
        :rtype: PtsV2PaymentsPost201ResponseEmbeddedActionsDECISION
        """
        return self._decision

    @decision.setter
    def decision(self, decision):
        """
        Sets the decision of this PtsV2PaymentsPost201ResponseEmbeddedActions.

        :param decision: The decision of this PtsV2PaymentsPost201ResponseEmbeddedActions.
        :type: PtsV2PaymentsPost201ResponseEmbeddedActionsDECISION
        """

        self._decision = decision

    @property
    def consumer_authentication(self):
        """
        Gets the consumer_authentication of this PtsV2PaymentsPost201ResponseEmbeddedActions.

        :return: The consumer_authentication of this PtsV2PaymentsPost201ResponseEmbeddedActions.
        :rtype: PtsV2PaymentsPost201ResponseEmbeddedActionsCONSUMERAUTHENTICATION
        """
        return self._consumer_authentication

    @consumer_authentication.setter
    def consumer_authentication(self, consumer_authentication):
        """
        Sets the consumer_authentication of this PtsV2PaymentsPost201ResponseEmbeddedActions.

        :param consumer_authentication: The consumer_authentication of this PtsV2PaymentsPost201ResponseEmbeddedActions.
        :type: PtsV2PaymentsPost201ResponseEmbeddedActionsCONSUMERAUTHENTICATION
        """

        self._consumer_authentication = consumer_authentication

    @property
    def validate_consumer_authentication(self):
        """
        Gets the validate_consumer_authentication of this PtsV2PaymentsPost201ResponseEmbeddedActions.

        :return: The validate_consumer_authentication of this PtsV2PaymentsPost201ResponseEmbeddedActions.
        :rtype: PtsV2PaymentsPost201ResponseEmbeddedActionsCONSUMERAUTHENTICATION
        """
        return self._validate_consumer_authentication

    @validate_consumer_authentication.setter
    def validate_consumer_authentication(self, validate_consumer_authentication):
        """
        Sets the validate_consumer_authentication of this PtsV2PaymentsPost201ResponseEmbeddedActions.

        :param validate_consumer_authentication: The validate_consumer_authentication of this PtsV2PaymentsPost201ResponseEmbeddedActions.
        :type: PtsV2PaymentsPost201ResponseEmbeddedActionsCONSUMERAUTHENTICATION
        """

        self._validate_consumer_authentication = validate_consumer_authentication

    @property
    def watchlist_screening(self):
        """
        Gets the watchlist_screening of this PtsV2PaymentsPost201ResponseEmbeddedActions.

        :return: The watchlist_screening of this PtsV2PaymentsPost201ResponseEmbeddedActions.
        :rtype: PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING
        """
        return self._watchlist_screening

    @watchlist_screening.setter
    def watchlist_screening(self, watchlist_screening):
        """
        Sets the watchlist_screening of this PtsV2PaymentsPost201ResponseEmbeddedActions.

        :param watchlist_screening: The watchlist_screening of this PtsV2PaymentsPost201ResponseEmbeddedActions.
        :type: PtsV2PaymentsPost201ResponseEmbeddedActionsWATCHLISTSCREENING
        """

        self._watchlist_screening = watchlist_screening

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseEmbeddedActions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
