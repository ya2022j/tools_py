class MockBase():

    headers = {}

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, trace):
        pass

    def getcode(self):
        return 200

    def read(self):
        return ''.encode('UTF-8')

class MockCreate(MockBase):
    def read(self):
        res = ''
        return res.encode('UTF-8')
