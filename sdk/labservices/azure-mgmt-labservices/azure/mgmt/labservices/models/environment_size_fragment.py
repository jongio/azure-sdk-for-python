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


class EnvironmentSizeFragment(Model):
    """Represents a size category supported by this Lab Account (small, medium or
    large).

    :param name: The size category. Possible values include: 'Basic',
     'Standard', 'Performance'
    :type name: str or ~azure.mgmt.labservices.models.ManagedLabVmSize
    :param vm_sizes: Represents a set of compute sizes that can serve this
     given size type
    :type vm_sizes: list[~azure.mgmt.labservices.models.SizeInfoFragment]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'vm_sizes': {'key': 'vmSizes', 'type': '[SizeInfoFragment]'},
    }

    def __init__(self, **kwargs):
        super(EnvironmentSizeFragment, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.vm_sizes = kwargs.get('vm_sizes', None)