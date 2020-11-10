import toornament
from tests.local_file import TOKEN

t = toornament.SyncViewerAPI(TOKEN)

print(t.fetch_match(3555729080809455616, '3555734570995318785'))
