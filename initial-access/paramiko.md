# Paramiko Handbook

## Basic Password Login
- `ssh = paramiko.SSHClient()`
- `ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())` controls what happens with uknown hosts, auto trusts
- `ssh.connec(hostname="example.com", username="user", password="pass")`

## sftp = ssh.open_sftp()
- simple file transfer protocol
