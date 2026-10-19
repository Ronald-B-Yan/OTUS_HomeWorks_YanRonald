"""
Модуль с описанием самолёта.
"""

from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    """Самолёт — транспортное средство с грузовым отсеком.

    Атрибуты:
        cargo (float): Текущая загрузка (по умолчанию 0).
        max_cargo (float): Максимальная грузоподъёмность.
    """

    def __init__(
        self,
        cargo: float = 0.0,
        max_cargo: float = 0.0,
        weight: float = 0.0,
        fuel: float = 0.0,
        fuel_consumption: float = 0.0,
    ):

        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)

        if max_cargo < 0:
            raise ValueError("Максимальная грузоподъёмность не может быть отрицательной.")
        if cargo < 0:
            raise ValueError("Текущая загрузка не может быть отрицательной.")
        if cargo > max_cargo:
            raise CargoOverload(
                f"Превышение максимальной грузоподъёмности: {cargo} > {max_cargo}."
            )

        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, amount: float) -> None:
        """Загружает дополнительное количество груза.
        Если суммарная загрузка превысит максимальную — выходит ошибка CargoOverload.
        """
        if amount < 0:
            raise ValueError("Вес груза не может быть отрицательным.")

        if self.cargo + amount > self.max_cargo:
            raise CargoOverload(
                f"Перегруз: {self.cargo + amount} > {self.max_cargo}."
            )

        self.cargo += amount

    def remove_all_cargo(self) -> float:
        """Обнуляет загрузку и возвращает значение, которое было до обнуления."""
        old_cargo = self.cargo
        self.cargo = 0.0
        return old_cargo
