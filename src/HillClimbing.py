import MagicCube

class HillClimbing:
    def __init__(self) -> None:
        """
        Constructor kelas HillClimbing
        membuat objek HillClimbing
        """        

    def steepestAscent(self, cube: MagicCube) -> MagicCube:
        """
        melakukan pencarian steepest ascent hill-climbing pada kubus magic

        Args:
            cube (MagicCube): objek kubus magic

        return:
        MagicCube: objek kubus hasil pencarian
        """
        return cube
    
    def sidewaysMove(self, cube: MagicCube) -> MagicCube:
        """
        melakukan pencarian sideways move hill-climbing pada kubus magic

        Args:
            cube (MagicCube): objek kubus magic

        return:
        MagicCube: objek kubus hasil pencarian
        """
        return cube
    
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

hc = HillClimbing()
cube = MagicCube.MagicCube()

# Test steepestAscent
result = hc.steepestAscent(cube)
print(result)

# Test sidewaysMove
result = hc.sidewaysMove(cube)
print(result)

# Test randomRestart
result = hc.randomRestart(cube)
print(result)

# Test stochastic
result = hc.stochastic(cube)
print(result)