from .functions_dictionary_helper import Converter, ParameterType, ResultConverter
from .viewer_schemas import ViewerSchema as VS


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
        'response': {
            'list': True,
            'converter': VS.BracketNode,
        },
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
        'response': {
            'list': True,
            'converter': VS.CustomField,
        },
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
        'response': {
            'list': True,
            'converter': VS.Discipline,
        },
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
        'response': {
            'list': False,
            'converter': VS.DisciplineDetailed,
        },
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
        'response': {
            'list': True,
            'converter': VS.Group,
        },
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
        'response': {
            'list': False,
            'converter': VS.Group,
        },
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
        'response': {
            'list': True,
            'converter': VS.Match,
        },
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
        'response': {
            'list': False,
            'converter': VS.MatchDetailed,
        },
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
        'response': {
            'list': True,
            'converter': VS.MatchDiscipline,
        },
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
        'response': {
            'list': False,
            'converter': VS.Game,
        },
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
        'response': {
            'list': True,
            'converter': ResultConverter.participant,
        },
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
        'response': {
            'list': False,
            'converter': ResultConverter.participant,
        },
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
        'response': {
            'list': False,
            'converter': VS.Playlist,
        },
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
        'response': {
            'list': True,
            'converter': VS.RankingItem,
        },
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
        'response': {
            'list': True,
            'converter': VS.Round,
        },
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
        'response': {
            'list': False,
            'converter': VS.Round,
        },
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
        'response': {
            'list': True,
            'converter': VS.Stage,
        },
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
        'response': {
            'list': False,
            'converter': VS.Stage,
        },
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
        'response': {
            'list': True,
            'converter': VS.StandingItem,
        },
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
        'response': {
            'list': True,
            'converter': VS.Stream,
        },
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
        'response': {
            'list': True,
            'converter': VS.Tournament,
        },
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
        'response': {
            'list': False,
            'converter': VS.TournamentDetailed,
        },
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
        'response': {
            'list': True,
            'converter': VS.Tournament,
        },
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
        'response': {
            'list': True,
            'converter': VS.VideoTournament,
        },
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
        'response': {
            'list': True,
            'converter': VS.Video,
        },
    },
}
