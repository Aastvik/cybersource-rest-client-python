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


class V1FileDetailsGet200ResponseFileDetails(object):
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
        'file_id': 'str',
        'name': 'str',
        'created_time': 'datetime',
        'last_modified_time': 'datetime',
        'date': 'date',
        'mime_type': 'str',
        'size': 'int'
    }

    attribute_map = {
        'file_id': 'fileId',
        'name': 'name',
        'created_time': 'createdTime',
        'last_modified_time': 'lastModifiedTime',
        'date': 'date',
        'mime_type': 'mimeType',
        'size': 'size'
    }

    def __init__(self, file_id=None, name=None, created_time=None, last_modified_time=None, date=None, mime_type=None, size=None):
        """
        V1FileDetailsGet200ResponseFileDetails - a model defined in Swagger
        """

        self._file_id = None
        self._name = None
        self._created_time = None
        self._last_modified_time = None
        self._date = None
        self._mime_type = None
        self._size = None

        if file_id is not None:
          self.file_id = file_id
        if name is not None:
          self.name = name
        if created_time is not None:
          self.created_time = created_time
        if last_modified_time is not None:
          self.last_modified_time = last_modified_time
        if date is not None:
          self.date = date
        if mime_type is not None:
          self.mime_type = mime_type
        if size is not None:
          self.size = size

    @property
    def file_id(self):
        """
        Gets the file_id of this V1FileDetailsGet200ResponseFileDetails.
        Unique identifier of a file

        :return: The file_id of this V1FileDetailsGet200ResponseFileDetails.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """
        Sets the file_id of this V1FileDetailsGet200ResponseFileDetails.
        Unique identifier of a file

        :param file_id: The file_id of this V1FileDetailsGet200ResponseFileDetails.
        :type: str
        """

        self._file_id = file_id

    @property
    def name(self):
        """
        Gets the name of this V1FileDetailsGet200ResponseFileDetails.
        Name of the file

        :return: The name of this V1FileDetailsGet200ResponseFileDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1FileDetailsGet200ResponseFileDetails.
        Name of the file

        :param name: The name of this V1FileDetailsGet200ResponseFileDetails.
        :type: str
        """

        self._name = name

    @property
    def created_time(self):
        """
        Gets the created_time of this V1FileDetailsGet200ResponseFileDetails.
        Date and time for the file in PST

        :return: The created_time of this V1FileDetailsGet200ResponseFileDetails.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """
        Sets the created_time of this V1FileDetailsGet200ResponseFileDetails.
        Date and time for the file in PST

        :param created_time: The created_time of this V1FileDetailsGet200ResponseFileDetails.
        :type: datetime
        """

        self._created_time = created_time

    @property
    def last_modified_time(self):
        """
        Gets the last_modified_time of this V1FileDetailsGet200ResponseFileDetails.
        Date and time for the file in PST

        :return: The last_modified_time of this V1FileDetailsGet200ResponseFileDetails.
        :rtype: datetime
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """
        Sets the last_modified_time of this V1FileDetailsGet200ResponseFileDetails.
        Date and time for the file in PST

        :param last_modified_time: The last_modified_time of this V1FileDetailsGet200ResponseFileDetails.
        :type: datetime
        """

        self._last_modified_time = last_modified_time

    @property
    def date(self):
        """
        Gets the date of this V1FileDetailsGet200ResponseFileDetails.
        Date and time for the file in PST

        :return: The date of this V1FileDetailsGet200ResponseFileDetails.
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this V1FileDetailsGet200ResponseFileDetails.
        Date and time for the file in PST

        :param date: The date of this V1FileDetailsGet200ResponseFileDetails.
        :type: date
        """

        self._date = date

    @property
    def mime_type(self):
        """
        Gets the mime_type of this V1FileDetailsGet200ResponseFileDetails.
        File extension

        :return: The mime_type of this V1FileDetailsGet200ResponseFileDetails.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """
        Sets the mime_type of this V1FileDetailsGet200ResponseFileDetails.
        File extension

        :param mime_type: The mime_type of this V1FileDetailsGet200ResponseFileDetails.
        :type: str
        """
        allowed_values = ["application/xml", "text/csv", "application/pdf", "application/octet-stream"]
        if mime_type not in allowed_values:
            raise ValueError(
                "Invalid value for `mime_type` ({0}), must be one of {1}"
                .format(mime_type, allowed_values)
            )

        self._mime_type = mime_type

    @property
    def size(self):
        """
        Gets the size of this V1FileDetailsGet200ResponseFileDetails.
        Size of the file in bytes

        :return: The size of this V1FileDetailsGet200ResponseFileDetails.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this V1FileDetailsGet200ResponseFileDetails.
        Size of the file in bytes

        :param size: The size of this V1FileDetailsGet200ResponseFileDetails.
        :type: int
        """

        self._size = size

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
        if not isinstance(other, V1FileDetailsGet200ResponseFileDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
