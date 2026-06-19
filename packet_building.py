from scapy.all import TCP, IP, ICMP

p = IP(dst="8.8.8.8")/TCP(dport=12)
p[TCP].dport = 35

### ICMP Ping
ping = IP(dst="8.8.8.8")/ICMP()

### TCP SYN
syn = IP(dst="google.com")/TCP(dport=80, flags="S")
