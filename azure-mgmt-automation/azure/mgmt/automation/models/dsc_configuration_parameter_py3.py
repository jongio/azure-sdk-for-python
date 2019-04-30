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


class DscConfigurationParameter(Model):
    """Definition of the configuration parameter type.

    :param type: Gets or sets the type of the parameter.
    :type type: str
    :param is_mandatory: Gets or sets a Boolean value to indicate whether the
     parameter is mandatory or not.
    :type is_mandatory: bool
    :param position: Get or sets the position of the parameter.
    :type position: int
    :param default_value: Gets or sets the default value of parameter.
    :type default_value: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'is_mandatory': {'key': 'isMandatory', 'type': 'bool'},
        'position': {'key': 'position', 'type': 'int'},
        'default_value': {'key': 'defaultValue', 'type': 'str'},
    }

    def __init__(self, *, type: str=None, is_mandatory: bool=None, position: int=None, default_value: str=None, **kwargs) -> None:
        super(DscConfigurationParameter, self).__init__(**kwargs)
        self.type = type
        self.is_mandatory = is_mandatory
        self.position = position
        self.default_value = default_value