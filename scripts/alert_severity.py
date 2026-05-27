#!/usr/bin/env python3
"""observability-monitoring helper script."""
import json,sys
def assess(data):
    error_rate=data.get("error_rate",0);latency_p99=data.get("latency_p99",0)
    severity="critical" if error_rate>5 or latency_p99>5000 else "warning" if error_rate>1 or latency_p99>2000 else "ok"
    return {"severity":severity,"error_rate":error_rate,"latency_p99":latency_p99}
if __name__=="__main__":print(json.dumps(assess(json.loads(sys.argv[1])),indent=2))
