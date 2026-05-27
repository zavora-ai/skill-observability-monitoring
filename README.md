# Observability & Monitoring Skill

> Full-stack observability for AI agents — debug errors from logs, trace latency across services, manage alerts, respond to incidents with runbooks, and protect SLO error budgets via Datadog, Grafana, or New Relic.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--observability-green)](https://github.com/zavora-ai/mcp-observability)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

This skill orchestrates 28 observability tools into **SRE workflows** — from debugging a production error to declaring an incident to protecting SLO budgets.

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Debug Errors | 3-4 | Logs → traces → root cause |
| Trace Latency | 3-4 | Find the slow span |
| System Health | 1-2 | CPU/memory/disk overview |
| Alert Management | 2-3 | Triage + runbook + acknowledge |
| Incident Response | 3-4 | Declare + investigate + resolve |
| SLO Tracking | 2-3 | Budget remaining + forecast |
| Dashboards | 1-2 | Overview panels |

### Without this skill:
- Debugging takes 30+ minutes of manual log searching
- Alerts pile up without triage (alert fatigue)
- Incidents declared too late (after customer impact)
- SLO budget burned without awareness
- No runbooks found during emergencies

### With this skill:
- Root cause found in 3-4 tool calls (logs → traces → span)
- Alerts triaged with runbook in hand
- Incidents declared within 5 minutes of detection
- SLO burn rate checked before every deploy
- Runbooks surfaced automatically for known issues

## Installation

```bash
git clone https://github.com/zavora-ai/skill-observability-monitoring.git \
  ~/.skills/skills/observability-monitoring
```

## Requirements

**Required:** `mcp-observability` (28 tools)

**Backends supported:**
- Datadog (logs, metrics, traces, monitors, dashboards)
- Grafana Cloud (Loki + Prometheus + Tempo)
- New Relic (APM, logs, dashboards, alerts)
- Custom API (your own monitoring stack)

**Cross-MCP:**
- `mcp-slack` — alert escalation and incident channels
- `mcp-itsm` — auto-create incident tickets
- `mcp-cicd` — deploy gates based on SLO health
- `mcp-environment` — rollback on degradation

## Folder Structure

```
observability-monitoring/
├── SKILL.md                       # 200 lines — 7 workflows + decision tree
├── scripts/
│   └── alert_severity.py          # Severity classifier from error rate + latency
├── references/
│   ├── tool-sequences.md          # 28 tools across 8 categories
│   ├── cross-mcp-workflows.md     # Obs + Slack + ITSM + CI/CD + Environment
│   └── examples.md                # 3 real scenarios (debug, SLO, alerts)
├── README.md
└── LICENSE
```

## Example

**User:** "Why is the payment service erroring?"

**Agent behavior:**
1. Gets recent errors with stack traces
2. Searches traces for failing requests
3. Gets full trace — finds downstream timeout
4. Reports root cause with next steps

**Result:**
```
Root Cause: customer-service timeout → null response → NPE at PaymentHandler:45
Started: 12 min ago | Occurrences: 23
Next: Check customer-service health, restart if overloaded
```

## Success Criteria

| Metric | Target |
|--------|--------|
| Debug speed | Root cause in 3-4 tool calls |
| Incident response | Declare + runbook in < 5 calls |
| SLO awareness | Always check before deploying |
| Alert triage | Runbook found for every known alert |

## Scripts

### `alert_severity.py`
Classifies alert severity from error rate and latency:
```bash
python scripts/alert_severity.py '{"error_rate": 5.2, "latency_p99": 3000}'
# → {"severity": "critical", "error_rate": 5.2, "latency_p99": 3000}
```

## MCP Server Compatibility

| Category | Tools | Count |
|----------|-------|:-----:|
| Logs | query, stats, errors, tail | 4 |
| Metrics | query, list, health, compare | 4 |
| Traces | search, get, service_map, latency | 4 |
| Alerts | list, get, create, acknowledge | 4 |
| Incidents | list, get, create, update | 4 |
| SLOs | list, get, forecast | 3 |
| Dashboards | list, get, runbook | 3 |
| Services | list, get | 2 |
| **Total** | | **28** |

## Related Skills

- [skill-cicd-pipeline-management](https://github.com/zavora-ai/skill-cicd-pipeline-management) — Deploy gates
- [skill-itsm-service-management](https://github.com/zavora-ai/skill-itsm-service-management) — Incident tickets
- [skill-slack-collaboration](https://github.com/zavora-ai/skill-slack-collaboration) — Alert channels

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0

---

Part of the [ADK-Rust Enterprise](https://enterprise.adk-rust.com) skills ecosystem. Built with ❤️ by [Zavora AI](https://zavora.ai)
