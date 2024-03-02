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


class PatchInstrumentIdentifierRequest(object):
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
        'links': 'TmsEmbeddedInstrumentIdentifierLinks',
        'id': 'str',
        'object': 'str',
        'state': 'str',
        'type': 'str',
        'card': 'TmsEmbeddedInstrumentIdentifierCard',
        'bank_account': 'TmsEmbeddedInstrumentIdentifierBankAccount',
        'tokenized_card': 'TmsEmbeddedInstrumentIdentifierTokenizedCard',
        'issuer': 'TmsEmbeddedInstrumentIdentifierIssuer',
        'processing_information': 'TmsEmbeddedInstrumentIdentifierProcessingInformation',
        'bill_to': 'TmsEmbeddedInstrumentIdentifierBillTo',
        'metadata': 'TmsEmbeddedInstrumentIdentifierMetadata'
    }

    attribute_map = {
        'links': '_links',
        'id': 'id',
        'object': 'object',
        'state': 'state',
        'type': 'type',
        'card': 'card',
        'bank_account': 'bankAccount',
        'tokenized_card': 'tokenizedCard',
        'issuer': 'issuer',
        'processing_information': 'processingInformation',
        'bill_to': 'billTo',
        'metadata': 'metadata'
    }

    def __init__(self, links=None, id=None, object=None, state=None, type=None, card=None, bank_account=None, tokenized_card=None, issuer=None, processing_information=None, bill_to=None, metadata=None):
        """
        PatchInstrumentIdentifierRequest - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._object = None
        self._state = None
        self._type = None
        self._card = None
        self._bank_account = None
        self._tokenized_card = None
        self._issuer = None
        self._processing_information = None
        self._bill_to = None
        self._metadata = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if object is not None:
          self.object = object
        if state is not None:
          self.state = state
        if type is not None:
          self.type = type
        if card is not None:
          self.card = card
        if bank_account is not None:
          self.bank_account = bank_account
        if tokenized_card is not None:
          self.tokenized_card = tokenized_card
        if issuer is not None:
          self.issuer = issuer
        if processing_information is not None:
          self.processing_information = processing_information
        if bill_to is not None:
          self.bill_to = bill_to
        if metadata is not None:
          self.metadata = metadata

    @property
    def links(self):
        """
        Gets the links of this PatchInstrumentIdentifierRequest.

        :return: The links of this PatchInstrumentIdentifierRequest.
        :rtype: TmsEmbeddedInstrumentIdentifierLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this PatchInstrumentIdentifierRequest.

        :param links: The links of this PatchInstrumentIdentifierRequest.
        :type: TmsEmbeddedInstrumentIdentifierLinks
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this PatchInstrumentIdentifierRequest.
        The Id of the Instrument Identifier Token. 

        :return: The id of this PatchInstrumentIdentifierRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PatchInstrumentIdentifierRequest.
        The Id of the Instrument Identifier Token. 

        :param id: The id of this PatchInstrumentIdentifierRequest.
        :type: str
        """

        self._id = id

    @property
    def object(self):
        """
        Gets the object of this PatchInstrumentIdentifierRequest.
        The type.  Possible Values: - instrumentIdentifier 

        :return: The object of this PatchInstrumentIdentifierRequest.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this PatchInstrumentIdentifierRequest.
        The type.  Possible Values: - instrumentIdentifier 

        :param object: The object of this PatchInstrumentIdentifierRequest.
        :type: str
        """

        self._object = object

    @property
    def state(self):
        """
        Gets the state of this PatchInstrumentIdentifierRequest.
        Issuers state for the card number. Possible Values: - ACTIVE - CLOSED : The account has been closed. 

        :return: The state of this PatchInstrumentIdentifierRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this PatchInstrumentIdentifierRequest.
        Issuers state for the card number. Possible Values: - ACTIVE - CLOSED : The account has been closed. 

        :param state: The state of this PatchInstrumentIdentifierRequest.
        :type: str
        """

        self._state = state

    @property
    def type(self):
        """
        Gets the type of this PatchInstrumentIdentifierRequest.
        The type of Instrument Identifier. Possible Values: - enrollable card 

        :return: The type of this PatchInstrumentIdentifierRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PatchInstrumentIdentifierRequest.
        The type of Instrument Identifier. Possible Values: - enrollable card 

        :param type: The type of this PatchInstrumentIdentifierRequest.
        :type: str
        """

        self._type = type

    @property
    def card(self):
        """
        Gets the card of this PatchInstrumentIdentifierRequest.

        :return: The card of this PatchInstrumentIdentifierRequest.
        :rtype: TmsEmbeddedInstrumentIdentifierCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this PatchInstrumentIdentifierRequest.

        :param card: The card of this PatchInstrumentIdentifierRequest.
        :type: TmsEmbeddedInstrumentIdentifierCard
        """

        self._card = card

    @property
    def bank_account(self):
        """
        Gets the bank_account of this PatchInstrumentIdentifierRequest.

        :return: The bank_account of this PatchInstrumentIdentifierRequest.
        :rtype: TmsEmbeddedInstrumentIdentifierBankAccount
        """
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        """
        Sets the bank_account of this PatchInstrumentIdentifierRequest.

        :param bank_account: The bank_account of this PatchInstrumentIdentifierRequest.
        :type: TmsEmbeddedInstrumentIdentifierBankAccount
        """

        self._bank_account = bank_account

    @property
    def tokenized_card(self):
        """
        Gets the tokenized_card of this PatchInstrumentIdentifierRequest.

        :return: The tokenized_card of this PatchInstrumentIdentifierRequest.
        :rtype: TmsEmbeddedInstrumentIdentifierTokenizedCard
        """
        return self._tokenized_card

    @tokenized_card.setter
    def tokenized_card(self, tokenized_card):
        """
        Sets the tokenized_card of this PatchInstrumentIdentifierRequest.

        :param tokenized_card: The tokenized_card of this PatchInstrumentIdentifierRequest.
        :type: TmsEmbeddedInstrumentIdentifierTokenizedCard
        """

        self._tokenized_card = tokenized_card

    @property
    def issuer(self):
        """
        Gets the issuer of this PatchInstrumentIdentifierRequest.

        :return: The issuer of this PatchInstrumentIdentifierRequest.
        :rtype: TmsEmbeddedInstrumentIdentifierIssuer
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this PatchInstrumentIdentifierRequest.

        :param issuer: The issuer of this PatchInstrumentIdentifierRequest.
        :type: TmsEmbeddedInstrumentIdentifierIssuer
        """

        self._issuer = issuer

    @property
    def processing_information(self):
        """
        Gets the processing_information of this PatchInstrumentIdentifierRequest.

        :return: The processing_information of this PatchInstrumentIdentifierRequest.
        :rtype: TmsEmbeddedInstrumentIdentifierProcessingInformation
        """
        return self._processing_information

    @processing_information.setter
    def processing_information(self, processing_information):
        """
        Sets the processing_information of this PatchInstrumentIdentifierRequest.

        :param processing_information: The processing_information of this PatchInstrumentIdentifierRequest.
        :type: TmsEmbeddedInstrumentIdentifierProcessingInformation
        """

        self._processing_information = processing_information

    @property
    def bill_to(self):
        """
        Gets the bill_to of this PatchInstrumentIdentifierRequest.

        :return: The bill_to of this PatchInstrumentIdentifierRequest.
        :rtype: TmsEmbeddedInstrumentIdentifierBillTo
        """
        return self._bill_to

    @bill_to.setter
    def bill_to(self, bill_to):
        """
        Sets the bill_to of this PatchInstrumentIdentifierRequest.

        :param bill_to: The bill_to of this PatchInstrumentIdentifierRequest.
        :type: TmsEmbeddedInstrumentIdentifierBillTo
        """

        self._bill_to = bill_to

    @property
    def metadata(self):
        """
        Gets the metadata of this PatchInstrumentIdentifierRequest.

        :return: The metadata of this PatchInstrumentIdentifierRequest.
        :rtype: TmsEmbeddedInstrumentIdentifierMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this PatchInstrumentIdentifierRequest.

        :param metadata: The metadata of this PatchInstrumentIdentifierRequest.
        :type: TmsEmbeddedInstrumentIdentifierMetadata
        """

        self._metadata = metadata

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
        if not isinstance(other, PatchInstrumentIdentifierRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
