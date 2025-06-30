from mock_readings import MockReadings
from threading import Thread


mock = MockReadings("Fake")
if __name__ == '__main__':
    Thread(target=mock.readDHT22).start()
    Thread(target=mock.readBME280).start()
    Thread(target=mock.readMH_RD).start()
    Thread(target=mock.readSound).start()
