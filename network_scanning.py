'''Nmap Scan
diagnostic process to discover devices, map out networks topology,
find open ports or security vulnerabilities
'''
from scapy.all import IP, TCP, UDP, sr, DNS, DNSQR

ports = [25, 80, 53, 443, 445, 8080, 8443]

def syn_scan(host): #sr() sends out packers and waits for replies
    ans, unans = sr(IP(dst=host)/TCP(sport=5555, dport=ports, flags="S"), timeout=2, verbose=0)
    #(<Results: TCP:2 UDP:0 ICMP:0 Other:0>, <Unanswered: TCP:5 UDP:0 ICMP:0 Other:0>)
    for send, receive in ans:
        if send[TCP].dport == receive[TCP].sport:
            print(receive[TCP].sport) #can see that they are all "SA"s 

def dns_scan(host):
    packet = IP(dst=host)/UDP(sport=5555, dport=53)/DNS(rd=1, qd=DNSQR(qname="google.com"))
    ans, unans = sr(packet, timeout=5, verbose=0)
    if ans:
        print(f"DNS Server at {host}") # will get ans if DNS service is running on that host
        #if None, it could mean no DNS serveice running, or wrong port, or firewall/packet filtering, or packet never reached
host = "8.8.8.8"
syn_scan(host)
dns_scan(host)