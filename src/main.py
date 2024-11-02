from MagicCube import MagicCube 
from HillClimbing import HillClimbing
from utils.visualization import visualize_3d_cube
import time

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

    if choice == "1":
        for i in range (3):
            cube = MagicCube()
            print(f'Initial Objective Value: {cube.value}')
            visualize_3d_cube(cube.cube, f"Initial Cube {i+1}")
            hill_climbing = HillClimbing()

            start = time.time()
            result, objective_value = hill_climbing.steepestAscent(cube)
            end = time.time()

            print(f'Time taken: {end - start} seconds')
            print(f'Final Objective Value: {result.value}')
            hill_climbing.plot_objective_value(objective_value, f"Objective value over iterations {i+1}")
            visualize_3d_cube(result.cube, f"Final Cube {i+1}")

    elif choice == "2":
        max_iterations = int(input("Enter the maximum number of sideways moves: "))
        for i in range (3):
            cube = MagicCube()

            print(f'Initial Objective Value: {cube.value}')
            visualize_3d_cube(cube.cube, f"Initial Cube {i+1}")
            hill_climbing = HillClimbing()

            start = time.time()
            result, objective_value = hill_climbing.sidewaysMove(cube, max_iterations)
            end = time.time()

            print(f'Time taken: {end - start} seconds')
            print(f'Number of iterations: {len(objective_value)}')
            print(f'Final Objective Value: {result.value}')
            hill_climbing.plot_objective_value(objective_value, f"Objective value over iterations {i+1}")
            visualize_3d_cube(result.cube, f"Final Cube {i+1}")

    elif choice == "3":
        print("Random Restart Hill Climbing")
    elif choice == "4":
        print("Stochastic Hill Climbing")
    elif choice == "5":
        print("Simulated Annealing")
    elif choice == "6":
        print("Genetic Algorithm")
    elif choice == "7":
        print("Exit")
        break
    else:
        print("Invalid input. Please try again.")
        continue