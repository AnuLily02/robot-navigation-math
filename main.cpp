#include <iostream>
#include <iomanip>
#include "distance.hpp"

int main() {
    // 2D Navigation
    Point2D robot2D = {1.5, 2.5};
    Point2D target2D = {4.5, 6.5};
    generateTrajectoryLog2D(robot2D, target2D, 20, "trajectory.csv");

    // 3D Navigation
    Point3D robot3D = {1.5, 2.5, 0.0};
    Point3D target3D = {6.5, 8.5, 5.0};
    generateTrajectoryLog3D(robot3D, target3D, 25, "trajectory_3d.csv");

    std::cout << "========== Robot Navigation Simulation ==========\n";
    std::cout << "2D Distance: " << calculateEuclideanDistance(robot2D, target2D) << " units\n";
    std::cout << "3D Distance: " << calculateEuclideanDistance3D(robot3D, target3D) << " units\n";
    std::cout << "Generated 'trajectory.csv' and 'trajectory_3d.csv' successfully.\n";
    std::cout << "=================================================\n";

    return 0;
}