import toornament
from tests.local_file import TOKEN
from requests import HTTPError

t = toornament.SyncViewerAPI(TOKEN)

try:
    m = t.get_matches_from_discipline('splatoon2', range = toornament.Range(0, 4))
except HTTPError as e:
    print(e.response)
else:
    print(m)
