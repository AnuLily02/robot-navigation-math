import bpy
import csv
import os

# --- 1. Clean Scene ---
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

scene = bpy.context.scene

# --- 2. Version-Safe EEVEE Engine Setup ---
# Handles EEVEE settings safely across Blender 4.0, 4.1, 4.2+
if hasattr(scene, "eevee"):
    # Legacy EEVEE Bloom attribute check
    if hasattr(scene.eevee, "use_bloom"):
        scene.eevee.use_bloom = True
    elif hasattr(scene.eevee, "use_gtaao"):
        # EEVEE Next (Blender 4.2+) ambient occlusion
        scene.eevee.use_gtaao = True

# --- 3. Create Shader Material Helper ---
def create_metallic_material(name, color_rgb, metallic=0.8, roughness=0.2):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    nodes.clear()
    
    # Shader Nodes
    node_output = nodes.new(type='ShaderNodeOutputMaterial')
    node_bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
    
    # Set Color and Metallic Shading
    node_bsdf.inputs['Base Color'].default_value = color_rgb
    node_bsdf.inputs['Metallic'].default_value = metallic
    node_bsdf.inputs['Roughness'].default_value = roughness
    
    # Connect Shader Nodes
    mat.node_tree.links.new(node_bsdf.outputs['BSDF'], node_output.inputs['Surface'])
    return mat

mat_robot = create_metallic_material("Mat_Robot", (0.7, 0.7, 0.75, 1.0), metallic=0.9, roughness=0.1)
mat_start = create_metallic_material("Mat_Start", (0.1, 0.8, 0.2, 1.0), metallic=0.3, roughness=0.3)
mat_target = create_metallic_material("Mat_Target", (0.9, 0.1, 0.1, 1.0), metallic=0.3, roughness=0.3)

# --- 4. Read C++ CSV Trajectory Data ---
# --- 4. Read C++ CSV Trajectory Data safely ---
# Try finding trajectory_3d.csv relative to the script location or blend file
script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else ""
csv_filename = os.path.join(script_dir, "..", "trajectory_3d.csv")

# Fallback check for absolute desktop project path
if not os.path.exists(csv_filename):
    csv_filename = r"C:\Users\Anupama\OneDrive\Desktop\robot-navigation-math\trajectory_3d.csv"

if not os.path.exists(csv_filename):
    raise FileNotFoundError(f"Could not locate trajectory_3d.csv at: {csv_filename}")

trajectory_points = []
with open(csv_filename, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        trajectory_points.append((float(row['x']), float(row['y']), float(row['z'])))
# --- 5. Spawn Start, Target & Robot Spheres ---
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.3, location=trajectory_points[0])
bpy.context.active_object.data.materials.append(mat_start)

bpy.ops.mesh.primitive_uv_sphere_add(radius=0.4, location=trajectory_points[-1])
bpy.context.active_object.data.materials.append(mat_target)

bpy.ops.mesh.primitive_uv_sphere_add(radius=0.35, location=trajectory_points[0])
robot = bpy.context.active_object
robot.name = "Robot_Sphere"
robot.data.materials.append(mat_robot)

# --- 6. Sun Lighting & Ground Plane ---
bpy.ops.mesh.primitive_plane_add(size=30, location=(0, 0, 0))
ground = bpy.context.active_object
ground.name = "Ground_Grid"

bpy.ops.object.light_add(type='SUN', location=(10, 10, 15))
sun = bpy.context.active_object
sun.data.energy = 3.0

# --- 7. Keyframe Animation from C++ Data ---
frame_spacing = 5
scene.frame_start = 1
scene.frame_end = len(trajectory_points) * frame_spacing

for idx, pt in enumerate(trajectory_points):
    current_frame = 1 + idx * frame_spacing
    robot.location = pt
    robot.keyframe_insert(data_path="location", frame=current_frame)

print("Script executed successfully without EEVEE attribute errors!")