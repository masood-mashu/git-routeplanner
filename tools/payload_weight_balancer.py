"""
payload_weight_balancer.py - Verifies steer, drive, and trailer tandem axle weights against 80,000 lb GVWR limit
"""
import sys
import json


def balance_payload_weight(axle_weights_json: str):
    import json
    data = json.loads(axle_weights_json) if isinstance(axle_weights_json, str) else axle_weights_json
    steer = data.get("steer_lbs", 12000)
    drive = data.get("drive_lbs", 34000)
    tandem = data.get("tandem_lbs", 34000)
    gross = steer + drive + tandem
    is_legal = gross <= 80000 and steer <= 12500 and drive <= 34000 and tandem <= 34000
    return {"gross_weight_lbs": gross, "is_legal": is_legal, "status": "AXLES_BALANCED" if is_legal else "OVERWEIGHT"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "payload-weight-balancer"}))
