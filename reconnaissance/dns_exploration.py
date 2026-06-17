import dns
import dns.resolver
import socket
import dns.exception

def reverse_dns(ip):
    try:
        result = socket.gethostbyaddr(ip)
    except:
        return []
    else:
        return [result[0]] + result[1]

def dns_request(domain):
    try:
        result = dns.resolver.resolve(domain, "A") #this can return multiple IPs of A records
        if result:
            print(domain) #because domain name can have multiple A records
            #why? load balanceing, redundancy, geographic distribution
            for arecordip in result:
                print(arecordip)
                print(f"Domain Names: {reverse_dns(arecordip.to_text())}")
                #then again, each of these IPs returns one PTR (pointer record)
                #why are we looking at PTRs?????
                #PTRs are not the inverse of forward DNS lookups, so you get a diff result
                #PTRs tell you What hostname is associated with this IP address in reverse DNS
                # tbj idk what the heck is the point of knowing the pTR for a particular IP??? bruh
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout, dns.resolver.NoAnswer):
        return

def subdomain_search(root, lst, nums: bool):
    successes = []
    for subdomain in lst:
        domain = subdomain + "." + root
        dns_request(domain)
        if nums:
            for i in range(0,10):
                numbered_domain = subdomain+str(i)+"."+root
                dns_request(numbered_domain)

root = "google.com"
d = "/Users/keiratan/Desktop/Cybersec/python-for-cybersec/additional-files/subdomains.txt"

with open(d, "r") as f:
    lst =[line.strip() for line in f]

subdomain_search(root, lst, True)