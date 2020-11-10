import toornament
from tests.local_file import TOKEN

t = toornament.SyncViewerAPI(TOKEN)

m = t.get_match(3555729080809455616, '3555734570995318785')

print(m)
