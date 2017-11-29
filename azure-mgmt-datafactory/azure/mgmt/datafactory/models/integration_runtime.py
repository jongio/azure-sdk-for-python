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


class IntegrationRuntime(Model):
    """Azure Data Factory nested object which serves as a compute resource for
    activities.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: SelfHostedIntegrationRuntime, ManagedIntegrationRuntime

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param description: Integration runtime description.
    :type description: str
    :param type: Constant filled by server.
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'SelfHosted': 'SelfHostedIntegrationRuntime', 'Managed': 'ManagedIntegrationRuntime'}
    }

    def __init__(self, additional_properties=None, description=None):
        self.additional_properties = additional_properties
        self.description = description
        self.type = None
