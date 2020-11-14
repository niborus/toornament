from .functions_dictionary_helper import Converter, ParameterType


FUNCTIONS = {
    'viewer_get_bracket_nodes': {
        'parameters': {
            'range': {
                'type': ParameterType.HEADER,
                'optional': False,
                'list': False,
                'converter': Converter.range
            },
            'tournament_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'stage_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'group_ids': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.to_str
            },
            'group_numbers': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.none
            },
            'round_ids': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.to_str
            },
            'round_numbers': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.none
            },
            'min_depth': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'max_depth': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
        },
        'method': 'GET',
        'range': 'nodes',
        'path': '/tournaments/{tournament_id}/stages/{stage_id}/bracket-nodes',
    },
    'viewer_get_custom_fields': {
        'parameters': {
            'tournament_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'target_type': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
        },
        'method': 'GET',
        'range': None,
        'path': '/tournaments/{tournament_id}/custom-fields',
    },
    'viewer_get_disciplines': {
        'parameters': {
            'range': {
                'type': ParameterType.HEADER,
                'optional': False,
                'list': False,
                'converter': Converter.range
            },
        },
        'method': 'GET',
        'range': 'disciplines',
        'path': '/disciplines',
    },
    'viewer_get_discipline': {
        'parameters': {
            'id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
        },
        'method': 'GET',
        'range': None,
        'path': '/disciplines/{id}',
    },
    'viewer_get_groups': {
        'parameters': {
            'range': {
                'type': ParameterType.HEADER,
                'optional': False,
                'list': False,
                'converter': Converter.range
            },
            'tournament_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'stage_ids': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.to_str
            },
            'stage_numbers': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.none
            },
        },
        'method': 'GET',
        'range': 'groups',
        'path': '/tournaments/{tournament_id}/groups',
    },
    'viewer_get_group': {
        'parameters': {
            'tournament_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
        },
        'method': 'GET',
        'range': None,
        'path': '/tournaments/{tournament_id}/groups/{id}',
    },
    'viewer_get_matches_from_tournament': {
        'parameters': {
            'range': {
                'type': ParameterType.HEADER,
                'optional': False,
                'list': False,
                'converter': Converter.range
            },
            'tournament_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'stage_ids': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.to_str
            },
            'stage_numbers': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.none
            },
            'group_ids': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.to_str
            },
            'group_numbers': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.none
            },
            'round_ids': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.to_str
            },
            'round_numbers': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.none
            },
            'statuses': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.none
            },
            'is_scheduled': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'scheduled_before': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.to_datetime
            },
            'scheduled_after': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.to_datetime
            },
            'participant_ids': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.to_str
            },
            'sort': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
        },
        'method': 'GET',
        'range': 'matches',
        'path': '/tournaments/{tournament_id}/matches',
    },
    'viewer_get_match': {
        'parameters': {
            'tournament_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
        },
        'method': 'GET',
        'range': None,
        'path': '/tournaments/{tournament_id}/matches/{id}',
    },
    'viewer_get_matches_from_discipline': {
        'parameters': {
            'range': {
                'type': ParameterType.HEADER,
                'optional': False,
                'list': False,
                'converter': Converter.range
            },
            'discipline_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'is_featured': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'statuses': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.none
            },
            'scheduled_before': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.to_datetime
            },
            'scheduled_after': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.to_datetime
            },
            'participant_ids': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.to_str
            },
            'tournament_ids': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.to_str
            },
            'sort': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
        },
        'method': 'GET',
        'range': 'matches',
        'path': '/disciplines/{discipline_id}/matches',
    },
    'viewer_get_game': {
        'parameters': {
            'tournament_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'match_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'number': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.none
            },
        },
        'method': 'GET',
        'range': None,
        'path': '/tournaments/{tournament_id}/matches/{match_id}/games/{number}',
    },
    'viewer_get_participants': {
        'parameters': {
            'range': {
                'type': ParameterType.HEADER,
                'optional': False,
                'list': False,
                'converter': Converter.range
            },
            'tournament_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'name': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'sort': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
        },
        'method': 'GET',
        'range': 'participants',
        'path': '/tournaments/{tournament_id}/participants',
    },
    'viewer_get_participant': {
        'parameters': {
            'tournament_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
        },
        'method': 'GET',
        'range': None,
        'path': '/tournaments/{tournament_id}/participants/{id}',
    },
    'viewer_get_playlist': {
        'parameters': {
            'id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
        },
        'method': 'GET',
        'range': None,
        'path': '/playlists/{id}',
    },
    'viewer_get_ranking_items': {
        'parameters': {
            'range': {
                'type': ParameterType.HEADER,
                'optional': False,
                'list': False,
                'converter': Converter.range
            },
            'tournament_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'stage_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'group_ids': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.to_str
            },
            'group_numbers': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.none
            },
        },
        'method': 'GET',
        'range': 'items',
        'path': '/tournaments/{tournament_id}/stages/{stage_id}/ranking-items',
    },
    'viewer_get_rounds': {
        'parameters': {
            'range': {
                'type': ParameterType.HEADER,
                'optional': False,
                'list': False,
                'converter': Converter.range
            },
            'tournament_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'stage_ids': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.to_str
            },
            'stage_numbers': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.none
            },
            'group_ids': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.to_str
            },
            'group_numbers': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.none
            },
        },
        'method': 'GET',
        'range': 'rounds',
        'path': '/tournaments/{tournament_id}/rounds',
    },
    'viewer_get_round': {
        'parameters': {
            'tournament_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
        },
        'method': 'GET',
        'range': None,
        'path': '/tournaments/{tournament_id}/rounds/{id}',
    },
    'viewer_get_stages': {
        'parameters': {
            'tournament_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
        },
        'method': 'GET',
        'range': None,
        'path': '/tournaments/{tournament_id}/stages',
    },
    'viewer_get_stage': {
        'parameters': {
            'tournament_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
        },
        'method': 'GET',
        'range': None,
        'path': '/tournaments/{tournament_id}/stages/{id}',
    },
    'viewer_get_standings': {
        'parameters': {
            'range': {
                'type': ParameterType.HEADER,
                'optional': False,
                'list': False,
                'converter': Converter.range
            },
            'tournament_ids': {
                'type': ParameterType.QUERY,
                'optional': False,
                'list': True,
                'converter': Converter.to_str
            },
            'participant_ids': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.to_str
            },
        },
        'method': 'GET',
        'range': 'items',
        'path': '/standings',
    },
    'viewer_get_streams': {
        'parameters': {
            'tournament_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'range': {
                'type': ParameterType.HEADER,
                'optional': False,
                'list': False,
                'converter': Converter.range
            },
            'match_ids': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.to_str
            },
        },
        'method': 'GET',
        'range': 'streams',
        'path': '/tournaments/{tournament_id}/streams',
    },
    'viewer_get_tournaments_featured': {
        'parameters': {
            'range': {
                'type': ParameterType.HEADER,
                'optional': False,
                'list': False,
                'converter': Converter.range
            },
            'name': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'disciplines': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'statuses': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'scheduled_before': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.to_date
            },
            'scheduled_after': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.to_date
            },
            'countries': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'platforms': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'is_online': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'sort': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
        },
        'method': 'GET',
        'range': 'tournaments',
        'path': '/tournaments/featured',
    },
    'viewer_get_tournament': {
        'parameters': {
            'id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
        },
        'method': 'GET',
        'range': None,
        'path': '/tournaments/{id}',
    },
    'viewer_get_tournaments_by_playlist': {
        'parameters': {
            'range': {
                'type': ParameterType.HEADER,
                'optional': False,
                'list': False,
                'converter': Converter.range
            },
            'id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'name': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'disciplines': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'statuses': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'scheduled_before': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.to_date
            },
            'scheduled_after': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.to_date
            },
            'countries': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'platforms': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'is_online': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'sort': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
        },
        'method': 'GET',
        'range': 'tournaments',
        'path': '/playlists/{id}/tournaments',
    },
    'viewer_get_videos': {
        'parameters': {
            'tournament_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'range': {
                'type': ParameterType.HEADER,
                'optional': False,
                'list': False,
                'converter': Converter.range
            },
            'participant_ids': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': True,
                'converter': Converter.to_str
            },
            'category': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'sort': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
        },
        'method': 'GET',
        'range': 'videos',
        'path': '/tournaments/{tournament_id}/videos',
    },
    'viewer_get_videos_by_match': {
        'parameters': {
            'tournament_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'match_id': {
                'type': ParameterType.PATH,
                'optional': False,
                'list': False,
                'converter': Converter.to_str
            },
            'category': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
            'sort': {
                'type': ParameterType.QUERY,
                'optional': True,
                'list': False,
                'converter': Converter.none
            },
        },
        'method': 'GET',
        'range': None,
        'path': '/tournaments/{tournament_id}/matches/{match_id}/videos',
    },
}
