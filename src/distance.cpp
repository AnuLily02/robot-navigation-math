#include "distance.hpp"
#include <cmath>

namespace RobotMath {

double euclideanDistance2D(const Point2D& p1, const Point2D& p2) {
    double dx = p2.x - p1.x;
    double dy = p2.y - p1.y;
    return std::sqrt(dx * dx + dy * dy);
}

} // namespace RobotMath