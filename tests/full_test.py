import toornament
from tests.local_file import TOKEN
import asyncio


class TestFailed(Exception):
    """Test failed"""
    pass


def sync_test():
    t = toornament.SyncViewerAPI(TOKEN)

    # Testing
    res = t.get_matches_from_tournament(3045919883406483456, range = toornament.Range(0, 9))
    print(res)

    res = t.get_match(3045919883406483456, 3075364820084678691)
    print(res)

    res = t.get_matches_from_discipline('splatoon2', range = toornament.Range(0, 9))
    print(res)

    res = t.get_bracket_nodes(3045919883406483456, 3075364819614916608, range = toornament.Range(0, 4))
    print(res)

    res = t.get_custom_fields(3555729080809455616)
    print(res)

    res = t.get_disciplines(range = toornament.Range(0, 4))
    print(res)

    res = t.get_discipline('splatoon2')
    print(res)

    res = t.get_groups(3555729080809455616, range = toornament.Range(0, 4))
    print(res)

    res = t.get_group(3555729080809455616, 3555734570961764352)
    print(res)

    res = t.get_game(3045919883406483456, 3075364820084678691, 1)
    print(res)

    res = t.get_participant(3045919883406483456, 3046102039785750528)
    print(res)

    res = t.get_participants(1755617972580818944, range = toornament.Range(0, 4))
    print(res)

    res = t.get_playlist(4092769699448848384)
    print(res)

    # Normal Ranking Items Properties
    res = t.get_ranking_items(3555729080809455616, 4092841286829129728, range = toornament.Range(0, 2))
    print(res)

    # Ranking Items Properties with Score
    res = t.get_ranking_items(3555729080809455616, 4092864627355385856, range = toornament.Range(0, 2))
    print(res)

    res = t.get_rounds(3555729080809455616, range = toornament.Range(0, 2))
    print(res)

    res = t.get_round(3555729080809455616, 3555734570995318830)
    print(res)

    res = t.get_stages(3555729080809455616)
    print(res)

    res = t.get_stage(3555729080809455616, 3555733280880140288)
    print(res)

    res = t.get_standings(range = toornament.Range(0, 9), tournament_ids = [3555729080809455616, '1755617972580818944'])
    print(res)

    res = t.get_videos(3555729080809455616, range = toornament.Range(0, 49))
    print(res)

    res = t.get_videos_by_match(3555729080809455616, 3555734570995318785)
    print(res)

    res = t.get_streams(1755617972580818944, range = toornament.Range(0, 1))
    print(res)

    res = t.get_tournaments_featured(range = toornament.Range(0, 4), disciplines = 'splatoon2')
    print(res)

    res = t.get_tournament(1755617972580818944)
    print(res)

    res = t.get_tournaments_by_playlist(4092769699448848384, range = toornament.Range(0, 2))
    print(res)

    print(toornament.Information.fetch_platforms())


async def async_test():
    t = toornament.AsyncViewerAPI(TOKEN)

    # Testing
    res = await t.get_matches_from_tournament(3045919883406483456, range = toornament.Range(0, 9))
    print(res)

    res = await t.get_match(3045919883406483456, 3075364820084678691)
    print(res)

    res = await t.get_matches_from_discipline('splatoon2', range = toornament.Range(0, 9))
    print(res)

    res = await t.get_bracket_nodes(3045919883406483456, 3075364819614916608, range = toornament.Range(0, 4))
    print(res)

    res = await t.get_custom_fields(3555729080809455616)
    print(res)

    res = await t.get_disciplines(range = toornament.Range(0, 4))
    print(res)

    res = await t.get_discipline('splatoon2')
    print(res)

    res = await t.get_groups(3555729080809455616, range = toornament.Range(0, 4))
    print(res)

    res = await t.get_group(3555729080809455616, 3555734570961764352)
    print(res)

    res = await t.get_game(3045919883406483456, 3075364820084678691, 1)
    print(res)

    res = await t.get_participant(3045919883406483456, 3046102039785750528)
    print(res)

    res = await t.get_participants(1755617972580818944, range = toornament.Range(0, 4))
    print(res)

    res = await t.get_playlist(4092769699448848384)
    print(res)

    # Normal Ranking Items Properties
    res = await t.get_ranking_items(3555729080809455616, 4092841286829129728, range = toornament.Range(0, 2))
    print(res)

    # Ranking Items Properties with Score
    res = await t.get_ranking_items(3555729080809455616, 4092864627355385856, range = toornament.Range(0, 2))
    print(res)

    res = await t.get_rounds(3555729080809455616, range = toornament.Range(0, 2))
    print(res)

    res = await t.get_round(3555729080809455616, 3555734570995318830)
    print(res)

    res = await t.get_stages(3555729080809455616)
    print(res)

    res = await t.get_stage(3555729080809455616, 3555733280880140288)
    print(res)

    res = await t.get_standings(range = toornament.Range(0, 9), tournament_ids = [3555729080809455616, '1755617972580818944'])
    print(res)

    res = await t.get_videos(3555729080809455616, range = toornament.Range(0, 49))
    print(res)

    res = await t.get_videos_by_match(3555729080809455616, 3555734570995318785)
    print(res)

    res = await t.get_streams(1755617972580818944, range = toornament.Range(0, 1))
    print(res)

    res = await t.get_tournaments_featured(range = toornament.Range(0, 4), disciplines = 'splatoon2')
    print(res)

    res = await t.get_tournament(1755617972580818944)
    print(res)

    res = await t.get_tournaments_by_playlist(4092769699448848384, range = toornament.Range(0, 2))
    print(res)


def internal_test():
    pass

# Test Sync Access
sync_test()

# Test Async Access
loop = asyncio.get_event_loop()
res = loop.run_until_complete(async_test())

# Test internal functions
internal_test()
