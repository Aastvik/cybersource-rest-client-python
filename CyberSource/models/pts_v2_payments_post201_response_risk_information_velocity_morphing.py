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


class PtsV2PaymentsPost201ResponseRiskInformationVelocityMorphing(object):
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
        'count': 'int',
        'field_name': 'str',
        'information_code': 'str'
    }

    attribute_map = {
        'count': 'count',
        'field_name': 'fieldName',
        'information_code': 'informationCode'
    }

    def __init__(self, count=None, field_name=None, information_code=None):
        """
        PtsV2PaymentsPost201ResponseRiskInformationVelocityMorphing - a model defined in Swagger
        """

        self._count = None
        self._field_name = None
        self._information_code = None

        if count is not None:
          self.count = count
        if field_name is not None:
          self.field_name = field_name
        if information_code is not None:
          self.information_code = information_code

    @property
    def count(self):
        """
        Gets the count of this PtsV2PaymentsPost201ResponseRiskInformationVelocityMorphing.
        Morphing count specified by the number #.  **Note** The count is not returned for the initial transaction. 

        :return: The count of this PtsV2PaymentsPost201ResponseRiskInformationVelocityMorphing.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this PtsV2PaymentsPost201ResponseRiskInformationVelocityMorphing.
        Morphing count specified by the number #.  **Note** The count is not returned for the initial transaction. 

        :param count: The count of this PtsV2PaymentsPost201ResponseRiskInformationVelocityMorphing.
        :type: int
        """

        self._count = count

    @property
    def field_name(self):
        """
        Gets the field_name of this PtsV2PaymentsPost201ResponseRiskInformationVelocityMorphing.
        Field name of the morphing element. specified by the setting that you chose in the Velocity Editor.  For all possible values, see the `decisionReply_morphingElement_#_fieldName` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :return: The field_name of this PtsV2PaymentsPost201ResponseRiskInformationVelocityMorphing.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this PtsV2PaymentsPost201ResponseRiskInformationVelocityMorphing.
        Field name of the morphing element. specified by the setting that you chose in the Velocity Editor.  For all possible values, see the `decisionReply_morphingElement_#_fieldName` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** > **Documentation** > **Guides** > _Decision Manager Using the SCMP API Developer Guide_ (PDF link). 

        :param field_name: The field_name of this PtsV2PaymentsPost201ResponseRiskInformationVelocityMorphing.
        :type: str
        """

        self._field_name = field_name

    @property
    def information_code(self):
        """
        Gets the information_code of this PtsV2PaymentsPost201ResponseRiskInformationVelocityMorphing.
        Identifier that CyberSource assigned to the velocity rule specified by the number #.  For all possible values, see the `decision_velocity_morphing_#_info_code` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** >  

        :return: The information_code of this PtsV2PaymentsPost201ResponseRiskInformationVelocityMorphing.
        :rtype: str
        """
        return self._information_code

    @information_code.setter
    def information_code(self, information_code):
        """
        Sets the information_code of this PtsV2PaymentsPost201ResponseRiskInformationVelocityMorphing.
        Identifier that CyberSource assigned to the velocity rule specified by the number #.  For all possible values, see the `decision_velocity_morphing_#_info_code` field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** >  

        :param information_code: The information_code of this PtsV2PaymentsPost201ResponseRiskInformationVelocityMorphing.
        :type: str
        """

        self._information_code = information_code

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
        if not isinstance(other, PtsV2PaymentsPost201ResponseRiskInformationVelocityMorphing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
