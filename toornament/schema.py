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


class SchemaElement:

    def to_dict(self):
        return convert_to_dict(self)
