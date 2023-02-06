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


class Ptsv1pushfundstransferPointOfServiceInformation(object):
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
        'terminal_id': 'str',
        'cat_level': 'int',
        'entry_mode': 'str',
        'pin_entry_capability': 'int',
        'terminal_capability': 'int'
    }

    attribute_map = {
        'terminal_id': 'terminalId',
        'cat_level': 'catLevel',
        'entry_mode': 'entryMode',
        'pin_entry_capability': 'pinEntryCapability',
        'terminal_capability': 'terminalCapability'
    }

    def __init__(self, terminal_id=None, cat_level=None, entry_mode=None, pin_entry_capability=None, terminal_capability=None):
        """
        Ptsv1pushfundstransferPointOfServiceInformation - a model defined in Swagger
        """

        self._terminal_id = None
        self._cat_level = None
        self._entry_mode = None
        self._pin_entry_capability = None
        self._terminal_capability = None

        if terminal_id is not None:
          self.terminal_id = terminal_id
        if cat_level is not None:
          self.cat_level = cat_level
        if entry_mode is not None:
          self.entry_mode = entry_mode
        if pin_entry_capability is not None:
          self.pin_entry_capability = pin_entry_capability
        if terminal_capability is not None:
          self.terminal_capability = terminal_capability

    @property
    def terminal_id(self):
        """
        Gets the terminal_id of this Ptsv1pushfundstransferPointOfServiceInformation.
        Identifier for the terminal at your retail location. You can define this value yourself, but consult the processor for requirements.  Visa Platform Connect A list of all possible values is stored in your CyberSource account. If terminal ID validation is enabled for your CyberSource account, the value you send for this field is validated against the list each time you include the field in a request. To enable or disable terminal ID validation, contact CyberSource Customer Support.   Used by Authorization Optional for the following processors. When you do not include this field in a request, the default value that is defined in your account is used.  Chase Paymentech Solutions: Optional field. If you include this field in your request, you must also include pointOfSaleInformation.catLevel. 

        :return: The terminal_id of this Ptsv1pushfundstransferPointOfServiceInformation.
        :rtype: str
        """
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, terminal_id):
        """
        Sets the terminal_id of this Ptsv1pushfundstransferPointOfServiceInformation.
        Identifier for the terminal at your retail location. You can define this value yourself, but consult the processor for requirements.  Visa Platform Connect A list of all possible values is stored in your CyberSource account. If terminal ID validation is enabled for your CyberSource account, the value you send for this field is validated against the list each time you include the field in a request. To enable or disable terminal ID validation, contact CyberSource Customer Support.   Used by Authorization Optional for the following processors. When you do not include this field in a request, the default value that is defined in your account is used.  Chase Paymentech Solutions: Optional field. If you include this field in your request, you must also include pointOfSaleInformation.catLevel. 

        :param terminal_id: The terminal_id of this Ptsv1pushfundstransferPointOfServiceInformation.
        :type: str
        """

        self._terminal_id = terminal_id

    @property
    def cat_level(self):
        """
        Gets the cat_level of this Ptsv1pushfundstransferPointOfServiceInformation.
        Type of cardholder-activated terminal. Possible values:  - `1`: Automated dispensing machine - `2`: Self-service terminal - `3`: Limited amount terminal - `4`: In-flight commerce (IFC) terminal - `5`: Radio frequency device - `6`: Mobile acceptance terminal - `7`: Electronic cash register - `8`: E-commerce device at your location - `9`: Terminal or cash register that uses a dialup connection to connect to the transaction processing network  Chase Paymentech Solutions Only values 1, 2, and 3 are supported. Required if pointOfSaleInformation.terminalID is included in the request; otherwise, optional.  Visa Platform COnnect Values 1 through 6 are supported on CyberSource through VisaNet, but some acquirers do not support all six values. Optional field.  Nonnegative integer. 

        :return: The cat_level of this Ptsv1pushfundstransferPointOfServiceInformation.
        :rtype: int
        """
        return self._cat_level

    @cat_level.setter
    def cat_level(self, cat_level):
        """
        Sets the cat_level of this Ptsv1pushfundstransferPointOfServiceInformation.
        Type of cardholder-activated terminal. Possible values:  - `1`: Automated dispensing machine - `2`: Self-service terminal - `3`: Limited amount terminal - `4`: In-flight commerce (IFC) terminal - `5`: Radio frequency device - `6`: Mobile acceptance terminal - `7`: Electronic cash register - `8`: E-commerce device at your location - `9`: Terminal or cash register that uses a dialup connection to connect to the transaction processing network  Chase Paymentech Solutions Only values 1, 2, and 3 are supported. Required if pointOfSaleInformation.terminalID is included in the request; otherwise, optional.  Visa Platform COnnect Values 1 through 6 are supported on CyberSource through VisaNet, but some acquirers do not support all six values. Optional field.  Nonnegative integer. 

        :param cat_level: The cat_level of this Ptsv1pushfundstransferPointOfServiceInformation.
        :type: int
        """

        self._cat_level = cat_level

    @property
    def entry_mode(self):
        """
        Gets the entry_mode of this Ptsv1pushfundstransferPointOfServiceInformation.
        Method of entering payment card information into the POS terminal. Possible values:  - `contact`: Read from direct contact with chip card. - `contactless`: Read from a contactless interface using chip data. - `keyed`: Manually keyed into POS terminal. This value is not supported on OmniPay Direct. - `msd`: Read from a contactless interface using magnetic stripe data (MSD). This value is not supported on OmniPay Direct. - `swiped`: Read from credit card magnetic stripe. The contact, contactless, and msd values are supported only for EMV transactions. 

        :return: The entry_mode of this Ptsv1pushfundstransferPointOfServiceInformation.
        :rtype: str
        """
        return self._entry_mode

    @entry_mode.setter
    def entry_mode(self, entry_mode):
        """
        Sets the entry_mode of this Ptsv1pushfundstransferPointOfServiceInformation.
        Method of entering payment card information into the POS terminal. Possible values:  - `contact`: Read from direct contact with chip card. - `contactless`: Read from a contactless interface using chip data. - `keyed`: Manually keyed into POS terminal. This value is not supported on OmniPay Direct. - `msd`: Read from a contactless interface using magnetic stripe data (MSD). This value is not supported on OmniPay Direct. - `swiped`: Read from credit card magnetic stripe. The contact, contactless, and msd values are supported only for EMV transactions. 

        :param entry_mode: The entry_mode of this Ptsv1pushfundstransferPointOfServiceInformation.
        :type: str
        """

        self._entry_mode = entry_mode

    @property
    def pin_entry_capability(self):
        """
        Gets the pin_entry_capability of this Ptsv1pushfundstransferPointOfServiceInformation.
        PIN Entry Capability - 0 Unknown. - 1 Indicates terminal can accept and forward online PINs. - 2 Indicates terminal cannot accept and forward online PINs. - 8 Terminal PIN pad down. - 9 Reserved for future use. 

        :return: The pin_entry_capability of this Ptsv1pushfundstransferPointOfServiceInformation.
        :rtype: int
        """
        return self._pin_entry_capability

    @pin_entry_capability.setter
    def pin_entry_capability(self, pin_entry_capability):
        """
        Sets the pin_entry_capability of this Ptsv1pushfundstransferPointOfServiceInformation.
        PIN Entry Capability - 0 Unknown. - 1 Indicates terminal can accept and forward online PINs. - 2 Indicates terminal cannot accept and forward online PINs. - 8 Terminal PIN pad down. - 9 Reserved for future use. 

        :param pin_entry_capability: The pin_entry_capability of this Ptsv1pushfundstransferPointOfServiceInformation.
        :type: int
        """

        self._pin_entry_capability = pin_entry_capability

    @property
    def terminal_capability(self):
        """
        Gets the terminal_capability of this Ptsv1pushfundstransferPointOfServiceInformation.
        integer [ 1 .. 5 ] POS terminal’s capability. Possible values:  - `1`: Terminal has a magnetic stripe reader only. - `2`: Terminal has a magnetic stripe reader and manual entry capability. - `3`: Terminal has manual entry capability only. - `4`: Terminal can read chip cards. - `5`: Terminal can read contactless chip cards; cannot use contact to read chip cards. For an EMV transaction, the value of this field must be 4 or 5.  Used by Authorization Required for the following processors: Chase Paymentech Solutions  Optional for the following processors: Visa Platform Connect 

        :return: The terminal_capability of this Ptsv1pushfundstransferPointOfServiceInformation.
        :rtype: int
        """
        return self._terminal_capability

    @terminal_capability.setter
    def terminal_capability(self, terminal_capability):
        """
        Sets the terminal_capability of this Ptsv1pushfundstransferPointOfServiceInformation.
        integer [ 1 .. 5 ] POS terminal’s capability. Possible values:  - `1`: Terminal has a magnetic stripe reader only. - `2`: Terminal has a magnetic stripe reader and manual entry capability. - `3`: Terminal has manual entry capability only. - `4`: Terminal can read chip cards. - `5`: Terminal can read contactless chip cards; cannot use contact to read chip cards. For an EMV transaction, the value of this field must be 4 or 5.  Used by Authorization Required for the following processors: Chase Paymentech Solutions  Optional for the following processors: Visa Platform Connect 

        :param terminal_capability: The terminal_capability of this Ptsv1pushfundstransferPointOfServiceInformation.
        :type: int
        """

        self._terminal_capability = terminal_capability

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
        if not isinstance(other, Ptsv1pushfundstransferPointOfServiceInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
