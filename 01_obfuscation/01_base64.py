"""
import socket
import json

data = {'Hi': 'there'}
data_string = json.dumps(data)
data_bytes = data_string.encode('utf-8')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8080))
s.sendall(b'POST / HTTP/1.1\\r\\nHost: 127.0.0.1:8080\\r\\nContent-Type: application/json\\r\\nContent-Length: ' + str(len(data_bytes)).encode('utf-8') + b'\\r\\n\\r\\n' + data_bytes)
s.close()
"""

import base64
exec(base64.b64decode(b'=oQKoU2cvx2YuMnCpMXZ0lnYfFGdhRGIrAyJuxlcc5GXyx1JiByKgkyJ40iZ0V3JoUGZvNmbl5SKpMXZ0lnYfFGdhRGKuVGboIHdzByKgcCI6gGdn5WZM1CduVGdu92Quxlcc52bzp2Lu9Wa0F2YpxGcwFGI6UGc5RVL05WZ052bD5GXyxFM4ADO6AjLw4CMuADI6Q3cvhkbcJHXx4SMvAFVUhEIvACVT9EUnIGKsxWYk5WZz5ycKkSKwgDM4ACLnAjLw4CMuAzJogCdjVmbu92YuMnCp0UQFJFVT91SD90UuQXZrN2bzBCLUVkTJ9lRB5Cdlt2YvNHK0V2aj92cuQXZrN2bzBSPgMnCKkyJ40iZ0V3JoUGZvNmbl5yZulmc0N3XhRXYkBSPgMXZ0lnYfFGdhRmCpEGdhRGKzBXb1RmLu92cqBSPgcmbpJHdz9VY0FGZK03JlJXZoR3JgozJph0J7BSPgEGdhRmCK42bzpGI0J3bw1WaKQXZrN2bzBCdy9GctlmC'[::-1]).decode('utf-8'))
