import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Determine correct trajectory.csv location
csv_path = 'trajectory.csv' if os.path.exists('trajectory.csv') else '../trajectory.csv'
data = pd.read_csv(csv_path)

fig, ax = plt.subplots(figsize=(8, 6))

# Plot static elements
ax.plot(data['x'].iloc[0], data['y'].iloc[0], 'go', markersize=12, label='Start Position')
ax.plot(data['x'].iloc[-1], data['y'].iloc[-1], 'ro', markersize=12, label='Target Waypoint')

# Trajectory line and robot marker
line, = ax.plot([], [], 'b--', label='Robot Trajectory')
robot_dot, = ax.plot([], [], 'bo', markersize=10, label='Robot')

# Set plot bounds and labels
ax.set_xlim(min(data['x']) - 1, max(data['x']) + 1)
ax.set_ylim(min(data['y']) - 1, max(data['y']) + 1)
ax.set_title('Robot 2D Navigation Trajectory (Animated)', fontsize=14)
ax.set_xlabel('X Coordinate (meters)', fontsize=12)
ax.set_ylabel('Y Coordinate (meters)', fontsize=12)
ax.grid(True)
ax.legend(loc='upper left')

# Animation update callback
def update(frame):
    # Update trail and robot position
    line.set_data(data['x'].iloc[:frame+1], data['y'].iloc[:frame+1])
    robot_dot.set_data([data['x'].iloc[frame]], [data['y'].iloc[frame]])
    return line, robot_dot

# Build animation
ani = FuncAnimation(fig, update, frames=len(data), interval=200, repeat=True)

# Save animated GIF
gif_filename = 'trajectory_animation.gif'
ani.save(gif_filename, writer='pillow', fps=5)
print(f"Successfully generated animated GIF: '{gif_filename}'")

plt.show()