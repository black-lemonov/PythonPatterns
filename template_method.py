
from abc import ABC, abstractmethod


class Algorithm(ABC):
    def template_method(self) -> None:
        self.default_step1()
        self.default_step2()
        self.step1()
        self.hook1()
        self.step2()
        self.hook2()
        self.step3()
    
    def default_step1(self) -> None:
        print('метод, одинаковый для любых алгоритмов.')
        
    def default_step2(self) -> None:
        print('метод, одинаковый для любых алгоритмов.')
    
    @abstractmethod
    def step1(self) -> None:
        pass
    
    @abstractmethod
    def step2(self) -> None:
        pass
    
    @abstractmethod
    def step3(self) -> None:
        pass
    
    def hook1(self) -> None:
        print('дополнительный метод, к-ый необязательно переопределять.')
        
    def hook2(self) -> None:
        print('дополнительный метод, к-ый необязательно переопределять.')
        
        
class AlgorithmA(Algorithm):
    def step1(self) -> None:
        print('шаг 1 по А')
    
    def step2(self) -> None:
        print('шаг 2 по А')
        
    def step3(self) -> None:
        print('шаг 3 по А') 
        
    def hook1(self) -> None:
        print('логирование...')
        
        
class AlgorithmB(Algorithm):
    def step1(self) -> None:
        print('шаг 1 по B')
    
    def step2(self) -> None:
        print('шаг 2 по B')
        
    def step3(self) -> None:
        print('шаг 3 по B') 


if __name__ == "__main__":
    alg: Algorithm = AlgorithmA()
    alg.template_method()
    
    alg: Algorithm = AlgorithmB()
    alg.template_method()