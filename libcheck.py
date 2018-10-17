import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--port', '-p', default = 22, help="The port to check, leave alone if you don't know what this means.")
parser.add_argument('ips', nargs='+', help="The IPs you want to check to see if they are vulnerable.")
args = parser.parse_args()
for ip in args.ips:
    output = subprocess.check_output('nc -nw 3 {} {}'.format(ip, args.port), shell=True).decode()
    if 'libssh' in output:
        if not '8.4' in output and not '7.6' in output:
            print('{} looks vulnerable'.format(ip))
    else:
        print('{} may not be vulnerable'.format(ip))
