
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
from dataclasses import dataclass


class Builder(ABC):
    @abstractmethod
    def set_power_supply(self) -> None:
        pass
    
    @abstractmethod
    def set_motherboard(self) -> None:
        pass
    
    @abstractmethod
    def set_CPU(self) -> None:
        pass
    
    @abstractmethod
    def set_RAM(self) -> None:
        pass
    
    @abstractmethod
    def set_graphics_card(self) -> None:
        pass
    
    @abstractmethod
    def set_case(self) -> None:
        pass
    
    @abstractmethod
    def set_monitor(self) -> None:
        pass
    
    @abstractmethod
    def set_keyboard(self) -> None:
        pass
    
    @abstractmethod
    def set_mouse(self) -> None:
        pass
    
    @property
    @abstractmethod
    def computer(self) -> Any:
        pass
    
    
class LowPriceBuilder(Builder):
    def __init__(self) -> None:
        self._computer = Computer()

    def set_power_supply(self) -> None:
        self._computer.power_supply = 500
        
    def set_motherboard(self) -> None:
        self._computer.mother_board = 'Intel H61 Express'
        
    def set_CPU(self) -> None:
        self._computer.CPU = 'Intel Core I5'
        
    def set_RAM(self) -> None:
        self._computer.RAM = 8
        
    def set_graphics_card(self) -> None:
        self._computer.graphics_card = 4
        
    def set_case(self) -> None:
        self._computer.computer_case = 'black'
        
    def set_monitor(self) -> None:
        self._computer.monitor = 'HP HD'
        
    def set_keyboard(self) -> None:
        self._computer.keyboard = 'оклик'
        
    def set_mouse(self) -> None:
        self._computer.mouse = 'оклик'
        
    @property
    def computer(self) -> Computer:
        return self._computer
    

class HighPriceBuilder(Builder):
    def __init__(self) -> None:
        self._computer = Computer()

    def set_power_supply(self) -> None:
        self._computer.power_supply = 5000
        
    def set_motherboard(self) -> None:
        self._computer.mother_board = 'Intel TITAN Express'
        
    def set_CPU(self) -> None:
        self._computer.CPU = 'Intel Core I9'
        
    def set_RAM(self) -> None:
        self._computer.RAM = 64
        
    def set_graphics_card(self) -> None:
        self._computer.graphics_card = 16
        
    def set_case(self) -> None:
        self._computer.computer_case = 'golden rod'
        
    def set_monitor(self) -> None:
        self._computer.monitor = 'Lenovo PRO gamer ULTRA 8k'
        
    def set_keyboard(self) -> None:
        self._computer.keyboard = 'RAZOR PRO MLG ULTRA X'
        
    def set_mouse(self) -> None:
        self._computer.mouse = 'BLOODY BEAST ULTRA HARDCORE GAMER'
        
    @property
    def computer(self) -> Computer:
        return self._computer

    
@dataclass
class Computer:
    power_supply: int = None
    mother_board: str = None
    CPU: str = None
    RAM: int = None
    graphics_card: int = None
    computer_case: str = None
    monitor: str | None = None
    keyboard: str | None = None
    mouse: str | None = None


class Director:
    def __init__(self, builder: Builder) -> None:
        self._builder = builder
        
    @property
    def builder(self) -> Builder:
        return self._builder
    
    @builder.setter
    def builder(self, new_builder: Builder) -> None:
        self._builder = new_builder
        
    def build_max_configuration(self) -> None:
        self._builder.set_motherboard()
        self._builder.set_CPU()
        self._builder.set_graphics_card()
        self._builder.set_power_supply()
        self._builder.set_RAM()
        self._builder.set_case()
        self._builder.set_monitor()
        self._builder.set_keyboard()
        self._builder.set_mouse()
        
    def build_min_configuration(self) -> None:
        self._builder.set_motherboard()
        self._builder.set_CPU()
        self._builder.set_graphics_card()
        self._builder.set_power_supply()
        self._builder.set_RAM()
        self._builder.set_case()
        
        
if __name__ == "__main__":
    low_budget: Builder = LowPriceBuilder()
    high_budget: Builder = HighPriceBuilder()
    
    director: Director = Director(low_budget)
    
    director.build_min_configuration()
    print(low_budget.computer)
    
    director.builder = high_budget
    director.build_max_configuration()
    print(high_budget.computer)
    
    
    
        

    
    
    
    
