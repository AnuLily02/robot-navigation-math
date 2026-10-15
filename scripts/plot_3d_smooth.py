import os
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# 1. Load C++ 3D Trajectory Output
csv_path = 'trajectory_3d.csv' if os.path.exists('trajectory_3d.csv') else '../trajectory_3d.csv'
data = pd.read_csv(csv_path)

# 2. Setup Dark Studio Viewport
fig = plt.figure(figsize=(10, 8), facecolor='#1e1e24')
ax = fig.add_subplot(111, projection='3d', facecolor='#1e1e24')

# Dark Grid & Frame Styling
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('#33333d')
ax.yaxis.pane.set_edgecolor('#33333d')
ax.zaxis.pane.set_edgecolor('#33333d')
ax.tick_params(colors='white')

# Static Start & Target Waypoint Spheres
ax.scatter(data['x'].iloc[0], data['y'].iloc[0], data['z'].iloc[0], 
           color='#2ecc71', s=150, depthshade=True, label='Start Position')
ax.scatter(data['x'].iloc[-1], data['y'].iloc[-1], data['z'].iloc[-1], 
           color='#e74c3c', s=180, depthshade=True, label='Target Waypoint')

# Dynamic Trajectory Trail & Silver Metallic Robot Marker
trail_line, = ax.plot([], [], [], color='#3498db', linewidth=3, linestyle='--', label='Robot Trajectory')
robot_marker, = ax.plot([], [], [], marker='o', markersize=14, color='#d1d5db', 
                        markeredgecolor='white', markeredgewidth=1.5, label='Robot (Silver)')

# Set Viewport Limits and Labels
ax.set_xlim(min(data['x']) - 1, max(data['x']) + 1)
ax.set_ylim(min(data['y']) - 1, max(data['y']) + 1)
ax.set_zlim(min(data['z']) - 1, max(data['z']) + 1)

ax.set_xlabel('X Axis (m)', color='white', labelpad=10)
ax.set_ylabel('Y Axis (m)', color='white', labelpad=10)
ax.set_zlabel('Z Axis (m)', color='white', labelpad=10)

legend = ax.legend(loc='upper left', facecolor='#2b2b36', edgecolor='none')
plt.setp(legend.get_texts(), color='white')

# 3. Step-by-Step Trajectory Animation
def update(frame):
    # Update trailing path line
    trail_line.set_data(data['x'].iloc[:frame+1], data['y'].iloc[:frame+1])
    trail_line.set_3d_properties(data['z'].iloc[:frame+1])
    
    # Move metallic robot position
    robot_marker.set_data([data['x'].iloc[frame]], [data['y'].iloc[frame]])
    robot_marker.set_3d_properties([data['z'].iloc[frame]])
    
    # Real-time Telemetry HUD
    dist = data['remaining_distance'].iloc[frame]
    ax.set_title(f"3D Navigation Telemetry | Distance to Target: {dist:.2f} m", 
                 color='white', fontsize=12, pad=20)
    
    return trail_line, robot_marker

ani = FuncAnimation(fig, update, frames=len(data), interval=150, repeat=True)

# Save 3D GIF for GitHub README
ani.save('trajectory_3d_smooth.gif', writer='pillow', fps=6)
print("Saved 3D animation to 'trajectory_3d_smooth.gif'")

# Launch interactive 3D window (Click and drag to rotate/pan)
plt.show()