# coding: utf-8

"""
    Demisto API

    This is the public REST API to integrate with the demisto server. HTTP request can be sent using any HTTP-client.  For an example dedicated client take a look at: https://github.com/demisto/demisto-py.  Requests must include API-key that can be generated in the Demisto web client under 'Settings' -> 'Integrations' -> 'API keys'   Optimistic Locking and Versioning\\:  When using Demisto REST API, you will need to make sure to work on the latest version of the item (incident, entry, etc.), otherwise, you will get a DB version error (which not allow you to override a newer item). In addition, you can pass 'version\\: -1' to force data override (make sure that other users data might be lost).  Assume that Alice and Bob both read the same data from Demisto server, then they both changed the data, and then both tried to write the new versions back to the server. Whose changes should be saved? Alice’s? Bob’s? To solve this, each data item in Demisto has a numeric incremental version. If Alice saved an item with version 4 and Bob trying to save the same item with version 3, Demisto will rollback Bob request and returns a DB version conflict error. Bob will need to get the latest item and work on it so Alice work will not get lost.  Example request using 'curl'\\:  ``` curl 'https://hostname:443/incidents/search' -H 'content-type: application/json' -H 'accept: application/json' -H 'Authorization: <API Key goes here>' --data-binary '{\"filter\":{\"query\":\"-status:closed -category:job\",\"period\":{\"by\":\"day\",\"fromValue\":7}}}' --compressed ```  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from demisto_client.demisto_api.models.incident_filter import IncidentFilter  # noqa: F401,E501


class UpdateDataBatch(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'custom_fields': 'dict(str, object)',
        'all': 'bool',
        'close_notes': 'str',
        'close_reason': 'str',
        'columns': 'list[str]',
        'data': 'dict(str, object)',
        'filter': 'IncidentFilter',
        'force': 'bool',
        'ids': 'list[str]',
        'line': 'str',
        'original_incident_id': 'str',
        'override_investigation': 'bool'
    }

    attribute_map = {
        'custom_fields': 'CustomFields',
        'all': 'all',
        'close_notes': 'closeNotes',
        'close_reason': 'closeReason',
        'columns': 'columns',
        'data': 'data',
        'filter': 'filter',
        'force': 'force',
        'ids': 'ids',
        'line': 'line',
        'original_incident_id': 'originalIncidentId',
        'override_investigation': 'overrideInvestigation'
    }

    def __init__(self, custom_fields=None, all=None, close_notes=None, close_reason=None, columns=None, data=None, filter=None, force=None, ids=None, line=None, original_incident_id=None, override_investigation=None):  # noqa: E501
        """UpdateDataBatch - a model defined in Swagger"""  # noqa: E501

        self._custom_fields = None
        self._all = None
        self._close_notes = None
        self._close_reason = None
        self._columns = None
        self._data = None
        self._filter = None
        self._force = None
        self._ids = None
        self._line = None
        self._original_incident_id = None
        self._override_investigation = None
        self.discriminator = None

        if custom_fields is not None:
            self.custom_fields = custom_fields
        if all is not None:
            self.all = all
        if close_notes is not None:
            self.close_notes = close_notes
        if close_reason is not None:
            self.close_reason = close_reason
        if columns is not None:
            self.columns = columns
        if data is not None:
            self.data = data
        if filter is not None:
            self.filter = filter
        if force is not None:
            self.force = force
        if ids is not None:
            self.ids = ids
        if line is not None:
            self.line = line
        if original_incident_id is not None:
            self.original_incident_id = original_incident_id
        if override_investigation is not None:
            self.override_investigation = override_investigation

    @property
    def custom_fields(self):
        """Gets the custom_fields of this UpdateDataBatch.  # noqa: E501


        :return: The custom_fields of this UpdateDataBatch.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this UpdateDataBatch.


        :param custom_fields: The custom_fields of this UpdateDataBatch.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    @property
    def all(self):
        """Gets the all of this UpdateDataBatch.  # noqa: E501


        :return: The all of this UpdateDataBatch.  # noqa: E501
        :rtype: bool
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this UpdateDataBatch.


        :param all: The all of this UpdateDataBatch.  # noqa: E501
        :type: bool
        """

        self._all = all

    @property
    def close_notes(self):
        """Gets the close_notes of this UpdateDataBatch.  # noqa: E501


        :return: The close_notes of this UpdateDataBatch.  # noqa: E501
        :rtype: str
        """
        return self._close_notes

    @close_notes.setter
    def close_notes(self, close_notes):
        """Sets the close_notes of this UpdateDataBatch.


        :param close_notes: The close_notes of this UpdateDataBatch.  # noqa: E501
        :type: str
        """

        self._close_notes = close_notes

    @property
    def close_reason(self):
        """Gets the close_reason of this UpdateDataBatch.  # noqa: E501


        :return: The close_reason of this UpdateDataBatch.  # noqa: E501
        :rtype: str
        """
        return self._close_reason

    @close_reason.setter
    def close_reason(self, close_reason):
        """Sets the close_reason of this UpdateDataBatch.


        :param close_reason: The close_reason of this UpdateDataBatch.  # noqa: E501
        :type: str
        """

        self._close_reason = close_reason

    @property
    def columns(self):
        """Gets the columns of this UpdateDataBatch.  # noqa: E501


        :return: The columns of this UpdateDataBatch.  # noqa: E501
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this UpdateDataBatch.


        :param columns: The columns of this UpdateDataBatch.  # noqa: E501
        :type: list[str]
        """

        self._columns = columns

    @property
    def data(self):
        """Gets the data of this UpdateDataBatch.  # noqa: E501


        :return: The data of this UpdateDataBatch.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this UpdateDataBatch.


        :param data: The data of this UpdateDataBatch.  # noqa: E501
        :type: dict(str, object)
        """

        self._data = data

    @property
    def filter(self):
        """Gets the filter of this UpdateDataBatch.  # noqa: E501


        :return: The filter of this UpdateDataBatch.  # noqa: E501
        :rtype: IncidentFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this UpdateDataBatch.


        :param filter: The filter of this UpdateDataBatch.  # noqa: E501
        :type: IncidentFilter
        """

        self._filter = filter

    @property
    def force(self):
        """Gets the force of this UpdateDataBatch.  # noqa: E501


        :return: The force of this UpdateDataBatch.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this UpdateDataBatch.


        :param force: The force of this UpdateDataBatch.  # noqa: E501
        :type: bool
        """

        self._force = force

    @property
    def ids(self):
        """Gets the ids of this UpdateDataBatch.  # noqa: E501


        :return: The ids of this UpdateDataBatch.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this UpdateDataBatch.


        :param ids: The ids of this UpdateDataBatch.  # noqa: E501
        :type: list[str]
        """

        self._ids = ids

    @property
    def line(self):
        """Gets the line of this UpdateDataBatch.  # noqa: E501


        :return: The line of this UpdateDataBatch.  # noqa: E501
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this UpdateDataBatch.


        :param line: The line of this UpdateDataBatch.  # noqa: E501
        :type: str
        """

        self._line = line

    @property
    def original_incident_id(self):
        """Gets the original_incident_id of this UpdateDataBatch.  # noqa: E501


        :return: The original_incident_id of this UpdateDataBatch.  # noqa: E501
        :rtype: str
        """
        return self._original_incident_id

    @original_incident_id.setter
    def original_incident_id(self, original_incident_id):
        """Sets the original_incident_id of this UpdateDataBatch.


        :param original_incident_id: The original_incident_id of this UpdateDataBatch.  # noqa: E501
        :type: str
        """

        self._original_incident_id = original_incident_id

    @property
    def override_investigation(self):
        """Gets the override_investigation of this UpdateDataBatch.  # noqa: E501


        :return: The override_investigation of this UpdateDataBatch.  # noqa: E501
        :rtype: bool
        """
        return self._override_investigation

    @override_investigation.setter
    def override_investigation(self, override_investigation):
        """Sets the override_investigation of this UpdateDataBatch.


        :param override_investigation: The override_investigation of this UpdateDataBatch.  # noqa: E501
        :type: bool
        """

        self._override_investigation = override_investigation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UpdateDataBatch, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateDataBatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
