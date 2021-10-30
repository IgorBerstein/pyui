class DictToObject(object):
    def __init__(self, myDict):
        for key, value in myDict.items():
            if type(value) == dict:
                setattr(self, key, DictToObject(value))
            else:
                setattr(self, key, value)



