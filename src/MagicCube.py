import random
import numpy as np

class MagicCube:
    def __init__(self) -> None:
        """
        Constructor kelas Cube
        membuat kubus magic berukuran 5x5x5 secara acak
        """
        self.cube = list(range(1, 126))
        random.shuffle(self.cube)
        self.cube = np.array(self.cube).reshape(5,5,5)
        self.value = self.__value()
        self.fitness = self.__fitness()
    
    def __getitem__(self, key: tuple) -> int:
        """
        mengembalikan elemen kubus pada indeks tertentu

        Args:
            key (tuple): indeks elemen kubus

        return:
        int: elemen kubus pada indeks tertentu
        """
        return self.cube[key]

    def __value(self) -> int:
        """
        mengembalikan nilai objektif dari kubus
        value = -(banyaknya baris, kolom, tiang, dan diagonal yang belum berjumlah 315)
        range value = (-109, 0)
        
        return:
        int: nilai objektif kubus
        """
        target = 315
        count_mismatch = 0

        # Mengecek baris, kolom, dan tiang
        for i in range(5):
            for j in range(5):
                if np.sum(self[i, j, :]) != target:  # Baris sepanjang sumbu z
                    count_mismatch += 1
                if np.sum(self[i, :, j]) != target:  # Kolom sepanjang sumbu y
                    count_mismatch += 1
                if np.sum(self[:, i, j]) != target:  # Tiang sepanjang sumbu x
                    count_mismatch += 1

        # Mengecek diagonal pada setiap potongan bidang
        for i in range(5):
            if np.sum(np.diagonal(self[i, :, :])) != target:  # Diagonal bidang xy
                count_mismatch += 1
            if np.sum(np.diagonal(self[:, i, :])) != target:  # Diagonal bidang xz
                count_mismatch += 1
            if np.sum(np.diagonal(self[:, :, i])) != target:  # Diagonal bidang yz
                count_mismatch += 1
            if np.sum(np.diagonal(np.fliplr(self[i, :, :]))) != target:  # Diagonal bidang xy (berlawanan)
                count_mismatch += 1
            if np.sum(np.diagonal(np.fliplr(self[:, i, :]))) != target:  # Diagonal bidang xz (berlawanan)
                count_mismatch += 1
            if np.sum(np.diagonal(np.fliplr(self[:, :, i]))) != target:  # Diagonal bidang yz (berlawanan)
                count_mismatch += 1

        # Mengecek diagonal pada kubus
        if np.sum([self[i, i, i] for i in range(5)]) != target:          # Diagonal ruang 1
            count_mismatch += 1
        if np.sum([self[i, i, 4 - i] for i in range(5)]) != target:      # Diagonal ruang 2
            count_mismatch += 1
        if np.sum([self[i, 4 - i, i] for i in range(5)]) != target:      # Diagonal ruang 3
            count_mismatch += 1
        if np.sum([self[4 - i, i, i] for i in range(5)]) != target:      # Diagonal ruang 4
            count_mismatch += 1
        
        return -count_mismatch 

    def __fitness(self) -> int:
        """
        mengembalikan nilai fitness dari kubus
        fitness = 109 + value
        range fitness = (0, 109)

        return:
        int: nilai fitness kubus
        """
        return 109 + self.value

    def swap(self, a: tuple, b: tuple) -> None:
        """
        menukar dua elemen dalam kubus

        Args:
            a (tuple): indeks elemen pertama
            b (tuple): indeks elemen kedua
        """
        self.cube[a], self.cube[b] = self.cube[b], self.cube[a]
        
    def highestSuccessor(self) -> None:
        """
        mengembalikan succussor dengan objective value tertinggi

        return:
        Cube: objek kubus successor
        """
        max_value = -109
        max_cube = None
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    for l in range(i, 5):
                        for m in range(j, 5):
                            for n in range(k, 5):
                                new_cube = MagicCube()
                                new_cube.cube = self.cube.copy()
                                new_cube.swap((i, j, k), (l, m, n))
                                new_value = new_cube.value
                                if new_value > max_value:
                                    max_value = new_value
                                    max_cube = new_cube

        return max_cube

    def randomSuccessor(self) -> None:
        """
        mengembalikan succussor secara random

        return:
        Cube: objek kubus successor
        """
        i, j, k = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)
        l, m, n = random.randint(i, 4), random.randint(j, 4), random.randint(k, 4)
        new_cube = MagicCube()
        new_cube.cube = self.cube.copy()
        new_cube.swap((i, j, k), (l, m, n))

        return new_cube
    
# Test
a = MagicCube()
print(a.cube)
print(a.value)
print(a.fitness)
a.swap((1,1,1),(2,2,2))
print(a.highestSuccessor().value)
print(a.randomSuccessor().value)