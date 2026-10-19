"""
Модуль с описанием двигателя.
"""

from dataclasses import dataclass

@dataclass
class Engine:
    """Двигатель транспортного средства.

    Атрибуты:
        volume (float): Объём двигателя (литров).
        pistons (int): Количество поршней.
    """

    volume: float
    pistons: int