
from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.impl = implementation
        
    def complex_operation(self) -> None:
        print('Выполнение сложных вычислений...')
        self.impl.operation1()
        self.impl.operation2()
        self.impl.operation3()
        print('Выполнение завершено!')


class Implementation(ABC):
    @abstractmethod
    def operation1(self) -> None:
        pass
    
    @abstractmethod
    def operation2(self) -> None:
        pass
    
    @abstractmethod
    def operation3(self) -> None:
        pass
    

class ConcreteImplementationA(Implementation):
    def operation1(self) -> None:
        print('реализация из класса А...')
    
    def operation2(self) -> None:
        print('реализация из класса А...')
    
    def operation3(self) -> None:
        print('реализация из класса А...')
        

class ConcreteImplementationB(Implementation):
    def operation1(self) -> None:
        print('реализация из класса B...')
    
    def operation2(self) -> None:
        print('реализация из класса B...')
    
    def operation3(self) -> None:
        print('реализация из класса B...')  


if __name__ == '__main__':
    abstraction = Abstraction(ConcreteImplementationA())
    abstraction.complex_operation()
    
    abstraction = Abstraction(ConcreteImplementationB())
    abstraction.complex_operation()
    