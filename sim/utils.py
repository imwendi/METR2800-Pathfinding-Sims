import numpy as np


def find_nearest(array, value, n=1):
    """
    Finds the first n indexes of value in an array closest to the given value

    Args:
        array: Array to search
        value: Value to search for

    Returns:
        Found index

    """
    array = np.asarray(array)
    idx = np.argpartition(np.abs(array - value), n)[:n]

    return idx if idx.shape[0] > 1 else idx[0]


def angle_is_between(theta, lower, upper):
    """
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

