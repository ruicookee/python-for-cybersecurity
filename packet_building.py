from scapy.all import TCP, IP

p = IP(dst="8.8.8.8")/TCP(dport=12)
p[TCP].dport = 35