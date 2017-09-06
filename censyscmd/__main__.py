# -*- coding: utf-8 -*-

import argparse
import json

from censyscmd import commands


def _certificates(args):
    c = commands.CertificateCommand()
    res = c.do_action(args.action, args.target)
    return res


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-id", type=str, help="Censys API ID")
    parser.add_argument("--api-secret", type=str, help="Censys API secret")

    subparsers = parser.add_subparsers(help="Censys target")
    parser_certs = subparsers.add_parser('certificates')
    parser_certs.add_argument('action', choices=['view'])
    parser_certs.add_argument('target', help="X")
    parser_certs.set_defaults(func=_certificates)

    args = parser.parse_args()
    res = args.func(args)
    out = json.dumps(res)
    print out


if __name__ == "__main__":
    main()
