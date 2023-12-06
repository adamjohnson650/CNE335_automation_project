pip install paramiko --user
import paramiko

hostname = '52.32.42.247'
username = 'ubuntu'
key_filename = 'C:\\Users\\ajjoh\\Downloads\\AutomateSSH_Adam_JohnsonKPpem.pem'


update_command = 'sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove && sudo apt-get autoclean'




stdin, stdout, stdout = ssh.exec_command('lsb_release -a')
line = stdout.readline()
while line:
	line = stdout.readline()


ssh_client.close()

