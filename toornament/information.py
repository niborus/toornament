import requests


class Information:
    PLATFORMS = ['pc', 'playstation4', 'xbox_one', 'nintendo_switch', 'mobile', 'playstation3', 'playstation2',
                 'playstation1', 'ps_vita', 'psp', 'xbox360', 'xbox', 'wii_u', 'wii', 'gamecube', 'nintendo64', 'snes',
                 'nes', 'dreamcast', 'saturn', 'megadrive', 'master_system', '3ds', 'ds', 'game_boy', 'neo_geo',
                 'other_platform', 'not_video_game']

    @staticmethod
    def fetch_platforms(**kwargs):
        """This will fetch the all Platforms (according to the Docs).
        Function is blocking and not guaranteed to succeed.
        :param kwargs Arguments for request.get()
        :returns List with Platforms.
        :raises HTTP-Exception"""

        res = requests.get('https://api.toornament.com/schema/oas/v2/viewer/tournament.json', **kwargs)

        res = res.json()

        return res['components']['schemas']['Tournament']['properties']['platforms']['items']['enum']


class Scopes:
    PARTICIPANT_MANAGE_REGISTRATIONS = 'participant:manage_registrations'
    PARTICIPANT_MANAGE_PARTICIPATIONS = 'participant:manage_participations'
    USER_INFO = 'user:info'
    ORGANIZER_VIEW = 'organizer:view'
    ORGANIZER_ADMIN = 'organizer:admin'
    ORGANIZER_RESULT = 'organizer:result'
    ORGANIZER_PARTICIPANT = 'organizer:participant'
    ORGANIZER_REGISTRATION = 'organizer:registration'
    ORGANIZER_PERMISSION = 'organizer:permission'
    ORGANIZER_DELETE = 'organizer:delete'

    LIST_WITH_SCOPES = [
        'participant:manage_registrations',
        'participant:manage_participations',
        'user:info',
        'organizer:view',
        'organizer:admin',
        'organizer:result',
        'organizer:participant',
        'organizer:registration',
        'organizer:permission',
        'organizer:delete',
    ]
