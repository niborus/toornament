# toornament.py
A wrapper for the toornament.org API (https://developer.toornament.com/v2/overview/get-started).

**Note: At the moment you can only use the Viewer-API. New APIs get integrated in the wrapper over time.**

## Getting started

### Available APIs

To start, create a new Toornament-Connector for the API you want to request. There are eight APIs in Theory, but only two of them are implemeted yet.

|                 | Asynchron Functions   | Synchron Functions    |
| --------------- | --------------------- | --------------------- |
| Viewer API      | AsyncViewerAPI        | SyncViewerAPI         |
| Organizer API   | *not implemented yet* | *not implemented yet* |
| Participant API | *not implemented yet* | *not implemented yet* |
| Account API     | *not implemented yet* | *not implemented yet* |

### Using Toornament-Connectors

In this example, you create a Connector for the Synchron Viewer API:

````python
import toornament

connector = toornament.SyncViewerAPI('X-API Key')
````

Once you created a connector, you can access the Data via the Methodes of the Connector:

````python
import toornament
connector = toornament.SyncViewerAPI('X-API Key')

my_tournament = connector.get_tournament(10000000000000)
````

 If you are using  a Asynch connector, you have to await these Methodes. But they have the same arguments and return the same values.

````python
import toornament
connector = toornament.AsyncViewerAPI('X-API Key')

async def foo():
	my_tournament = await connector.get_tournament(10000000000000)
````

### Using Range

Some Endpoints require you to provide a Range. You have to do this by providing a Range-Object.

```python
from toornament import SyncViewerAPI, Range
connector = toornament.SyncViewerAPI('X-API Key')

my_tournament = connector.get_matches(10000000000000, range=Range(0,49))
```

## Viewer API

### Endpoints

The Methods are using the same parameter as the official API-Doc. 

- Path parameters are positional arguments. They are always required.

- If the Method takes a *range*, it is required. Ranges must be provided as keyword argument. `.foo(range=toornament.Range(x,y))`.

- Query Parameters are keyword arguments. They use the same names.

| Method                        | Range? | Returns                                          | Documentation                                                |
| ----------------------------- | ------ | ------------------------------------------------ | ------------------------------------------------------------ |
| `get_match`                   | N      | MatchDetailed                                    | [here](https://developer.toornament.com/v2/doc/viewer_matches#get:tournaments:tournament_id:matches:id) |
| `get_matches_from_tournament` | Y      | Array[Match]                                     | [here](https://developer.toornament.com/v2/doc/viewer_matches#get:tournaments:tournament_id:matches) |
| `get_matches_from_discipline` | Y      | Array[MatchDiscipline]                           | [here](https://developer.toornament.com/v2/doc/viewer_matches#get:disciplines:discipline_id:matches) |
| `get_bracket_nodes`           | Y      | Array[BracketNode]                               | [here](https://developer.toornament.com/v2/doc/viewer_bracket_nodes#get:tournaments:tournament_id:stages:stage_id:bracket-nodes) |
| `get_custom_fields`           | N      | Array[CustomField]                               | [here](https://developer.toornament.com/v2/doc/viewer_custom_fields#get:tournaments:tournament_id:custom-fields) |
| `get_disciplines`             | Y      | Array[Discipline]                                | [here](https://developer.toornament.com/v2/doc/viewer_disciplines#get:disciplines) |
| `get_discipline`              | N      | DisciplineDetailed                               | [here](https://developer.toornament.com/v2/doc/viewer_disciplines#get:disciplines:id) |
| `get_groups`                  | Y      | Array[Group]                                     | [here](https://developer.toornament.com/v2/doc/viewer_groups#get:tournaments:tournament_id:groups) |
| `get_group`                   | N      | Group                                            | [here](https://developer.toornament.com/v2/doc/viewer_groups#get:tournaments:tournament_id:groups:id) |
| `get_game`                    | N      | Game                                             | [here](https://developer.toornament.com/v2/doc/viewer_match_games#get:tournaments:tournament_id:matches:match_id:games:number) |
| `get_participants`            | Y      | Array[Union[ParticipantPlayer, ParticipantTeam]] | [here](https://developer.toornament.com/v2/doc/viewer_participants#get:tournaments:tournament_id:participants) |
| `get_participant`             | N      | Union[ParticipantPlayer, ParticipantTeam]        | [here](https://developer.toornament.com/v2/doc/viewer_participants#get:tournaments:tournament_id:participants:id) |
| `get_playlist`                | N      | Playlist                                         | [here](https://developer.toornament.com/v2/doc/viewer_playlists#get:playlists:id) |
| `get_ranking_items`           | Y      | Array[RankingItem]                               | [here](https://developer.toornament.com/v2/doc/viewer_ranking_items#get:tournaments:tournament_id:stages:stage_id:ranking-items) |
| `get_rounds`                  | Y      | Array[Round]                                     | [here](https://developer.toornament.com/v2/doc/viewer_rounds#get:tournaments:tournament_id:rounds) |
| `get_round`                   | N      | Round                                            | [here](https://developer.toornament.com/v2/doc/viewer_rounds#get:tournaments:tournament_id:rounds:id) |
| `get_stages`                  | N      | Array[Stage]                                     | [here](https://developer.toornament.com/v2/doc/viewer_stages#get:tournaments:tournament_id:stages) |
| `get_stage`                   | N      | Stage                                            | [here](https://developer.toornament.com/v2/doc/viewer_stages#get:tournaments:tournament_id:stages:id) |
| `get_standings`               | Y      | Array[StandingItem]                              | [here](https://developer.toornament.com/v2/doc/viewer_standings#get:standings) |
| `get_streams`                 | Y      | Array[Stream]                                    | [here](https://developer.toornament.com/v2/doc/viewer_streams#get:tournaments:tournament_id:streams) |
| `get_videos`                  | Y      | Array[VideoTournament]                           | [here](https://developer.toornament.com/v2/doc/viewer_videos#get:tournaments:tournament_id:videos) |
| `get_videos_by_match`         | N      | Array[Video]                                     | [here](https://developer.toornament.com/v2/doc/viewer_videos#get:tournaments:tournament_id:matches:match_id:videos) |
| `get_tournaments_featured`    | Y      | Array[Tournament]                                | [here](https://developer.toornament.com/v2/doc/viewer_tournaments#get:tournamentsfeatured) |
| `get_tournament`              | N      | TournamentDetailed                               | [here](https://developer.toornament.com/v2/doc/viewer_tournaments#get:tournaments:id) |
| `get_tournaments_by_playlist` | Y      | Array[Tournament]                                | [here](https://developer.toornament.com/v2/doc/viewer_tournaments#get:playlists:id:tournaments) |

