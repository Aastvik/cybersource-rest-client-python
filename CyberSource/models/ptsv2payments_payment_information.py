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


class Ptsv2paymentsPaymentInformation(object):
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
        'card': 'Ptsv2paymentsPaymentInformationCard',
        'tokenized_card': 'Ptsv2paymentsPaymentInformationTokenizedCard',
        'direct_debit': 'Ptsv2paymentsPaymentInformationDirectDebit',
        'fluid_data': 'Ptsv2paymentsPaymentInformationFluidData',
        'customer': 'Ptsv2paymentsPaymentInformationCustomer',
        'payment_instrument': 'Ptsv2paymentsPaymentInformationPaymentInstrument',
        'instrument_identifier': 'Ptsv2paymentsPaymentInformationInstrumentIdentifier',
        'shipping_address': 'Ptsv2paymentsPaymentInformationShippingAddress',
        'legacy_token': 'Ptsv2paymentsPaymentInformationLegacyToken',
        'bank': 'Ptsv2paymentsPaymentInformationBank',
        'options': 'Ptsv2paymentsPaymentInformationOptions',
        'payment_type': 'Ptsv2paymentsPaymentInformationPaymentType',
        'initiation_channel': 'str',
        'e_wallet': 'Ptsv2paymentsPaymentInformationEWallet'
    }

    attribute_map = {
        'card': 'card',
        'tokenized_card': 'tokenizedCard',
        'direct_debit': 'directDebit',
        'fluid_data': 'fluidData',
        'customer': 'customer',
        'payment_instrument': 'paymentInstrument',
        'instrument_identifier': 'instrumentIdentifier',
        'shipping_address': 'shippingAddress',
        'legacy_token': 'legacyToken',
        'bank': 'bank',
        'options': 'options',
        'payment_type': 'paymentType',
        'initiation_channel': 'initiationChannel',
        'e_wallet': 'eWallet'
    }

    def __init__(self, card=None, tokenized_card=None, direct_debit=None, fluid_data=None, customer=None, payment_instrument=None, instrument_identifier=None, shipping_address=None, legacy_token=None, bank=None, options=None, payment_type=None, initiation_channel=None, e_wallet=None):
        """
        Ptsv2paymentsPaymentInformation - a model defined in Swagger
        """

        self._card = None
        self._tokenized_card = None
        self._direct_debit = None
        self._fluid_data = None
        self._customer = None
        self._payment_instrument = None
        self._instrument_identifier = None
        self._shipping_address = None
        self._legacy_token = None
        self._bank = None
        self._options = None
        self._payment_type = None
        self._initiation_channel = None
        self._e_wallet = None

        if card is not None:
          self.card = card
        if tokenized_card is not None:
          self.tokenized_card = tokenized_card
        if direct_debit is not None:
          self.direct_debit = direct_debit
        if fluid_data is not None:
          self.fluid_data = fluid_data
        if customer is not None:
          self.customer = customer
        if payment_instrument is not None:
          self.payment_instrument = payment_instrument
        if instrument_identifier is not None:
          self.instrument_identifier = instrument_identifier
        if shipping_address is not None:
          self.shipping_address = shipping_address
        if legacy_token is not None:
          self.legacy_token = legacy_token
        if bank is not None:
          self.bank = bank
        if options is not None:
          self.options = options
        if payment_type is not None:
          self.payment_type = payment_type
        if initiation_channel is not None:
          self.initiation_channel = initiation_channel
        if e_wallet is not None:
          self.e_wallet = e_wallet

    @property
    def card(self):
        """
        Gets the card of this Ptsv2paymentsPaymentInformation.

        :return: The card of this Ptsv2paymentsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """
        Sets the card of this Ptsv2paymentsPaymentInformation.

        :param card: The card of this Ptsv2paymentsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationCard
        """

        self._card = card

    @property
    def tokenized_card(self):
        """
        Gets the tokenized_card of this Ptsv2paymentsPaymentInformation.

        :return: The tokenized_card of this Ptsv2paymentsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationTokenizedCard
        """
        return self._tokenized_card

    @tokenized_card.setter
    def tokenized_card(self, tokenized_card):
        """
        Sets the tokenized_card of this Ptsv2paymentsPaymentInformation.

        :param tokenized_card: The tokenized_card of this Ptsv2paymentsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationTokenizedCard
        """

        self._tokenized_card = tokenized_card

    @property
    def direct_debit(self):
        """
        Gets the direct_debit of this Ptsv2paymentsPaymentInformation.

        :return: The direct_debit of this Ptsv2paymentsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationDirectDebit
        """
        return self._direct_debit

    @direct_debit.setter
    def direct_debit(self, direct_debit):
        """
        Sets the direct_debit of this Ptsv2paymentsPaymentInformation.

        :param direct_debit: The direct_debit of this Ptsv2paymentsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationDirectDebit
        """

        self._direct_debit = direct_debit

    @property
    def fluid_data(self):
        """
        Gets the fluid_data of this Ptsv2paymentsPaymentInformation.

        :return: The fluid_data of this Ptsv2paymentsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationFluidData
        """
        return self._fluid_data

    @fluid_data.setter
    def fluid_data(self, fluid_data):
        """
        Sets the fluid_data of this Ptsv2paymentsPaymentInformation.

        :param fluid_data: The fluid_data of this Ptsv2paymentsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationFluidData
        """

        self._fluid_data = fluid_data

    @property
    def customer(self):
        """
        Gets the customer of this Ptsv2paymentsPaymentInformation.

        :return: The customer of this Ptsv2paymentsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """
        Sets the customer of this Ptsv2paymentsPaymentInformation.

        :param customer: The customer of this Ptsv2paymentsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationCustomer
        """

        self._customer = customer

    @property
    def payment_instrument(self):
        """
        Gets the payment_instrument of this Ptsv2paymentsPaymentInformation.

        :return: The payment_instrument of this Ptsv2paymentsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationPaymentInstrument
        """
        return self._payment_instrument

    @payment_instrument.setter
    def payment_instrument(self, payment_instrument):
        """
        Sets the payment_instrument of this Ptsv2paymentsPaymentInformation.

        :param payment_instrument: The payment_instrument of this Ptsv2paymentsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationPaymentInstrument
        """

        self._payment_instrument = payment_instrument

    @property
    def instrument_identifier(self):
        """
        Gets the instrument_identifier of this Ptsv2paymentsPaymentInformation.

        :return: The instrument_identifier of this Ptsv2paymentsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationInstrumentIdentifier
        """
        return self._instrument_identifier

    @instrument_identifier.setter
    def instrument_identifier(self, instrument_identifier):
        """
        Sets the instrument_identifier of this Ptsv2paymentsPaymentInformation.

        :param instrument_identifier: The instrument_identifier of this Ptsv2paymentsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationInstrumentIdentifier
        """

        self._instrument_identifier = instrument_identifier

    @property
    def shipping_address(self):
        """
        Gets the shipping_address of this Ptsv2paymentsPaymentInformation.

        :return: The shipping_address of this Ptsv2paymentsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationShippingAddress
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """
        Sets the shipping_address of this Ptsv2paymentsPaymentInformation.

        :param shipping_address: The shipping_address of this Ptsv2paymentsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationShippingAddress
        """

        self._shipping_address = shipping_address

    @property
    def legacy_token(self):
        """
        Gets the legacy_token of this Ptsv2paymentsPaymentInformation.

        :return: The legacy_token of this Ptsv2paymentsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationLegacyToken
        """
        return self._legacy_token

    @legacy_token.setter
    def legacy_token(self, legacy_token):
        """
        Sets the legacy_token of this Ptsv2paymentsPaymentInformation.

        :param legacy_token: The legacy_token of this Ptsv2paymentsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationLegacyToken
        """

        self._legacy_token = legacy_token

    @property
    def bank(self):
        """
        Gets the bank of this Ptsv2paymentsPaymentInformation.

        :return: The bank of this Ptsv2paymentsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationBank
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """
        Sets the bank of this Ptsv2paymentsPaymentInformation.

        :param bank: The bank of this Ptsv2paymentsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationBank
        """

        self._bank = bank

    @property
    def options(self):
        """
        Gets the options of this Ptsv2paymentsPaymentInformation.

        :return: The options of this Ptsv2paymentsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this Ptsv2paymentsPaymentInformation.

        :param options: The options of this Ptsv2paymentsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationOptions
        """

        self._options = options

    @property
    def payment_type(self):
        """
        Gets the payment_type of this Ptsv2paymentsPaymentInformation.

        :return: The payment_type of this Ptsv2paymentsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationPaymentType
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """
        Sets the payment_type of this Ptsv2paymentsPaymentInformation.

        :param payment_type: The payment_type of this Ptsv2paymentsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationPaymentType
        """

        self._payment_type = payment_type

    @property
    def initiation_channel(self):
        """
        Gets the initiation_channel of this Ptsv2paymentsPaymentInformation.
        Mastercard-defined code that indicates how the account information was obtained.  - `00`: Card - `01`: Mobile Network Operator (MNO) controlled removable secure element (SIM or UICC) personalized for use with a mobile phone or smartphone - `02`: Key fob - `03`: Watch using a contactless chip or a fixed (non-removable) secure element not controlled by the MNO - `04`: Mobile tag - `05`: Wristband - `06`: Mobile phone case or sleeve - `07`: Mobile phone or smartphone with a fixed (non-removable) secure element controlled by the MNO,for example, code division multiple access (CDMA) - `08`: Removable secure element not controlled by the MNO, for example, memory card personalized forused with a mobile phone or smartphone - `09`: Mobile Phone or smartphone with a fixed (non-removable) secure element not controlled by the MNO - `10`: MNO controlled removable secure element (SIM or UICC) personalized for use with a tablet or e-book - `11`: Tablet or e-book with a fixed (non-removable) secure element controlled by the MNO - `12`: Removable secure element not controlled by the MNO, for example, memory card personalized foruse with a tablet or e-book - `13`: Tablet or e-book with fixed (non-removable) secure element not controlled by the MNO - `14`: Mobile phone or smartphone with a payment application running in a host processor - `15`: Tablet or e-book with a payment application running in a host processor - `16`: Mobile phone or smartphone with a payment application running in the Trusted ExecutionEnvironment (TEE) of a host processor - `17`: Tablet or e-book with a payment application running in the TEE of a host processor - `18`: Watch with a payment application running in the TEE of a host processor - `19`: Watch with a payment application running in a host processor  Values from 20–99 exclusively indicate the form factor only without also indicating the storage technology  - `20`: Card - `21`: Phone e.g. Mobile Phone - `22`: Tablet/e-reader - `23`: Watch/Wristband e.g. Watch or wristband, including a fitness band, smart strap, disposable band, watch add-on, and security/ID band - `24`: Sticker - `25`: PC - `26`: Device Peripheral e.g. mobile phone case or sleeve - `27`: Tag e.g. key fob or mobile tag - `28`: Jewelry e.g. ring, bracelet, necklace and cuff links - `29`: Fashion Accessory e.g. handbag, bag charm and glasses - `30`: Garment e.g. dress - `31`: Domestic Appliance e.g refrigerator, washing machine - `32`: Vehicle e.g. vehicle, including vehicle attached devices - `33`: Media/Gaming Device e.g. media or gaming device, including a set top box, media player and television  34–99 are reserved for future form factors. Any value in this range may occur within form factor and transaction data without prior notice.  This field is supported only for Mastercard on CyberSource through VisaNet. When initiation channel is not provided via this API field, the value is extracted from EMV tag 9F6E for Mastercard transactions. To enable this feature please call support.  #### Used by **Authorization** Optional field. 

        :return: The initiation_channel of this Ptsv2paymentsPaymentInformation.
        :rtype: str
        """
        return self._initiation_channel

    @initiation_channel.setter
    def initiation_channel(self, initiation_channel):
        """
        Sets the initiation_channel of this Ptsv2paymentsPaymentInformation.
        Mastercard-defined code that indicates how the account information was obtained.  - `00`: Card - `01`: Mobile Network Operator (MNO) controlled removable secure element (SIM or UICC) personalized for use with a mobile phone or smartphone - `02`: Key fob - `03`: Watch using a contactless chip or a fixed (non-removable) secure element not controlled by the MNO - `04`: Mobile tag - `05`: Wristband - `06`: Mobile phone case or sleeve - `07`: Mobile phone or smartphone with a fixed (non-removable) secure element controlled by the MNO,for example, code division multiple access (CDMA) - `08`: Removable secure element not controlled by the MNO, for example, memory card personalized forused with a mobile phone or smartphone - `09`: Mobile Phone or smartphone with a fixed (non-removable) secure element not controlled by the MNO - `10`: MNO controlled removable secure element (SIM or UICC) personalized for use with a tablet or e-book - `11`: Tablet or e-book with a fixed (non-removable) secure element controlled by the MNO - `12`: Removable secure element not controlled by the MNO, for example, memory card personalized foruse with a tablet or e-book - `13`: Tablet or e-book with fixed (non-removable) secure element not controlled by the MNO - `14`: Mobile phone or smartphone with a payment application running in a host processor - `15`: Tablet or e-book with a payment application running in a host processor - `16`: Mobile phone or smartphone with a payment application running in the Trusted ExecutionEnvironment (TEE) of a host processor - `17`: Tablet or e-book with a payment application running in the TEE of a host processor - `18`: Watch with a payment application running in the TEE of a host processor - `19`: Watch with a payment application running in a host processor  Values from 20–99 exclusively indicate the form factor only without also indicating the storage technology  - `20`: Card - `21`: Phone e.g. Mobile Phone - `22`: Tablet/e-reader - `23`: Watch/Wristband e.g. Watch or wristband, including a fitness band, smart strap, disposable band, watch add-on, and security/ID band - `24`: Sticker - `25`: PC - `26`: Device Peripheral e.g. mobile phone case or sleeve - `27`: Tag e.g. key fob or mobile tag - `28`: Jewelry e.g. ring, bracelet, necklace and cuff links - `29`: Fashion Accessory e.g. handbag, bag charm and glasses - `30`: Garment e.g. dress - `31`: Domestic Appliance e.g refrigerator, washing machine - `32`: Vehicle e.g. vehicle, including vehicle attached devices - `33`: Media/Gaming Device e.g. media or gaming device, including a set top box, media player and television  34–99 are reserved for future form factors. Any value in this range may occur within form factor and transaction data without prior notice.  This field is supported only for Mastercard on CyberSource through VisaNet. When initiation channel is not provided via this API field, the value is extracted from EMV tag 9F6E for Mastercard transactions. To enable this feature please call support.  #### Used by **Authorization** Optional field. 

        :param initiation_channel: The initiation_channel of this Ptsv2paymentsPaymentInformation.
        :type: str
        """

        self._initiation_channel = initiation_channel

    @property
    def e_wallet(self):
        """
        Gets the e_wallet of this Ptsv2paymentsPaymentInformation.

        :return: The e_wallet of this Ptsv2paymentsPaymentInformation.
        :rtype: Ptsv2paymentsPaymentInformationEWallet
        """
        return self._e_wallet

    @e_wallet.setter
    def e_wallet(self, e_wallet):
        """
        Sets the e_wallet of this Ptsv2paymentsPaymentInformation.

        :param e_wallet: The e_wallet of this Ptsv2paymentsPaymentInformation.
        :type: Ptsv2paymentsPaymentInformationEWallet
        """

        self._e_wallet = e_wallet

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
        if not isinstance(other, Ptsv2paymentsPaymentInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
