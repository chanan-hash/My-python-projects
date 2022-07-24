# All of the code here is base on youtube video of David Bomal
# https://www.youtube.com/watch?v=SzYKzAHsdMg&t=530s
# The code in github https://github.com/davidbombal/red-python-scripts/blob/main/windows10-wifi.py
# Import subprocess so we can use python commands
import subprocess

# Import the re module so that we can make use of regular expression
import re

# here we are attaching/assigning the commands we wants to put in the cmd to a variable
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

# we are looknig for what we will have int the output of the command above
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

# we're going to grab all profile names and store it in a list
wifi_list = list() # we've created an empty list

# for every name in the profile name we are going to create a dictionary to see every profile with is password
if len(profile_names) !=0:
    for name in profile_names:
        wifi_profile = dict()
        profile_info = subprocess.run(["netsh","wlan","show","profile", name], capture_output = True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(["netsh","wlan","show","profile",name,"key=clear"], capture_output= True).stdout.decode()
            password = re.search("Key Content            : (.*)\r",profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile)

# We want to print the list we have, to see it.
for x in range(len(wifi_list)):
    print(wifi_list[x])
