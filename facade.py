
class Subsystem1:
    def useful_method1(self):
        pass


class Subsystem2: 
    def useful_method2(self):
        pass
    
    
class Subsystem3:
    def useful_method3(self):
        pass


class Facade:
    def __init__(self,
                 sub1: Subsystem1 | None,
                 sub2: Subsystem2 | None,
                 sub3: Subsystem3 | None):
        self.sub1 = sub1 or Subsystem1()
        self.sub2 = sub2 or Subsystem2()
        self.sub3 = sub3 or Subsystem3()
        
    def useful_method1(self):
        self.sub1.useful_method1()
        
    def useful_method2(self):
        self.sub2.useful_method2()
        
    def useful_method3(self):
        self.sub3.useful_method3()
        
        
