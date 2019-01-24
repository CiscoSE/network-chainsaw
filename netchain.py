#####################################
# This script is a work in progress
# The Script will be called and given a start IP address to SSH to, A mac address
# The goal functionality will be to connect to a switch,  search for the mac address
# and then determine if the mac is on a local port or on a switch elsewhere in the network
# it will spider  out  using CDP information until it finds the mac address and return the switch name and port 
# where the mac address can be found
# Future versions may add other forms of switch discovery such as LLDP, or an existing network
# Graph or perhaps even spanning tree data
# 
#
#####################################



import getpass
import paramiko
import time
import re
import platform
import datetime


#Login info for First switch to start searching from


username=input("Username : ")
password=getpass.getpass()