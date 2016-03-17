#!/bin/env python3
#
# icarus cms
#
# (c) 2016 Daniel Jankowski


import re

import generator.server

CONFIG_FILE = "./config/icarus.conf"

CONF_REGEX = re.compile('(.*)\s=\s')


def start_server(port, addr):
    ms = server.management_server(port, addr)
    ms.start()
    return


def parse_config(filename):
    webadmin, port, address = None, None, None
    with open(filename, 'r')  as fp:
        for line in fp.readlines():
            if line.startswith('webadmin'):
                if re.sub(CONF_REGEX, '', line)[:-1] == "True":
                    webadmin = True
                else:
                    webadmin = False
            if line.startswith('port'):
                port = int(re.sub(CONF_REGEX, '', line)[:-1])
            if line.startswith('addr'):
                address = re.sub(CONF_REGEX, '', line)[:-1]
    return webadmin, port, address


def main():
    webadmin, port, addr = parse_config(CONFIG_FILE)
    pass


if __name__ =='__main__':
    main()
