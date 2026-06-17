# Scapy Handbook

## Protocol Layers
`/`stacking order according to encapsulation in OSI Model\
`field =...` can be `.field`ed, dont forget (fields behave like obj attributes)
### Ether()
### IP(src, dst, ttl, id, proto, len)
- `src` need not be set as OS kernel or Scapy will choose real outgoing interface IP
- `proto` tells receiving host what protocol is encapsulated inside this IP packet eg. 1 = ICMP, 6 = TCP...
### IPv6
### TCP(sport, dport, seq, ack, flags, window)
- `flags=` S, SA, A, F, R, P, URG
### UDP(sport, dport, len)
### ICMP(type, code)
### DNS(id, qr, opcode, qd, an, rd)
- DNSQR(qname)
- `DNS(qd=DNSQR(qname='google.com'))`
### ARP()
### Raw(load)
- create `Raw(load=b"hello")`
- access `pkt[Raw].load`

## Packet Inspection
- .show()
- .summary()
- hexdump(pkt)

## Accessing Layers
- `if DNS in pkt: pkt[DNS].qd.qname`

## Sending and Receiving Packets
### send()
### sendp()
### sr()

## Sniffing
- pkts = sniff(count=10)
- pkts = sniff(filter="tcp")

## PCAP Handling and PacketList Features
-  `rdpcap("filename")` returns PacketList
- access `packets[0]`
- loop `for packet in packets`
- `packets.summary()`
- `packets.nsummary()`
- `packets.filter()`
- `len(packets)`

## Utility Funcs
- ls()
- fuzz()