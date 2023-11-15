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


class CreateWebhook(object):
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
        'name': 'str',
        'description': 'str',
        'organization_id': 'str',
        'product_id': 'str',
        'event_types': 'list[str]',
        'webhook_url': 'str',
        'health_check_url': 'str',
        'notification_scope': 'str',
        'retry_policy': 'Notificationsubscriptionsv1webhooksRetryPolicy',
        'security_policy': 'Notificationsubscriptionsv1webhooksSecurityPolicy1'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'organization_id': 'organizationId',
        'product_id': 'productId',
        'event_types': 'eventTypes',
        'webhook_url': 'webhookUrl',
        'health_check_url': 'healthCheckUrl',
        'notification_scope': 'notificationScope',
        'retry_policy': 'retryPolicy',
        'security_policy': 'securityPolicy'
    }

    def __init__(self, name=None, description=None, organization_id=None, product_id=None, event_types=None, webhook_url=None, health_check_url=None, notification_scope=None, retry_policy=None, security_policy=None):
        """
        CreateWebhook - a model defined in Swagger
        """

        self._name = None
        self._description = None
        self._organization_id = None
        self._product_id = None
        self._event_types = None
        self._webhook_url = None
        self._health_check_url = None
        self._notification_scope = None
        self._retry_policy = None
        self._security_policy = None

        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if organization_id is not None:
          self.organization_id = organization_id
        if product_id is not None:
          self.product_id = product_id
        if event_types is not None:
          self.event_types = event_types
        if webhook_url is not None:
          self.webhook_url = webhook_url
        if health_check_url is not None:
          self.health_check_url = health_check_url
        if notification_scope is not None:
          self.notification_scope = notification_scope
        if retry_policy is not None:
          self.retry_policy = retry_policy
        if security_policy is not None:
          self.security_policy = security_policy

    @property
    def name(self):
        """
        Gets the name of this CreateWebhook.
        Client friendly webhook name.

        :return: The name of this CreateWebhook.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateWebhook.
        Client friendly webhook name.

        :param name: The name of this CreateWebhook.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateWebhook.
        Client friendly webhook description.

        :return: The description of this CreateWebhook.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateWebhook.
        Client friendly webhook description.

        :param description: The description of this CreateWebhook.
        :type: str
        """

        self._description = description

    @property
    def organization_id(self):
        """
        Gets the organization_id of this CreateWebhook.
        Organization Identifier (OrgId) or Merchant Identifier (MID).

        :return: The organization_id of this CreateWebhook.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """
        Sets the organization_id of this CreateWebhook.
        Organization Identifier (OrgId) or Merchant Identifier (MID).

        :param organization_id: The organization_id of this CreateWebhook.
        :type: str
        """

        self._organization_id = organization_id

    @property
    def product_id(self):
        """
        Gets the product_id of this CreateWebhook.
        To see the valid productId and eventTypes, call the \"Create and Manage Webhooks - Retrieve a list of event types\" endpoint.

        :return: The product_id of this CreateWebhook.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this CreateWebhook.
        To see the valid productId and eventTypes, call the \"Create and Manage Webhooks - Retrieve a list of event types\" endpoint.

        :param product_id: The product_id of this CreateWebhook.
        :type: str
        """

        self._product_id = product_id

    @property
    def event_types(self):
        """
        Gets the event_types of this CreateWebhook.
        Array of the different events for a given product id.

        :return: The event_types of this CreateWebhook.
        :rtype: list[str]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        """
        Sets the event_types of this CreateWebhook.
        Array of the different events for a given product id.

        :param event_types: The event_types of this CreateWebhook.
        :type: list[str]
        """

        self._event_types = event_types

    @property
    def webhook_url(self):
        """
        Gets the webhook_url of this CreateWebhook.
        The client's endpoint (URL) to receive webhooks.

        :return: The webhook_url of this CreateWebhook.
        :rtype: str
        """
        return self._webhook_url

    @webhook_url.setter
    def webhook_url(self, webhook_url):
        """
        Sets the webhook_url of this CreateWebhook.
        The client's endpoint (URL) to receive webhooks.

        :param webhook_url: The webhook_url of this CreateWebhook.
        :type: str
        """

        self._webhook_url = webhook_url

    @property
    def health_check_url(self):
        """
        Gets the health_check_url of this CreateWebhook.
        The client's health check endpoint (URL). This should be as close as possible to the actual webhookUrl. If the user does not provide the health check URL, it is the user's responsibility to re-activate the webhook if it is deactivated by calling the test endpoint. 

        :return: The health_check_url of this CreateWebhook.
        :rtype: str
        """
        return self._health_check_url

    @health_check_url.setter
    def health_check_url(self, health_check_url):
        """
        Sets the health_check_url of this CreateWebhook.
        The client's health check endpoint (URL). This should be as close as possible to the actual webhookUrl. If the user does not provide the health check URL, it is the user's responsibility to re-activate the webhook if it is deactivated by calling the test endpoint. 

        :param health_check_url: The health_check_url of this CreateWebhook.
        :type: str
        """

        self._health_check_url = health_check_url

    @property
    def notification_scope(self):
        """
        Gets the notification_scope of this CreateWebhook.
        The webhook scope. 1. SELF The Webhook is used to deliver webhooks for only this Organization (or Merchant). 2. DESCENDANTS The Webhook is used to deliver webhooks for this Organization and its children. 3. CUSTOM The Webhook is used to deliver webhooks for the OrgIds (or MiDs) explicitly listed in scopeData field. 

        :return: The notification_scope of this CreateWebhook.
        :rtype: str
        """
        return self._notification_scope

    @notification_scope.setter
    def notification_scope(self, notification_scope):
        """
        Sets the notification_scope of this CreateWebhook.
        The webhook scope. 1. SELF The Webhook is used to deliver webhooks for only this Organization (or Merchant). 2. DESCENDANTS The Webhook is used to deliver webhooks for this Organization and its children. 3. CUSTOM The Webhook is used to deliver webhooks for the OrgIds (or MiDs) explicitly listed in scopeData field. 

        :param notification_scope: The notification_scope of this CreateWebhook.
        :type: str
        """

        self._notification_scope = notification_scope

    @property
    def retry_policy(self):
        """
        Gets the retry_policy of this CreateWebhook.

        :return: The retry_policy of this CreateWebhook.
        :rtype: Notificationsubscriptionsv1webhooksRetryPolicy
        """
        return self._retry_policy

    @retry_policy.setter
    def retry_policy(self, retry_policy):
        """
        Sets the retry_policy of this CreateWebhook.

        :param retry_policy: The retry_policy of this CreateWebhook.
        :type: Notificationsubscriptionsv1webhooksRetryPolicy
        """

        self._retry_policy = retry_policy

    @property
    def security_policy(self):
        """
        Gets the security_policy of this CreateWebhook.

        :return: The security_policy of this CreateWebhook.
        :rtype: Notificationsubscriptionsv1webhooksSecurityPolicy1
        """
        return self._security_policy

    @security_policy.setter
    def security_policy(self, security_policy):
        """
        Sets the security_policy of this CreateWebhook.

        :param security_policy: The security_policy of this CreateWebhook.
        :type: Notificationsubscriptionsv1webhooksSecurityPolicy1
        """

        self._security_policy = security_policy

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
        if not isinstance(other, CreateWebhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
