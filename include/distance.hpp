#ifndef DISTANCE_HPP
#define DISTANCE_HPP

#include <string>

// 2D Point Structure
struct Point2D {
    double x;
    double y;
};

// 3D Point Structure
struct Point3D {
    double x;
    double y;
    double z;
};

// 2D and 3D Euclidean Distance Functions
double calculateEuclideanDistance(const Point2D& p1, const Point2D& p2);
double calculateEuclideanDistance3D(const Point3D& p1, const Point3D& p2);

// Trajectory Loggers
void generateTrajectoryLog2D(const Point2D& start, const Point2D& target, int steps, const std::string& filename);
void generateTrajectoryLog3D(const Point3D& start, const Point3D& target, int steps, const std::string& filename);

#endif // DISTANCE_HPP