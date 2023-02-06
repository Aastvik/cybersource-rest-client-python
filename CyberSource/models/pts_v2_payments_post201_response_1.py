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


class PtsV2PaymentsPost201Response1(object):
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
        'id': 'str',
        'status': 'str',
        'submit_time_utc': 'str',
        'processor_information': 'PtsV2PaymentsPost201Response1ProcessorInformation',
        'reconciliation_id': 'str',
        'payment_information': 'PtsV2PaymentsPost201Response1PaymentInformation',
        'order_information': 'PtsV2PaymentsPost201Response1OrderInformation',
        'client_reference_information': 'PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'submit_time_utc': 'submitTimeUtc',
        'processor_information': 'processorInformation',
        'reconciliation_id': 'reconciliationId',
        'payment_information': 'paymentInformation',
        'order_information': 'orderInformation',
        'client_reference_information': 'clientReferenceInformation'
    }

    def __init__(self, id=None, status=None, submit_time_utc=None, processor_information=None, reconciliation_id=None, payment_information=None, order_information=None, client_reference_information=None):
        """
        PtsV2PaymentsPost201Response1 - a model defined in Swagger
        """

        self._id = None
        self._status = None
        self._submit_time_utc = None
        self._processor_information = None
        self._reconciliation_id = None
        self._payment_information = None
        self._order_information = None
        self._client_reference_information = None

        if id is not None:
          self.id = id
        if status is not None:
          self.status = status
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if processor_information is not None:
          self.processor_information = processor_information
        if reconciliation_id is not None:
          self.reconciliation_id = reconciliation_id
        if payment_information is not None:
          self.payment_information = payment_information
        if order_information is not None:
          self.order_information = order_information
        if client_reference_information is not None:
          self.client_reference_information = client_reference_information

    @property
    def id(self):
        """
        Gets the id of this PtsV2PaymentsPost201Response1.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :return: The id of this PtsV2PaymentsPost201Response1.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PtsV2PaymentsPost201Response1.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :param id: The id of this PtsV2PaymentsPost201Response1.
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """
        Gets the status of this PtsV2PaymentsPost201Response1.
        The status of the submitted transaction.  Possible values:  - AUTHORIZED  - PARTIAL_AUTHORIZED  - AUTHORIZED_PENDING_REVIEW  - AUTHORIZED_RISK_DECLINED  - PENDING_AUTHENTICATION  - PENDING_REVIEW  - DECLINED  - INVALID_REQUEST 

        :return: The status of this PtsV2PaymentsPost201Response1.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PtsV2PaymentsPost201Response1.
        The status of the submitted transaction.  Possible values:  - AUTHORIZED  - PARTIAL_AUTHORIZED  - AUTHORIZED_PENDING_REVIEW  - AUTHORIZED_RISK_DECLINED  - PENDING_AUTHENTICATION  - PENDING_REVIEW  - DECLINED  - INVALID_REQUEST 

        :param status: The status of this PtsV2PaymentsPost201Response1.
        :type: str
        """

        self._status = status

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this PtsV2PaymentsPost201Response1.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :return: The submit_time_utc of this PtsV2PaymentsPost201Response1.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this PtsV2PaymentsPost201Response1.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :param submit_time_utc: The submit_time_utc of this PtsV2PaymentsPost201Response1.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

    @property
    def processor_information(self):
        """
        Gets the processor_information of this PtsV2PaymentsPost201Response1.

        :return: The processor_information of this PtsV2PaymentsPost201Response1.
        :rtype: PtsV2PaymentsPost201Response1ProcessorInformation
        """
        return self._processor_information

    @processor_information.setter
    def processor_information(self, processor_information):
        """
        Sets the processor_information of this PtsV2PaymentsPost201Response1.

        :param processor_information: The processor_information of this PtsV2PaymentsPost201Response1.
        :type: PtsV2PaymentsPost201Response1ProcessorInformation
        """

        self._processor_information = processor_information

    @property
    def reconciliation_id(self):
        """
        Gets the reconciliation_id of this PtsV2PaymentsPost201Response1.
        Reference number for the transaction. Depending on how your Cybersource account is configured, this value could either be provided in the API request or generated by CyberSource. The actual value used in the request to the processor is provided back to you by Cybersource in the response. 

        :return: The reconciliation_id of this PtsV2PaymentsPost201Response1.
        :rtype: str
        """
        return self._reconciliation_id

    @reconciliation_id.setter
    def reconciliation_id(self, reconciliation_id):
        """
        Sets the reconciliation_id of this PtsV2PaymentsPost201Response1.
        Reference number for the transaction. Depending on how your Cybersource account is configured, this value could either be provided in the API request or generated by CyberSource. The actual value used in the request to the processor is provided back to you by Cybersource in the response. 

        :param reconciliation_id: The reconciliation_id of this PtsV2PaymentsPost201Response1.
        :type: str
        """

        self._reconciliation_id = reconciliation_id

    @property
    def payment_information(self):
        """
        Gets the payment_information of this PtsV2PaymentsPost201Response1.

        :return: The payment_information of this PtsV2PaymentsPost201Response1.
        :rtype: PtsV2PaymentsPost201Response1PaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this PtsV2PaymentsPost201Response1.

        :param payment_information: The payment_information of this PtsV2PaymentsPost201Response1.
        :type: PtsV2PaymentsPost201Response1PaymentInformation
        """

        self._payment_information = payment_information

    @property
    def order_information(self):
        """
        Gets the order_information of this PtsV2PaymentsPost201Response1.

        :return: The order_information of this PtsV2PaymentsPost201Response1.
        :rtype: PtsV2PaymentsPost201Response1OrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this PtsV2PaymentsPost201Response1.

        :param order_information: The order_information of this PtsV2PaymentsPost201Response1.
        :type: PtsV2PaymentsPost201Response1OrderInformation
        """

        self._order_information = order_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this PtsV2PaymentsPost201Response1.

        :return: The client_reference_information of this PtsV2PaymentsPost201Response1.
        :rtype: PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this PtsV2PaymentsPost201Response1.

        :param client_reference_information: The client_reference_information of this PtsV2PaymentsPost201Response1.
        :type: PtsV2IncrementalAuthorizationPatch201ResponseClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

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
        if not isinstance(other, PtsV2PaymentsPost201Response1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
