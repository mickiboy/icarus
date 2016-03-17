#!/bin/env python3
#
# icarus cms
#
# (c) 2016 Daniel Jankowski

import re
import colorama

from colorama import Fore, Back, Style


def write_html(filename, content):
    with open(filename, "w") as fp:
        fp.write(content)
    return True


def get_month(date):
    month = ['January', 'February', 'March', 'April', 'June', 'Juli', 'August', 'September', 'October', 'November', 'December']
    return month[int(re.sub(r'(.*)\-(.*)\-(.*)', r'\2', date)) - 1]


#################
# LOG-FUNCTIONS #
#################

def log(text):
    print(Fore.GREEN + '==> ' + Fore.WHITE + text)


def log_warn(text):
    print(Fore.YELLOW + '==> Warning: ' + Fore.WHITE + text)


def log_err(text):
    print(Fore.RED + '==> Error: ' + Fore.WHITE + text)


def main():
    print('module tests\n')

    log('normal log')
    log_warn('warining log')
    log_err('error log')

    print('\nmonth conversion')
    print(get_month('2016-03-16'))

    print('\ntests passed!')
    pass


if __name__ == '__main__':
    main()
