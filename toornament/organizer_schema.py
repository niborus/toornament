from .converter import Converter
from .schema_element import SchemaElement


class OrganizerSchema:
    class CustomFieldBase(SchemaElement):

        def __init__(self, *, label=None, default_value=None, required=None, public=None, position=None):
            """
            :param label string The display name of a custom field in forms.
            :param default_value  A default value (can be array, scalar or null).
            :param required boolean Whether the custom field is required.
            :param public boolean Whether the value of the custom field is public.
            :param position integer The position of the field in forms.
            """

            self.label = label
            self.default_value = default_value
            self.required = required
            self.public = public
            self.position = position

    class CustomFieldCreate(CustomFieldBase):

        def __init__(self, *, machine_name, type, target_type=None, **kwargs):
            """
            :param machine_name string A name used to identify a custom field for computing purposes.
            :param type string A data type used for both input and computing.
            :param target_type string The entity concerned by the custom field.
            """

            super().__init__(**kwargs)

            self.machine_name = machine_name
            self.type = type
            self.target_type = target_type

    class CustomField(CustomFieldCreate):

        def __init__(self, *, id, **kwargs):
            """
            :param id string The unique identifier of the custom field.
            """

            super().__init__(**kwargs)

            self.id = int(id)
