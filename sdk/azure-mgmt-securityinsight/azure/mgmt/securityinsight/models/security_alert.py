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

from .entity import Entity


class SecurityAlert(Entity):
    """Represents a security alert entity.

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
    :ivar system_alert_id: Holds the product identifier of the alert for the
     product.
    :vartype system_alert_id: str
    :ivar confidence_reasons: The confidence reasons
    :vartype confidence_reasons: list[str or
     ~azure.mgmt.securityinsight.models.ConfidenceReason]
    :ivar confidence_score_status: The confidence score calculation status,
     i.e. indicating if score calculation is pending for this alert, not
     applicable or final. Possible values include: 'NotApplicable',
     'InProcess', 'NotFinal', 'Final'
    :vartype confidence_score_status: str or
     ~azure.mgmt.securityinsight.models.ConfidenceScoreStatus
    :ivar intent: Holds the alert intent stage(s) mapping for this alert.
     Possible values include: 'Unknown', 'Probing', 'Exploitation',
     'Persistence', 'PrivilegeEscalation', 'DefenseEvasion',
     'CredentialAccess', 'Discovery', 'LateralMovement', 'Execution',
     'Collection', 'Exfiltration', 'CommandAndControl', 'Impact'
    :vartype intent: str or ~azure.mgmt.securityinsight.models.KillChainIntent
    :ivar confidence_score: The confidence score of the alert.
    :vartype confidence_score: float
    :ivar alert_display_name: The display name of the alert.
    :vartype alert_display_name: str
    :ivar description: Alert description.
    :vartype description: str
    :ivar remediation_steps: Manual action items to take to remediate the
     alert.
    :vartype remediation_steps: list[str]
    :ivar confidence_level: The confidence level of this alert. Possible
     values include: 'Unknown', 'Low', 'High'
    :vartype confidence_level: str or
     ~azure.mgmt.securityinsight.models.ConfidenceLevel
    :ivar severity: The severity of the alert. Possible values include:
     'Informational', 'Low', 'Medium', 'High'
    :vartype severity: str or ~azure.mgmt.securityinsight.models.Severity
    :ivar vendor_name: The name of the vendor that raise the alert.
    :vartype vendor_name: str
    :ivar product_name: The name of the product which published this alert.
    :vartype product_name: str
    :ivar product_component_name: The name of a component inside the product
     which generated the alert.
    :vartype product_component_name: str
    :ivar alert_type: The type name of the alert.
    :vartype alert_type: str
    :ivar product_version: The version of the product generating the alert.
    :vartype product_version: str
    :ivar processing_end_time: The time the alert was made available for
     consumption.
    :vartype processing_end_time: datetime
    :ivar status: The lifecycle status of the alert. Possible values include:
     'Unknown', 'New', 'Resolved', 'Dismissed', 'InProgress'
    :vartype status: str or ~azure.mgmt.securityinsight.models.AlertStatus
    :ivar end_time_utc: The impact end time of the alert (the time of the last
     event contributing to the alert).
    :vartype end_time_utc: datetime
    :ivar start_time_utc: The impact start time of the alert (the time of the
     first event contributing to the alert).
    :vartype start_time_utc: datetime
    :ivar time_generated: The time the alert was generated.
    :vartype time_generated: datetime
    :ivar compromised_entity: Display name of the main entity being reported
     on.
    :vartype compromised_entity: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'kind': {'required': True},
        'friendly_name': {'readonly': True},
        'additional_data': {'readonly': True},
        'system_alert_id': {'readonly': True},
        'confidence_reasons': {'readonly': True},
        'confidence_score_status': {'readonly': True},
        'intent': {'readonly': True},
        'confidence_score': {'readonly': True},
        'alert_display_name': {'readonly': True},
        'description': {'readonly': True},
        'remediation_steps': {'readonly': True},
        'confidence_level': {'readonly': True},
        'severity': {'readonly': True},
        'vendor_name': {'readonly': True},
        'product_name': {'readonly': True},
        'product_component_name': {'readonly': True},
        'alert_type': {'readonly': True},
        'product_version': {'readonly': True},
        'processing_end_time': {'readonly': True},
        'status': {'readonly': True},
        'end_time_utc': {'readonly': True},
        'start_time_utc': {'readonly': True},
        'time_generated': {'readonly': True},
        'compromised_entity': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'additional_data': {'key': 'properties.additionalData', 'type': '{object}'},
        'system_alert_id': {'key': 'properties.systemAlertId', 'type': 'str'},
        'confidence_reasons': {'key': 'properties.confidenceReasons', 'type': '[str]'},
        'confidence_score_status': {'key': 'properties.confidenceScoreStatus', 'type': 'str'},
        'intent': {'key': 'properties.intent', 'type': 'str'},
        'confidence_score': {'key': 'properties.confidenceScore', 'type': 'float'},
        'alert_display_name': {'key': 'properties.alertDisplayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'remediation_steps': {'key': 'properties.remediationSteps', 'type': '[str]'},
        'confidence_level': {'key': 'properties.confidenceLevel', 'type': 'str'},
        'severity': {'key': 'properties.severity', 'type': 'str'},
        'vendor_name': {'key': 'properties.vendorName', 'type': 'str'},
        'product_name': {'key': 'properties.productName', 'type': 'str'},
        'product_component_name': {'key': 'properties.productComponentName', 'type': 'str'},
        'alert_type': {'key': 'properties.alertType', 'type': 'str'},
        'product_version': {'key': 'properties.productVersion', 'type': 'str'},
        'processing_end_time': {'key': 'properties.processingEndTime', 'type': 'iso-8601'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'end_time_utc': {'key': 'properties.endTimeUtc', 'type': 'iso-8601'},
        'start_time_utc': {'key': 'properties.startTimeUtc', 'type': 'iso-8601'},
        'time_generated': {'key': 'properties.timeGenerated', 'type': 'iso-8601'},
        'compromised_entity': {'key': 'properties.compromisedEntity', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SecurityAlert, self).__init__(**kwargs)
        self.friendly_name = None
        self.additional_data = None
        self.system_alert_id = None
        self.confidence_reasons = None
        self.confidence_score_status = None
        self.intent = None
        self.confidence_score = None
        self.alert_display_name = None
        self.description = None
        self.remediation_steps = None
        self.confidence_level = None
        self.severity = None
        self.vendor_name = None
        self.product_name = None
        self.product_component_name = None
        self.alert_type = None
        self.product_version = None
        self.processing_end_time = None
        self.status = None
        self.end_time_utc = None
        self.start_time_utc = None
        self.time_generated = None
        self.compromised_entity = None
        self.kind = 'SecurityAlert'
