#!/usr/bin/env python

import subprocess
import optparse
import re

def getArgs():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='INTERFACE',
                      help='used to specify interface which mac add you want to change')
    parser.add_option('-m', '--mac', dest='MAC_ADDRESS', help='used to specify new Mac Add')
    (options, arguments) = parser.parse_args()
    if not options.INTERFACE:
        parser.error('please specify an interface , use -h for help')
    elif not options.MAC_ADDRESS:
        parser.error('please specify a new mac, use -h for help')
    return options

def MacChanger(interface,newMac):
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', newMac])
    subprocess.call(['ifconfig', interface, 'up'])

ifconfig_result = subprocess.check_output(['ifconfig', getArgs().INTERFACE])
searchedMac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

MacChanger(getArgs().INTERFACE, getArgs().MAC_ADDRESS)
if searchedMac :
    if searchedMac != getArgs().MAC_ADDRESS:
        print('[+] MAC ADDRESS CHANGED FROM ' + searchedMac.group(0) + ' to ' + getArgs().MAC_ADDRESS)
else :
    print('[+] PLEASE TRY USING VALID INTERFACE ')


