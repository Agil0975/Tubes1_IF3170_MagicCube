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
        mengembalikan nilai elemen kubus pada indeks tertentu

        Args:
            key (tuple): indeks elemen kubus

        return:
        int: nilai elemen kubus
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
                if np.sum(self[i, j, :]) != target:  # Baris
                    count_mismatch += 1
                if np.sum(self[i, :, j]) != target:  # Kolom
                    count_mismatch += 1
                if np.sum(self[:, i, j]) != target:  # Tiang
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
    
    def value2point0(self) -> int:
        """
        mengembalikan nilai objektif dari kubus
        value = -(banyaknya baris, kolom, tiang, dan diagonal yang belum berjumlah 315)
        range value = (-109, 0)
        
        return:
        int: nilai objektif kubus
        """
        target = 315
        sum = 0

        # Mengecek baris, kolom, dan tiang
        for i in range(5):
            for j in range(5):
                sum += abs(np.sum(self[i, j, :]) - target) # Baris
                sum += abs(np.sum(self[i, :, j]) - target)  # Kolom
                sum += abs(np.sum(self[:, i, j]) - target)  # Tiang

        # Mengecek diagonal pada setiap potongan bidang
        for i in range(5):
            sum += abs(np.sum(np.diagonal(self[i, :, :])) - target)  # Diagonal bidang xy
            sum += abs(np.sum(np.diagonal(self[:, i, :])) - target)  # Diagonal bidang xz
            sum += abs(np.sum(np.diagonal(self[:, :, i])) - target)  # Diagonal bidang yz
            sum += abs(np.sum(np.diagonal(np.fliplr(self[i, :, :]))) - target)  # Diagonal bidang xy (berlawanan)
            sum += abs(np.sum(np.diagonal(np.fliplr(self[:, i, :]))) - target)  # Diagonal bidang xz (berlawanan)
            sum += abs(np.sum(np.diagonal(np.fliplr(self[:, :, i]))) - target)  # Diagonal bidang yz (berlawanan)

        # Mengecek diagonal pada kubus
        sum += abs(np.sum([self[i, i, i] for i in range(5)]) - target)  # Diagonal ruang 1
        sum += abs(np.sum([self[i, i, 4 - i] for i in range(5)]) - target)  # Diagonal ruang 2
        sum += abs(np.sum([self[i, 4 - i, i] for i in range(5)]) - target)  # Diagonal ruang 3
        sum += abs(np.sum([self[4 - i, i, i] for i in range(5)]) - target)  # Diagonal ruang 4
        
        return -sum

    def __fitness(self) -> int:
        """
        mengembalikan nilai fitness dari kubus
        fitness = 109 + value
        range fitness = (0, 109)

        return:
        int: nilai fitness kubus
        """
        return 109 + self.value
    
    def refresh(self) -> None:
        """
        mengupdate nilai value dan fitness kubus
        """
        self.value = self.__value()
        self.fitness = self.__fitness()

    def swap(self, a: tuple, b: tuple) -> None:
        """
        menukar dua elemen dalam kubus

        Args:
            a (tuple): indeks elemen pertama
            b (tuple): indeks elemen kedua
        """
        self.cube[a], self.cube[b] = self.cube[b], self.cube[a]
        self.refresh()

    def scramble(self, start: int, end: int) -> None:
        """
        mengacak elemen kubus pada range tertentu

        Args:
            start (int): indeks awal
            end (int): indeks akhir
        """
        # ubah cube menjadi 1 dimensi
        cube = self.cube.flatten()
        # acak elemen pada range tertentu
        cube[start:end] = np.random.permutation(cube[start:end])
        # ubah cube menjadi 3 dimensi
        self.cube = cube.reshape(5,5,5)
        self.refresh()

    def inverse(self, start: int, end: int) -> None:
        """
        membalik elemen kubus pada range tertentu

        Args:
            start (int): indeks awal
            end (int): indeks akhir
        """
        # ubah cube menjadi 1 dimensi
        cube = self.cube.flatten()
        # balik elemen pada range tertentu
        cube[start:end] = cube[start:end][::-1]
        # ubah cube menjadi 3 dimensi
        self.cube = cube.reshape(5,5,5)
        self.refresh()

    def highestSuccessor(self) -> 'MagicCube':
        """
        mengembalikan succussor dengan objective value tertinggi

        return:
        MagicCube: objek kubus successor
        """
        max_value = -109
        max_cube = None
        for x1 in range(5):
            for y1 in range(5):
                for z1 in range(5):
                    for x2 in range(x1, 5):
                        for y2 in range(y1, 5):
                            for z2 in range(z1 + 1, 5):
                                new_cube = MagicCube()
                                new_cube.cube = self.cube.copy()
                                new_cube.swap((x1, y1, z1), (x2, y2, z2))

                                if new_cube.value > max_value:
                                    max_value = new_cube.value
                                    max_cube = new_cube
        return max_cube

    def randomSuccessor(self) -> 'MagicCube':
        """
        mengembalikan succussor secara random

        return:
        MagicCube: objek kubus successor
        """
        first_elmt = tuple(np.random.randint(5, size=3))
        second_elmt = tuple(np.random.randint(5, size=3))
        while first_elmt == second_elmt:
            second_elmt = tuple(np.random.randint(5, size=3))

        new_cube = MagicCube()
        new_cube.cube = self.cube.copy()
        new_cube.swap(first_elmt, second_elmt)

        return new_cube