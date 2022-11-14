#class for design pattern
#python@3.9

#Method 1 : A Method way
class Singleton:
    __instance = None

    @classmethod
    def getInstance(cls, *args, **kargs):
        if cls.__instance is None:
            cls.__instance = cls(*args, **kargs)
        return cls.__instance
    

#--------------------------------------------------------------------#
#Method 2 : A decorator returning function

def singleton(cls):
    instances = {}

    def getInstance(cls, *args, **kargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kargs)
        return instances[cls]

    return getInstance

#--------------------------------------------------------------------#
#Method 3 : A decorator
def singleton(cls):

    class Singleton(cls):
        __instance = None
        __is__init__ = False

        def __new__(cls, *args, **kargs):
            if cls.__instance is None:
                cls.__instance = super(Singleton, cls).__new__(cls)
            return cls.__instance

        def __init__(self):
            if self.__is__init__:
                return
            super(cls, self).__init__()
        
    Singleton.__name__ = cls.__name__

    return Singleton

#--------------------------------------------------------------------#            
#Method 4 : A Base class 

class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kargs):
        if cls.__instance is None:
            cls.__instance = cls(*args, **kargs)
        return cls.__instance

#--------------------------------------------------------------------#
#Method 5 : A Meta class

class Singleton(type):
    __instance = {}
    
    def __call__(cls, *args, **kargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(Singleton, cls).__call__(*args, **kargs)
        return cls.__instance[cls]

#--------------------------------------------------------------------#