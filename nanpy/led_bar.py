from nanpy.arduinoboard import ArduinoObject
from nanpy.arduinoboard import (arduinoobjectmethod, returns)

class led_bar(ArduinoObject):

    def __init__(self, connection=None):
        ArduinoObject.__init__(self, connection=connection)
        self.id = self.call('new')

 
    @arduinoobjectmethod
    def barInit(self, digitalPin):
        pass
    
    @arduinoobjectmethod
    def barSetLevel(self, level):
        pass

    @arduinoobjectmethod
    def barSetLed(self, led, brightness):
        pass
