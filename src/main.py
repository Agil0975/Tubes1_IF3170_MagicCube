from MagicCube import MagicCube 
from HillClimbing import HillClimbing
from GeneticAlgorithm import GeneticAlgorithm
from utils.visualization import visualize_3d_cube
import time

if __name__ == "__main__":
    while True:

        print("Choose one of the following algorithms:")
        print("1. Steepest Ascent Hill Climbing")
        print("2. Sideways Move Hill Climbing")
        print("3. Random Restart Hill Climbing")
        print("4. Stochastic Hill Climbing")
        print("5. Simulated Annealing")
        print("6. Genetic Algorithm")
        print("7. Exit")

        choice = input("Enter the number of the algorithm you want to use: ")

        if choice == "1": # Steepest Ascent Hill Climbing
            cube = MagicCube()
            print(f'Initial Objective Value: {cube.value}')
            visualize_3d_cube(cube.cube, f"Initial Cube")
            hill_climbing = HillClimbing()

            start = time.time()
            result, objective_value = hill_climbing.steepestAscent(cube)
            end = time.time()
            
            print(f'Time taken: {end - start} seconds')
            print(f'Final Objective Value: {result.value}')
            hill_climbing.plot_objective_value(objective_value, f"Objective Value")
            visualize_3d_cube(result.cube, f"Final Cube")

        elif choice == "2": # Sideways Move Hill Climbing
            max_iterations = int(input("Enter the maximum number of sideways moves: "))

            cube = MagicCube()
            print(f'Initial Objective Value: {cube.value}')
            visualize_3d_cube(cube.cube, f"Initial Cube")
            hill_climbing = HillClimbing()

            start = time.time()
            result, objective_value = hill_climbing.sidewaysMove(cube, max_iterations)
            end = time.time()

            print(f'Time taken: {end - start} seconds')
            print(f'Number of iterations: {len(objective_value)}')
            print(f'Final Objective Value: {result.value}')
            hill_climbing.plot_objective_value(objective_value, f"Objective Value")
            visualize_3d_cube(result.cube, f"Final Cube")

        elif choice == "3": # Random Restart Hill Climbing
            max_restarts = int(input("Enter the maximum number of restarts: "))
    
            cube = MagicCube()
            print(f"Initial Objective Value: {cube.value}")
            visualize_3d_cube(cube.cube, f"Initial Cube")
                
            hill_climbing = HillClimbing()
            start = time.time()
            result, objective_values, iterations_per_restart = hill_climbing.randomRestart(cube, max_restarts)
            end = time.time()

            print(f"Time taken: {end - start} seconds")
            print(f"Final Objective Value: {result.value}")
            print(f"Number of restarts: {len(iterations_per_restart) - 1}")
            for j in range(len(iterations_per_restart)):
                if (j == 0):
                    print(f'Number of iterations for first trial: {iterations_per_restart[j]}')
                else:
                    print(f'Number of iterations for restart {j}: {iterations_per_restart[j]}')
            hill_climbing.plot_objective_value(objective_values, f"Objective Value")
            visualize_3d_cube(result.cube, f"Final Cube")

        elif choice == "4": # Stochastic Hill Climbing
            max_iterations = int(input("Enter the maximum number of iterations: "))
            
            cube = MagicCube()
            print(f"Initial Objective Value: {cube.value}")
            visualize_3d_cube(cube.cube, f"Initial Cube")
                
            hill_climbing = HillClimbing()
            start = time.time()
            result, objective_values, number_of_iterations = hill_climbing.stochastic(cube, max_iterations)
            end = time.time()

            print(f"Time taken: {end - start} seconds")
            print(f"Final Objective Value: {result.value}")
            print(f"Number of iterations: {number_of_iterations + 1}")
            hill_climbing.plot_objective_value(objective_values, f"Objective Value")
            visualize_3d_cube(result.cube, f"Final Cube")

        elif choice == "5": # Simulated Annealing
            print("Simulated Annealing")

        elif choice == "6": # Genetic Algorithm
            ga = GeneticAlgorithm()
            max_iterations = int(input("Enter the maximum number of generations: "))
            max_population = int(input("Enter the maximum number of population: "))
            
            # Generate initial population
            population = [MagicCube() for _ in range(max_population)]
            population.sort(key=lambda x: x.fitness, reverse=True)

            # Perform genetic algorithm
            ga.plot(*ga.run(population, max_population, max_iterations))

        elif choice == "7":
            print("Exit")
            break
        
        else:
            print("Invalid input. Please try again.")
            continue