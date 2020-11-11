import toornament
from tests.local_file import TOKEN
from requests import HTTPError

t = toornament.SyncViewerAPI(TOKEN)

try:
    m = t.get_bracket_nodes(3045919883406483456, 3075364819614916608, range = toornament.Range(0, 4))
except HTTPError as e:
    print(e.response)
else:
    print(m)
