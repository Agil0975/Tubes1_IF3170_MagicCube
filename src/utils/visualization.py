import matplotlib.pyplot as plt

colors = ['red', 'blue', 'green', 'black', 'purple']
def visualize_3d_cube(magic_cube, message: str) -> None:
    """
    Membuat visualisasi 3D dari magic cube 5x5x5
    
    Params:
            magic_cube (numpy.ndarray): 5x5x5 array of numbers
            message (str): title of the plot
    """
    fig = plt.figure(figsize=(15, 12))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot tiap cube
    for i in range(5):
        for j in range(5):
            for k in range(5):
                # Create white cube
                ax.bar3d(i, j, k, 0.8, 0.8, 0.8, color='white', alpha=0.1)
                
                # Tambahkan angka di tengah cube
                value = str(int(magic_cube[i,j,k]))
                # Center coordinates
                x_center = i + 0.4
                y_center = j + 0.4
                z_center = k + 0.4

                ax.text(x_center, y_center, z_center, 
                        value, color=colors[k], fontweight='bold',
                        ha='center', va='center', fontsize=16)
    
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
    
    # Adjust layout
    plt.tight_layout()
    plt.show()

def visualize_3d_cube_2(ax, magic_cube, message: str):
    """
    Create 3D visualization of a magic cube 5x5x5

    Params:
            ax (matplotlib.axes._subplots.Axes3DSubplot): 3D axes
            magic_cube (numpy.ndarray): 5x5x5 array of numbers
            message (str): title of the plot
    """
    for i in range(5):
        for j in range(5):
            for k in range(5):
                # Create white cube
                ax.bar3d(i, j, k, 0.8, 0.8, 0.8, color='white', alpha=0.1)

                # Add number in the middle of the cube
                value = str(int(magic_cube[i, j, k]))
                x_center, y_center, z_center = i + 0.4, j + 0.4, k + 0.4
                ax.text(x_center, y_center, z_center, 
                        value, color=colors[k], fontweight='bold',
                        ha='center', va='center', fontsize=12)
                
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