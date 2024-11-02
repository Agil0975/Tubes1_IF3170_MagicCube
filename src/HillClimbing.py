from MagicCube import MagicCube
import matplotlib.pyplot as plt
from utils.visualization import visualize_3d_cube

class HillClimbing:

    def steepestAscent(self, cube: MagicCube) -> MagicCube:
        """
        melakukan pencarian steepest ascent hill-climbing pada kubus magic

        Args:
            cube (MagicCube): objek kubus magic

        return:
        MagicCube: objek kubus hasil pencarian
        """
        current = cube
        objective_value = [] # List of objective value of the cube
        while True:
            best_neighbor = current.highestSuccessor()
            if best_neighbor.value <= current.value:
                break   
            current = best_neighbor
            objective_value.append(current.value)

        return current, objective_value
    
    
    def sidewaysMove(self, cube: MagicCube, max_iterations= 3) -> MagicCube:
        """
        melakukan pencarian sideways move hill-climbing pada kubus magic

        Args:
            cube (MagicCube): objek kubus magic

        return:
        MagicCube: objek kubus hasil pencarian
        """
        current = cube
        value_count = {} 
        objective_value = [] # List of objective value of the cube
        
        while True:
            best_neighbor = current.highestSuccessor()
            
            if best_neighbor.value < current.value:
                break
            
            if best_neighbor.value == current.value:
                # Add count of the value
                value_count[best_neighbor.value] = value_count.get(best_neighbor.value, 0) + 1
                
                # If the value has been reached 3 times, break
                if value_count[best_neighbor.value] >= max_iterations:
                    break
                    
            current = best_neighbor
            objective_value.append(current.value)

        return current, objective_value
    
    def randomRestart(self, cube: MagicCube) -> MagicCube:
        """
        melakukan pencarian random restart hill-climbing pada kubus magic

        Args:
            cube (MagicCube): objek kubus magic

        return:
        MagicCube: objek kubus hasil pencarian
        """
        return cube
    
    def stochastic(self, cube: MagicCube) -> MagicCube:
        """
        melakukan pencarian stochastic hill-climbing pada kubus magic

        Args:
            cube (MagicCube): objek kubus magic

        return:
        MagicCube: objek kubus hasil pencarian
        """
        return cube
    
    def plot_objective_value(self, objective_value: list, message: str) -> None:
        """
        melakukan plotting objective value

        Args:
            objective_value (list): list of objective value
        """
        plt.plot(objective_value)
        plt.xlabel('Iteration')
        plt.ylabel('Objective Value')
        plt.title(message)
        plt.show()