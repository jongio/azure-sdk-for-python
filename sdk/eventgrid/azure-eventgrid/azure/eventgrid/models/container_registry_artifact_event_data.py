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

from msrest.serialization import Model


class ContainerRegistryArtifactEventData(Model):
    """The content of the event request message.

    :param id: The event ID.
    :type id: str
    :param timestamp: The time at which the event occurred.
    :type timestamp: datetime
    :param action: The action that encompasses the provided event.
    :type action: str
    :param target: The target of the event.
    :type target: ~azure.eventgrid.models.ContainerRegistryArtifactEventTarget
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'action': {'key': 'action', 'type': 'str'},
        'target': {'key': 'target', 'type': 'ContainerRegistryArtifactEventTarget'},
    }

    def __init__(self, **kwargs):
        super(ContainerRegistryArtifactEventData, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.timestamp = kwargs.get('timestamp', None)
        self.action = kwargs.get('action', None)
        self.target = kwargs.get('target', None)