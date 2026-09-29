"""
dispatch_window_solver.py - Verifies that scheduled stop arrival times fall within customer receiving hours
"""
import sys
import json


def solve_dispatch_windows(windows_json: str):
    import json
    stops = json.loads(windows_json) if isinstance(windows_json, str) else windows_json
    on_time = all(s.get("open_hour", 8) <= s.get("arrival_hour", 10) <= s.get("close_hour", 17) for s in stops)
    return {"all_stops_on_time": on_time, "status": "WINDOWS_RESPECTED" if on_time else "WINDOW_VIOLATION"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "dispatch-window-solver"}))
