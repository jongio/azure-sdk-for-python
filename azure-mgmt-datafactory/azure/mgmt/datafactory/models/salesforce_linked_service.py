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

from .linked_service import LinkedService


class SalesforceLinkedService(LinkedService):
    """Linked service for Salesforce.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param type: Constant filled by server.
    :type type: str
    :param environment_url: The URL of Salesforce instance. Default is
     'https://login.salesforce.com'. To copy data from sandbox, specify
     'https://test.salesforce.com'. To copy data from custom domain, specify,
     for example, 'https://[domain].my.salesforce.com'. Type: string (or
     Expression with resultType string).
    :type environment_url: object
    :param username: The username for Basic authentication of the Salesforce
     instance. Type: string (or Expression with resultType string).
    :type username: object
    :param password: The password for Basic authentication of the Salesforce
     instance.
    :type password: ~azure.mgmt.datafactory.models.SecretBase
    :param security_token: The security token is required to remotely access
     Salesforce instance.
    :type security_token: ~azure.mgmt.datafactory.models.SecretBase
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'environment_url': {'key': 'typeProperties.environmentUrl', 'type': 'object'},
        'username': {'key': 'typeProperties.username', 'type': 'object'},
        'password': {'key': 'typeProperties.password', 'type': 'SecretBase'},
        'security_token': {'key': 'typeProperties.securityToken', 'type': 'SecretBase'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, additional_properties=None, connect_via=None, description=None, environment_url=None, username=None, password=None, security_token=None, encrypted_credential=None):
        super(SalesforceLinkedService, self).__init__(additional_properties=additional_properties, connect_via=connect_via, description=description)
        self.environment_url = environment_url
        self.username = username
        self.password = password
        self.security_token = security_token
        self.encrypted_credential = encrypted_credential
        self.type = 'Salesforce'
