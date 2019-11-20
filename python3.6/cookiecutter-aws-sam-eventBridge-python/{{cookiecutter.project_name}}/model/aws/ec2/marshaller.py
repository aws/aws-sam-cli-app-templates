import datetime
import re
import six
import model.aws.ec2

class Marshaller:
    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types

    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    @classmethod
    def marshall(cls, obj):
        if obj is None:
            return None
        elif isinstance(obj, cls.PRIMITIVE_TYPES):
            return obj
        elif isinstance(obj, list):
            return [cls.marshall(sub_obj)
                    for sub_obj in obj]
        elif isinstance(obj, tuple):
            return tuple(cls.marshall(sub_obj)
                         for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        if isinstance(obj, dict):
            obj_dict = obj
        else:
            obj_dict = {obj._attribute_map[attr]: getattr(obj, attr)
                        for attr, _ in six.iteritems(obj._types)
                        if getattr(obj, attr) is not None}

        return {key: cls.marshall(val)
                for key, val in six.iteritems(obj_dict)}

    @classmethod
    def unmarshall(cls, data, typeName):

        if data is None:
            return None

        if type(typeName) == str:
            if typeName.startswith('list['):
                sub_kls = re.match(r'list\[(.*)\]', typeName).group(1)
                return [cls.unmarshall(sub_data, sub_kls)
                        for sub_data in data]

            if typeName.startswith('dict('):
                sub_kls = re.match(r'dict\(([^,]*), (.*)\)', typeName).group(2)
                return {k: cls.unmarshall(v, sub_kls)
                        for k, v in six.iteritems(data)}

            if typeName in cls.NATIVE_TYPES_MAPPING:
                typeName = cls.NATIVE_TYPES_MAPPING[typeName]
            else:
                typeName = getattr(model.aws.ec2, typeName)

        if typeName in cls.PRIMITIVE_TYPES:
            return cls.__unmarshall_primitive(data, typeName)
        elif typeName == object:
            return cls.__unmarshall_object(data)
        elif typeName == datetime.date:
            return cls.__unmarshall_date(data)
        elif typeName == datetime.datetime:
            return cls.__unmarshall_datatime(data)
        else:
            return cls.__unmarshall_model(data, typeName)

    @classmethod
    def __unmarshall_primitive(cls, data, typeName):
        try:
            return typeName(data)
        except UnicodeEncodeError:
            return six.text_type(data)
        except TypeError:
            return data

    @classmethod
    def __unmarshall_object(cls, value):
        return value

    @classmethod
    def __unmarshall_date(cls, string):
        try:
            from dateutil.parser import parse
            return parse(string).date()
        except ImportError:
            return string

    @classmethod
    def __unmarshall_datatime(cls, string):
        try:
            from dateutil.parser import parse
            return parse(string)
        except ImportError:
            return string

    @classmethod
    def __unmarshall_model(cls, data, typeName):
        if (not typeName._types and
                not cls.__hasattr(typeName, 'get_real_child_model')):
            return data

        kwargs = {}
        if typeName._types is not None:
            for attr, attr_type in six.iteritems(typeName._types):
                if (data is not None and
                        typeName._attribute_map[attr] in data and
                        isinstance(data, (list, dict))):
                    value = data[typeName._attribute_map[attr]]
                    kwargs[attr] = cls.unmarshall(value, attr_type)

        instance = typeName(**kwargs)

        if (isinstance(instance, dict) and
                typeName._types is not None and
                isinstance(data, dict)):
            for key, value in data.items():
                if key not in typeName._types:
                    instance[key] = value
        if cls.__hasattr(instance, 'get_real_child_model'):
            type_name = instance.get_real_child_model(data)
            if type_name:
                instance = cls.unmarshall(data, type_name)
        return instance

    @classmethod
    def __hasattr(cls, object, name):
        return name in object.__class__.__dict__
