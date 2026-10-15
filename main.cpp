#include <iostream>
#include <iomanip>
#include "distance.hpp"

int main() {
    // Current robot coordinates
    RobotMath::Point2D robotPosition{1.5, 2.5};

    // Target waypoint coordinates
    RobotMath::Point2D targetWaypoint{4.5, 6.5};

    // Calculate distance
    double distance = RobotMath::euclideanDistance2D(robotPosition, targetWaypoint);

    // Display output
    std::cout << std::fixed << std::setprecision(4);
    std::cout << "========== Robot Navigation Math ==========\n";
    std::cout << "Robot Position   : (" << robotPosition.x << ", " << robotPosition.y << ")\n";
    std::cout << "Target Waypoint  : (" << targetWaypoint.x << ", " << targetWaypoint.y << ")\n";
    std::cout << "Euclidean Distance: " << distance << " units\n";
    std::cout << "===========================================\n";

    return 0;
}