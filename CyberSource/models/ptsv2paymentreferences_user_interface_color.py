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


class Ptsv2paymentreferencesUserInterfaceColor(object):
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
        'border': 'str',
        'border_selected': 'str',
        'button': 'str',
        'button_text': 'str',
        'checkbox': 'str',
        'checkbox_check_mark': 'str',
        'header': 'str',
        'link': 'str',
        'text': 'str'
    }

    attribute_map = {
        'border': 'border',
        'border_selected': 'borderSelected',
        'button': 'button',
        'button_text': 'buttonText',
        'checkbox': 'checkbox',
        'checkbox_check_mark': 'checkboxCheckMark',
        'header': 'header',
        'link': 'link',
        'text': 'text'
    }

    def __init__(self, border=None, border_selected=None, button=None, button_text=None, checkbox=None, checkbox_check_mark=None, header=None, link=None, text=None):
        """
        Ptsv2paymentreferencesUserInterfaceColor - a model defined in Swagger
        """

        self._border = None
        self._border_selected = None
        self._button = None
        self._button_text = None
        self._checkbox = None
        self._checkbox_check_mark = None
        self._header = None
        self._link = None
        self._text = None

        if border is not None:
          self.border = border
        if border_selected is not None:
          self.border_selected = border_selected
        if button is not None:
          self.button = button
        if button_text is not None:
          self.button_text = button_text
        if checkbox is not None:
          self.checkbox = checkbox
        if checkbox_check_mark is not None:
          self.checkbox_check_mark = checkbox_check_mark
        if header is not None:
          self.header = header
        if link is not None:
          self.link = link
        if text is not None:
          self.text = text

    @property
    def border(self):
        """
        Gets the border of this Ptsv2paymentreferencesUserInterfaceColor.
        Border Color 

        :return: The border of this Ptsv2paymentreferencesUserInterfaceColor.
        :rtype: str
        """
        return self._border

    @border.setter
    def border(self, border):
        """
        Sets the border of this Ptsv2paymentreferencesUserInterfaceColor.
        Border Color 

        :param border: The border of this Ptsv2paymentreferencesUserInterfaceColor.
        :type: str
        """

        self._border = border

    @property
    def border_selected(self):
        """
        Gets the border_selected of this Ptsv2paymentreferencesUserInterfaceColor.
        Selected Border Color 

        :return: The border_selected of this Ptsv2paymentreferencesUserInterfaceColor.
        :rtype: str
        """
        return self._border_selected

    @border_selected.setter
    def border_selected(self, border_selected):
        """
        Sets the border_selected of this Ptsv2paymentreferencesUserInterfaceColor.
        Selected Border Color 

        :param border_selected: The border_selected of this Ptsv2paymentreferencesUserInterfaceColor.
        :type: str
        """

        self._border_selected = border_selected

    @property
    def button(self):
        """
        Gets the button of this Ptsv2paymentreferencesUserInterfaceColor.
        Button Color 

        :return: The button of this Ptsv2paymentreferencesUserInterfaceColor.
        :rtype: str
        """
        return self._button

    @button.setter
    def button(self, button):
        """
        Sets the button of this Ptsv2paymentreferencesUserInterfaceColor.
        Button Color 

        :param button: The button of this Ptsv2paymentreferencesUserInterfaceColor.
        :type: str
        """

        self._button = button

    @property
    def button_text(self):
        """
        Gets the button_text of this Ptsv2paymentreferencesUserInterfaceColor.
        Button Text Color 

        :return: The button_text of this Ptsv2paymentreferencesUserInterfaceColor.
        :rtype: str
        """
        return self._button_text

    @button_text.setter
    def button_text(self, button_text):
        """
        Sets the button_text of this Ptsv2paymentreferencesUserInterfaceColor.
        Button Text Color 

        :param button_text: The button_text of this Ptsv2paymentreferencesUserInterfaceColor.
        :type: str
        """

        self._button_text = button_text

    @property
    def checkbox(self):
        """
        Gets the checkbox of this Ptsv2paymentreferencesUserInterfaceColor.
        Checkbox Color 

        :return: The checkbox of this Ptsv2paymentreferencesUserInterfaceColor.
        :rtype: str
        """
        return self._checkbox

    @checkbox.setter
    def checkbox(self, checkbox):
        """
        Sets the checkbox of this Ptsv2paymentreferencesUserInterfaceColor.
        Checkbox Color 

        :param checkbox: The checkbox of this Ptsv2paymentreferencesUserInterfaceColor.
        :type: str
        """

        self._checkbox = checkbox

    @property
    def checkbox_check_mark(self):
        """
        Gets the checkbox_check_mark of this Ptsv2paymentreferencesUserInterfaceColor.
        Checkbox Checkmark Color 

        :return: The checkbox_check_mark of this Ptsv2paymentreferencesUserInterfaceColor.
        :rtype: str
        """
        return self._checkbox_check_mark

    @checkbox_check_mark.setter
    def checkbox_check_mark(self, checkbox_check_mark):
        """
        Sets the checkbox_check_mark of this Ptsv2paymentreferencesUserInterfaceColor.
        Checkbox Checkmark Color 

        :param checkbox_check_mark: The checkbox_check_mark of this Ptsv2paymentreferencesUserInterfaceColor.
        :type: str
        """

        self._checkbox_check_mark = checkbox_check_mark

    @property
    def header(self):
        """
        Gets the header of this Ptsv2paymentreferencesUserInterfaceColor.
        Header Color 

        :return: The header of this Ptsv2paymentreferencesUserInterfaceColor.
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """
        Sets the header of this Ptsv2paymentreferencesUserInterfaceColor.
        Header Color 

        :param header: The header of this Ptsv2paymentreferencesUserInterfaceColor.
        :type: str
        """

        self._header = header

    @property
    def link(self):
        """
        Gets the link of this Ptsv2paymentreferencesUserInterfaceColor.
        Link Color 

        :return: The link of this Ptsv2paymentreferencesUserInterfaceColor.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """
        Sets the link of this Ptsv2paymentreferencesUserInterfaceColor.
        Link Color 

        :param link: The link of this Ptsv2paymentreferencesUserInterfaceColor.
        :type: str
        """

        self._link = link

    @property
    def text(self):
        """
        Gets the text of this Ptsv2paymentreferencesUserInterfaceColor.
        Text Color 

        :return: The text of this Ptsv2paymentreferencesUserInterfaceColor.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this Ptsv2paymentreferencesUserInterfaceColor.
        Text Color 

        :param text: The text of this Ptsv2paymentreferencesUserInterfaceColor.
        :type: str
        """

        self._text = text

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
        if not isinstance(other, Ptsv2paymentreferencesUserInterfaceColor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
