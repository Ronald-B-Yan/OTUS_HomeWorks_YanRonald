"""
Модуль с описанием автомобиля.
"""

from base import Vehicle
from engine import Engine

class Car(Vehicle):
    """Класс Car представляет собой автомобиль, который наследует от класса Vehicle.
    
    Атрибуты:
        engine (Engine): Двигатель автомобиля.
        weight (float): Вес автомобиля. По умолчанию 0.0.
        fuel (float): Количество топлива в автомобиле. По умолчанию 0.0.
        fuel_consumption (float): Расход топлива автомобиля. По умолчанию 0.0.
    
    Методы:
        set_engine(engine: Engine) -> None:
            Устанавливает двигатель на текущий экземпляр автомобиля.
            Если переданный объект не является экземпляром класса Engine, 
            вызывается исключение TypeError.
    """

    def __init__(
        self,
        engine: Engine,
        weight: float = 0.0,
        fuel: float = 0.0,
        fuel_consumption: float = 0.0,
    ):
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self.set_engine(engine)

    def set_engine(self, engine: Engine) -> None:
        """Устанавливает двигатель на текущий экземпляр автомобиля."""
        
        if not isinstance(engine, Engine):
            raise TypeError("engine должен быть экземпляром класса Engine.")
        self.engine = engine
