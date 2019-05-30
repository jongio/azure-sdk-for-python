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


class TrackedResourceModificationDetails(Model):
    """The details of the policy triggered deployment that created or modified the
    tracked resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar policy_details: The details of the policy that created or modified
     the tracked resource.
    :vartype policy_details: ~azure.mgmt.policyinsights.models.PolicyDetails
    :ivar deployment_id: The ID of the deployment that created or modified the
     tracked resource.
    :vartype deployment_id: str
    :ivar deployment_time: Timestamp of the deployment that created or
     modified the tracked resource.
    :vartype deployment_time: datetime
    """

    _validation = {
        'policy_details': {'readonly': True},
        'deployment_id': {'readonly': True},
        'deployment_time': {'readonly': True},
    }

    _attribute_map = {
        'policy_details': {'key': 'policyDetails', 'type': 'PolicyDetails'},
        'deployment_id': {'key': 'deploymentId', 'type': 'str'},
        'deployment_time': {'key': 'deploymentTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(TrackedResourceModificationDetails, self).__init__(**kwargs)
        self.policy_details = None
        self.deployment_id = None
        self.deployment_time = None