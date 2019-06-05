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


class ServiceCosmosDbConfigurationInfo(Model):
    """The settings for the Cosmos DB database backing the service.

    :param offer_throughput: The provisioned throughput for the backing
     database.
    :type offer_throughput: int
    """

    _attribute_map = {
        'offer_throughput': {'key': 'offerThroughput', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(ServiceCosmosDbConfigurationInfo, self).__init__(**kwargs)
        self.offer_throughput = kwargs.get('offer_throughput', None)
