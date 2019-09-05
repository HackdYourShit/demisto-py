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


class Audit(object):
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
        'action': 'dict(str, object)',
        'id': 'str',
        'identifier': 'str',
        'modified': 'datetime',
        'object': 'str',
        'sort_values': 'list[str]',
        'type': 'str',
        'user': 'str',
        'version': 'int'
    }

    attribute_map = {
        'action': 'action',
        'id': 'id',
        'identifier': 'identifier',
        'modified': 'modified',
        'object': 'object',
        'sort_values': 'sortValues',
        'type': 'type',
        'user': 'user',
        'version': 'version'
    }

    def __init__(self, action=None, id=None, identifier=None, modified=None, object=None, sort_values=None, type=None, user=None, version=None):  # noqa: E501
        """Audit - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._id = None
        self._identifier = None
        self._modified = None
        self._object = None
        self._sort_values = None
        self._type = None
        self._user = None
        self._version = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if id is not None:
            self.id = id
        if identifier is not None:
            self.identifier = identifier
        if modified is not None:
            self.modified = modified
        if object is not None:
            self.object = object
        if sort_values is not None:
            self.sort_values = sort_values
        if type is not None:
            self.type = type
        if user is not None:
            self.user = user
        if version is not None:
            self.version = version

    @property
    def action(self):
        """Gets the action of this Audit.  # noqa: E501


        :return: The action of this Audit.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Audit.


        :param action: The action of this Audit.  # noqa: E501
        :type: dict(str, object)
        """

        self._action = action

    @property
    def id(self):
        """Gets the id of this Audit.  # noqa: E501


        :return: The id of this Audit.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Audit.


        :param id: The id of this Audit.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def identifier(self):
        """Gets the identifier of this Audit.  # noqa: E501


        :return: The identifier of this Audit.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Audit.


        :param identifier: The identifier of this Audit.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def modified(self):
        """Gets the modified of this Audit.  # noqa: E501


        :return: The modified of this Audit.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Audit.


        :param modified: The modified of this Audit.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def object(self):
        """Gets the object of this Audit.  # noqa: E501


        :return: The object of this Audit.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this Audit.


        :param object: The object of this Audit.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def sort_values(self):
        """Gets the sort_values of this Audit.  # noqa: E501


        :return: The sort_values of this Audit.  # noqa: E501
        :rtype: list[str]
        """
        return self._sort_values

    @sort_values.setter
    def sort_values(self, sort_values):
        """Sets the sort_values of this Audit.


        :param sort_values: The sort_values of this Audit.  # noqa: E501
        :type: list[str]
        """

        self._sort_values = sort_values

    @property
    def type(self):
        """Gets the type of this Audit.  # noqa: E501


        :return: The type of this Audit.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Audit.


        :param type: The type of this Audit.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def user(self):
        """Gets the user of this Audit.  # noqa: E501


        :return: The user of this Audit.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Audit.


        :param user: The user of this Audit.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def version(self):
        """Gets the version of this Audit.  # noqa: E501


        :return: The version of this Audit.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Audit.


        :param version: The version of this Audit.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(Audit, dict):
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
        if not isinstance(other, Audit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other