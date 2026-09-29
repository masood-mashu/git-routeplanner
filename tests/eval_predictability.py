"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitRoutePlanner.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.dispatch_window_solver import *
from tools.fuel_idle_minimizer import *
from tools.payload_weight_balancer import *

class TestGitRoutePlannerPredictability(unittest.TestCase):
    def test_dispatch_window_solver(self):
        res = solve_dispatch_windows('[{"arrival_hour": 10, "open_hour": 8, "close_hour": 16}]')
        self.assertTrue(res["all_stops_on_time"])
        self.assertEqual(res["status"], "WINDOWS_RESPECTED")

    def test_fuel_idle_minimizer(self):
        res = minimize_fuel_idling('{"stop_count": 8, "total_miles": 150.0}')
        self.assertGreater(res["estimated_fuel_saved_gal"], 0.0)
        self.assertEqual(res["status"], "FUEL_SAVED")

    def test_payload_weight_balancer(self):
        res = balance_payload_weight('{"steer_lbs": 12000, "drive_lbs": 33000, "tandem_lbs": 33000}')
        self.assertTrue(res["is_legal"])
        self.assertEqual(res["status"], "AXLES_BALANCED")


if __name__ == "__main__":
    unittest.main()
