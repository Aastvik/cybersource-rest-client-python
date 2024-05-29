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


class TssV2TransactionsGet200ResponsePaymentInformationCard(object):
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
        'suffix': 'str',
        'prefix': 'str',
        'expiration_month': 'str',
        'expiration_year': 'str',
        'start_month': 'str',
        'start_year': 'str',
        'issue_number': 'str',
        'type': 'str',
        'brand_name': 'str',
        'currency': 'str',
        'account_encoder_id': 'str',
        'use_as': 'str'
    }

    attribute_map = {
        'suffix': 'suffix',
        'prefix': 'prefix',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'start_month': 'startMonth',
        'start_year': 'startYear',
        'issue_number': 'issueNumber',
        'type': 'type',
        'brand_name': 'brandName',
        'currency': 'currency',
        'account_encoder_id': 'accountEncoderId',
        'use_as': 'useAs'
    }

    def __init__(self, suffix=None, prefix=None, expiration_month=None, expiration_year=None, start_month=None, start_year=None, issue_number=None, type=None, brand_name=None, currency=None, account_encoder_id=None, use_as=None):
        """
        TssV2TransactionsGet200ResponsePaymentInformationCard - a model defined in Swagger
        """

        self._suffix = None
        self._prefix = None
        self._expiration_month = None
        self._expiration_year = None
        self._start_month = None
        self._start_year = None
        self._issue_number = None
        self._type = None
        self._brand_name = None
        self._currency = None
        self._account_encoder_id = None
        self._use_as = None

        if suffix is not None:
          self.suffix = suffix
        if prefix is not None:
          self.prefix = prefix
        if expiration_month is not None:
          self.expiration_month = expiration_month
        if expiration_year is not None:
          self.expiration_year = expiration_year
        if start_month is not None:
          self.start_month = start_month
        if start_year is not None:
          self.start_year = start_year
        if issue_number is not None:
          self.issue_number = issue_number
        if type is not None:
          self.type = type
        if brand_name is not None:
          self.brand_name = brand_name
        if currency is not None:
          self.currency = currency
        if account_encoder_id is not None:
          self.account_encoder_id = account_encoder_id
        if use_as is not None:
          self.use_as = use_as

    @property
    def suffix(self):
        """
        Gets the suffix of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Last four digits of the cardholder's account number. This field is included in the reply message when the client software that is installed on the POS terminal uses the token management service (TMS) to retrieve tokenized payment details.  You must contact customer support to have your account enabled to receive these fields in the credit reply message.  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response.  #### PIN debit This field is returned only for tokenized transactions. You can use this value on the receipt that you give to the cardholder.  Returned by PIN debit credit and PIN debit purchase.  This field is supported only by the following processors: - American Express Direct - Credit Mutuel-CIC - FDC Nashville Global - OmniPay Direct - SIX 

        :return: The suffix of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """
        Sets the suffix of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Last four digits of the cardholder's account number. This field is included in the reply message when the client software that is installed on the POS terminal uses the token management service (TMS) to retrieve tokenized payment details.  You must contact customer support to have your account enabled to receive these fields in the credit reply message.  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response.  #### PIN debit This field is returned only for tokenized transactions. You can use this value on the receipt that you give to the cardholder.  Returned by PIN debit credit and PIN debit purchase.  This field is supported only by the following processors: - American Express Direct - Credit Mutuel-CIC - FDC Nashville Global - OmniPay Direct - SIX 

        :param suffix: The suffix of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """

        self._suffix = suffix

    @property
    def prefix(self):
        """
        Gets the prefix of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Bank Identification Number (BIN). This is the initial four to six numbers on a credit card account number.  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response. 

        :return: The prefix of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Bank Identification Number (BIN). This is the initial four to six numbers on a credit card account number.  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response. 

        :param prefix: The prefix of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """

        self._prefix = prefix

    @property
    def expiration_month(self):
        """
        Gets the expiration_month of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Two-digit month in which the payment card expires.  Format: `MM`.  Valid values: `01` through `12`. Leading 0 is required.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`01` through `12`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (_type_=039), if there is no expiration date on the card, use `12`.  #### FDMS Nashville Required field.  #### All other processors Required if `pointOfSaleInformation.entryMode=keyed`. However, this field is optional if your account is configured for relaxed requirements for address data and expiration date. **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response. 

        :return: The expiration_month of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """
        Sets the expiration_month of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Two-digit month in which the payment card expires.  Format: `MM`.  Valid values: `01` through `12`. Leading 0 is required.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`01` through `12`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (_type_=039), if there is no expiration date on the card, use `12`.  #### FDMS Nashville Required field.  #### All other processors Required if `pointOfSaleInformation.entryMode=keyed`. However, this field is optional if your account is configured for relaxed requirements for address data and expiration date. **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response. 

        :param expiration_month: The expiration_month of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """
        Gets the expiration_year of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Four-digit year in which the payment card expires.  Format: `YYYY`.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`1900` through `3000`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (**_type_**`=039`), if there is no expiration date on the card, use `2021`.  #### FDMS Nashville Required field.  #### FDC Nashville Global and FDMS South You can send in 2 digits or 4 digits. If you send in 2 digits, they must be the last 2 digits of the year.  #### All other processors Required if `pointOfSaleInformation.entryMode=keyed`. However, this field is optional if your account is configured for relaxed requirements for address data and expiration date. **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response. 

        :return: The expiration_year of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """
        Sets the expiration_year of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Four-digit year in which the payment card expires.  Format: `YYYY`.  #### Barclays and Streamline For Maestro (UK Domestic) and Maestro (International) cards on Barclays and Streamline, this must be a valid value (`1900` through `3000`) but is not required to be a valid expiration date. In other words, an expiration date that is in the past does not cause CyberSource to reject your request. However, an invalid expiration date might cause the issuer to reject your request.  #### Encoded Account Numbers For encoded account numbers (**_type_**`=039`), if there is no expiration date on the card, use `2021`.  #### FDMS Nashville Required field.  #### FDC Nashville Global and FDMS South You can send in 2 digits or 4 digits. If you send in 2 digits, they must be the last 2 digits of the year.  #### All other processors Required if `pointOfSaleInformation.entryMode=keyed`. However, this field is optional if your account is configured for relaxed requirements for address data and expiration date. **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response. 

        :param expiration_year: The expiration_year of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """

        self._expiration_year = expiration_year

    @property
    def start_month(self):
        """
        Gets the start_month of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Month of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: MM`. Possible values: 01 through 12.  **Note** The start date is not required for Maestro (UK Domestic) transactions. 

        :return: The start_month of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._start_month

    @start_month.setter
    def start_month(self, start_month):
        """
        Sets the start_month of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Month of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: MM`. Possible values: 01 through 12.  **Note** The start date is not required for Maestro (UK Domestic) transactions. 

        :param start_month: The start_month of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """

        self._start_month = start_month

    @property
    def start_year(self):
        """
        Gets the start_year of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Year of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: YYYY`.  **Note** The start date is not required for Maestro (UK Domestic) transactions. 

        :return: The start_year of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._start_year

    @start_year.setter
    def start_year(self, start_year):
        """
        Sets the start_year of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Year of the start of the Maestro (UK Domestic) card validity period. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card. `Format: YYYY`.  **Note** The start date is not required for Maestro (UK Domestic) transactions. 

        :param start_year: The start_year of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """

        self._start_year = start_year

    @property
    def issue_number(self):
        """
        Gets the issue_number of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Number of times a Maestro (UK Domestic) card has been issued to the account holder. The card might or might not have an issue number. The number can consist of one or two digits, and the first digit might be a zero. When you include this value in your request, include exactly what is printed on the card. A value of 2 is different than a value of 02. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card.  **Note** The issue number is not required for Maestro (UK Domestic) transactions. 

        :return: The issue_number of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._issue_number

    @issue_number.setter
    def issue_number(self, issue_number):
        """
        Sets the issue_number of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Number of times a Maestro (UK Domestic) card has been issued to the account holder. The card might or might not have an issue number. The number can consist of one or two digits, and the first digit might be a zero. When you include this value in your request, include exactly what is printed on the card. A value of 2 is different than a value of 02. Do not include the field, even with a blank value, if the card is not a Maestro (UK Domestic) card.  **Note** The issue number is not required for Maestro (UK Domestic) transactions. 

        :param issue_number: The issue_number of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """

        self._issue_number = issue_number

    @property
    def type(self):
        """
        Gets the type of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Three-digit value that indicates the card type.  **IMPORTANT** It is strongly recommended that you include the card type field in request messages even if it is optional for your processor and card type. Omitting the card type can cause the transaction to be processed with the wrong card type.  Possible values: - `001`: Visa. For card-present transactions on all processors except SIX, the Visa Electron card type is processed the same way that the Visa debit card is processed. Use card type value `001` for Visa Electron. - `002`: Mastercard, Eurocard[^1], which is a European regional brand of Mastercard. - `003`: American Express - `004`: Discover - `005`: Diners Club - `006`: Carte Blanche[^1] - `007`: JCB[^1] - `014`: Enroute[^1] - `021`: JAL[^1] - `024`: Maestro (UK Domestic)[^1] - `031`: Delta[^1]: Use this value only for Ingenico ePayments. For other processors, use `001` for all Visa card types. - `033`: Visa Electron[^1]. Use this value only for Ingenico ePayments and SIX. For other processors, use `001` for all Visa card types. - `034`: Dankort[^1] - `036`: Cartes Bancaires[^1,4] - `037`: Carta Si[^1] - `039`: Encoded account number[^1] - `040`: UATP[^1] - `042`: Maestro (International)[^1] - `050`: Hipercard[^2,3] - `051`: Aura - `054`: Elo[^3] - `062`: China UnionPay - '070': EFTPOS  [^1]: For this card type, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in your request for an authorization or a stand-alone credit. [^2]: For this card type on Cielo 3.0, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit. This card type is not supported on Cielo 1.5. [^3]: For this card type on Getnet and Rede, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit. [^4]: For this card type, you must include the `paymentInformation.card.type` in your request for any payer authentication services.  #### Used by **Authorization** Required for Carte Blanche and JCB. Optional for all other card types.  #### Card Present reply This field is included in the reply message when the client software that is installed on the POS terminal uses the token management service (TMS) to retrieve tokenized payment details. You must contact customer support to have your account enabled to receive these fields in the credit reply message.  Returned by the Credit service.  This reply field is only supported by the following processors: - American Express Direct - Credit Mutuel-CIC - FDC Nashville Global - OmniPay Direct - SIX  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response.  #### GPX This field only supports transactions from the following card types: - Visa - Mastercard - AMEX - Discover - Diners - JCB - Union Pay International 

        :return: The type of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Three-digit value that indicates the card type.  **IMPORTANT** It is strongly recommended that you include the card type field in request messages even if it is optional for your processor and card type. Omitting the card type can cause the transaction to be processed with the wrong card type.  Possible values: - `001`: Visa. For card-present transactions on all processors except SIX, the Visa Electron card type is processed the same way that the Visa debit card is processed. Use card type value `001` for Visa Electron. - `002`: Mastercard, Eurocard[^1], which is a European regional brand of Mastercard. - `003`: American Express - `004`: Discover - `005`: Diners Club - `006`: Carte Blanche[^1] - `007`: JCB[^1] - `014`: Enroute[^1] - `021`: JAL[^1] - `024`: Maestro (UK Domestic)[^1] - `031`: Delta[^1]: Use this value only for Ingenico ePayments. For other processors, use `001` for all Visa card types. - `033`: Visa Electron[^1]. Use this value only for Ingenico ePayments and SIX. For other processors, use `001` for all Visa card types. - `034`: Dankort[^1] - `036`: Cartes Bancaires[^1,4] - `037`: Carta Si[^1] - `039`: Encoded account number[^1] - `040`: UATP[^1] - `042`: Maestro (International)[^1] - `050`: Hipercard[^2,3] - `051`: Aura - `054`: Elo[^3] - `062`: China UnionPay - '070': EFTPOS  [^1]: For this card type, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in your request for an authorization or a stand-alone credit. [^2]: For this card type on Cielo 3.0, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit. This card type is not supported on Cielo 1.5. [^3]: For this card type on Getnet and Rede, you must include the `paymentInformation.card.type` or `paymentInformation.tokenizedCard.type` field in a request for an authorization or a stand-alone credit. [^4]: For this card type, you must include the `paymentInformation.card.type` in your request for any payer authentication services.  #### Used by **Authorization** Required for Carte Blanche and JCB. Optional for all other card types.  #### Card Present reply This field is included in the reply message when the client software that is installed on the POS terminal uses the token management service (TMS) to retrieve tokenized payment details. You must contact customer support to have your account enabled to receive these fields in the credit reply message.  Returned by the Credit service.  This reply field is only supported by the following processors: - American Express Direct - Credit Mutuel-CIC - FDC Nashville Global - OmniPay Direct - SIX  #### Google Pay transactions For PAN-based Google Pay transactions, this field is returned in the API response.  #### GPX This field only supports transactions from the following card types: - Visa - Mastercard - AMEX - Discover - Diners - JCB - Union Pay International 

        :param type: The type of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """

        self._type = type

    @property
    def brand_name(self):
        """
        Gets the brand_name of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        This field contains the card brand name.   Some of the possible values (not an exhaustive list) are -    - VISA   - MASTERCARD   - AMERICAN EXPRESS   - DISCOVER   - DINERS CLUB   - CARTE BLANCHE   - JCB   - OPTIMA   - TWINPAY CREDIT CARD   - TWINPAY DEBIT CARD   - WALMART   - ENROUTE   - LOWES CONSUMER   - HOME DEPOT CONSUMER   - MBNA   - DICKS SPORTWEAR   - CASUAL CORNER   - SEARS   - JAL   - DISNEY CARD   - SWITCH/SOLO   - SAMS CLUB CONSUMER   - SAMS CLUB BUSINESS   - NICOS HOUSE CARD   - BEBE   - RESTORATION HARDWARE   - DELTA ONLINE   - SOLO   - VISA ELECTRON   - DANKORT   - LASER   - CARTE BANCAIRE   - CARTA SI   - ENCODED ACCOUNT   - UATP   - HOUSEHOLD   - MAESTRO   - GE CAPITAL   - KOREAN CARDS   - STYLE CARDS   - JCREW   - MEIJER   - HIPERCARD   - AURA   - REDECARD   - ORICO HOUSE CARD   - ELO   - CAPITAL ONE PRIVATE LABEL   - CARNET   - RUPAY   - CHINA UNION PAY   - FALABELLA PRIVATE LABEL   - PROMPTCARD   - KOREAN DOMESTIC   - BANRICOMPRAS 

        :return: The brand_name of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name):
        """
        Sets the brand_name of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        This field contains the card brand name.   Some of the possible values (not an exhaustive list) are -    - VISA   - MASTERCARD   - AMERICAN EXPRESS   - DISCOVER   - DINERS CLUB   - CARTE BLANCHE   - JCB   - OPTIMA   - TWINPAY CREDIT CARD   - TWINPAY DEBIT CARD   - WALMART   - ENROUTE   - LOWES CONSUMER   - HOME DEPOT CONSUMER   - MBNA   - DICKS SPORTWEAR   - CASUAL CORNER   - SEARS   - JAL   - DISNEY CARD   - SWITCH/SOLO   - SAMS CLUB CONSUMER   - SAMS CLUB BUSINESS   - NICOS HOUSE CARD   - BEBE   - RESTORATION HARDWARE   - DELTA ONLINE   - SOLO   - VISA ELECTRON   - DANKORT   - LASER   - CARTE BANCAIRE   - CARTA SI   - ENCODED ACCOUNT   - UATP   - HOUSEHOLD   - MAESTRO   - GE CAPITAL   - KOREAN CARDS   - STYLE CARDS   - JCREW   - MEIJER   - HIPERCARD   - AURA   - REDECARD   - ORICO HOUSE CARD   - ELO   - CAPITAL ONE PRIVATE LABEL   - CARNET   - RUPAY   - CHINA UNION PAY   - FALABELLA PRIVATE LABEL   - PROMPTCARD   - KOREAN DOMESTIC   - BANRICOMPRAS 

        :param brand_name: The brand_name of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """

        self._brand_name = brand_name

    @property
    def currency(self):
        """
        Gets the currency of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        This field indicates the 3-letter [ISO Standard Currency Codes](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf) for the card currency. 

        :return: The currency of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        This field indicates the 3-letter [ISO Standard Currency Codes](http://apps.cybersource.com/library/documentation/sbc/quickref/currencies.pdf) for the card currency. 

        :param currency: The currency of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """

        self._currency = currency

    @property
    def account_encoder_id(self):
        """
        Gets the account_encoder_id of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Identifier for the issuing bank that provided the customer's encoded account number. Contact your processor for the bank's ID. 

        :return: The account_encoder_id of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._account_encoder_id

    @account_encoder_id.setter
    def account_encoder_id(self, account_encoder_id):
        """
        Sets the account_encoder_id of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Identifier for the issuing bank that provided the customer's encoded account number. Contact your processor for the bank's ID. 

        :param account_encoder_id: The account_encoder_id of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """

        self._account_encoder_id = account_encoder_id

    @property
    def use_as(self):
        """
        Gets the use_as of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Flag that specifies the type of account associated with the card.  This field is available only for China UnionPay, Cielo, Comercio Latino and Visa Platform Connect. The cardholder provides this information during the payment process.  This field is required for:  - Debit transactions on Cielo and Comercio Latino.  - Transactions with Brazilian-issued cards on CyberSource through VisaNet.  **China UnionPayCard Transactions on China UnionPay:** Possible values:  - C: Domestic credit card  - D: Domestic debit card  - F: International credit card  - I: International debit card  When the value is D, the e-commerce indicator and CAVV fields must be included in the authorization request. When the value is C, F or I the card verification number, expiration month and expiration year fields must in included in the authorization request.  **Cielo and Comercio Latino Credit Card Transactions:** On these processors, this field is supported only for authorizations.  Possible values:  - CR: Credit card  - DB: Debit card       **Visa Platform Connect Credit Card Transactions:** This field is supported for all card types on Visa Platform Connect. For combo **card present** transactions with Mastercard on Brazilian-issued cards, possible values:  - CR: Credit card  - DB: Debit Card  For combo **card not present** transactions with Mastercard on Brazilian-issued cards, possible values:  - C: Credit card  - D: Debit card  A value of CR or DB in the useAs field takes precedence over any value in the Source Account Type field. 

        :return: The use_as of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :rtype: str
        """
        return self._use_as

    @use_as.setter
    def use_as(self, use_as):
        """
        Sets the use_as of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        Flag that specifies the type of account associated with the card.  This field is available only for China UnionPay, Cielo, Comercio Latino and Visa Platform Connect. The cardholder provides this information during the payment process.  This field is required for:  - Debit transactions on Cielo and Comercio Latino.  - Transactions with Brazilian-issued cards on CyberSource through VisaNet.  **China UnionPayCard Transactions on China UnionPay:** Possible values:  - C: Domestic credit card  - D: Domestic debit card  - F: International credit card  - I: International debit card  When the value is D, the e-commerce indicator and CAVV fields must be included in the authorization request. When the value is C, F or I the card verification number, expiration month and expiration year fields must in included in the authorization request.  **Cielo and Comercio Latino Credit Card Transactions:** On these processors, this field is supported only for authorizations.  Possible values:  - CR: Credit card  - DB: Debit card       **Visa Platform Connect Credit Card Transactions:** This field is supported for all card types on Visa Platform Connect. For combo **card present** transactions with Mastercard on Brazilian-issued cards, possible values:  - CR: Credit card  - DB: Debit Card  For combo **card not present** transactions with Mastercard on Brazilian-issued cards, possible values:  - C: Credit card  - D: Debit card  A value of CR or DB in the useAs field takes precedence over any value in the Source Account Type field. 

        :param use_as: The use_as of this TssV2TransactionsGet200ResponsePaymentInformationCard.
        :type: str
        """

        self._use_as = use_as

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
        if not isinstance(other, TssV2TransactionsGet200ResponsePaymentInformationCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
