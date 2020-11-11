import toornament
from tests.local_file import TOKEN

t = toornament.SyncViewerAPI(TOKEN)

# Testing
m = t.get_matches_from_tournament(3045919883406483456, range = toornament.Range(0, 9))
print(m)

m = t.get_match(3045919883406483456, 3075364820084678691)
print(m)

m = t.get_matches_from_discipline('splatoon2', range = toornament.Range(0, 9))
print(m)
