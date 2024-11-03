from MagicCube import MagicCube

class HillClimbing:

    def steepestAscent(self, cube: MagicCube) -> tuple[MagicCube, list]:
        """
        melakukan pencarian steepest ascent hill-climbing pada kubus magic

        Args:
            cube (MagicCube): objek kubus magic

        return:
        tuple[MagicCube, list]: objek kubus hasil pencarian dan list nilai objektif
        """
        current = cube
        objective_value = [current.value] # List of objective value of the cube

        while True:
            print(f"Current Value: {current.value}")
            best_neighbor = current.highestSuccessor()
            if best_neighbor.value <= current.value:
                break
            current = best_neighbor
            objective_value.append(current.value)

        return current, objective_value
    
    def sidewaysMove(self, cube: MagicCube, max_iterations: int = 3) -> tuple[MagicCube, list]:
        """
        melakukan pencarian sideways move hill-climbing pada kubus magic

        Args:
            cube (MagicCube): objek kubus magic
            max_iterations (int): maksimum sideways move

        return:
        tuple[MagicCube, list]: objek kubus hasil pencarian dan list nilai objektif
        """
        current = cube
        value_count = {} # the count of the side way move
        objective_value = [current.value] # List of objective value of the cube
        
        while True:
            print(f"Current Value: {current.value}")
            best_neighbor = current.highestSuccessor()
            
            if best_neighbor.value < current.value:
                break
            
            if best_neighbor.value == current.value:
                # Add count of the value
                value_count[best_neighbor.value] = value_count.get(best_neighbor.value, 0) + 1
                
                # If the value has been reached max_iterations, break
                if value_count[best_neighbor.value] >= max_iterations:
                    break
                    
            current = best_neighbor
            objective_value.append(current.value)

        return current, objective_value
    
    def randomRestart(self, cube: MagicCube, max_restarts: int = 3) -> tuple[MagicCube, list, list, int]:
        """
        melakukan pencarian random restart hill-climbing pada kubus magic

        Args:
            cube (MagicCube): objek kubus magic
            max_restarts (int): maksimum restart

        return:
        tuple[MagicCube, list, list, int]: objek kubus hasil pencarian, list nilai objektif, list iterasi per restart, dan jumlah restart
        """

        objective_values = []
        iterations_per_restart = []

        for i in range(max_restarts + 1):
            print(f"Restart {i}")
            steepest_ascent_result, objective_values_per_restart = self.steepestAscent(cube)
            objective_values.extend(objective_values_per_restart)
            iterations_per_restart.append(len(objective_values_per_restart))
            
            if steepest_ascent_result.value == 0:
                return steepest_ascent_result, objective_values, iterations_per_restart, i
            
            if i < max_restarts:
                cube = MagicCube()

        return steepest_ascent_result, objective_values, iterations_per_restart, i
    
    def stochastic(self, cube: MagicCube, max_iterations: int) -> tuple[MagicCube, list, int]:
        """
        melakukan pencarian stochastic hill-climbing pada kubus magic

        Args:
            cube (MagicCube): objek kubus magic
            max_iterations (int): maksimum iterasi

        return:
        tuple[MagicCube, list, int]: objek kubus hasil pencarian, list nilai objektif, dan jumlah iterasi
        """
        objective_values = []
        objective_values.append(cube.value)

        for i in range(max_iterations):
            print(f"iterasi-{i} Current Value: {cube.value}")
            neighbor = cube.randomSuccessor()
            if neighbor.value > cube.value:
                cube = neighbor
            
            objective_values.append(cube.value)
            
            if cube.value == 0:
                return cube, objective_values, i
        
        return cube, objective_values, i