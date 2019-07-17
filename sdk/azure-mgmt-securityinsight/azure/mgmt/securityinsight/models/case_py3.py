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

from .resource_py3 import Resource


class Case(Resource):
    """Represents a case in Azure Security Insights.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar name: Azure resource name
    :vartype name: str
    :param etag: Etag of the alert rule.
    :type etag: str
    :param last_updated_time_utc: The last time the case was updated
    :type last_updated_time_utc: datetime
    :param created_time_utc: The time the case was created
    :type created_time_utc: datetime
    :param end_time_utc: The end time of the case
    :type end_time_utc: datetime
    :param start_time_utc: Required. The start time of the case
    :type start_time_utc: datetime
    :param labels: List of labels relevant to this case
    :type labels: list[str]
    :param description: The description of the case
    :type description: str
    :param title: Required. The title of the case
    :type title: str
    :param assigned_to: Describes a user that the case is assigned to
    :type assigned_to: ~azure.mgmt.securityinsight.models.UserInfo
    :param severity: Required. The severity of the case. Possible values
     include: 'Critical', 'High', 'Medium', 'Low', 'Informational'
    :type severity: str or ~azure.mgmt.securityinsight.models.CaseSeverity
    :param status: Required. The status of the case. Possible values include:
     'Draft', 'New', 'InProgress', 'Closed'
    :type status: str or ~azure.mgmt.securityinsight.models.CaseStatus
    :param close_reason: The reason the case was closed. Possible values
     include: 'Resolved', 'Dismissed', 'Other'
    :type close_reason: str or ~azure.mgmt.securityinsight.models.CloseReason
    :param closed_reason_text: the case close reason details
    :type closed_reason_text: str
    :param related_alert_ids: List of related alert identifiers
    :type related_alert_ids: list[str]
    :param case_number: a sequential number
    :type case_number: int
    :param last_comment: the last comment in the case
    :type last_comment: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'start_time_utc': {'required': True},
        'title': {'required': True},
        'severity': {'required': True},
        'status': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'last_updated_time_utc': {'key': 'properties.lastUpdatedTimeUtc', 'type': 'iso-8601'},
        'created_time_utc': {'key': 'properties.createdTimeUtc', 'type': 'iso-8601'},
        'end_time_utc': {'key': 'properties.endTimeUtc', 'type': 'iso-8601'},
        'start_time_utc': {'key': 'properties.startTimeUtc', 'type': 'iso-8601'},
        'labels': {'key': 'properties.labels', 'type': '[str]'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'title': {'key': 'properties.title', 'type': 'str'},
        'assigned_to': {'key': 'properties.assignedTo', 'type': 'UserInfo'},
        'severity': {'key': 'properties.severity', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'close_reason': {'key': 'properties.closeReason', 'type': 'str'},
        'closed_reason_text': {'key': 'properties.closedReasonText', 'type': 'str'},
        'related_alert_ids': {'key': 'properties.relatedAlertIds', 'type': '[str]'},
        'case_number': {'key': 'properties.caseNumber', 'type': 'int'},
        'last_comment': {'key': 'properties.lastComment', 'type': 'str'},
    }

    def __init__(self, *, start_time_utc, title: str, severity, status, etag: str=None, last_updated_time_utc=None, created_time_utc=None, end_time_utc=None, labels=None, description: str=None, assigned_to=None, close_reason=None, closed_reason_text: str=None, related_alert_ids=None, case_number: int=None, last_comment: str=None, **kwargs) -> None:
        super(Case, self).__init__(**kwargs)
        self.etag = etag
        self.last_updated_time_utc = last_updated_time_utc
        self.created_time_utc = created_time_utc
        self.end_time_utc = end_time_utc
        self.start_time_utc = start_time_utc
        self.labels = labels
        self.description = description
        self.title = title
        self.assigned_to = assigned_to
        self.severity = severity
        self.status = status
        self.close_reason = close_reason
        self.closed_reason_text = closed_reason_text
        self.related_alert_ids = related_alert_ids
        self.case_number = case_number
        self.last_comment = last_comment
