from MagicCube import MagicCube 
from HillClimbing import HillClimbing
from GeneticAlgorithm import GeneticAlgorithm
from Visualization import Visualization
from SimulatedAnnealing import SimulatedAnnealing
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
            hill_climbing = HillClimbing()

            start = time.time()
            result, objective_value = hill_climbing.steepestAscent(cube)
            end = time.time()
            time_execution = end - start
            
            array_stats_text = f"""
            Initial Value        : {cube.value}
            Final Value          : {result.value}
            Number of Iterations : {len(objective_value) - 1}
            Time Execution       : {time_execution:.2f} seconds
            """

            Visualization.plot(objective_value, array_stats_text, cube, result)

        elif choice == "2": # Sideways Move Hill Climbing
            max_iterations = int(input("Enter the maximum number of sideways moves: "))

            cube = MagicCube()
            hill_climbing = HillClimbing()

            start = time.time()
            result, objective_value = hill_climbing.sidewaysMove(cube, max_iterations)
            end = time.time()
            time_execution = end - start

            array_stats_text = f"""
            Initial Value        : {cube.value}
            Final Value          : {result.value}
            Number of Iterations : {len(objective_value) - 1}
            Time Execution       : {time_execution:.2f} seconds
            """

            Visualization.plot(objective_value, array_stats_text, cube, result)

        elif choice == "3": # Random Restart Hill Climbing
            max_restarts = int(input("Enter the maximum number of restarts: "))
            cube = MagicCube()
            hill_climbing = HillClimbing()
            
            start = time.time()
            result, objective_values, iterations_per_restart, restart = hill_climbing.randomRestart(cube, max_restarts)
            end = time.time()
            time_execution = end - start
            
            array_stats_text = f"""
            Initial Value        : {cube.value}
            Final Value          : {result.value}
            Time Execution       : {time_execution:.2f} seconds
            Number of Restarts   : {restart}
            First Try            : {iterations_per_restart[0]} iterations
            """

            for i in range(1, restart+1):
                array_stats_text += f"\nRestart {i} : {iterations_per_restart[i]} iterations"

            Visualization.plot(objective_values, array_stats_text, cube, result)

        elif choice == "4": # Stochastic Hill Climbing
            max_iterations = int(input("Enter the maximum number of iterations: "))
            cube = MagicCube()                
            hill_climbing = HillClimbing()
            
            start = time.time()
            result, objective_values, number_of_iterations = hill_climbing.stochastic(cube, max_iterations)
            end = time.time()
            time_execution = end - start

            array_stats_text = f"""
            Initial Value        : {cube.value}
            Final Value          : {result.value}
            Number of Iterations : {number_of_iterations+1}
            Time Execution       : {time_execution:.2f} seconds
            """

            Visualization.plot(objective_values, array_stats_text, cube, result)

        elif choice == "5": # Simulated Annealing
            cube = MagicCube()
            sa = SimulatedAnnealing()
            start = time.time()
            resultCube, valuePerIteration, totalIteration = sa.simulatedAnnealing(cube)
            end = time.time()
            time_execution = end - start

            array_stats_text = f"""
            Initial Value        : {cube.value}
            Final Value          : {resultCube.value}
            Number of Iterations : {totalIteration}
            Time Execution       : {time_execution:.2f} seconds
            """

            Visualization.plot(valuePerIteration, array_stats_text, cube, resultCube)



        elif choice == "6": # Genetic Algorithm
            ga = GeneticAlgorithm()
            max_iterations = int(input("Enter the maximum number of generations: "))
            max_population = int(input("Enter the maximum number of population: "))
            
            # Generate initial population
            population = [MagicCube() for _ in range(max_population)]
            population.sort(key=lambda x: x.fitness, reverse=True)

            # Perform genetic algorithm
            time_execution, generation = ga.run(population, max_population, max_iterations)

            # plot the result
            max_initial_cube = ga.max_initial_cube
            max_final_cube = ga.max_final_cube
            array_stats_text = f"""
            Initial Maksimum Value    : {ga.value_max_history[0]}
            Final Maksimum Value      : {ga.value_max_history[-1]}
            Maksimum Value Achieved   : {ga.value_max_history.max()}
            Jumlah Populasi           : {max_population}
            Jumlah Generasi (Iterasi) : {generation}
            Waktu Eksekusi            : {time_execution:.2f} seconds
            """

            Visualization.plot(ga.value_max_history,
                 array_stats_text,
                 max_initial_cube,
                 max_final_cube,
                 ga.value_avg_history
                 )
            
        elif choice == "7":
            print("Exit")
            break

        else:
            print("Invalid input. Please try again.")
            continue