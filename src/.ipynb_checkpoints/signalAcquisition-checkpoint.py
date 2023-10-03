#A module that define functions to shh to the rasberry pi's and run commands and get data back to the local PC

import paramiko
import tkinter as tk
from threading import Thread
import os
import sys






def pi1(ip_address="192.168.137.57",console=None):
    console.text.insert(tk.END,f'Connecting {ip_address}...\n')
    try:
        os.system(f"ssh eee3097s@{ip_address} sudo nice -n -20 arecord -D plughw:0 -c2 -r 48000 -f S32_LE -t wav -V stereo -v signal1.wav")
        console.text.insert(tk.END,"Connection established.\n")
    except Exception as e:
        console.text.insert(tk.END,f"Error Occured: {str(e)}\n")


def acquire(console,server_ip,username,password,remote_command,verbose=False):

    """
        Funtion that creates shh client and runs command on the remote machine

    """
    
# Create an SSH client instance
    ssh = paramiko.SSHClient()

# Automatically add the server's host key (this is insecure in production)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        console.text.insert(tk.END,f"Connecting to {username}@{server_ip}...\n")
        ssh.connect(server_ip,username=username,password=password)
        console.text.insert(tk.END,"Connection successfully established.\n")
        console.text.insert(tk.END,f"Runing command: {remote_command}...\n")
        stdin,stdout,stderr=ssh.exec_command(remote_command)
        ssh.close()		#Clone ssh command after
        console.text.insert(tk.END,"Connection closed.\n")
        if verbose:
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
        console.text.insert(tk.END,f"An error occurred: {str(e)}\n")






def main():
	print("Tested!")
if __name__ == '__main__':
	main()