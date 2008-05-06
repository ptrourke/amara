########################################################################
# amara/__init__.py

XML_NAMESPACE = u"http://www.w3.org/XML/1998/namespace"
XMLNS_NAMESPACE = u"http://www.w3.org/2000/xmlns/"

class Error(Exception):
    def __init__(self, code, message, **kwds):
        Exception.__init__(self, code, message)
        self.code = code
        self.message = message
        # map keywords into attributes
        for attr in kwds:
            setattr(self, attr, kwds[attr])

    def __str__(self):
        return self.message


class ReaderError(Error):
    pass


class XIncludeError(ReaderError):
    pass
