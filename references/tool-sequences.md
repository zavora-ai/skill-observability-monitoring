# Observability Tool Sequences (28 tools)

## Logs (4)
| Tool | Purpose |
|------|---------|
| `query_logs` | Search by query, time, service, level |
| `get_log_stats` | Volume and error rate over time |
| `get_errors` | Recent errors with stack traces |
| `tail_logs` | Live tail (last 50 entries) |

## Metrics (4)
| Tool | Purpose |
|------|---------|
| `query_metric` | Time-series (CPU, latency, throughput) |
| `list_metrics` | Available metrics for a service |
| `get_system_health` | CPU/memory/disk across services |
| `compare_metrics` | Compare across services or periods |

## Traces (4)
| Tool | Purpose |
|------|---------|
| `search_traces` | Find by service, duration, status |
| `get_trace` | Full trace with all spans |
| `get_service_map` | Dependency graph with latencies |
| `get_latency_breakdown` | p50/p95/p99 by operation |

## Alerts (4)
| Tool | Purpose |
|------|---------|
| `list_alerts` | Active alerts by status/severity |
| `get_alert` | Details + history + related metrics |
| `create_alert` | New alert rule |
| `acknowledge_alert` | Ack a firing alert |

## Incidents (4)
| Tool | Purpose |
|------|---------|
| `list_incidents` | Open/investigating/resolved |
| `get_incident` | Timeline, services, responders |
| `create_incident` | Declare new incident |
| `update_incident` | Update status/resolution |

## SLOs (3)
| Tool | Purpose |
|------|---------|
| `list_slos` | All SLOs with burn rate |
| `get_slo` | Target vs current + error budget |
| `forecast_slo` | When will budget run out? |

## Dashboards & Runbooks (3)
| Tool | Purpose |
|------|---------|
| `list_dashboards` | Available dashboards |
| `get_dashboard` | Dashboard with panel values |
| `get_runbook` | Resolution steps for alert/service |

## Services (2)
| Tool | Purpose |
|------|---------|
| `list_services` | All services + health |
| `get_service` | Service overview (health, deps, alerts, SLOs) |

## Sequence: Debug Production Error (4 calls)

```
1. get_errors(service: "payments", last: "1h")
   → [{error: "NullPointerException at PaymentHandler:45", count: 23, first_seen: "10 min ago"}]

2. query_logs(query: "level:error service:payments", last: "1h")
   → Context: "Failed to process payment for order_123: null customer_id"

3. search_traces(service: "payments", status: "error", last: "1h")
   → [{trace_id: "abc123", duration: "45ms", status: "error"}]

4. get_trace(trace_id: "abc123")
   → Span breakdown: API gateway → payments → customer-service (FAILED: timeout)
   → Root cause: customer-service is timing out, causing null response
```

## Sequence: Incident Response (4 calls)

```
1. create_incident(title: "Payment failures", severity: "P1", services: ["payments", "customer-service"])
2. get_runbook(service: "payments", alert: "high_error_rate")
   → "1. Check customer-service health 2. Restart if unresponsive 3. Failover to cache"
3. get_system_health() → customer-service: CPU 98%, memory 95% (overloaded)
4. update_incident(id, status: "identified", notes: "customer-service overloaded, restarting")
```
