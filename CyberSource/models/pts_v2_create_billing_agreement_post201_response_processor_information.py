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


class PtsV2CreateBillingAgreementPost201ResponseProcessorInformation(object):
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
        'approval_code': 'str',
        'response_code': 'str',
        'transaction_id': 'str',
        'response_details': 'str',
        'reason_code': 'str'
    }

    attribute_map = {
        'approval_code': 'approvalCode',
        'response_code': 'responseCode',
        'transaction_id': 'transactionId',
        'response_details': 'responseDetails',
        'reason_code': 'reasonCode'
    }

    def __init__(self, approval_code=None, response_code=None, transaction_id=None, response_details=None, reason_code=None):
        """
        PtsV2CreateBillingAgreementPost201ResponseProcessorInformation - a model defined in Swagger
        """

        self._approval_code = None
        self._response_code = None
        self._transaction_id = None
        self._response_details = None
        self._reason_code = None

        if approval_code is not None:
          self.approval_code = approval_code
        if response_code is not None:
          self.response_code = response_code
        if transaction_id is not None:
          self.transaction_id = transaction_id
        if response_details is not None:
          self.response_details = response_details
        if reason_code is not None:
          self.reason_code = reason_code

    @property
    def approval_code(self):
        """
        Gets the approval_code of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        Authorization code. Returned only when the processor returns this value.  The length of this value depends on your processor.  Returned by authorization service.  #### PIN debit Authorization code that is returned by the processor.  Returned by PIN debit credit.  #### Elavon Encrypted Account Number Program The returned value is OFFLINE.  #### TSYS Acquiring Solutions The returned value for a successful zero amount authorization is 000000. 

        :return: The approval_code of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        :rtype: str
        """
        return self._approval_code

    @approval_code.setter
    def approval_code(self, approval_code):
        """
        Sets the approval_code of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        Authorization code. Returned only when the processor returns this value.  The length of this value depends on your processor.  Returned by authorization service.  #### PIN debit Authorization code that is returned by the processor.  Returned by PIN debit credit.  #### Elavon Encrypted Account Number Program The returned value is OFFLINE.  #### TSYS Acquiring Solutions The returned value for a successful zero amount authorization is 000000. 

        :param approval_code: The approval_code of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        :type: str
        """

        self._approval_code = approval_code

    @property
    def response_code(self):
        """
        Gets the response_code of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        For most processors, this is the error message sent directly from the bank. Returned only when the processor returns this value.  **Important** Do not use this field to evaluate the result of the authorization. #### SEPA/BACS Response code from the processor. Possible values: 00000–99999. See Appendix C, \"Reason Codes and Processor Response Codes,\" on page 42.  #### PIN debit Response value that is returned by the processor or bank. **Important** Do not use this field to evaluate the results of the transaction request.  Returned by PIN debit credit, PIN debit purchase, and PIN debit reversal.  #### AIBMS If this value is `08`, you can accept the transaction if the customer provides you with identification.  #### Atos This value is the response code sent from Atos and it might also include the response code from the bank. Format: `aa,bb` with the two values separated by a comma and where: - `aa` is the two-digit error message from Atos. - `bb` is the optional two-digit error message from the bank.  #### Comercio Latino This value is the status code and the error or response code received from the processor separated by a colon. Format: [status code]:E[error code] or [status code]:R[response code] Example `2:R06`  #### JCN Gateway Processor-defined detail error code. The associated response category code is in the `processorInformation.responseCategoryCode` field. String (3) 

        :return: The response_code of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        For most processors, this is the error message sent directly from the bank. Returned only when the processor returns this value.  **Important** Do not use this field to evaluate the result of the authorization. #### SEPA/BACS Response code from the processor. Possible values: 00000–99999. See Appendix C, \"Reason Codes and Processor Response Codes,\" on page 42.  #### PIN debit Response value that is returned by the processor or bank. **Important** Do not use this field to evaluate the results of the transaction request.  Returned by PIN debit credit, PIN debit purchase, and PIN debit reversal.  #### AIBMS If this value is `08`, you can accept the transaction if the customer provides you with identification.  #### Atos This value is the response code sent from Atos and it might also include the response code from the bank. Format: `aa,bb` with the two values separated by a comma and where: - `aa` is the two-digit error message from Atos. - `bb` is the optional two-digit error message from the bank.  #### Comercio Latino This value is the status code and the error or response code received from the processor separated by a colon. Format: [status code]:E[error code] or [status code]:R[response code] Example `2:R06`  #### JCN Gateway Processor-defined detail error code. The associated response category code is in the `processorInformation.responseCategoryCode` field. String (3) 

        :param response_code: The response_code of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        :type: str
        """

        self._response_code = response_code

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        Transaction ID assigned by the processor. 

        :return: The transaction_id of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        Transaction ID assigned by the processor. 

        :param transaction_id: The transaction_id of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def response_details(self):
        """
        Gets the response_details of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        Response code indicating that creating the agreement failed 

        :return: The response_details of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        :rtype: str
        """
        return self._response_details

    @response_details.setter
    def response_details(self, response_details):
        """
        Sets the response_details of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        Response code indicating that creating the agreement failed 

        :param response_details: The response_details of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        :type: str
        """

        self._response_details = response_details

    @property
    def reason_code(self):
        """
        Gets the reason_code of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        Numeric value corresponding to the result of the request. 

        :return: The reason_code of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """
        Sets the reason_code of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        Numeric value corresponding to the result of the request. 

        :param reason_code: The reason_code of this PtsV2CreateBillingAgreementPost201ResponseProcessorInformation.
        :type: str
        """

        self._reason_code = reason_code

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
        if not isinstance(other, PtsV2CreateBillingAgreementPost201ResponseProcessorInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
