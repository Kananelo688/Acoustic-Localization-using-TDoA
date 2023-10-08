#A module that define functions to shh to the rasberry pi's and run commands and get data back to the local PC

import paramiko
import tkinter as tk
from threading import Thread
import os
import sys
import subprocess
import time

def reboot(console,server_ip,username,password,no,eventHandler=None):

    """
        Funtion that creates shh client and runs command on the remote machine

    """
    
# Create an SSH client instance
    ssh = paramiko.SSHClient()

# Automatically add the server's host key (this is insecure in production)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        console.text.insert(tk.END,f"Rebooting machine:{server_ip}...\n")
        ssh.connect(server_ip,username=username,password=password)
        stdin,stdout,stderr=ssh.exec_command("sudo reboot")
        ssh.close()     #Clone ssh command after
        console.text.insert(tk.END,f"Machine:{server_ip} successfully rebooted.\n")
        if no==1:
            eventHandler.flag1=True
        else:
            eventHandler.flag2=True

    except Exception as e:
        console.text.insert(tk.END,f"Error occurred: {str(e)}\n")




def start(console,server_ip,username,password):

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
        console.text.insert(tk.END,f"Preparing for acquisition...\n")
        stdin,stdout,stderr=ssh.exec_command("python3 /home/eee3097s/start.py")
        ssh.close()		#Clone ssh command after
        console.text.insert(tk.END,f"Preparation done, Machine({server_ip}) ready to sample.\n")

    except Exception as e:
        console.text.insert(tk.END,f"Error occurred: {str(e)}\n")

def getData(console,server_ip, username, password, remote_file_path, local_file_path):
    try:
        # Create an SSH client instance
        ssh = paramiko.SSHClient()
        # Automatically add the server's host key (this is insecure in production)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the SSH server
        console.text.insert(tk.END,f"Connecting to {username}@{server_ip}...\n")
        ssh.connect(server_ip, username=username, password=password)
        console.text.insert(tk.END,"Connection established.\n")

        # Create an SFTP session
        console.text.insert(tk.END,f"Transferring data from machine:{server_ip}...\n")

        sftp = ssh.open_sftp()

        # Copy the remote file to the local machine
        sftp.get(remote_file_path, local_file_path)
        # Close the SFTP session
        sftp.close()
        console.text.insert(tk.END,f"Data transfer from machine: {server_ip} complete.\n")
        # Close the SSH connection
        ssh.close()
    except Exception as e:
    	#print(f'Error: {str(e)}\n')
        console.text.insert(tk.END,f"An error occurred: {str(e)}\n")



def main():
    pass
	
if __name__ == '__main__':
	main()