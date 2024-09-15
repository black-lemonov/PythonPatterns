
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Context:
    def __init__(self, algorithm: Algorithm) -> Context:
        self._algorithm = algorithm
        
    @property
    def algorithm(self) -> Algorithm:
        return self._algorithm
    
    @algorithm.setter
    def algorithm(self, new_algorithm: Algorithm) -> None:
        self._algorithm = new_algorithm
        
    def execute(self):
        print("исполняю", self._algorithm)
        self._algorithm.find_min()
        self._algorithm.find_max()
        

class Algorithm(ABC):
    @abstractmethod
    def find_min(self) -> Any:
        pass
    
    @abstractmethod
    def find_max(self) -> Any:
        pass
    

class PSO(Algorithm):
    def find_min(self) -> Any:
        print("поиск минимума")
        
    def find_max(self) -> Any:
        print("поиск максимума")
        
    def __repr__(self) -> str:
        return "PSO"
    
    def __str__(self) -> str:
        return "алгоритм роя частиц"
        
        
class Bee(Algorithm):
    def find_min(self) -> Any:
        print("поиск минимума")
        
    def find_max(self) -> Any:
        print("поиск максимума")
        
    def __str__(self) -> str:
        return "пчелинный алгоритм"
    
        
if __name__ == "__main__":
    context = Context(Bee())
    context.execute()
    context.algorithm = PSO()
    context.execute()