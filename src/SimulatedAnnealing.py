from MagicCube import MagicCube
import random
import time

class SimulatedAnnealing:
    def __init__(self):
        """
        Constructor kelas SimulatedAnnealing
        """
        self.temperature = 4
        self.alpha = 0.99999
        self.min_temperature = 0.0009
        self.iteration = 0

    def getTemperature(self) -> float:
        """
        Mengembalikan suhu saat ini

        return:
        float: suhu saat ini
        """
        return self.temperature
    
    def setTemperature(self, temperature: float) -> None:
        """
        Mengatur suhu saat ini

        Args:
        temperature (float): suhu yang akan diatur
        """
        self.temperature = temperature

    def simulatedAnnealing(self, current: MagicCube) -> MagicCube:
        random_successor = MagicCube()
        x = 0
        no_improvement_steps = 0
        sameRes = 0
        start_Line = False
        lastScore = 0

        while self.getTemperature() > self.min_temperature:
            random_successor = current.randomSuccessor()
            delta = random_successor.value - current.value

            if delta >= 0:
                current = random_successor
                lastScore = current.value2point0()
                if delta == 0:
                    no_improvement_steps += 0
                else :
                    no_improvement_steps = 0
            else:
                probability = 2.71828 ** (delta / self.getTemperature())
                if probability > 0.8:
                    lastScore = current.value2point0()
                    current = random_successor
                    no_improvement_steps = 0  # Reset counter on acceptance
                else:
                    no_improvement_steps += 1

            self.setTemperature(self.getTemperature() * self.alpha)
                
            self.iteration += 1    

            # self.temperature *= self.alpha

            if current.value == 0 :
                return current


        return current

    