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

from .proxy_only_resource_py3 import ProxyOnlyResource


class ResourceMetricDefinition(ProxyOnlyResource):
    """Metadata for the metrics.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar unit: Unit of the metric.
    :vartype unit: str
    :ivar primary_aggregation_type: Primary aggregation type.
    :vartype primary_aggregation_type: str
    :ivar metric_availabilities: List of time grains supported for the metric
     together with retention period.
    :vartype metric_availabilities:
     list[~azure.mgmt.web.models.ResourceMetricAvailability]
    :ivar resource_uri: Resource URI.
    :vartype resource_uri: str
    :ivar properties: Resource metric definition properties.
    :vartype properties: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'unit': {'readonly': True},
        'primary_aggregation_type': {'readonly': True},
        'metric_availabilities': {'readonly': True},
        'resource_uri': {'readonly': True},
        'properties': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'unit': {'key': 'properties.unit', 'type': 'str'},
        'primary_aggregation_type': {'key': 'properties.primaryAggregationType', 'type': 'str'},
        'metric_availabilities': {'key': 'properties.metricAvailabilities', 'type': '[ResourceMetricAvailability]'},
        'resource_uri': {'key': 'properties.resourceUri', 'type': 'str'},
        'properties': {'key': 'properties.properties', 'type': '{str}'},
    }

    def __init__(self, *, kind: str=None, **kwargs) -> None:
        super(ResourceMetricDefinition, self).__init__(kind=kind, **kwargs)
        self.unit = None
        self.primary_aggregation_type = None
        self.metric_availabilities = None
        self.resource_uri = None
        self.properties = None