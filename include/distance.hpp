#ifndef DISTANCE_HPP
#define DISTANCE_HPP

namespace RobotMath {

/**
 * @brief Represents a 2D point or robot coordinate in Cartesian space.
 */
struct Point2D {
    double x;
    double y;
};

/**
 * @brief Calculates the 2D Euclidean distance between two points.
 * 
 * @param p1 Starting coordinate (e.g., current robot position)
 * @param p2 Target coordinate (e.g., waypoint or obstacle position)
 * @return double Straight-line distance between p1 and p2
 */
double euclideanDistance2D(const Point2D& p1, const Point2D& p2);

} // namespace RobotMath

#endif // DISTANCE_HPP