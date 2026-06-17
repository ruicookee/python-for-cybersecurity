''' Active Scanning
identification of potential target systems, discovery of vulnerable applications;
learning a target network architecture —
port scanning, banner collectioni, vulnerability scanning
'''
from scapy.all import *
packetlist = rdpcap('/Users/keiratan/Desktop/Cybersec/python-for-cybersec/pcap-files/http.cap')
print(packetlist)
# <http.cap: TCP:41 UDP:2 ICMP:0 Other:0>
# returns a PacketList
packet0 = packetlist[0]
packet1 = packetlist[1]
packet2 = packetlist[2]
packet3 = packetlist[3]
print(packet0.summary()) #TCP flag: S (syn)
print(packet1.summary()) #TCP flag: SA
print(packet2.summary()) #TCP flag: A
print(packet3.summary())  #TCP flag: PA (push data instad of waiting), RAW (payload)