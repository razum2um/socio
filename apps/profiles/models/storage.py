# -*- coding: utf-8 -*-
import re
from django.core.files.storage import FileSystemStorage

class MD5Storage(FileSystemStorage):
    def _open(name, mode='rb'):
        """ implementation required """
        return super(FileSystemStorage, self)._open(name, mode)

    def _save(self, name, content):
        """ 
        existing files handling: no action if such a md5-name exists
        """
        if self.exists(name) and is_md5(name):
            return name
        return super(FileSystemStorage, self)._save(name, content)

def is_md5(name):
    """ 
    assumes 'path/path/a_{MD5}.ext'
    see helpers
    """
    if re.search('.*_[0-9a-f]{32}\.', name):
        return True
    return False
