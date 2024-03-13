# Network Scanner (analogue Netdiscover in Kali Linux)


Network Scanner script was developed using Python 3, Linux commands and can be launched in Linux command line. Netdiscover is an ultimate scanning tool used to get the internal IP address and MAC address of live hosts in the network. After scanning the network, we get table of devices with IP-addresses and MAC-addresses. 


### Running  

To run this project, install it locally cloning repo, than using next configurations in Linux CLI:
```
> cd ./network_scanner
> python3 network_scanner.py -t "specify an IP-address"
> ./ network_scanner.py -t 192.168.31.1
```

![Command](./ReadmeMaterials/network_scanner.gif)



### Help command

To get more information about script's argument, use next command:

```
> cd ./network_scanner
> ./ network_scanner.py --help
```

![Help command](./ReadmeMaterials/network_scanning_help.gif)
