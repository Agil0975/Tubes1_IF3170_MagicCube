from MagicCube import MagicCube
import random

class SimulatedAnnealing:
    def __init__(self):
        """
        Constructor kelas SimulatedAnnealing
        """
        self.temperature = 10
        self.alpha = 0.9999
        self.min_temperature = 0.0001

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
        # print(random_successor.cube)
        """
        melakukan pencarian simulated annealing pada kubus magic

        Args:
            cube (MagicCube): objek kubus magic

        return:
        MagicCube: objek kubus hasil pencarian
        """
        no_improvement_steps = 0
        while self.getTemperature() > self.min_temperature:
            random_successor = current.randomSuccessor()
            delta = random_successor.value - current.value

            if delta >= 0:
                current = random_successor
                if delta == 0:
                    no_improvement_steps += 1
                else :
                    no_improvement_steps = 0
            else:
                probability = 2.71828 ** (delta / self.getTemperature())
                if random.random() < probability:
                    current = random_successor
                    no_improvement_steps = 0  # Reset counter on acceptance
                else:
                    no_improvement_steps += 1

            # Adaptive cooling: if no improvement for a while, cool faster
            if no_improvement_steps > 10 and self.getTemperature() > 1:
                self.setTemperature(self.getTemperature() * self.alpha * 0.99)
                print("Cooling faster")
            else:
                self.setTemperature(self.getTemperature() * self.alpha)
                

            # self.temperature *= self.alpha

            if current.value == 0 :
                return current


        return current
    
# Testing
sim_anneal = SimulatedAnnealing()
cube = MagicCube()
cube = sim_anneal.simulatedAnnealing(cube)
print(cube.value)
    