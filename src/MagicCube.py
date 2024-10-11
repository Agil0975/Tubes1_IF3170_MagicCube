class MagicCube:
    def __init__(self) -> None:
        """
        Constructor kelas Cube
        membuat kubus magic berukuran 5x5x5 secara acak

        return:
        Cube: objek kubus
        """

    def value(self) -> int:
        """
        mengembalikan nilai objektif dari kubus
        value = -(banyaknya baris, kolom, tiang, dan diagonal yang belum berjumlah 315)

        return:
        int: nilai objektif kubus
        """
    
    def fitness(self) -> int:
        """
        mengembalikan nilai fitness dari kubus
        fitness = 109 + value

        return:
        int: nilai fitness kubus
        """

    def swap(self, a: tuple, b: tuple) -> None:
        """
        menukar dua elemen dalam kubus

        Args:
            a (tuple): indeks elemen pertama
            b (tuple): indeks elemen kedua
        """

    def highestSuccessor(self) -> None:
        """
        mengembalikan succussor dengan objective value tertinggi

        return:
        Cube: objek kubus successor
        """

    def randomSuccessor(self) -> None:
        """
        mengembalikan succussor secara random

        return:
        Cube: objek kubus successor
        """