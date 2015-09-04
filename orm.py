#!/usr/bin/env python3
# _*_codeding:ctf-8 

class Model(dict,metaclass=MedelMetaclass):

    def __init__(self,**kw):
        super(Model,self).__init__(**kw) #调用父类  等于 dict.__init__(self,**kw)
        
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" %key)
            
    def __setattr__(self,key,value):
        self[key]=value
        
    def getValue(self,key):
        return getattr(self,key,None) # not defined? why None
        
    def getValueOrDefault(self,key):
        value=getattr(self,key,None)
        if value is None:
            field=self.__mappings__[key]
            if field.default is not None:
                value=field.default() if callable(field.default) else field.default
                logging.debug('using default value for %s:%s' %(key,str(value)))
                setattr(self,key,value)
        return value
        
def Field(object):

    def __init__(self,name,column_type,primary_key,default):
        self.name=name
        self.column_type=columntype
        self.primary_key=primary_key
        self.default=default
        
    def __str__(self):
        return '<%s,%s,%s>' %(self.__class__.__name__,self.column_type,self.name)
        
def StringField(Field):

    def __init__(self,name=None,Primary_key=False,default=None,ddl='varchar(100)'):
        super().__init__(name,ddl,primary_key,default)
        
def IngeterField(Field):
    
    def __init__(self,name=None,primary_key=False,default=None,ddl='int(20)'):
        super().__init__(self,ddl,primary_key,default)
        

    
    