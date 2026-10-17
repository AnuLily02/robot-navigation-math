# 🤖 3D Robotics Trajectory & Navigation Pipeline

A modular C++ and Python pipeline that calculates 3D Euclidean spatial trajectories and renders them into interactive telemetry visualizations and cinematic 3D keyframe animations via the Blender Python API (`bpy`).

---

## 📌 Features

- **Dual 2D/3D Math Engine**: Low-level C++ engine computing step-by-step spatial positions and remaining Euclidean distances.
- **Decoupled Architecture**: Separation of math logic (`include/` and `src/`) from visualization using structured CSV telemetry outputs (`trajectory.csv` and `trajectory_3d.csv`).
- **Multi-Backend Visualization**:
  - **Level 1 (2D Analytics)**: Fast trajectory prototyping using Matplotlib.
  - **Level 2 (Interactive 3D Telemetry)**: Dark-themed 3D viewport with real-time camera manipulation and live distance HUD tracking.
  - **Level 3 (Cinematic 3D Rendering)**: Automated Blender Python script generating metallic PBR materials, floor grids, sun lighting, and frame-by-frame keyframed motion.

---

## 📐 Mathematical Foundation

The core C++ engine calculates spatial separation in 3D Euclidean space between two points $P_1(x_1, y_1, z_1)$ and $P_2(x_2, y_2, z_2)$ using the formula:

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$

Linear interpolation (LERP) generates step-by-step coordinates along the trajectory path over $N$ discrete steps:

$$\vec{P}(t) = \vec{P}_{\text{start}} + t \cdot (\vec{P}_{\text{target}} - \vec{P}_{\text{start}}), \quad t = \frac{i}{N}, \; i \in \{0, 1, \dots, N\}$$

---

## 📁 Repository Structure

```text
robot-navigation-math/
├── include/
│   └── distance.hpp         # Dual 2D & 3D C++ function declarations and structs
├── src/
│   └── distance.cpp         # LERP path calculation and CSV logging logic
├── scripts/
│   ├── plot_trajectory.py   # 2D Matplotlib animation script
│   ├── plot_3d_smooth.py    # Interactive 3D telemetry visualizer
│   └── blender_render.py    # Blender bpy automation script (shaders & keyframes)
├── main.cpp                 # C++ execution entry point
├── trajectory.csv           # Logged 2D trajectory telemetry
├── trajectory_3d.csv        # Logged 3D trajectory telemetry
└── README.md                # Project documentation

## 🛠️ Installation & Requirements

System Requirements
C++ Compiler: GCC (g++) supporting C++11 or higher

Python: Python 3.8+

3D Engine (Optional): Blender 4.0+

Python Dependencies
Install required packages using pip:

---

##🚀 How to Build and Run

1. Compile & Execute the C++ Math Engine
Compile the C++ code from the project root directory to compute trajectory data and generate telemetry files (trajectory.csv & trajectory_3d.csv):

PowerShell
# Compile C++ source files
g++ -Iinclude main.cpp src/distance.cpp -o robot_distance.exe

# Execute C++ simulation binary
.\robot_distance.exe

---
2. Run Interactive 3D Telemetry (Python)
Launch the 3D telemetry script to view an interactive viewport with full mouse rotation, zoom, and live distance tracking:

PowerShell
python scripts/plot_3d_smooth.py

---
3. Render Cinematic 3D Scene in Blender
Run the automation script inside Blender to load keyframed motion, metallic shaders, and lighting:

----
## Inside Blender GUI

Open Blender and go to the Scripting workspace tab.

Open scripts/blender_render.py and click Run Script (▶) (or press Alt + P).

Switch Viewport Shading to Material Preview (top-right corner) and press Spacebar to play.

## From Terminal
& "C:\Program Files\Blender Foundation\Blender 4.0\blender.exe" --python scripts/blender_render.py

---

## 💻 Tech Stack

Languages: C++17, Python 3

Libraries & APIs: Matplotlib, Pandas, Blender Python API (bpy)

Build Tools: GCC / MinGW-w64

IDE: VS Code