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


class ChaosContextMapItem(Model):
    """Describes an item in the ChaosContextMap in ChaosParameters.
    .

    :param key: The key for a ChaosContextMapItem.
    :type key: str
    :param value: The value for a ChaosContextMapItem.
    :type value: str
    """

    _validation = {
        'key': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        'key': {'key': 'Key', 'type': 'str'},
        'value': {'key': 'Value', 'type': 'str'},
    }

    def __init__(self, key, value):
        super(ChaosContextMapItem, self).__init__()
        self.key = key
        self.value = value
