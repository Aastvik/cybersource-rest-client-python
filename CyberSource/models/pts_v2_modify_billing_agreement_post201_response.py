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


class PtsV2ModifyBillingAgreementPost201Response(object):
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
        'links': 'PtsV2ModifyBillingAgreementPost201ResponseLinks',
        'id': 'str',
        'submit_time_utc': 'str',
        'status': 'str',
        'processor_information': 'PtsV2CreateBillingAgreementPost201ResponseProcessorInformation',
        'installment_information': 'PtsV2CreateBillingAgreementPost201ResponseInstallmentInformation',
        'client_reference_information': 'PtsV2CreateBillingAgreementPost201ResponseClientReferenceInformation',
        'risk_information': 'PtsV2CreateBillingAgreementPost201ResponseRiskInformation',
        'agreement_information': 'PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation',
        'order_information': 'PtsV2ModifyBillingAgreementPost201ResponseOrderInformation',
        'payment_information': 'PtsV2ModifyBillingAgreementPost201ResponsePaymentInformation'
    }

    attribute_map = {
        'links': '_links',
        'id': 'id',
        'submit_time_utc': 'submitTimeUtc',
        'status': 'status',
        'processor_information': 'processorInformation',
        'installment_information': 'installmentInformation',
        'client_reference_information': 'clientReferenceInformation',
        'risk_information': 'riskInformation',
        'agreement_information': 'agreementInformation',
        'order_information': 'orderInformation',
        'payment_information': 'paymentInformation'
    }

    def __init__(self, links=None, id=None, submit_time_utc=None, status=None, processor_information=None, installment_information=None, client_reference_information=None, risk_information=None, agreement_information=None, order_information=None, payment_information=None):
        """
        PtsV2ModifyBillingAgreementPost201Response - a model defined in Swagger
        """

        self._links = None
        self._id = None
        self._submit_time_utc = None
        self._status = None
        self._processor_information = None
        self._installment_information = None
        self._client_reference_information = None
        self._risk_information = None
        self._agreement_information = None
        self._order_information = None
        self._payment_information = None

        if links is not None:
          self.links = links
        if id is not None:
          self.id = id
        if submit_time_utc is not None:
          self.submit_time_utc = submit_time_utc
        if status is not None:
          self.status = status
        if processor_information is not None:
          self.processor_information = processor_information
        if installment_information is not None:
          self.installment_information = installment_information
        if client_reference_information is not None:
          self.client_reference_information = client_reference_information
        if risk_information is not None:
          self.risk_information = risk_information
        if agreement_information is not None:
          self.agreement_information = agreement_information
        if order_information is not None:
          self.order_information = order_information
        if payment_information is not None:
          self.payment_information = payment_information

    @property
    def links(self):
        """
        Gets the links of this PtsV2ModifyBillingAgreementPost201Response.

        :return: The links of this PtsV2ModifyBillingAgreementPost201Response.
        :rtype: PtsV2ModifyBillingAgreementPost201ResponseLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this PtsV2ModifyBillingAgreementPost201Response.

        :param links: The links of this PtsV2ModifyBillingAgreementPost201Response.
        :type: PtsV2ModifyBillingAgreementPost201ResponseLinks
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this PtsV2ModifyBillingAgreementPost201Response.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :return: The id of this PtsV2ModifyBillingAgreementPost201Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PtsV2ModifyBillingAgreementPost201Response.
        An unique identification number generated by Cybersource to identify the submitted request. Returned by all services. It is also appended to the endpoint of the resource. On incremental authorizations, this value with be the same as the identification number returned in the original authorization response. 

        :param id: The id of this PtsV2ModifyBillingAgreementPost201Response.
        :type: str
        """

        self._id = id

    @property
    def submit_time_utc(self):
        """
        Gets the submit_time_utc of this PtsV2ModifyBillingAgreementPost201Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :return: The submit_time_utc of this PtsV2ModifyBillingAgreementPost201Response.
        :rtype: str
        """
        return self._submit_time_utc

    @submit_time_utc.setter
    def submit_time_utc(self, submit_time_utc):
        """
        Sets the submit_time_utc of this PtsV2ModifyBillingAgreementPost201Response.
        Time of request in UTC. Format: `YYYY-MM-DDThh:mm:ssZ` **Example** `2016-08-11T22:47:57Z` equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The `T` separates the date and the time. The `Z` indicates UTC.  Returned by Cybersource for all services. 

        :param submit_time_utc: The submit_time_utc of this PtsV2ModifyBillingAgreementPost201Response.
        :type: str
        """

        self._submit_time_utc = submit_time_utc

    @property
    def status(self):
        """
        Gets the status of this PtsV2ModifyBillingAgreementPost201Response.
        The status of the billing agreement. Possible value is:   - PENDING   - REVOKED   - ACTIVE   - FAILED   - EXPIRED   - INACTIVE 

        :return: The status of this PtsV2ModifyBillingAgreementPost201Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PtsV2ModifyBillingAgreementPost201Response.
        The status of the billing agreement. Possible value is:   - PENDING   - REVOKED   - ACTIVE   - FAILED   - EXPIRED   - INACTIVE 

        :param status: The status of this PtsV2ModifyBillingAgreementPost201Response.
        :type: str
        """

        self._status = status

    @property
    def processor_information(self):
        """
        Gets the processor_information of this PtsV2ModifyBillingAgreementPost201Response.

        :return: The processor_information of this PtsV2ModifyBillingAgreementPost201Response.
        :rtype: PtsV2CreateBillingAgreementPost201ResponseProcessorInformation
        """
        return self._processor_information

    @processor_information.setter
    def processor_information(self, processor_information):
        """
        Sets the processor_information of this PtsV2ModifyBillingAgreementPost201Response.

        :param processor_information: The processor_information of this PtsV2ModifyBillingAgreementPost201Response.
        :type: PtsV2CreateBillingAgreementPost201ResponseProcessorInformation
        """

        self._processor_information = processor_information

    @property
    def installment_information(self):
        """
        Gets the installment_information of this PtsV2ModifyBillingAgreementPost201Response.

        :return: The installment_information of this PtsV2ModifyBillingAgreementPost201Response.
        :rtype: PtsV2CreateBillingAgreementPost201ResponseInstallmentInformation
        """
        return self._installment_information

    @installment_information.setter
    def installment_information(self, installment_information):
        """
        Sets the installment_information of this PtsV2ModifyBillingAgreementPost201Response.

        :param installment_information: The installment_information of this PtsV2ModifyBillingAgreementPost201Response.
        :type: PtsV2CreateBillingAgreementPost201ResponseInstallmentInformation
        """

        self._installment_information = installment_information

    @property
    def client_reference_information(self):
        """
        Gets the client_reference_information of this PtsV2ModifyBillingAgreementPost201Response.

        :return: The client_reference_information of this PtsV2ModifyBillingAgreementPost201Response.
        :rtype: PtsV2CreateBillingAgreementPost201ResponseClientReferenceInformation
        """
        return self._client_reference_information

    @client_reference_information.setter
    def client_reference_information(self, client_reference_information):
        """
        Sets the client_reference_information of this PtsV2ModifyBillingAgreementPost201Response.

        :param client_reference_information: The client_reference_information of this PtsV2ModifyBillingAgreementPost201Response.
        :type: PtsV2CreateBillingAgreementPost201ResponseClientReferenceInformation
        """

        self._client_reference_information = client_reference_information

    @property
    def risk_information(self):
        """
        Gets the risk_information of this PtsV2ModifyBillingAgreementPost201Response.

        :return: The risk_information of this PtsV2ModifyBillingAgreementPost201Response.
        :rtype: PtsV2CreateBillingAgreementPost201ResponseRiskInformation
        """
        return self._risk_information

    @risk_information.setter
    def risk_information(self, risk_information):
        """
        Sets the risk_information of this PtsV2ModifyBillingAgreementPost201Response.

        :param risk_information: The risk_information of this PtsV2ModifyBillingAgreementPost201Response.
        :type: PtsV2CreateBillingAgreementPost201ResponseRiskInformation
        """

        self._risk_information = risk_information

    @property
    def agreement_information(self):
        """
        Gets the agreement_information of this PtsV2ModifyBillingAgreementPost201Response.

        :return: The agreement_information of this PtsV2ModifyBillingAgreementPost201Response.
        :rtype: PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation
        """
        return self._agreement_information

    @agreement_information.setter
    def agreement_information(self, agreement_information):
        """
        Sets the agreement_information of this PtsV2ModifyBillingAgreementPost201Response.

        :param agreement_information: The agreement_information of this PtsV2ModifyBillingAgreementPost201Response.
        :type: PtsV2ModifyBillingAgreementPost201ResponseAgreementInformation
        """

        self._agreement_information = agreement_information

    @property
    def order_information(self):
        """
        Gets the order_information of this PtsV2ModifyBillingAgreementPost201Response.

        :return: The order_information of this PtsV2ModifyBillingAgreementPost201Response.
        :rtype: PtsV2ModifyBillingAgreementPost201ResponseOrderInformation
        """
        return self._order_information

    @order_information.setter
    def order_information(self, order_information):
        """
        Sets the order_information of this PtsV2ModifyBillingAgreementPost201Response.

        :param order_information: The order_information of this PtsV2ModifyBillingAgreementPost201Response.
        :type: PtsV2ModifyBillingAgreementPost201ResponseOrderInformation
        """

        self._order_information = order_information

    @property
    def payment_information(self):
        """
        Gets the payment_information of this PtsV2ModifyBillingAgreementPost201Response.

        :return: The payment_information of this PtsV2ModifyBillingAgreementPost201Response.
        :rtype: PtsV2ModifyBillingAgreementPost201ResponsePaymentInformation
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """
        Sets the payment_information of this PtsV2ModifyBillingAgreementPost201Response.

        :param payment_information: The payment_information of this PtsV2ModifyBillingAgreementPost201Response.
        :type: PtsV2ModifyBillingAgreementPost201ResponsePaymentInformation
        """

        self._payment_information = payment_information

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
        if not isinstance(other, PtsV2ModifyBillingAgreementPost201Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
