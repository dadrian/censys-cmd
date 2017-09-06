# -*- coding: utf-8 -*-
import censys.certificates


class Command(object):

    def __init__(self, api_id=None, api_secret=None, *args, **kwargs):
        self._api_id = None
        self._api_secret = None

    def do_action(self, action, target):
        method = getattr(self, action)
        return method(target)


class CertificateCommand(Command):

    def __init__(self, api_id=None, api_secret=None, *args, **kwargs):
        super(CertificateCommand, self).__init__(
            api_id=api_id, api_secret=api_secret, *args, **kwargs)
        self._censys = censys.certificates.CensysCertificates(
            api_id=self._api_id, api_secret=self._api_secret)

    def view(self, sha256fp):
        out = self._censys.view(sha256fp)
        return out
