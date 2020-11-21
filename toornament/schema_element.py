def convert_to_dict(instance):
    if isinstance(instance, SchemaElement):
        dictionary = instance.__dict__

        return convert_to_dict(dictionary)

    elif isinstance(instance, dict):
        return {k: convert_to_dict(v) for k, v in instance.items()}

    elif isinstance(instance, (list, tuple)):
        return [convert_to_dict(e) for e in instance]

    else:
        return instance


def convert_to_dict_remove_none(instance):
    if isinstance(instance, SchemaElement):
        dictionary = instance.__dict__

        return convert_to_dict_remove_none(dictionary)

    elif isinstance(instance, dict):
        return {k: convert_to_dict_remove_none(v) for k, v in instance.items() if v is not None}

    elif isinstance(instance, (list, tuple)):
        return [convert_to_dict_remove_none(e) for e in instance]

    else:
        return instance


class SchemaElement:

    def to_dict(self):
        return convert_to_dict(self)

    def to_dict_remove_none(self):
        return convert_to_dict_remove_none(self)
