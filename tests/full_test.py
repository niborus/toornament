import toornament
from tests.local_file import TOKEN

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

res = t.get_disciplines(range = toornament.Range(0,4))
print(res)

res = t.get_discipline('splatoon2')
print(res)
