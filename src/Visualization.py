import matplotlib.pyplot as plt
from MagicCube import MagicCube

colors = ['red', 'blue', 'green', 'black', 'purple']
class Visualization:
    
    @staticmethod
    def plot(objective_value: list, message: str, 
            initial_cube: MagicCube, final_cube: MagicCube,
            avg_objective_value: list = None, euler_value: list = None) -> None:
            """
            membuat plot hasil pencarian

            Args:
                objective_value (list): list nilai objektif
                message (str): keterangan plot
                initial_cube (MagicCube): kubus awal
                final_cube (MagicCube): kubus akhir
                avg_objective_value (list): list rata-rata nilai objektif
            """
            # Membuat figure dengan gridspec dan mengatur rasio
            fig = plt.figure(figsize=(15, 12))
            if euler_value is None:
                gs = fig.add_gridspec(3, 2, height_ratios=[30, 5, 65], width_ratios=[70, 30])
            else:
                gs = fig.add_gridspec(3, 2, height_ratios=[35, 2, 40], width_ratios=[50, 50])

            # Baris 1, Kolom 1: Grafik garis nilai objektif
            ax1 = fig.add_subplot(gs[0, 0])
            if avg_objective_value is not None:
                ax1.plot(objective_value, label="Max Fitness Value")
                ax1.plot(avg_objective_value, label="Average Fitness Value")
            else:
                ax1.plot(objective_value, label="")
            ax1.set_title("Objective Value")
            ax1.set_xlabel("Iteration")
            ax1.set_ylabel("Objective Value")
            ax1.legend()

            if euler_value is not None:
                axEuler = fig.add_subplot(gs[0,1])
                axEuler.plot(euler_value, label="Euler Value")
                axEuler.set_title("Euler Value")
                axEuler.set_xlabel("Iteration")
                axEuler.set_ylabel("Euler Value")
                axEuler.legend()


            # Baris 1, Kolom 2: Statistik algoritma genetika
            if euler_value is None:
                ax2 = fig.add_subplot(gs[0, 1])
            else :
                ax2 = fig.add_subplot(gs[1, 0])
            array_stats_text = message

            ax2.axis("off")
            ax2.text(0, 0.75, array_stats_text, ha="left", va="center", fontsize=12, fontdict={"family": "monospace"})
            ax2.set_title("Statistics")

            # Baris 3: Visualisasi 3D kubus
            gs_bottom = gs[2, :].subgridspec(1, 2, width_ratios=[50, 50])

            # Baris 3, Kolom 1 dan 2: Plot 3D kubus
            ax3 = fig.add_subplot(gs_bottom[0, 0], projection='3d')
            Visualization.visualize_3d_cube(ax3, initial_cube, "Initial Cube")

            ax4 = fig.add_subplot(gs_bottom[0, 1], projection='3d')
            Visualization.visualize_3d_cube(ax4, final_cube, "Final Cube")

            plt.tight_layout()
            plt.subplots_adjust(hspace=0.45, wspace=0.3)
            plt.show()

    @staticmethod
    def visualize_3d_cube(ax: plt.Axes, magic_cube: MagicCube, message: str) -> None:
        """
        Create 3D visualization of a magic cube 5x5x5

        Params:
                ax (matplotlib.axes._subplots.Axes3DSubplot): 3D axes
                magic_cube (MagicCube): 5x5x5 array of numbers
                message (str): title of the plot
        """
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    # Create white cube
                    ax.bar3d(i, j, k, 0.8, 0.8, 0.8, color='white', alpha=0.05)

                    # Add number in the middle of the cube
                    value = str(int(magic_cube[i, j, k]))
                    x_center, y_center, z_center = i + 0.4, j + 0.4, k + 0.4
                    ax.text(x_center, y_center, z_center, 
                            value, color=colors[k],
                            ha='center', va='center', 
                            fontsize=8)
                    
        # Set labels and title
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(message)

        # Set axis limits
        ax.set_xlim([0, 5])
        ax.set_ylim([0, 5])
        ax.set_zlim([0, 5])

        # Set viewing angle
        ax.view_init(elev=30, azim=45)

        # Add grid
        ax.grid(True)