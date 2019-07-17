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

from .entity import Entity


class DnsEntity(Entity):
    """Represents a dns entity.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar name: Azure resource name
    :vartype name: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :ivar friendly_name: The graph item display name which is a short humanly
     readable description of the graph item instance. This property is optional
     and might be system generated.
    :vartype friendly_name: str
    :ivar additional_data: A bag of custom fields that should be part of the
     entity and will be presented to the user.
    :vartype additional_data: dict[str, object]
    :ivar domain_name: The name of the dns record associated with the alert
    :vartype domain_name: str
    :ivar ip_address_entity_ids: Ip Entitiy identifiers for the resolved ip
     address.
    :vartype ip_address_entity_ids: list[str]
    :ivar dns_server_ip_entity_id: An ip entity id for the dns server
     resolving the request
    :vartype dns_server_ip_entity_id: str
    :ivar host_ip_address_entity_id: An ip entity id for the dns request
     client
    :vartype host_ip_address_entity_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'kind': {'required': True},
        'friendly_name': {'readonly': True},
        'additional_data': {'readonly': True},
        'domain_name': {'readonly': True},
        'ip_address_entity_ids': {'readonly': True},
        'dns_server_ip_entity_id': {'readonly': True},
        'host_ip_address_entity_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'additional_data': {'key': 'properties.additionalData', 'type': '{object}'},
        'domain_name': {'key': 'properties.domainName', 'type': 'str'},
        'ip_address_entity_ids': {'key': 'properties.ipAddressEntityIds', 'type': '[str]'},
        'dns_server_ip_entity_id': {'key': 'properties.dnsServerIpEntityId', 'type': 'str'},
        'host_ip_address_entity_id': {'key': 'properties.hostIpAddressEntityId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DnsEntity, self).__init__(**kwargs)
        self.friendly_name = None
        self.additional_data = None
        self.domain_name = None
        self.ip_address_entity_ids = None
        self.dns_server_ip_entity_id = None
        self.host_ip_address_entity_id = None
        self.kind = 'DnsResolution'
