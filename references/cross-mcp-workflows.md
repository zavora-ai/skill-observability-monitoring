# Observability Cross-MCP Workflows

## Observability + Slack: Critical Alert Pipeline
```
OBS: list_alerts(status: "firing", severity: "critical")
  → [{name: "high_error_rate", service: "payments", value: "5.2%"}]
OBS: get_runbook(alert: "high_error_rate")
  → "1. Check downstream deps 2. Restart if needed 3. Rollback last deploy"
SLACK: send_message(channel: "#incidents", text: "🚨 *P1 Alert: payments error rate 5.2%*\nRunbook: 1. Check deps 2. Restart 3. Rollback\n@oncall please acknowledge")
OBS: acknowledge_alert(id, reason: "Investigating — oncall notified")
```

## Observability + ITSM: Auto-Incident
```
OBS: list_alerts(status: "firing", duration: "> 5min") → persistent alert
OBS: create_incident(title: "Payment errors sustained > 5min", severity: "P1")
ITSM: create_ticket(type: "incident", priority: "critical", subject: "Payment error rate > 5%")
SLACK: create_channel(name: "incident-payments-0527")
```

## Observability + CI/CD: Deploy Safety Gate
```
OBS: get_slo(service: "payments") → {error_budget_remaining: 12%}
OBS: forecast_slo(id) → "Exhausted in 3 days"
→ BLOCK: "Cannot deploy — SLO error budget critical (12%)"
CICD: [blocked] trigger_deployment → denied
```

## Observability + Environment: Rollback on Degradation
```
OBS: get_errors(service: "payments", last: "10min") → spike after deploy
OBS: compare_metrics(metric: "error_rate", period_a: "last_10min", period_b: "prior_10min")
  → {before: 0.1%, after: 5.2%, change: "+5100%"}
ENVIRONMENT: rollback_release(env: "production", to_version: "v2.3.0")
OBS: get_errors(service: "payments", last: "5min") → back to normal
SLACK: send_message(channel: "#deploys", text: "↩️ Rolled back payments to v2.3.0. Error rate normalized.")
```
