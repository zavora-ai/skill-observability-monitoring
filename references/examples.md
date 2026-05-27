# Observability Examples

## Example 1: "Why is the payment service erroring?"

**User says:** "Payments is throwing 500s. What's happening?"

**Tool calls:**
```
1. get_errors(service: "payments", last: "1h")
   → [{error: "NullPointerException at PaymentHandler:45", count: 23, first: "12 min ago"}]

2. search_traces(service: "payments", status: "error", last: "30min")
   → [{trace_id: "abc123", duration: "45ms", error: "customer-service timeout"}]

3. get_trace(trace_id: "abc123")
   → payments → customer-service (TIMEOUT after 5s) → null response → NPE
```

**Response:**
```
## Root Cause Found

**Error:** NullPointerException at PaymentHandler:45 (23 occurrences, started 12 min ago)
**Trace:** payments calls customer-service → timeout after 5s → null response → crash

**Root cause:** customer-service is unresponsive, causing payments to get null and crash.

**Next steps:**
1. Check customer-service health
2. If overloaded: restart or scale
3. If down: failover to cache
```

## Example 2: "Are we burning through our SLO budget?"

**User says:** "How's our payments SLO looking?"

**Tool calls:**
```
1. get_slo(service: "payments")
   → {target: 99.9%, current: 99.7%, error_budget_remaining: 12%, burn_rate: 3.2x}

2. forecast_slo(id)
   → "At current burn rate (3.2x), error budget exhausted in 3 days"
```

**Response:**
```
## SLO Status: payments

| Metric | Value |
|--------|-------|
| Target | 99.9% |
| Current | 99.7% |
| Error budget remaining | ⚠️ 12% |
| Burn rate | 🚨 3.2x normal |
| Budget exhausted in | 3 days |

**Action needed:** At 3.2x burn rate, we'll breach SLO in 3 days. Fix the error source or freeze deployments.
```

## Example 3: "What alerts are firing right now?"

**Tool calls:**
```
1. list_alerts(status: "firing")
   → [{name: "high_error_rate", service: "payments", severity: "critical", duration: "8 min"},
      {name: "high_latency", service: "search", severity: "warning", duration: "3 min"}]

2. get_runbook(alert: "high_error_rate")
   → "1. Check downstream deps 2. Restart if unresponsive 3. Rollback last deploy"
```

**Response:**
```
## Active Alerts (2)

| Alert | Service | Severity | Duration | Runbook |
|-------|---------|----------|----------|---------|
| 🚨 high_error_rate | payments | Critical | 8 min | ✅ Available |
| ⚠️ high_latency | search | Warning | 3 min | ✅ Available |

**Priority:** payments (critical, 8 min). Runbook says: check downstream deps first.

Want me to acknowledge and start investigating?
```
