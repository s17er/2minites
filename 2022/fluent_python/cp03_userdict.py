import collections

class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    def __contains__(self, key: object) -> bool:
        return str(key) in self.data
    
    def __setitem__(self, key, item) -> None:
        self.data[str(key)] = item
        
if __name__ == '__main__':
    d = StrKeyDict()
    d[1] = 'abc'
    d['2'] = 'ddd'
    print(1 in d)
    print('1' in d)
    print(d)
