import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load 3D trajectory output from C++
data = pd.read_csv('trajectory_3d.csv')

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot 3D path, start, and target waypoints
ax.plot(data['x'], data['y'], data['z'], 'b--o', label='3D Robot Path')
ax.scatter(data['x'].iloc[0], data['y'].iloc[0], data['z'].iloc[0], color='g', s=100, label='Start (X,Y,Z)')
ax.scatter(data['x'].iloc[-1], data['y'].iloc[-1], data['z'].iloc[-1], color='r', s=100, label='Target Waypoint')

ax.set_title('3D Robot Navigation & Euclidean Distance Trajectory')
ax.set_xlabel('X (Meters)')
ax.set_ylabel('Y (Meters)')
ax.set_zlabel('Z (Meters)')
ax.legend()

plt.show()