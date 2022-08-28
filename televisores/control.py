from televisores.tv import TV

class Control:
    def __init__(self):
        pass

    def enlazar(self, televisor):
        self._tv = televisor
        self._tv.control = self

    def getTv(self):
        return self._tv

    def setTv(self, televisor):
        self._tv = televisor

    def turnOff(self):
        self._tv.turnOff()

    def turnOn(self):
        self._tv.turnOn()

    def setCanal(self, i):
        self._tv.setCanal(i)

    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()