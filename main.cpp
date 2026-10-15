#include <iostream>
#include <iomanip>
#include "distance.hpp"

int main() {
    Point2D robotPos = {1.5, 2.5};
    Point2D targetWaypoint = {4.5, 6.5};

    double distance = calculateEuclideanDistance(robotPos, targetWaypoint);

    std::cout << "========== Robot Navigation Math ==========\n";
    std::cout << std::fixed << std::setprecision(4);
    std::cout << "Robot Position   : (" << robotPos.x << ", " << robotPos.y << ")\n";
    std::cout << "Target Waypoint  : (" << targetWaypoint.x << ", " << targetWaypoint.y << ")\n";
    std::cout << "Euclidean Distance: " << distance << " units\n";
    std::cout << "===========================================\n";

    // Generate trajectory data for visualizer
    generateTrajectoryLog(robotPos, targetWaypoint, 20, "trajectory.csv");

    return 0;
}