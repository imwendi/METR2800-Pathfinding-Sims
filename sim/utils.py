import numpy as np


def angle_is_between(theta, lower, upper):
    """
    **UNUSED**

    Determine whether or not a given angle is between two given lower and
    upper bound angles.

    Note that all angles are in [0, 2pi], and angles are circular, i.e.
    pi/4 would be considered to be between 3pi/2 and pi/2

    Args:
        theta: Angle to test
        lower: Angle lower bound
        upper: Angle upper bound

    Returns:
        Whether or not theta is between lower and upper

    """
    if lower < 0:
        lower += 2*np.pi

    if upper < 0:
        upper += 2*np.pi

    if lower > upper:
        upper += 2*np.pi
        if theta < np.pi:
            theta += 2*np.pi

    return lower%360 <= theta <= upper

def pol2cart(r, theta):
    """
    Convert polar to cartesian coordinates

    Args:
        r: radius
        theta: angle

    Returns:
        Cartesian coordinates as array
    """
    x = r*np.cos(theta)
    y = r*np.sin(theta)

    return np.array([x, y])

