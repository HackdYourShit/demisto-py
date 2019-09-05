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

from demisto_client.demisto_api.models.automation_script import AutomationScript  # noqa: F401,E501
from demisto_client.demisto_api.models.generic_string_filter import GenericStringFilter  # noqa: F401,E501


class AutomationScriptFilterWrapper(object):
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
        'filter': 'GenericStringFilter',
        'save_password': 'bool',
        'script': 'AutomationScript'
    }

    attribute_map = {
        'filter': 'filter',
        'save_password': 'savePassword',
        'script': 'script'
    }

    def __init__(self, filter=None, save_password=None, script=None):  # noqa: E501
        """AutomationScriptFilterWrapper - a model defined in Swagger"""  # noqa: E501

        self._filter = None
        self._save_password = None
        self._script = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if save_password is not None:
            self.save_password = save_password
        if script is not None:
            self.script = script

    @property
    def filter(self):
        """Gets the filter of this AutomationScriptFilterWrapper.  # noqa: E501


        :return: The filter of this AutomationScriptFilterWrapper.  # noqa: E501
        :rtype: GenericStringFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this AutomationScriptFilterWrapper.


        :param filter: The filter of this AutomationScriptFilterWrapper.  # noqa: E501
        :type: GenericStringFilter
        """

        self._filter = filter

    @property
    def save_password(self):
        """Gets the save_password of this AutomationScriptFilterWrapper.  # noqa: E501


        :return: The save_password of this AutomationScriptFilterWrapper.  # noqa: E501
        :rtype: bool
        """
        return self._save_password

    @save_password.setter
    def save_password(self, save_password):
        """Sets the save_password of this AutomationScriptFilterWrapper.


        :param save_password: The save_password of this AutomationScriptFilterWrapper.  # noqa: E501
        :type: bool
        """

        self._save_password = save_password

    @property
    def script(self):
        """Gets the script of this AutomationScriptFilterWrapper.  # noqa: E501


        :return: The script of this AutomationScriptFilterWrapper.  # noqa: E501
        :rtype: AutomationScript
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this AutomationScriptFilterWrapper.


        :param script: The script of this AutomationScriptFilterWrapper.  # noqa: E501
        :type: AutomationScript
        """

        self._script = script

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
        if issubclass(AutomationScriptFilterWrapper, dict):
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
        if not isinstance(other, AutomationScriptFilterWrapper):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other