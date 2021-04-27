#!/usr/bin/env python3

import os
import datetime

from functions import get_datetime
from preferences import *


class Log:

    def __init__ (self, dirpath: str):
        self._content_add = list()
        self.start_dt = get_datetime(datetime_format=LOG_DATETIME_FORMAT)

        self.path = os.path.join (dirpath, LOG_FILENAME)

        if not os.path.exists (self.path):
            try:
                os.makedirs (dirpath)
            except:
                pass
            self._reset()
        
    def _reset (self):

        with open (self.path, 'w', encoding='utf-8') as log:
            log.write('pytags log\n')

    def add_line (self, line: str):
        self._content_add.append (line)

    def _make_header (self):
        header = [
            f'pytags version {VERSION}\n',
            f'start datetime: {self.start_dt}\n',
            f'stop datetime: {self.stop_dt}\n'
        ]
        return header

    def save (self):
        self.stop_dt = get_datetime(datetime_format=LOG_DATETIME_FORMAT)

        with open (self.path, 'a', encoding='utf-8') as log:
            log.write ('\n')

            log.writelines( self._make_header() )

            for line in self._content_add:
                log.write (f'{line}\n')
