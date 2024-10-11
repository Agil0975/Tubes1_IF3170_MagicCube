class MagicCube:
    def __init__(self) -> None:
        """
        Constructor kelas Cube
        membuat kubus magic berukuran 5x5x5 secara acak
        """
        self.cube = "ini kubus"

    def value(self) -> int:
        """
        mengembalikan nilai objektif dari kubus
        value = -(banyaknya baris, kolom, tiang, dan diagonal yang belum berjumlah 315)
        range value = (-109, 0)
        
        return:
        int: nilai objektif kubus
        """
        return 0

    
    def fitness(self) -> int:
        """
        mengembalikan nilai fitness dari kubus
        fitness = 109 + value
        range fitness = (0, 109)

        return:
        int: nilai fitness kubus
        """
        return 0

    def swap(self, a: tuple, b: tuple) -> None:
        """
        menukar dua elemen dalam kubus

        Args:
            a (tuple): indeks elemen pertama
            b (tuple): indeks elemen kedua
        """
        print("swap", a, b)

    def highestSuccessor(self) -> None:
        """
        mengembalikan succussor dengan objective value tertinggi

        return:
        Cube: objek kubus successor
        """
        return MagicCube()

    def randomSuccessor(self) -> None:
        """
        mengembalikan succussor secara random

        return:
        Cube: objek kubus successor
        """
        return MagicCube()
    
a = MagicCube()
print(a.cube)
print(a.value())
print(a.fitness())
a.swap((1,1,1),(2,2,2))
print(a.highestSuccessor().value())
print(a.randomSuccessor().value())