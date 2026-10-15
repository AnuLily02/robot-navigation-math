#ifndef DISTANCE_HPP
#define DISTANCE_HPP

#include <string>

struct Point2D {
    double x;
    double y;
};

// Calculates 2D Euclidean distance between two points
double calculateEuclideanDistance(const Point2D& p1, const Point2D& p2);

// Generates step-by-step simulation points and logs them to CSV
void generateTrajectoryLog(const Point2D& start, const Point2D& target, int steps, const std::string& filename);

#endif // DISTANCE_HPP