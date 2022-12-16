ftpServerIp = "192.168.1.1"
#s - supplier
#c - CI_name
#o - OS file name
#d - directory of the config file

def ciscoC(c,o,d):
    ipAdd = "enable\nconfigure terminal\ninterface vlan 1\nip address dhcp\nno shutdown\nend\ndir\ndel flash:\n\n"
    osDownload = f"copy tftp://{ftpServerIp}/{o} flash:\n"
    license = f"license install tftp://{ftpServerIp}/licenses/.lic\n"
    c_dwnld = f"copy tftp://{ftpServerIp}/customer-conf/{d}/{c}.cfg startup-config\n"
    full_config = f"\n{ipAdd+osDownload}\n{license}\n{c_dwnld}"
    return full_config

def oneAccess(c,o,d):
    ipAdd = "conf t\nint GigabitEthernet 0/0\nip add dhcp\nend\n\n"
    osDownload = f"copy tftp://{ftpServerIp}/{o} flash:\n"
    full_config = f"\n\nUsername/Password: admin\n\n"+ipAdd+osDownload
    return full_config

def generateConfiguration(s,c,o,d):
    if s == "Cisco":
        config = ciscoC(c,o,d)
        return config
    elif s =="OneAccess":
        config = oneAccess(c,o,d)
        return config
    else:
        error_msg = "Config is not in the database"
        return error_msg
    

#def oneAccessC(c,o,d):
