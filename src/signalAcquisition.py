#A module that define functions to shh to the rasberry pi's and run commands and get data back to the local PC

import paramiko
import tkinter as tk


def acquire(console,server_ip,username,password,remote_command,feedback=False):

# Create an SSH client instance
    ssh = paramiko.SSHClient()

# Automatically add the server's host key (this is insecure in production)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
    # Connect to the SSH server
    	console.text.insert(tk.END,f"Connecting to {username}@{server_ip}...\n")
    	ssh.connect(server_ip,username=username,password=password)
    	console.text.insert(tk.END,"Connection successfully established.\n")
    	
    	#Remote command to run python script

    	console.text.insert(tk.END,"Runing command: {remote_command}...\n")

    	#Execute the command on remove server
    	stdin,stdout,stderr=ssh.exec_command(remote_command)

    	ssh.close()		#Clone ssh command after
    	console.text.insert(tk.END,"Connection closed.\n")
    	if feedback:
        
    		console.text.insert(tk.END,"stdin: {stdin}\nstdout:{stdout}\nstderr{stderr}\n")

    except Exception as e:

        console.text.insert(tk.END,f"An error occurred: {str(e)}\n")
    
def transfer_file(console,server_ip, username, password, remote_file_path, local_file_path):
    try:
        # Create an SSH client instance
        ssh = paramiko.SSHClient()
        # Automatically add the server's host key (this is insecure in production)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the SSH server
        console.text.insert(tk.END,f"Connecting to {username}@{server_ip}...\n")
        ssh.connect(server_ip, username=username, password=password)
        console.text.insert(tk.END,"Connection successfully established.\n")

        # Create an SFTP session
        sftp = ssh.open_sftp()

        # Copy the remote file to the local machine
        sftp.get(remote_file_path, local_file_path)
        # Close the SFTP session
        sftp.close()
        console.text.insert(tk.END,f"Transferred file {remote_file_path} to {local_file_path}\n")
        # Close the SSH connection
        ssh.close()
       	console.text.insert(tk.END,"Connection Closed.\n")
    except Exception as e:
    	#print(f'Error: {str(e)}\n')
        console.text.intser(tk.END,f"An error occurred: {str(e)}\n")


def main():
	print("Tested!")
	acquire("10.42.0.179","eee3097s","!@#$%^&*()1234567890","python3 /home/eee3097s/Documents/signalAcquisition.py")
if __name__ == '__main__':
	main()