#**SSH Client/Server**

#*Rasperry Pi SSH Server*
# This is useful to access your Raspberry Pi without connecting it to a monitor/keyboard
# ssh server is runnign by default on your Raspberry Pi
# Should change the private host ID keys
#   -Otherwise, they have the same default values

>> sudo rm /etc/ssh/shh_host_* && sudo dpkg-reconfigure openssh-server
