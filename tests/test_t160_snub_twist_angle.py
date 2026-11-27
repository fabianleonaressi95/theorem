from math import atan, degrees, pi


def tribonacci_root():
    lo, hi = 1.0, 2.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if mid**3 - mid**2 - mid - 1 < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def test_standard_snub_cube_twist_angle_and_22_5_comparison():
    t = tribonacci_root()
    theta = atan((t - 1) / (t + 1))
    theta_deg = degrees(theta)
    assert abs(theta_deg - 16.46756040038636) < 1e-10
    assert abs((22.5 - theta_deg) - 6.03243959961364) < 1e-10
    assert abs(theta - 0.2874131487577776) < 1e-12
    assert abs(22.5 * pi / 180 - theta) > 0.1
