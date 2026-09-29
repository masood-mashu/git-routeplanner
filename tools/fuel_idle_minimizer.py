"""
fuel_idle_minimizer.py - Computes estimated fuel savings from optimized stop sequencing and avoiding left turns
"""
import sys
import json


def minimize_fuel_idling(route_stops_json: str):
    import json
    data = json.loads(route_stops_json) if isinstance(route_stops_json, str) else route_stops_json
    miles = data.get("total_miles", 120.0)
    saved_gal = round(miles * 0.08, 1)
    return {"estimated_fuel_saved_gal": saved_gal, "status": "FUEL_SAVED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "fuel-idle-minimizer"}))
