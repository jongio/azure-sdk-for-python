# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.operations import Operations
from .operations.signal_roperations import SignalROperations
from .operations.usages_operations import UsagesOperations
from . import models


class SignalRManagementClientConfiguration(AzureConfiguration):
    """Configuration for SignalRManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription Id which uniquely identify the
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(SignalRManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-signalr/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class SignalRManagementClient(SDKClient):
    """REST API for Azure SignalR Service

    :ivar config: Configuration for client.
    :vartype config: SignalRManagementClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.signalr.operations.Operations
    :ivar signal_r: SignalR operations
    :vartype signal_r: azure.mgmt.signalr.operations.SignalROperations
    :ivar usages: Usages operations
    :vartype usages: azure.mgmt.signalr.operations.UsagesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription Id which uniquely identify the
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = SignalRManagementClientConfiguration(credentials, subscription_id, base_url)
        super(SignalRManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-03-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.signal_r = SignalROperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self.config, self._serialize, self._deserialize)