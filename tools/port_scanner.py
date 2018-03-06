#!/usr/bin/env python
import socket
import subprocess
import sys
import argparse

def get_argparser():
    parser = argparse.ArgumentParser(
        description="Scan for open ARTIQ ports.")
    parser.add_argument("ip")
    return parser

artiq_ports = {
    1068: "core device (logging)",
    1380: "core device (management)",
    1381: "core device (main)",
    1382: "core device (analyzer)",
    1383: "core device (mon/inj)",


    1066: "master (logging input)",
    1067: "master (broadcasts)",
    3250: "master (notifications)",
    3251: "master (control)",
 
    3248: "InfluxDB bridge",

    3249: "controller manager",
    3252: "controller PDQ2 (out-of-tree)",
    3253: "controller LDA",
    3254: "controller Novatech 409B",
    3255: "controller Thorlabs T-Cube",
    3256: "controller Korad KA3005P"
    }

def do_scan(remoteServer):
    remoteServerIP  = socket.gethostbyname(remoteServer)
    try:
        for port in artiq_ports.keys():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("{} : {}".format(port, artiq_ports[port]), end="\n", flush=True)
            else:
                pass
            sock.close()
        print("")

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')

    except socket.error:
        print("Couldn't connect to server")

def main():
    args = get_argparser().parse_args()
    do_scan(args.ip)

if __name__ == "__main__":
    main()
