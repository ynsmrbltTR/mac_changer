import subprocess
import argparse

parser = argparse.ArgumentParser(description="You can change mac address of your interface",
                                 epilog="...........................................................",
                                 prog="mac_changer",
                                 usage="%(prog)s [options] interface")

parser.add_argument("-i", "--interface",
                    dest="interface" ,
                    help="The interface where you want to change the mac address",
                    metavar='',
                    required=True,
                    type=str)

parser.add_argument("-m", "--mac",
                    dest="mac_address" ,
                    help="Enter a valid mac address",
                    metavar='',
                    required=True,
                    type=str)
args = parser.parse_args()

interface = args.interface
mac_address = args.mac_address
try:
    subprocess.run(["ifconfig", interface, "down"],
                   capture_output=True,
                   text=True,
                   timeout=10,
                   check=True)
except subprocess.CalledProcessError as error:
    print(error.stderr)



try:
    subprocess.run(["ifconfig", interface, "hw", "ether", mac_address],
                   capture_output=True,
                   text=True,
                   timeout=10,
                   check=True)
except subprocess.CalledProcessError as error:
    print(error.stderr)


try:
    subprocess.run(["ifconfig", interface, "up"],
                   capture_output=True,
                   text=True,
                   timeout=10,
                   check=True)
except subprocess.CalledProcessError as error:
    print(error.stderr)


try:
    show = subprocess.run(["ifconfig", interface],
                   capture_output=True,
                   text=True,
                   timeout=10,
                   check=True)
    print(show.stdout)
except subprocess.CalledProcessError as error:
    print(error.stderr)