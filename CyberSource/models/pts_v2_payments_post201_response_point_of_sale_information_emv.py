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


class PtsV2PaymentsPost201ResponsePointOfSaleInformationEmv(object):
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
        'tags': 'str'
    }

    attribute_map = {
        'tags': 'tags'
    }

    def __init__(self, tags=None):
        """
        PtsV2PaymentsPost201ResponsePointOfSaleInformationEmv - a model defined in Swagger
        """

        self._tags = None

        if tags is not None:
          self.tags = tags

    @property
    def tags(self):
        """
        Gets the tags of this PtsV2PaymentsPost201ResponsePointOfSaleInformationEmv.
        EMV data that is transmitted from the chip card to the issuer, and from the issuer to the chip card. The EMV data is in the tag-length-value format and includes chip card tags, terminal tags, and transaction detail tags.  See \"Europay, MasterCard, Visa (EMV),\" page 10. For information about the individual tags, see the “Application Specification” section in the EMV 4.3 Specifications: http://emvco.com  **Important** The following tags contain sensitive information and **must not** be included in this field:   - **56**: Track 1 equivalent data  - **57**: Track 2 equivalent data  - **5A**: Application PAN  - **5F20**: Cardholder name  - **5F24**: Application expiration date (This sensitivity has been relaxed for cmcic, amexdirect, fdiglobal, opdfde, and six)  - **99**: Transaction PIN  - **9F0B**: Cardholder name (extended)  - **9F1F**: Track 1 discretionary data  - **9F20**: Track 2 discretionary data  For captures, this field is required for contact EMV transactions. Otherwise, it is optional.  For credits, this field is required for contact EMV stand-alone credits and contactless EMV stand-alone credits. Otherwise, it is optional.  **Important** For contact EMV captures, contact EMV stand-alone credits, and contactless EMV stand-alone credits, you must include the following tags in this field. For all other types of EMV transactions, the following tags are optional.   - **95**: Terminal verification results  - **9F10**: Issuer application data  - **9F26**: Application cryptogram 

        :return: The tags of this PtsV2PaymentsPost201ResponsePointOfSaleInformationEmv.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this PtsV2PaymentsPost201ResponsePointOfSaleInformationEmv.
        EMV data that is transmitted from the chip card to the issuer, and from the issuer to the chip card. The EMV data is in the tag-length-value format and includes chip card tags, terminal tags, and transaction detail tags.  See \"Europay, MasterCard, Visa (EMV),\" page 10. For information about the individual tags, see the “Application Specification” section in the EMV 4.3 Specifications: http://emvco.com  **Important** The following tags contain sensitive information and **must not** be included in this field:   - **56**: Track 1 equivalent data  - **57**: Track 2 equivalent data  - **5A**: Application PAN  - **5F20**: Cardholder name  - **5F24**: Application expiration date (This sensitivity has been relaxed for cmcic, amexdirect, fdiglobal, opdfde, and six)  - **99**: Transaction PIN  - **9F0B**: Cardholder name (extended)  - **9F1F**: Track 1 discretionary data  - **9F20**: Track 2 discretionary data  For captures, this field is required for contact EMV transactions. Otherwise, it is optional.  For credits, this field is required for contact EMV stand-alone credits and contactless EMV stand-alone credits. Otherwise, it is optional.  **Important** For contact EMV captures, contact EMV stand-alone credits, and contactless EMV stand-alone credits, you must include the following tags in this field. For all other types of EMV transactions, the following tags are optional.   - **95**: Terminal verification results  - **9F10**: Issuer application data  - **9F26**: Application cryptogram 

        :param tags: The tags of this PtsV2PaymentsPost201ResponsePointOfSaleInformationEmv.
        :type: str
        """
        if tags is not None and len(tags) > 1998:
            raise ValueError("Invalid value for `tags`, length must be less than or equal to `1998`")

        self._tags = tags

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
        if not isinstance(other, PtsV2PaymentsPost201ResponsePointOfSaleInformationEmv):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
