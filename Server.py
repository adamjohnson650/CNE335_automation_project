import subprocess

class Server:


    def __init__(self, server_ip):
        self.server_ip = server_ip

    def ping(self):

        command = ['ping', '-n', '4', self.server_ip]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, _ = process.communicate()
        if process.returncode == 0:
            return f"Server {self.server_ip} is reachable."
        else:
            return f"Server {self.server_ip} is unreachable."
