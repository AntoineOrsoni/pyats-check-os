import toolbox.pyats_diff as diff
import toolbox.database as db
import argparse
import sys
import json
import pprint

# Parsing the args
description = "Print the differences for a specific test and hostname."

test_help = '''
Possible test_name:
    - route_summary > show ip route summary
    - routes        > show ip route
    - isis          > show ip isis neighbors
    - xconnect      > show xconnect all'''

method_help:'''
- both for a diff before/after
- after for a specific output after
- before for a specific output before'''


parser = argparse.ArgumentParser(description=description, usage='use "%(prog)s --help" for more information', formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--hostname', dest='hostname', help = 'Hostname of the device', required = True)
parser.add_argument('--testname', dest='test_name', help = test_help, required = True)
parser.add_argument('--when', dest='when', default="both", help = 'diff for a diff before/after ',)
args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])

hostname = args.hostname
test_name = args.test_name
when = args.when

# Sends a diff
if when == "both": 
    diff.compare_output_before_after(hostname, test_name)
else:
    pp = pprint.PrettyPrinter(indent=4)
    output = db.get_output_test(hostname, test_name, when)
    pp.pprint(json.loads(output))