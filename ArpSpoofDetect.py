from scapy.all import *
import re
import subprocess


class ArpSpoofDetect:

    def arp_detect(self):
        gateway_mac = self.gateway_ip_mac()[1]
        arp_gateway_mac = self.arp_gateway_mac()
        if gateway_mac == arp_gateway_mac:
            print("[+] PC is safe from ARP spoofing.")
        else:
            print("[-] This PC is ARP poisoned. Use VPN.")
            print("AP's MAC\t\t\t", "Hacker's MAC")
            print("------------------------------------------------")
            print(gateway_mac+"\t\t"+arp_gateway_mac)
            print("Turning off wifi/ethernet")
            subprocess.call(["nmcli", "r", "wifi", "off"])

    @staticmethod
    def gateway_ip_mac():
        gateway_ip = conf.route.route("0.0.0.0")[2]
        gateway_mac = getmacbyip(gateway_ip)
        return [gateway_ip, gateway_mac]

    @staticmethod
    def arp_gateway_mac():
        arp_result_list = subprocess.check_output(["arp", "-a"]).decode().splitlines()
        if not arp_result_list:
            print("There is no internet connection to this PC.")
            exit()
        arp_result = ""
        for ele in arp_result_list:
            if "_gateway" in ele:
                arp_result = ele
                break
        arp_gateway_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", arp_result)
        return arp_gateway_mac.group(0)


obj = ArpSpoofDetect()
obj.arp_detect()
