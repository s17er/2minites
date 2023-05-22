from collections import abc
from keyword import iskeyword
import json

class FrozenJson:
    """A read-only facade for navigating a JSON-like object
       using attribute notation
    """
    
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg
        
    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if iskeyword(key):
                key += '_'
            self.__data[key] = value
            
    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJson(self.__data[name])
        
def main(json_str):
    raw_feed = json.loads(json_str)
    feed = FrozenJson(raw_feed)
    print(feed.code)
    print(feed.result[0].name)
    
if __name__ == '__main__':
    json_str = """{
        "code": 200,
        "message": "ok",
        "result": [
            {
                "id": 1,
                "name": "aaa"
            },
            {
                "id": 2,
                "name": "bbb"
            }
        ]
    }"""
    main(json_str)