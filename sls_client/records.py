import json

from voluptuous import Schema
from voluptuous import All, Any, Length, Range, Required

import constants

class Record(object):
    """Base class for record objects"""
    
    schema = Schema({
        Required("type"): Any(All(str, Length(min=1)), All([All(str, Length(min=1))], Length(min=1))),
        
        str: Any(str, [str])
    })
    
    def __init__(self, data):
        super(Record, self).__init__()
        try:
            self.schema(data)
        except:
            raise

    def dump(self, pretty=False):
        if pretty:
            return json.dumps(self._data, sort_keys=True, indent=4)
        else:
            return json.dumps(self._data)
    
    def pretty(self):
        return self.dump(True)
    
    def raw(self, pretty=False):
        return self.dump(pretty)
        
    def __getattr__():
        

class Host(Record):
    """Base class for host record objects"""
    
    def __init__(self, data):
        super(Record, self).__init__()
        try:
            self.schema(data)
        except:
            raise
    
class Interface(Record):
    """Base class for interface record objects"""
    
    def __init__(self, data):
        super(Record, self).__init__()
        try:
            self.schema(data)
        except:
            raise
    
class Person(Record):
    """Base class for person record objects"""
    
    def __init__(self, data):
        super(Record, self).__init__()
        try:
            self.schema(data)
        except:
            raise

class Service(Record):
    """Base class for service record objects"""
    
    def __init__(self, data):
        super(Record, self).__init__()
        try:
            self.schema(data)
        except:
            raise
