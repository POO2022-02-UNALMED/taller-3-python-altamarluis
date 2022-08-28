
class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        TV._numTV += 1
        self.control = None

    def getMarca(self):
        return self._marca

    def getControl(self):
        return self.control
    
    def getPrecio(self):
        return self._precio

    def getVolumen(self):
        return self._volumen
    
    def getCanal(self):
        return self._canal

    def getEstado(self):
        return self._estado
    
    @classmethod
    def getNumTV(self):
        return TV._numTV

    def setMarca(self, marca):
         self._marca = marca
    
    def setControl(self, control):
         self.control = control
    
    def setPrecio(self, precio):
         self._precio = precio

    def setVolumen(self, volumen):
         if self._estado and volumen > -1 and volumen < 8:
            self._volumen = volumen

    def setCanal(self, canal):
         if self._estado and canal > 0 and canal < 121:
            self._canal = canal

    @classmethod
    def setNumTV(self, num):
        TV._numTV = num

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def canalUp(self):
        if self._estado and self._canal > 0 and self._canal < 120:
            self._canal += 1

    def canalDown(self):
        if self._estado and self._canal > 1 and self._canal < 121:
            self._canal -= 1

    def volumenUp(self):
        if self._estado and self._volumen > -1 and self._volumen < 7:
            self._volumen += 1

    def volumenDown(self):
        if self._estado and self._volumen > 0 and self._volumen < 8:
            self._volumen -= 1














     