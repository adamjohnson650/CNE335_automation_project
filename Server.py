import os
import paramiko  #added

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def get_server_ip(self):
        return self.server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        response = os.system("ping -n 1 -w 5 " + self.server_ip)
        if response == 0:
            return (self.server_ip + "is up and running")
        else:
            return (self.server_ip + "is down.")

    def update(self):   #added here down
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.server_ip,
                    username='ubuntu',
                    key_filename=r""C:\Users\ajjoh\Downloads\AutomateSSH_Adam_JohnsonKPpem.pem")

        update_command = 'sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove && sudo apt-get autoclean'

        stdin, stdout, stdout = ssh.exec_command(update_command)
        line = stdout.readline()
        while line:
            print(line)
            line = stdout.readline()

        ssh.close()
