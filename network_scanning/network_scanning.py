#!/usr/bin/env python

import scapy.all as scapy
# for using this program in the newest Python versions write: import argparse
import optparse


# function that gets arguments from command line in Linux

# to use that function write route -n in your Linux command and write your IP for target

def get_arguments():
    # for argparse
    # parser = argparse.ArgumentParser()
    # parser.add_argument(....)
    # options = parser.parse_args()

    # object for parsing data
    parser = optparse.OptionParser()
    # adding new option for script
    parser.add_option("-t", "--target", dest="target", help="Target IP")
    # getting data from options and arguments
    (options, arguments) = parser.parse_args()

    # checking the argument that we have gotten
    if not options.target:
        parser.error("[-] Please specify target, enter --help for more info")
    else:
        return options


def scan(ip):
    # creating ARP request for getting IP of needed object
    arp_request = scapy.ARP(pdst=ip)

    # variable that helps us to direct our packet in our local network for each device
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # new packet that is combination of all the methods
    arp_request_broadcast = broadcast / arp_request

    # getting the response of each device in network
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    # list of dictionaries that contain information about IP/MAC
    clients_list = []

    # getting values for dictionary from answer_list
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)

    return clients_list


# printing function
def print_result(results_list):
    print("IP\t\t\tMAC Address\n------------------------------------------")
    for client in results_list:
        for key in client:
            print(client[key], end="\t\t")
        print("\t")


options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)


