#include "distance.hpp"
#include <cmath>
#include <fstream>
#include <iostream>

double calculateEuclideanDistance(const Point2D& p1, const Point2D& p2) {
    double dx = p2.x - p1.x;
    double dy = p2.y - p1.y;
    return std::sqrt(dx * dx + dy * dy);
}

void generateTrajectoryLog(const Point2D& start, const Point2D& target, int steps, const std::string& filename) {
    std::ofstream outFile(filename);
    if (!outFile.is_open()) {
        std::cerr << "Error opening file: " << filename << std::endl;
        return;
    }

    outFile << "step,x,y,remaining_distance\n";

    for (int i = 0; i <= steps; ++i) {
        double t = static_cast<double>(i) / steps;
        double currentX = start.x + t * (target.x - start.x);
        double currentY = start.y + t * (target.y - start.y);

        Point2D currentPos = {currentX, currentY};
        double distRemaining = calculateEuclideanDistance(currentPos, target);

        outFile << i << "," << currentX << "," << currentY << "," << distRemaining << "\n";
    }

    outFile.close();
    std::cout << "Trajectory successfully logged to " << filename << std::endl;
}