#include "distance.hpp"
#include <cmath>
#include <fstream>
#include <iostream>

// --- 2D Math & Trajectory ---
double calculateEuclideanDistance(const Point2D& p1, const Point2D& p2) {
    double dx = p2.x - p1.x;
    double dy = p2.y - p1.y;
    return std::sqrt(dx * dx + dy * dy);
}

void generateTrajectoryLog2D(const Point2D& start, const Point2D& target, int steps, const std::string& filename) {
    std::ofstream outFile(filename);
    if (!outFile.is_open()) return;

    outFile << "step,x,y,remaining_distance\n";
    for (int i = 0; i <= steps; ++i) {
        double t = static_cast<double>(i) / steps;
        double currentX = start.x + t * (target.x - start.x);
        double currentY = start.y + t * (target.y - start.y);
        Point2D currentPos = {currentX, currentY};
        outFile << i << "," << currentX << "," << currentY << "," << calculateEuclideanDistance(currentPos, target) << "\n";
    }
    outFile.close();
}

// --- 3D Math & Trajectory ---
double calculateEuclideanDistance3D(const Point3D& p1, const Point3D& p2) {
    double dx = p2.x - p1.x;
    double dy = p2.y - p1.y;
    double dz = p2.z - p1.z;
    return std::sqrt(dx * dx + dy * dy + dz * dz);
}

void generateTrajectoryLog3D(const Point3D& start, const Point3D& target, int steps, const std::string& filename) {
    std::ofstream outFile(filename);
    if (!outFile.is_open()) return;

    outFile << "step,x,y,z,remaining_distance\n";
    for (int i = 0; i <= steps; ++i) {
        double t = static_cast<double>(i) / steps;
        double currentX = start.x + t * (target.x - start.x);
        double currentY = start.y + t * (target.y - start.y);
        double currentZ = start.z + t * (target.z - start.z);
        Point3D currentPos = {currentX, currentY, currentZ};
        outFile << i << "," << currentX << "," << currentY << "," << currentZ << "," << calculateEuclideanDistance3D(currentPos, target) << "\n";
    }
    outFile.close();
}