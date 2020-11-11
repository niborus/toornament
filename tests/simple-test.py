import toornament
from tests.local_file import TOKEN
from requests import HTTPError

t = toornament.SyncViewerAPI(TOKEN)

try:
    m = t.get_custom_fields(3555729080809455616)
except HTTPError as e:
    print(e.response)
else:
    print(m)
