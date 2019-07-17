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

from .entity_py3 import Entity


class IpEntity(Entity):
    """Represents an ip entity.

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
    :ivar address: The IP address as string, e.g. 127.0.0.1 (either in Ipv4 or
     Ipv6)
    :vartype address: str
    :param location: The geo-location context attached to the ip entity
    :type location: ~azure.mgmt.securityinsight.models.GeoLocation
    :ivar threat_intelligence: Ip Entitiy identifiers for the resolved ip
     address.
    :vartype threat_intelligence:
     list[~azure.mgmt.securityinsight.models.ThreatIntelligence]
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'kind': {'required': True},
        'friendly_name': {'readonly': True},
        'additional_data': {'readonly': True},
        'address': {'readonly': True},
        'threat_intelligence': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'additional_data': {'key': 'properties.additionalData', 'type': '{object}'},
        'address': {'key': 'properties.address', 'type': 'str'},
        'location': {'key': 'properties.location', 'type': 'GeoLocation'},
        'threat_intelligence': {'key': 'properties.threatIntelligence', 'type': '[ThreatIntelligence]'},
    }

    def __init__(self, *, location=None, **kwargs) -> None:
        super(IpEntity, self).__init__(**kwargs)
        self.friendly_name = None
        self.additional_data = None
        self.address = None
        self.location = location
        self.threat_intelligence = None
        self.kind = 'Ip'
