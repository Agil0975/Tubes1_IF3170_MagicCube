from MagicCube import MagicCube

class SimulatedAnnealing:
    def __init__(self):
        """
        Constructor kelas SimulatedAnnealing
        """
        self.temperature = 1
        self.alpha_cold = 0.99999
        self.alpha = 0.9999
        self.min_temperature = 0.00001
        self.iteration = 0
        self.curretValue = [] 
        self.eulerValue = []
        self.probability = 0.3
        self.stuck = 0

    def getTemperature(self) -> float:
        """
        Mengembalikan suhu saat ini

        Returns:
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
        """
        Algoritma Simulated Annealing

        Args:
            current (MagicCube): objek kubus magic

        Returns:
            MagicCube: kube magic hasil pencarian
        """
        random_successor = MagicCube()
        no_improvement_steps = 0
        probability = 0
        self.curretValue.append(current.value)
        
        while self.getTemperature() > self.min_temperature:
            print(self.iteration, current.value)
            random_successor = current.randomSuccessor()
            delta = random_successor.value - current.value

            if delta >= 0:
                current = random_successor
                probability = 1
                if delta == 0:
                    no_improvement_steps += 0
                else :
                    no_improvement_steps = 0
            else:
                probability = 2.71828 ** (delta / self.getTemperature())
                self.stuck += 1
                if probability > self.probability:
                    current = random_successor
                    no_improvement_steps = 0  # Reset counter on acceptance
                else:
                    no_improvement_steps += 1

            self.eulerValue.append(probability)
            self.curretValue.append(current.value)
            self.iteration += 1    

            # self.temperature *= self.alpha
            
            if no_improvement_steps // 2000 > 0:
                if no_improvement_steps // 2000 > 0:
                    minus = no_improvement_steps // 2000
                elif no_improvement_steps // 2000 > 6:
                    minus = 2.9
                if current.value < -52 and self.temperature > 0.001:
                    self.probability = 0.3 + 0.05 * (1 - minus)
                self.temperature = self.temperature * self.alpha
            else:
                self.probability = 0.3
                self.temperature = self.temperature * self.alpha_cold

            if current.value == 0 :
                return current

        return current