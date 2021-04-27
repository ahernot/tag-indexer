#!/usr/bin/env python3

import os
import datetime

from preferences import *


def get_datetime ():
    return datetime.datetime.now () .strftime (LOG_DATETIME_FORMAT)


class Log:

    def __init__ (self, dirpath: str):
        self._content_add = list()

        self.path = os.path.join (dirpath, LOG_FILENAME)

        if not os.path.exists (self.path):
            try:
                os.makedirs (dirpath)
            except:
                pass
            self._reset()
        
    def _reset (self):

        with open (self.path, 'w', encoding='utf-8') as log:
            pass

    def add_line (self, line: str):
        self._content_add.append (line)

    def save (self):
        dt = get_datetime ()

        with open (self.path, 'a', encoding='utf-8') as log:
            for line in self._content_add:
                log.write (f'{dt} – {line}\n')
