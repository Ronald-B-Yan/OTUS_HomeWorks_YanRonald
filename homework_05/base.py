"""
Базовый модуль с описанием транспортного средства.
"""

from abc import ABC, abstractmethod
from exceptions import LowFuelError, NotEnoughFuel, EngineNotStarted

class Vehicle(ABC):
    """Класс Vehicle представляет абстрактное транспортное средство.
    
    Атрибуты:
        weight (float): Вес транспортного средства в килограммах.
        started (bool): Состояние, указывающее, запущено ли транспортное средство.
        fuel (float): Количество топлива в литрах.
        fuel_consumption (float): Расход топлива на единицу дистанции (литров / 100 километров).
    
    Методы:
        __init__():
            Инициализатор: установка веса, количества топлива и его расхода.
        
    Абстрактные методы:
        start() -> None:
            Запуск транспортного средства. Проверка уровня топлива, если машина ещё не заведена.
        
        move(distance: float) -> None:
            Перемещение на заданную дистанцию. Проверяет, заведён ли двигатель, хватит ли топлива, и уменьшает его количество.
    """

    def __init__(
        self, 
        weight: float = 0.0, 
        fuel: float = 0.0, 
        fuel_consumption: float = 0.0
    ):

        if weight < 0:
            raise ValueError("Вес не может быть отрицательным.")
        if fuel < 0:
            raise ValueError("Количество топлива не может быть отрицательным.")
        if fuel_consumption < 0:
            raise ValueError("Расход топлива не может быть отрицательным.")

        """
        Инициализатор: установка веса, количества топлива и его расхода.
        """
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False 

    @abstractmethod
    def start(self) -> None:
        """
        Запуск транспортного средства. 
        Проверка уровня топлива, если машина еще не заведена.
        """
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Невозможно запустить: низкий уровень топлива.")

    @abstractmethod
    def move(self, distance: float) -> None:
        """
        Перемещение на заданную дистанцию.
        Проверка, заведён ли двигатель и хватает ли топлива.
        """

        if not self.started:
            raise EngineNotStarted("Невозможно начать движение: двигатель не заведён.")
            
        required_fuel = distance * self.fuel_consumption
        
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
        else:
            raise NotEnoughFuel("Недостаточно топлива для преодоления этой дистанции.")