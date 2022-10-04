"""
Name: git-init.py
Discription: This script is used to initialize a git environment.
Usage: python3 git-init.py
Author: hdaojin
Version: 1.0
Date: 2022-10-4
Update: 2022-10-4
"""

import os
import sys
import platform
from pathlib import Path

# Check if the git is installed
def check_git():
    """
    Check if the git is installed
    """
    if os.system("git --version") != 0:
        print("Please install git first!")
        sys.exit(1)
    print("git is installed!")

# Check if the ssh package is installed
def check_ssh():
    """
    Check if the ssh package is installed
    """
    if os.system("ssh -V") != 0:
        print("Please install ssh first!")
        sys.exit(1)
    print("ssh is installed!")

# Configure git user name and email
def configure_git(name, mail):
    """
    Configure git user name and email
    """
    os.system("git config --global user.name " + name)
    os.system("git config --global user.email " + mail)
    print("git user name and email is configured!")

# Generate ssh key
def generate_ssh_key(mail):
    """
    Generate ssh key
    """
    ssh_key_file = Path.home() / ".ssh/id_ed25519"
    ssh_pub_key_file = Path.home() / ".ssh/id_ed25519.pub"
    if not ssh_key_file.exists() or not ssh_pub_key_file.exists():
        os.system("ssh-keygen -t ed25519 -C " + mail)
    print("ssh key is generated!")
    return ssh_key_file, ssh_pub_key_file

# Set ssh client config
def set_ssh_client_config(name, ssh_key_file):
    """
    Set ssh client config
    """
    ssh_config_file = Path.home() / ".ssh/config"
    with open(ssh_config_file, "a+") as f:
        f.write("\n")
        f.write("Host github.com\n")
        f.write("    HostName github.com\n")
        f.write("    Port 22\n")
        f.write("    User " + name + "\n")
        f.write("    IdentityFile " + str(ssh_key_file) + "\n")
    print("ssh client config is set!")


    
# Copy ssh public key to clipboard
def copy_ssh_pub_key(ssh_pub_key_file):
    """
    Copy ssh public key to clipboard
    """
    if os_platform == "Windows":
        os.system("clip < " + str(ssh_pub_key_file))
    elif os_platform == "Linux":
        os.system("xclip -sel clip < " + str(ssh_pub_key_file))
    elif os_platform == "Darwin":
        os.system("pbcopy < " + str(ssh_pub_key_file))
    print("ssh public key is copied to clipboard!")
    print("If not work, please copy it manually: \n")
    print(ssh_pub_key_file.read_text())
    
# Main function
def main():
    """
    Main function
    """
    check_git()
    check_ssh()
    name = input("Please input your name: ")
    mail = input("Please input your email: ")
    configure_git(name, mail)
    ssh_key_file, ssh_pub_key_file = generate_ssh_key(mail)
    set_ssh_client_config(name, ssh_key_file)
    copy_ssh_pub_key(ssh_pub_key_file)
    print("""Next,
             1. Login your github account;
             2. Click "Settings" -> "SSH and GPG keys" -> "New SSH key";
    """)

if __name__ == "__main__":
    # Check system platform
    if platform.system() == "Windows":
        os_platform = "Windows"
    elif platform.system() == "Linux":
        os_platform = "Linux"
    elif platform.system() == "Darwin":
        os_platform = "Darwin"
    else:
        print("This script only supports Windows, Linux and MacOS!")
        sys.exit(1)
    main()