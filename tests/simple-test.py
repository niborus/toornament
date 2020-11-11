import toornament
from tests.local_file import TOKEN
from requests import HTTPError

t = toornament.SyncViewerAPI(TOKEN)

try:
    r = toornament.Range(0, 50)
    m = t.get_matches_from_discipline(3555729080809455616, range = toornament.Range(0, 50))
except HTTPError as e:
    print(e.response.json())
else:
    print(m)
