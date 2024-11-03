from MagicCube import MagicCube
import numpy as np
import random
import time

class GeneticAlgorithm:
    def __init__(self) -> None:
        """
        Constructor kelas GeneticAlgorithm
        """
        self.value_max_history = np.array([])
        self.value_avg_history = np.array([])
        self.max_initial_cube = None
        self.max_final_cube = None

    def __update_history(self, population: list) -> None:
        """
        Memperbarui histori objective value maksimum dan rata-rata

        Args:
            population (list): populasi saat ini
        """
        total_value = sum([cube.value for cube in population])
        self.value_avg_history = np.append(self.value_avg_history, total_value / len(population))
        self.value_max_history = np.append(self.value_max_history, population[0].value)

    def __roulette_wheel(self, population: list, fitness_sum: int) -> list:
        """
        Membuat list roulette wheel berdasarkan populasi

        Args:
            population (list): daftar individu dalam populasi
                               populasi terurut berdasarkan fitness dari yang terbaik
            fitness_sum (int): total fitness dari populasi

        Returns:
            list: list roulette wheel
        """
        # Membuat roulette wheel
        roulette_wheel = []
        cumulative_probability = 0

        for cube in population:
            probability = (cube.fitness / fitness_sum) if fitness_sum > 0 else (1 / len(population))
            cumulative_probability += probability
            roulette_wheel.append((cumulative_probability, cube))

        return roulette_wheel

    def __selection(self, roulette_wheel: list) -> tuple[MagicCube, MagicCube]:
        """
        Seleksi dua individu dari roulette wheel

        Args:
            roulette_wheel (list): list roulette wheel

        Returns:
            tuple[MagicCube, MagicCube]: dua individu yang terpilih
        """
        parent1 = parent2 = None

        for _ in range(2):
            random_number = random.random()
            for probability, cube in roulette_wheel:
                if random_number <= probability:
                    if parent1 is None:
                        parent1 = cube
                    else:
                        parent2 = cube
                    break

        return parent1, parent2
        
    def __crossover(self, parent1: MagicCube, parent2: MagicCube, type: int) -> tuple[MagicCube, MagicCube]:
        """
        Crossover dua individu

        Args:
            parent1 (MagicCube): individu pertama
            parent2 (MagicCube): individu kedua
            type (int): tipe crossover
                        1: bidang-xy
                        2: bidang-xz
                        3: bidang-yz
        Returns:
            tuple[MagicCube, MagicCube]: dua individu hasil crossover
        """
        # Pilih dua titik potong secara acak
        cut = np.random.randint(1,4)
        child1 = child2 = None
        
        # Crossover
        if type == 1:
            child1 = self.__order_crossover_xy(parent1, parent2, cut)
            child2 = self.__order_crossover_xy(parent2, parent1, cut)
        elif type == 2:
            child1 = self.__order_crossover_xz(parent1, parent2, cut)
            child2 = self.__order_crossover_xz(parent2, parent1, cut)
        elif type == 3:
            child1 = self.__order_crossover_yz(parent1, parent2, cut)
            child2 = self.__order_crossover_yz(parent2, parent1, cut)

        return child1, child2
    
    def __order_crossover_xy(self, parent1: MagicCube, parent2: MagicCube, cut: int) -> MagicCube:
        """
        Crossover dengan order crossover pada bidang xy

        Args:
            parent1 (MagicCube): individu pertama
            parent2 (MagicCube): individu kedua
            cut (int): titik potong

        Returns:
            MagicCube: individu hasil crossover
        """
        child = MagicCube()
        child.cube = np.zeros((5, 5, 5), dtype=int)
        child.cube[:cut, :, :] = parent1.cube[:cut, :, :]

        # isi elemen yang belum ada dengan elemen dari parent2 berdasarkan urutan kemunculan di parent2
        child_x = cut
        child_y = 0
        child_z = 0

        # tempatkan elemen yang belum ada dengan urutan kemunculan di parent2
        for x in range(5):
            for y in range(5):
                for z in range(5):
                    if parent2.cube[x, y, z] not in child.cube:
                        child.cube[child_x, child_y, child_z] = parent2.cube[x, y, z]
                        child_z += 1
                        if child_z == 5:
                            child_z = 0
                            child_y += 1
                            if child_y == 5:
                                child_y = 0
                                child_x += 1
        return child
    
    def __order_crossover_xz(self, parent1: MagicCube, parent2: MagicCube, cut: int) -> MagicCube:
        """
        Crossover dengan order crossover pada bidang xz

        Args:
            parent1 (MagicCube): individu pertama
            parent2 (MagicCube): individu kedua
            cut (int): titik potong

        Returns:
            MagicCube: individu hasil crossover
        """
        child = MagicCube()
        child.cube = np.zeros((5, 5, 5), dtype=int)
        child.cube[:, :cut, :] = parent1.cube[:, :cut, :]

        # isi elemen yang belum ada dengan elemen dari parent2 berdasarkan urutan kemunculan di parent2
        child_x = 0
        child_y = cut
        child_z = 0

        # tempatkan elemen yang belum ada dengan urutan kemunculan di parent2
        for x in range(5):
            for y in range(5):
                for z in range(5):
                    if parent2.cube[x, y, z] not in child.cube:
                        child.cube[child_x, child_y, child_z] = parent2.cube[x, y, z]
                        child_z += 1
                        if child_z == 5:
                            child_z = 0
                            child_y += 1
                            if child_y == 5:
                                child_y = cut
                                child_x += 1
        return child

    def __order_crossover_yz(self, parent1: MagicCube, parent2: MagicCube, cut: int) -> MagicCube:
        """
        Crossover dengan order crossover pada bidang yz

        Args:
            parent1 (MagicCube): individu pertama
            parent2 (MagicCube): individu kedua
            cut (int): titik potong

        Returns:
            MagicCube: individu hasil crossover
        """
        child = MagicCube()
        child.cube = np.zeros((5, 5, 5), dtype=int)
        child.cube[:, :, :cut] = parent1.cube[:, :, :cut]

        # isi elemen yang belum ada dengan elemen dari parent
        child_x = 0
        child_y = 0
        child_z = cut

        # tempatkan elemen yang belum ada dengan urutan kemunculan di parent2
        for x in range(5):
            for y in range(5):
                for z in range(5):
                    if parent2.cube[x, y, z] not in child.cube:
                        child.cube[child_x, child_y, child_z] = parent2.cube[x, y, z]
                        child_z += 1
                        if child_z == 5:
                            child_z = cut
                            child_y += 1
                            if child_y == 5:
                                child_y = 0
                                child_x += 1
        return child
            
    def __mutation(self, individu: MagicCube, type: int = 1) -> None:
        """
        Mutasi individu

        Args:
            individu (MagicCube): individu yang akan dimutasi
            type (int): tipe mutasi
                        1: swap
                        2: scramble
                        3: inverse
        """
        # mutasi swap
        if type == 1:
            # pilih dua elemen secara acak
            a = tuple(np.random.randint(5, size=3))
            b = tuple(np.random.randint(5, size=3))
            # swap dua elemen
            individu.swap(a, b)
        # mutasi scramble
        elif type == 2:
            # pilih dua indeks secara acak
            start = np.random.randint(125)
            end = np.random.randint(start, min(126, start+20))
            # scramble elemen pada range tertentu
            individu.scramble(start, end)
        # mutasi inverse
        elif type == 3:
            # pilih dua indeks secara acak
            start = np.random.randint(125)
            end = np.random.randint(start, min(126, start+20))
            # balik elemen pada range tertentu
            individu.inverse(start, end)
        return

    def run(self, 
            population: list, 
            population_size: int,
            max_generation: int
            ) -> tuple[float, int]:
        """
        Menjalankan algoritma genetika

        Args:
            population (list): populasi awal
            population_size (int): ukuran populasi
            max_generation (int): maksimum generasi
            
        Returns:
            tuple: waktu eksekusi, generasi terakhir
        """
        current_generation = population
        generation = 0
        patient = 0 # jumlah generasi tanpa perubahan fitness terbaik
        total_fitness = sum([cube.fitness for cube in current_generation])
        self.__update_history(current_generation)
        self.max_initial_cube = current_generation[0]

        max_stuck = 0.1 * max_generation
        batas_mutasi_rendah = 0.05 if population_size >= 100 else 0.01
        batas_mutasi_tinggi = 0.1 if population_size >= 100 else 0.05
        batas_elitisme = 0.05

        start = time.time()
        while (current_generation[0].fitness < 109) and (generation < max_generation):
            print(f"Generasi ke-{generation}, fitness terbaik: {current_generation[0].fitness}, patient: {patient}")
            
            next_generation = []
            
            # Roulette wheel
            roulette_wheel = self.__roulette_wheel(current_generation, total_fitness)
            
            # Elitisme
            if patient < max_stuck:
                next_generation.extend(current_generation[:int(batas_elitisme * population_size)])
                
            # Seleksi dan Crossover
            for _ in range((population_size - len(next_generation)) // 2):
                parent1, parent2 = self.__selection(roulette_wheel)
                child1, child2 = self.__crossover(parent1, parent2, np.random.randint(1, 4))
                next_generation.extend([child1, child2])

            # Mutasi
            if patient < max_stuck: # mutasi rendah
                for i in range(1, len(next_generation)): # lewati individu terbaik
                    if np.random.random() < batas_mutasi_rendah:
                        self.__mutation(next_generation[i], np.random.randint(1, 4))
            else:   # mutasi tinggi
                for i in range(1, len(next_generation)): # lewati individu terbaik
                    if np.random.random() < batas_mutasi_tinggi:
                        self.__mutation(next_generation[i], np.random.randint(1, 4))

            # Update generasi
            current_generation = next_generation
            current_generation.sort(key=lambda x: x.fitness, reverse=True)
            total_fitness = sum([cube.fitness for cube in current_generation])
            self.__update_history(current_generation)

            # Update patient
            if self.value_max_history[-1] == self.value_max_history[-2]:
                patient += 1
            else:
                patient = 0

            generation += 1
        end = time.time()

        self.max_final_cube = current_generation[0]
        return end - start, generation