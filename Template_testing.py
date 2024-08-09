import textfsm
import pprint

# Sample output of the 'show interfaces' command
raw_output = """
Preparing to Display Configuration...
************************************************************************************
                Command Execution Time: Thu Aug 08 11:05:02 2024 EDT
************************************************************************************
#
# Thu Aug 08 11:05:02 2024 EDT
# box type             : VSP-8404C
# software version     : 8.10.1.0
# cli mode             : ECLI
#

#Card Info :

#  Slot 1 :
#       CardType          : 8418XSQ
#       CardDescription   : 8418XSQ
#       CardSerial#       : 18JP3430CD3M
#       CardPart#         : EC8404005-E6
#       CardAssemblyDate  : 20180821
#       CardHWRevision    : 06
#       CardHWConfig      :
#       AdminStatus       : up
#       OperStatus        : up


#  Slot 3 :
#       CardType          : 8418XSQ
#       CardDescription   : 8418XSQ
#       CardSerial#       : 17JP4530CD5H
#       CardPart#         : EC8404005-E6
#       CardAssemblyDate  : 20171107
#       CardHWRevision    : 05
#       CardHWConfig      :
#       AdminStatus       : up
#       OperStatus        : up

config terminal

#
# VLAN CONFIGURATION
#

vlan members remove 1 1/1-1/18,3/1-3/18 portmember
vlan create 10 name "Signage/PA" type port-mstprstp 1
vlan mlt 10 2
vlan members 10 1/1,3/1 portmember
vlan i-sid 10 1700010
interface Vlan 10

vrf corp_users
ip address 10.6.10.3 255.255.254.0 1
ip spb-multicast enable
ip igmp snoop-querier-addr 10.6.10.3

ip igmp access-list "UPnP" 0.0.0.0/0.0.0.0 deny-both
ip vrrp version 2
ip vrrp address 10 10.6.10.1
ip vrrp 10 backup-master enable
ip vrrp 10 priority 190
ip vrrp 10 enable
exit
vlan create 11 name "FareGate_Old" type port-mstprstp 1
vlan mlt 11 2
vlan members 11 1/1,3/1 portmember
vlan i-sid 11 1700011
interface Vlan 11
vrf corp_users
ip address 10.6.5.3 255.255.255.128 2
ip spb-multicast enable
ip igmp access-list "UPnP" 0.0.0.0/0.0.0.0 deny-both
ip vrrp version 2
ip vrrp address 11 10.6.5.1

ip vrrp 11 backup-master enable
ip vrrp 11 priority 200
ip vrrp 11 enable
exit
vlan create 12 name "Vendor-apps" type port-mstprstp 1
vlan mlt 12 2
vlan members 12 1/1,3/1 portmember
vlan i-sid 12 1700012
interface Vlan 12
vrf corp_users
ip address 10.6.0.189 255.255.255.224 3
ip igmp access-list "UPnP" 0.0.0.0/0.0.0.0 deny-both
ip vrrp version 2
ip vrrp address 12 10.6.0.161
ip vrrp 12 backup-master enable
ip vrrp 12 priority 190
ip vrrp 12 enable
exit
vlan create 19 name "Management" type port-mstprstp 1
vlan i-sid 19 1700019
interface Vlan 19
ip address 10.6.24.3 255.255.255.128 4
ip igmp access-list "UPnP" 0.0.0.0/0.0.0.0 deny-both

ip vrrp version 2
ip vrrp address 19 10.6.24.1
ip vrrp 19 backup-master enable
ip vrrp 19 priority 190
ip vrrp 19 enable
exit
vlan create 20 name "Corp-User-1" type port-mstprstp 1
vlan mlt 20 2
vlan members 20 1/1,3/1 portmember
vlan i-sid 20 1700020
interface Vlan 20
vrf corp_users
ip address 10.6.1.3 255.255.255.0 5
ip spb-multicast enable
ip igmp access-list "UPnP" 0.0.0.0/0.0.0.0 deny-both
ip dhcp-relay
ip vrrp version 2
ip vrrp address 20 10.6.1.1
ip vrrp 20 backup-master enable
ip vrrp 20 priority 190
ip vrrp 20 enable
exit
vlan create 22 name "CCTV" type port-mstprstp 1

vlan mlt 22 2
vlan members 22 1/1,3/1 portmember
vlan i-sid 22 1700022
interface Vlan 22
vrf corp_users
ip address 10.6.26.3 255.255.254.0 6
ip vrrp version 2
ip vrrp address 22 10.6.26.1
ip vrrp 22 backup-master enable
ip vrrp 22 priority 190
ip vrrp 22 enable
exit
vlan create 23 name "PCI" type port-mstprstp 1
vlan mlt 23 2
vlan members 23 1/1,3/1 portmember
vlan i-sid 23 1700023
interface Vlan 23
vrf pci_vrf
ip address 10.6.0.195 255.255.255.224 7
ip spb-multicast enable
ip igmp access-list "UPnP" 0.0.0.0/0.0.0.0 deny-both
ip vrrp version 2
ip vrrp address 23 10.6.0.193

ip vrrp 23 backup-master enable
ip vrrp 23 priority 190
ip vrrp 23 enable
exit
vlan create 27 name "Employee_TV" type port-mstprstp 1
vlan i-sid 27 1700027
interface Vlan 27
vrf corp_users
ip address 10.6.0.226 255.255.255.224 16
ip igmp access-list "UPnP" 0.0.0.0/0.0.0.0 deny-both
ip dhcp-relay
ip vrrp version 2
ip vrrp address 27 10.6.0.225
ip vrrp 27 backup-master enable
ip vrrp 27 priority 190
ip vrrp 27 enable
exit
vlan create 29 name "FareGate" type port-mstprstp 1
vlan mlt 29 2
vlan members 29 1/1,3/1 portmember
vlan i-sid 29 1700029
interface Vlan 29
vrf corp_users

ip address 10.6.12.3 255.255.255.0 8
ip igmp access-list "UPnP" 0.0.0.0/0.0.0.0 deny-both
ip vrrp version 2
ip vrrp address 29 10.6.12.1
ip vrrp 29 backup-master enable
ip vrrp 29 priority 190
ip vrrp 29 enable
exit
vlan create 30 name "Body_Cams" type port-mstprstp 1
vlan i-sid 30 1700030
interface Vlan 30
vrf corp_users
ip address 10.6.30.3 255.255.255.224 9
ip igmp access-list "UPnP" 0.0.0.0/0.0.0.0 deny-both
ip vrrp version 2
ip vrrp address 30 10.6.30.1
ip vrrp 30 backup-master enable
ip vrrp 30 priority 190
ip vrrp 30 enable
exit
vlan create 42 name "Police_Radio" type port-mstprstp 1
vlan i-sid 42 12990042
interface Vlan 42

vrf police_radio
exit
vlan create 103 name "HQ-BodyCam-VLAN-103" type port-mstprstp 1
vlan i-sid 103 11200103
interface Vlan 103
vrf corp_users
exit
vlan create 142 name "Meadowland_PC" type port-mstprstp 1
vlan i-sid 142 1700142
interface Vlan 142
vrf corp_users
ip address 10.6.24.163 255.255.255.224 10
ip igmp access-list "UPnP" 0.0.0.0/0.0.0.0 deny-both
ip vrrp version 2
ip vrrp address 142 10.6.24.161
ip vrrp 142 backup-master enable
ip vrrp 142 priority 190
ip vrrp 142 enable
exit
vlan create 143 name "Meadowland_CCTV" type port-mstprstp 1
vlan i-sid 143 1700143
interface Vlan 143
vrf corp_users

ip address 10.6.24.195 255.255.255.224 11
ip igmp access-list "UPnP" 0.0.0.0/0.0.0.0 deny-both
ip vrrp version 2
ip vrrp address 143 10.6.24.193
ip vrrp 143 backup-master enable
ip vrrp 143 priority 190
ip vrrp 143 enable
exit
vlan create 145 name "Meadowland_Signage" type port-mstprstp 1
vlan i-sid 145 1700145
interface Vlan 145
vrf corp_users
ip address 10.6.25.2 255.255.255.192 12
ip igmp access-list "UPnP" 0.0.0.0/0.0.0.0 deny-both
ip vrrp version 2
ip vrrp address 145 10.6.25.1
ip vrrp 145 backup-master enable
ip vrrp 145 priority 190
ip vrrp 145 enable
exit
vlan create 160 name "PBX-VLAN" type port-mstprstp 1
vlan i-sid 160 1700160
interface Vlan 160

vrf corp_users
ip address 10.6.0.66 255.255.255.224 14
ip igmp access-list "UPnP" 0.0.0.0/0.0.0.0 deny-both
ip vrrp version 2
ip vrrp address 160 10.6.0.65
ip vrrp 160 backup-master enable
ip vrrp 160 priority 200
ip vrrp 160 enable
exit
vlan create 165 name "VoIP_165" type port-mstprstp 1
vlan i-sid 165 1700165
interface Vlan 165
vrf corp_users
ip address 10.6.2.130 255.255.255.192 17
ip igmp access-list "UPnP" 0.0.0.0/0.0.0.0 deny-both
ip dhcp-relay
ip vrrp version 2
ip vrrp address 165 10.6.2.129
ip vrrp 165 backup-master enable
ip vrrp 165 priority 190
ip vrrp 165 enable
exit
vlan create 166 name "VoIP_166" type port-mstprstp 1

vlan i-sid 166 1700166
interface Vlan 166
vrf corp_users
ip address 10.6.2.194 255.255.255.192 18
ip igmp access-list "UPnP" 0.0.0.0/0.0.0.0 deny-both
ip dhcp-relay
ip vrrp version 2
ip vrrp address 166 10.6.2.193
ip vrrp 166 backup-master enable
ip vrrp 166 priority 190
ip vrrp 166 enable
exit
vlan create 300 name "Wireless AP" type port-mstprstp 1
vlan mlt 300 2
vlan members 300 1/1,3/1 portmember
vlan i-sid 300 1700300
interface Vlan 300
vrf corp_users
ip address 10.6.4.131 255.255.255.128 13
ip igmp access-list "UPnP" 0.0.0.0/0.0.0.0 deny-both
ip vrrp version 2
ip vrrp address 30 10.6.4.129
ip vrrp 30 backup-master enable

ip vrrp 30 priority 190
ip vrrp 30 enable
exit
vlan create 500 name "PT_LMR" type port-mstprstp 1
vlan i-sid 500 12990500
interface Vlan 500
vrf pt_lmr
ip igmp proxy
ip igmp snooping

exit
vlan create 530 name "FirstNet530" type port-mstprstp 1
vlan i-sid 530 12990530
vlan create 531 name "FirstNet531" type port-mstprstp 1
vlan i-sid 531 12990531
vlan create 532 name "FirstNet532" type port-mstprstp 1
vlan i-sid 532 12990532
vlan create 534 name "FirstNet534" type port-mstprstp 1
vlan i-sid 534 12990534
vlan create 535 name " FirstNet535" type port-mstprstp 1
vlan i-sid 535 12990535
vlan create 805 name "DMZ_Internet_VLAN_805" type port-mstprstp 1
vlan members 805 3/16 portmember

vlan i-sid 805 1299805
vlan create 4000 name "IST" type port-mstprstp 1
vlan i-sid 4000 1704000
interface Vlan 4000
ip address 10.29.2.81 255.255.255.252 0
exit
vlan create 4050 name "BVLAN-1" type spbm-bvlan
vlan create 4051 name "BVLAN-2" type spbm-bvlan
"""

# Load the TextFSM template
template_path = 'C:/Users/CISSSXS4/OneDrive - New Jersey Transit/Desktop/Scraper/ntc-templates-master/ntc-templates-master/ntc_templates/templates/extreme_exos_show_running_config.textfsm'

with open(template_path) as template_file:
    fsm = textfsm.TextFSM(template_file)
    parsed_output = fsm.ParseText(raw_output)

# Convert parsed output to a list of dictionaries
results = [dict(zip(fsm.header, entry)) for entry in parsed_output]

# Print the results
pprint.pprint(results)
