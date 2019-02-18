# -*- coding: utf-8 -*-
from __future__ import print_function

import argparse
import json

from . import commands


def _ipv4(args):
    c = commands.IPv4Command()
    res = c.do_action(args.action, args.target)
    return res


def _certificates(args):
    c = commands.CertificateCommand()
    res = c.do_action(args.action, args.target)
    return res


def _data(args):
    c = commands.DataCommand()
    res = c.do_action(args.action, *args.target)
    return res


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-id", type=str, help="Censys API ID")
    parser.add_argument("--api-secret", type=str, help="Censys API secret")

    subparsers = parser.add_subparsers(help="Censys target")

    parser_ipv4 = subparsers.add_parser('ipv4')
    parser_ipv4.add_argument('action', choices=['view', 'search'])
    parser_ipv4.add_argument('target', help="X")
    parser_ipv4.set_defaults(func=_ipv4)

    parser_certs = subparsers.add_parser('certificates')
    parser_certs.add_argument('action', choices=['view', 'search'])
    parser_certs.add_argument('target', help="X")
    parser_certs.set_defaults(func=_certificates)

    parser_data = subparsers.add_parser('data')
    parser_data.add_argument('action', choices=['series', 'view'])
    parser_data.add_argument('target', help="X", nargs="*")
    parser_data.set_defaults(func=_data)

    args = parser.parse_args()
    res = args.func(args)
    if not isinstance(res, list):
        res = [res]
    for obj in res:
        print(json.dumps(obj))


if __name__ == "__main__":
    main()
