
from __future__ import annotations
from abc import ABC, abstractmethod


class Interactor(ABC):
    @abstractmethod
    def factory_method(self) -> Algorithm:
        pass
    
    def run_algorithm(self):
        alg: Algorithm = self.factory_method()
        print(f'Запускаю: {alg}')
        alg.run()
        print(f'Выполнение {alg} завершено!')
        print('Продолжаю работу...')


class InteractorA(Interactor):
    def factory_method(self) -> Algorithm:
        return AlgorithmA()
    
class InteractorB(Interactor):
    def factory_method(self) -> Algorithm:
        return AlgorithmB()
    
    
class Algorithm(ABC):
    @abstractmethod
    def run(self) -> None:
        pass
    
    @abstractmethod
    def __repr__(self) -> str:
        pass
    

class AlgorithmA(Algorithm):
    def run(self) -> None:
        print('Выполняется алгоритм...')
    
    def __repr__(self) -> str:
        return 'Алогритм А'


class AlgorithmB(Algorithm):
    def run(self) -> None:
        print('Выполняется алгоритм...')
    
    def __repr__(self) -> str:
        return 'Алогритм B'
    
    
if __name__ == '__main__':
    interactor: Interactor = InteractorA()
    interactor.run_algorithm()
    
    interactor: Interactor = InteractorB()
    interactor.run_algorithm()


