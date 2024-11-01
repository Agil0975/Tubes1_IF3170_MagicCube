from MagicCube import MagicCube
import numpy as np
import random

class GeneticAlgorithm:
    def __init__(self) -> None:
        """
        Constructor kelas GeneticAlgorithm
        """
        self.fitness_max_history = np.array([])
        self.fitness_avg_history = np.array([])
        self.max_cube_history = np.array([])

    def __roulette_wheel(self, population: list) -> list:
        """
        Membuat list roulette wheel berdasarkan populasi

        Args:
            population (list): daftar individu dalam populasi
                               populasi terurut berdasarkan fitness dari yang terbaik

        Returns:
            list: list roulette wheel
        """
        # Menghitung total fitness
        total_fitness = sum([cube.fitness for cube in population])

        # sekalian menghitung rata-rata fitness
        avg_fitness = total_fitness / len(population)
        self.fitness_avg_history = np.append(self.fitness_avg_history, avg_fitness)

        # Membuat roulette wheel
        roulette_wheel = []
        cumulative_probability = 0

        for cube in population:
            probability = cube.fitness / total_fitness
            cumulative_probability += probability
            roulette_wheel.append((cumulative_probability, cube))

        return roulette_wheel

    def __selection(self, roulette_wheel: list) -> list:
        """
        Seleksi dua individu dari roulette wheel

        Args:
            roulette_wheel (list): list roulette wheel

        Returns:
            list: dua individu terpilih
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
        
    def __crossover(self, parent1: MagicCube, parent2: MagicCube) -> list:
        """
        Crossover dua individu

        Args:
            parent1 (MagicCube): individu pertama
            parent2 (MagicCube): individu kedua

        Returns:
            list: dua individu hasil crossover
        """
        
    
    def mutation(self, individu: MagicCube, type: int = 1) -> None:
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

    def run(self, population_size: int, max_generation: int, mutation_rate: float) -> MagicCube:
        """
        Menjalankan algoritma genetika

        Args:
            population_size (int): ukuran populasi
            max_generation (int): maksimum generasi
            mutation_rate (float): probabilitas mutasi

        Returns:
            MagicCube: kubus magic terbaik
        """