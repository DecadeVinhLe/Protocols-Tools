import paramiko

def examine_last(server, connection):
     command = "sudo last"
     expected = ["user1", "reboot", "root", "sys-admin"]
     _stdin, stdout, _stderr = connection.exec_command("sudo last")
     lines = stdout.read().decode()
     connection.close()
     for line in lines.split("\n"):
           # Ignore the last line of the last report.
         if line.startswith("wtmp begins"):
             break
         parts = line.split()
         if parts:
             account = parts[0]
             if not account in EXPECTED:
                 print(f"Entry '{line}' is a surprise on {server}.")

def key_based_connect(server):
     host = "192.0.2.0"
     special_account = "user1"
     pkey = paramiko.RSAKey.from_private_key_file("./id_rsa")
     client = paramiko.SSHClient()
     policy = paramiko.AutoAddPolicy()
     client.set_missing_host_key_policy(policy)
     client.connect(host, username=special_account, pkey=pkey)
     return client

def main():
     server_list = ["worker1", "worker2", "worker3"]
     for server in server_list:
         connection = key_based_connect(server)
         examine_last(server, connection)

main()