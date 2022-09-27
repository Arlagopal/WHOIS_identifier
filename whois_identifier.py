import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d","--domain", help="Domain Name")
args=parser.parse_args()


cmd = "whois "+args.domain+" | grep -e '^Domain Name:' -e '^Registry Domain ID:' -e '^Registrar WHOIS Server:' -e '^Registrar URL:' -e '^Creation Date:' -e '^Registrar:' | tr '\n' ';' | sed -e $'s:;$:\\\n:' >> out.csv"

os.system(cmd)	

# Resource: https://stackoverflow.com/questions/11604653/how-to-add-command-line-arguments-with-flags-in-python3
