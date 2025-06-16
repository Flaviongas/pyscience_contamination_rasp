from abc import ABC, abstractmethod


class AbstractReading(ABC):

    @abstractmethod
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def readDHT22(self) -> float:
        raise NotImplementedError("DHT22 no implementado en la subclase.")

    @abstractmethod
    def readBME280(self) -> float:
        raise NotImplementedError("BME280 no implementado en la subclase.")

    @abstractmethod
    def readMH_RD(self) -> float:
        raise NotImplementedError("MHRD no implementado en la subclase.")

    @abstractmethod
    def readSound(self) -> float:
        raise NotImplementedError("Sound no implementado en la subclase.")

    # @abstractmethod
    # def readLight(self) -> float:
    #     raise NotImplementedError("Light no implementado en la subclase.")
    #
    # @abstractmethod
    # def readDSM501A(self) -> float:
    #     raise NotImplementedError("DSM501A no implementado en la subclase.")
    #
    # @abstractmethod
    # def readSDS011(self) -> float:
    #     raise NotImplementedError("SDS011 no implementado en la subclase.")
