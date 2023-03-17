# coding: utf-8
import pprint
import re  # noqa: F401

import six

class EC2InstanceStateChangeNotification(object):


    _types = {
        'instance_id': 'str',
        'state': 'str'
    }

    _attribute_map = {
        'instance_id': 'instance-id',
        'state': 'state'
    }

    def __init__(self, instance_id=None, state=None):  # noqa: E501
        self._instance_id = None
        self._state = None
        self.discriminator = None
        self.instance_id = instance_id
        self.state = state

    @property
    def instance_id(self):
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        self._instance_id = instance_id

    @property
    def state(self):

        return self._state

    @state.setter
    def state(self, state):


        self._state = state

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self._types):
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
        if issubclass(EC2InstanceStateChangeNotification, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, EC2InstanceStateChangeNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other