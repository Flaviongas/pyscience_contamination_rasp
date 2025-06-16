from abc import ABC, abstractmethod


class AbstractSensor(ABC):

    @abstractmethod
    def __init__(self, name: str, pin: int):
        self.name = name
        self.pin = pin

    @abstractmethod
    def read(self) -> float:
        raise NotImplementedError(
            "Se debe implementar este método en las subclases.")
