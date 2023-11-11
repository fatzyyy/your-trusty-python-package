import ipaddress
import requests


class NetUtils:
    def ip_info(ip: str) -> tuple:
        """
        This method displays information about private ip addresses.

        Args:
            ip: ip-address in addr/prefix format
            prefix: netmask

        Returns:
            first_ip, last_ip (tuple): for ip ranges
            net_address, broadcast_address: for single ip subnets
        """
        network = ipaddress.ip_network(ip, strict=False)
        all_ips = list(network.hosts())

        print(f"Details for {ip}")

        if all_ips:
            print(f"Input type: IP range")
            first_ip = str(all_ips[0])
            last_ip = str(all_ips[-1])
            print(f"Range: {first_ip} - {last_ip}")
            return first_ip, last_ip
        else:
            net_address = str(network.network_address)
            broadcast_address = str(network.broadcast_address)
            print(f"Input type: Single IP-address")
            print("Detals:")
            print(f"Network address: {net_address}")
            print(f"Broadcast address: {broadcast_address}")
            return net_address, broadcast_address


    def public_ip_info() -> dict:
        """
        This method enables automatic detection of a public IP-address.
        and retrieval of supporting information for the address.

        Args:
            None

        Returns:
            ip_info (dict): dictionary with details of a public IP-address
            detected for your active Internet connection.
        """

        pip = requests.get("https://api.ipify.org/?format=json").json()
        pip_country = requests.get(f"https://api.country.is/{pip['ip']}").json()
        pip_geo = requests.get(f"https://get.geojs.io/v1/ip/geo.json").json()

        ip_info = {
            "pip": pip["ip"],
            "country": pip_country["country"],
            "region": pip_geo["region"],
            "organization": pip_geo["organization"],
            "organization_name": pip_geo["organization_name"]
        }
        return ip_info
