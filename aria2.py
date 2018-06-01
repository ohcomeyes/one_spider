import xmlrpc.client
from pprint import pprint


s = xmlrpc.client.ServerProxy("http://localhost:6800/rpc")
r = s.aria2.addUri(["http://qnvideo.ixiaochuan.cn/zyvd/ad/6d/7f12-a2a0-11e7-b6af-00163e06c279"])
print(r)