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


class Port(Model):
    """The port exposed on the container group.

    :param protocol: The protocol associated with the port. Possible values
     include: 'TCP', 'UDP'
    :type protocol: str or
     ~azure.mgmt.containerinstance.models.ContainerGroupNetworkProtocol
    :param port: The port number.
    :type port: int
    """

    _validation = {
        'port': {'required': True},
    }

    _attribute_map = {
        'protocol': {'key': 'protocol', 'type': 'str'},
        'port': {'key': 'port', 'type': 'int'},
    }

    def __init__(self, port, protocol=None):
        super(Port, self).__init__()
        self.protocol = protocol
        self.port = port
