import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='52.32.42.247',
            username='ubuntu',
            key_filename=r":\Users\ajjoh\Downloads\AutomateSSH_Adam_JohnsonKPpem.pem")

update_command = 'sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove && sudo apt-get autoclean'


stdin, stdout, stdout = ssh.exec_command(update_command)
line = stdout.readline()
while line:
    print(line)
    line = stdout.readline()


ssh.close()

