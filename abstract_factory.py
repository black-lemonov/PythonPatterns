
from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_item1(self) -> AbstractItem:
        pass
    
    @abstractmethod
    def create_item2(self) -> AbstractItem:
        pass
    
    @abstractmethod
    def create_item3(self) -> AbstractItem:
        pass

class ConreteFactory(AbstractFactory):
    def create_item1(self) -> AbstractItem:
        return ConcreteItemA()
    
    def create_item2(self) -> AbstractItem:
        return ConcreteItemB()
    
    def create_item3(self) -> AbstractItem:
        return ConcreteItemC()
    
class AbstractItem(ABC):
    @abstractmethod
    def useful_method(self):
        pass
    
class ConcreteItemA(AbstractItem):
    def useful_method(self):
        print("что-то полезное")
        
class ConcreteItemB(AbstractItem):
    def useful_method(self):
        print("что-то полезное 2")
        
class ConcreteItemC(AbstractItem):
    def useful_method(self):
        print("что-то полезное 3")