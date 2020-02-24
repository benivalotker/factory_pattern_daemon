from abc import ABC, abstractmethod

'''
factory design pattern
'''
class FactoryClass:
    '''
    Factory Class
    '''
    # return the request class messages
    @staticmethod
    def get_class(class_name):
        if class_name == "thread_number_1":
            return Thread_1()
        elif class_name == "thread_number_2":
            return Thread_2()
        
        assert 0, 'Could not find shape ' + class_name

'''
Interface - all the class that inherit from this interface must declare methods.
'''
class FactoryInterface(ABC):
    '''
    Messages Interface
    '''
    @abstractmethod
    def run(self): pass
    
   
'''
methods:
    - run: print some text
'''
class Thread_1(FactoryInterface):
    def __init__(self):
        pass

    def run(self):
        print("run thread number 1")

    
class Thread_2(FactoryInterface):
    def __init__(self):
        pass

    def run(self):
        print("run thread number 2")