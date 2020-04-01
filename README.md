### ARP

Address Resolution Protocol (ARP)
→ Simple protocol used to map IP Address of a machine to its MAC address.

→ What we actually happens in ARP spoof is we exploit the ARP protocol as it’s not secure.

Lets imagine a basic connection were there is an access point(gateway) and 2 systems hacker and client systems. We tell the router that I have the victims ip and router will update it’s arptable. And we will say the victim system that I am the access point I have the ip of router. Then it will update the arptable. what they actually update is the macadress of the hacker system in both the cases. Hence we become the man in the middle );
Why ARP spoofing is possible?
  ->Clients accept the responses even if they didn’t send a request.
When hacker system says I am at the victims IP router simply accepts it without any verification. Router doesn’t asks who am I if it would have asked my ip would be different than victim.Neither does the victim.
  ->Clients trust any responses without any form of verification.


Requirements-: scapy(2.4.0) or higher

To run this type -: python3 ArpSpoofDetector.py
