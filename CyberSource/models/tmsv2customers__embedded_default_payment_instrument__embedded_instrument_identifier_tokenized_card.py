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


class Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard(object):
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
        'type': 'str',
        'state': 'str',
        'enrollment_id': 'str',
        'token_reference_id': 'str',
        'reason': 'str',
        'number': 'str',
        'expiration_month': 'str',
        'expiration_year': 'str',
        'cryptogram': 'str',
        'card': 'Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCardCard'
    }

    attribute_map = {
        'type': 'type',
        'state': 'state',
        'enrollment_id': 'enrollmentId',
        'token_reference_id': 'tokenReferenceId',
        'reason': 'reason',
        'number': 'number',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'cryptogram': 'cryptogram',
        'card': 'card'
    }

    def __init__(self, type=None, state=None, enrollment_id=None, token_reference_id=None, reason=None, number=None, expiration_month=None, expiration_year=None, cryptogram=None, card=None):
        """
        Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard - a model defined in Swagger
        """

        self._type = None
        self._state = None
        self._enrollment_id = None
        self._token_reference_id = None
        self._reason = None
        self._number = None
        self._expiration_month = None
        self._expiration_year = None
        self._cryptogram = None
        self._card = None

        if type is not None:
          self.type = type
        if state is not None:
          self.state = state
        if enrollment_id is not None:
          self.enrollment_id = enrollment_id
        if token_reference_id is not None:
          self.token_reference_id = token_reference_id
        if reason is not None:
          self.reason = reason
        if number is not None:
          self.number = number
        if expiration_month is not None:
          self.expiration_month = expiration_month
        if expiration_year is not None:
          self.expiration_year = expiration_year
        if cryptogram is not None:
          self.cryptogram = cryptogram
        if card is not None:
          self.card = card

    @property
    def type(self):
        """
        Gets the type of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        The network token card association brand Possible Values: - visa - mastercard - americanexpress 

        :return: The type of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        The network token card association brand Possible Values: - visa - mastercard - americanexpress 

        :param type: The type of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :type: str
        """

        self._type = type

    @property
    def state(self):
        """
        Gets the state of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        State of the network token or network token provision Possible Values: - ACTIVE : Network token is active. - SUSPENDED : Network token is suspended. This state can change back to ACTIVE. - DELETED : This is a final state for a network token instance. - UNPROVISIONED : A previous network token provision was unsuccessful. 

        :return: The state of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        State of the network token or network token provision Possible Values: - ACTIVE : Network token is active. - SUSPENDED : Network token is suspended. This state can change back to ACTIVE. - DELETED : This is a final state for a network token instance. - UNPROVISIONED : A previous network token provision was unsuccessful. 

        :param state: The state of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :type: str
        """

        self._state = state

    @property
    def enrollment_id(self):
        """
        Gets the enrollment_id of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        Unique Identifier for the enrolled PAN. This Id is provided by the card association when a network token is provisioned successfully. 

        :return: The enrollment_id of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :rtype: str
        """
        return self._enrollment_id

    @enrollment_id.setter
    def enrollment_id(self, enrollment_id):
        """
        Sets the enrollment_id of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        Unique Identifier for the enrolled PAN. This Id is provided by the card association when a network token is provisioned successfully. 

        :param enrollment_id: The enrollment_id of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :type: str
        """

        self._enrollment_id = enrollment_id

    @property
    def token_reference_id(self):
        """
        Gets the token_reference_id of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        Unique Identifier for the network token. This Id is provided by the card association when a network token is provisioned successfully. 

        :return: The token_reference_id of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :rtype: str
        """
        return self._token_reference_id

    @token_reference_id.setter
    def token_reference_id(self, token_reference_id):
        """
        Sets the token_reference_id of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        Unique Identifier for the network token. This Id is provided by the card association when a network token is provisioned successfully. 

        :param token_reference_id: The token_reference_id of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :type: str
        """

        self._token_reference_id = token_reference_id

    @property
    def reason(self):
        """
        Gets the reason of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        Issuers state for the network token Possible Values: - INVALID_REQUEST : The network token provision request contained invalid data. - CARD_VERIFICATION_FAILED : The network token provision request contained data that could not be verified. - CARD_NOT_ELIGIBLE : Card can currently not be used with issuer for tokenization. - CARD_NOT_ALLOWED : Card can currently not be used with card association for tokenization. - DECLINED : Card can currently not be used with issuer for tokenization. - SERVICE_UNAVAILABLE : The network token service was unavailable or timed out. - SYSTEM_ERROR : An unexpected error occurred with network token service, check configuration. 

        :return: The reason of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        Issuers state for the network token Possible Values: - INVALID_REQUEST : The network token provision request contained invalid data. - CARD_VERIFICATION_FAILED : The network token provision request contained data that could not be verified. - CARD_NOT_ELIGIBLE : Card can currently not be used with issuer for tokenization. - CARD_NOT_ALLOWED : Card can currently not be used with card association for tokenization. - DECLINED : Card can currently not be used with issuer for tokenization. - SERVICE_UNAVAILABLE : The network token service was unavailable or timed out. - SYSTEM_ERROR : An unexpected error occurred with network token service, check configuration. 

        :param reason: The reason of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :type: str
        """

        self._reason = reason

    @property
    def number(self):
        """
        Gets the number of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        The token requestors network token 

        :return: The number of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        The token requestors network token 

        :param number: The number of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :type: str
        """

        self._number = number

    @property
    def expiration_month(self):
        """
        Gets the expiration_month of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        Two-digit month in which the network token expires.  Format: `MM`.  Possible Values: `01` through `12`. 

        :return: The expiration_month of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """
        Sets the expiration_month of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        Two-digit month in which the network token expires.  Format: `MM`.  Possible Values: `01` through `12`. 

        :param expiration_month: The expiration_month of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :type: str
        """

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """
        Gets the expiration_year of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        Four-digit year in which the network token expires.  Format: `YYYY`. 

        :return: The expiration_year of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """
        Sets the expiration_year of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        Four-digit year in which the network token expires.  Format: `YYYY`. 

        :param expiration_year: The expiration_year of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :type: str
        """

        self._expiration_year = expiration_year

    @property
    def cryptogram(self):
        """
        Gets the cryptogram of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        Generated value used in conjunction with the network token for making a payment. 

        :return: The cryptogram of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :rtype: str
        """
        return self._cryptogram

    @cryptogram.setter
    def cryptogram(self, cryptogram):
        """
        Sets the cryptogram of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        Generated value used in conjunction with the network token for making a payment. 

        :param cryptogram: The cryptogram of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :type: str
        """

        self._cryptogram = cryptogram

    @property
    def card(self):
        """
        Gets the card of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.

        :return: The card of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :rtype: Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCardCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.

        :param card: The card of this Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard.
        :type: Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCardCard
        """

        self._card = card

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
        if not isinstance(other, Tmsv2customersEmbeddedDefaultPaymentInstrumentEmbeddedInstrumentIdentifierTokenizedCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
