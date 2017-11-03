# -*- coding: utf-8 -*-
import censys.certificates
import censys.data


class Command(object):

    def __init__(self, api_id=None, api_secret=None, *args, **kwargs):
        self._api_id = None
        self._api_secret = None

    def do_action(self, action, *args):
        method = getattr(self, action)
        return method(*args)


class DataCommand(Command):

    def __init__(self, api_id=None, api_secret=None, *args, **kwargs):
        super(DataCommand, self).__init__(
            api_id=api_id, api_secret=api_secret, *args, **kwargs)
        self._censys = censys.data.CensysData(
            api_id=self._api_id, api_secret=self._api_secret)

        # TODO: Actually be able to pass this in
        self._fuzzy = 'fuzzy' in kwargs

    def series(self, series_name):
        out = self._censys.view_series(series_name)
        return out

    def view(self, series_name, result_id):
        if self._fuzzy:
            series = self.series(series_name)
            historical = series['results']['historical']
            for res in historical:
                if res['id'].startswith(result_id):
                    result_id = res['id']
                    break
        out = self._censys.view_result(series_name, result_id)
        return out


class CertificateCommand(Command):

    def __init__(self, api_id=None, api_secret=None, *args, **kwargs):
        super(CertificateCommand, self).__init__(
            api_id=api_id, api_secret=api_secret, *args, **kwargs)
        self._censys = censys.certificates.CensysCertificates(
            api_id=self._api_id, api_secret=self._api_secret)

    def view(self, sha256fp):
        out = self._censys.view(sha256fp)
        return out

    def search(self, query):
        return list(self._censys.search(query, fields=["parsed.fingerprint_sha256"]))
