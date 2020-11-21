from .toornament_connection import SyncToornamentConnection, AsyncToornamentConnection
from typing import Optional, List
from .range import Range
from .organizer_schema import OrganizerSchema as OS


class SyncOrganizerAPI(SyncToornamentConnection):

    @staticmethod
    def _base_url():
        return 'https://api.toornament.com/organizer/v2'

    def get_fields(self, tournament_id, *, target_type: str, **request_arguments):
        """Retrieve the custom fields of a tournament.
        Returns the complete definition of all custom fields for a given tournament. This includes both public and private custom fields. A custom field may be associated to a player, a team or a team's player. For more information, please read the [Custom Fields](https://developer.toornament.com/v2/core-concepts/custom-fields) documentation.


        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param target_type: The entity affected by the custom fields."""

        return self._access(
            'organizer_get_fields', request_arguments,
            tournament_id = tournament_id,
            target_type = target_type,
        )

    def post_field(self, tournament_id, body: OS.CustomFieldCreate, **request_arguments):
        """Create a new custom field in a tournament.
        Create a new custom field in a tournament. You can not have more than 128 custom fields in a tournament.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param body: OrganizerSchema.CustomFieldCreate Data to provide for create the custom field."""

        return self._access(
            'organizer_post_field', request_arguments,
            tournament_id = tournament_id,
            body = body,
        )

    def get_field(self, tournament_id, id, **request_arguments):
        """Retrieve a single custom field of a tournament.
        Returns a single custom field of a tournament.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the requested custom field."""

        return self._access(
            'organizer_get_field', request_arguments,
            tournament_id = tournament_id,
            id = id,
        )

    def patch_field(self, tournament_id, id, body: OS.CustomFieldBase, **request_arguments):
        """Update a single custom field of a tournament.
        Update a single custom field of a tournament.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the requested custom field.
        :param body: OrganizerSchema.CustomFieldBase Data to provide for update the custom field."""

        return self._access(
            'organizer_patch_field', request_arguments,
            tournament_id = tournament_id,
            id = id,
            body = body,
        )

    def delete_field(self, tournament_id, id, **request_arguments):
        """Delete a custom field of a tournament.
        Delete a custom field of a tournament.

        :param tournament_id: The id of the tournament you want to retrieve data about.
        :param id: The id of the requested custom field."""

        return self._access(
            'organizer_delete_field', request_arguments,
            tournament_id = tournament_id,
            id = id,
        )
