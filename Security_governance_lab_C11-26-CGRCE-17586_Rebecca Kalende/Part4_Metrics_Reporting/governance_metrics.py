#!/usr/bin/env python3

import json
from datetime import datetime, timedelta
from pathlib import Path

import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
CHARTS = BASE / "metrics_visualizations"
CHARTS.mkdir(parents=True, exist_ok=True)

# These trends are illustrative training data, not measured
# organisational performance or verified remediation results.
months = [
    (datetime.now() - timedelta(days=30 * i)).strftime("%b %Y")
    for i in range(5, -1, -1)
]

metrics = {
    "patch_compliance": {
        "name": "Patch Compliance",
        "values": [72, 76, 78, 81, 83, 85],
        "target": 95,
        "unit": "%"
    },
    "vulnerability_remediation": {
        "name": "Vulnerability Remediation Time",
        "values": [15, 14, 13, 13, 12, 12],
        "target": 7,
        "unit": "days"
    },
    "security_incidents": {
        "name": "Security Incidents",
        "values": [3, 2, 2, 3, 2, 1],
        "target": 0,
        "unit": "incidents"
    },
    "monitoring_coverage": {
        "name": "Security Monitoring Coverage",
        "values": [60, 65, 68, 70, 73, 75],
        "target": 95,
        "unit": "%"
    },
    "policy_compliance": {
        "name": "Policy Compliance",
        "values": [75, 79, 80, 84, 86, 88],
        "target": 95,
        "unit": "%"
    }
}

# Observations from the actual laboratory verification.
findings = [
    {
        "issue": "Apache Struts S2-045",
        "severity": "Critical",
        "status": "Open - retest unsuccessful",
        "evidence": (
            "The post-control scanner still reports the critical finding, "
            "and the lab check still returns its vulnerability marker."
        )
    },
    {
        "issue": "MySQL default root credentials",
        "severity": "High",
        "status": "Open - remediation not verified",
        "evidence": (
            "The configured default root password was still accepted "
            "by the database during technical verification."
        )
    },
    {
        "issue": "Web-to-database connectivity",
        "severity": "Review required",
        "status": "Connectivity confirmed",
        "evidence": (
            "The web container could reach database TCP port 3306."
        )
    },
    {
        "issue": "Network segmentation assessment",
        "severity": "Inconclusive",
        "status": "Further testing required",
        "evidence": (
            "The scanner's network check encountered a UTF-8 decoding error."
        )
    }
]

def create_chart(key, metric):
    """Create a trend chart using clearly labelled illustrative data."""
    path = CHARTS / f"{key}.png"

    plt.figure(figsize=(9, 5))
    plt.plot(months, metric["values"], marker="o", label="Illustrative values")
    plt.axhline(
        y=metric["target"],
        linestyle="--",
        label=f"Target: {metric['target']} {metric['unit']}"
    )
    plt.title(metric["name"] + "\nIllustrative Training Data")
    plt.xlabel("Month")
    plt.ylabel(metric["unit"])
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()

    return path.name


def main():
    chart_files = {}

    for key, metric in metrics.items():
        chart_files[key] = create_chart(key, metric)

    report_data = {
        "generated_at": datetime.now().isoformat(),
        "data_note": (
            "Trend values are illustrative training data, not actual "
            "organisational measurements."
        ),
        "illustrative_trends": metrics,
        "verified_lab_findings": findings,
        "chart_files": chart_files
    }

    data_file = BASE / "governance_metrics_data.json"
    data_file.write_text(json.dumps(report_data, indent=2))

    # Executive dashboard
    rows = ""
    for finding in findings:
        rows += (
            "<tr>"
            f"<td>{finding['issue']}</td>"
            f"<td>{finding['severity']}</td>"
            f"<td>{finding['status']}</td>"
            f"<td>{finding['evidence']}</td>"
            "</tr>"
        )

    charts_html = ""
    for key, metric in metrics.items():
        charts_html += (
            f"<section><h3>{metric['name']}</h3>"
            f"<img src='metrics_visualizations/{chart_files[key]}' "
            f"alt='{metric['name']} trend'>"
            "<p><em>Illustrative trend data, not verified "
            "organisational measurements.</em></p></section>"
        )

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Security Governance Executive Dashboard</title>
<style>
body {{ font-family: Arial, sans-serif; max-width: 1150px;
       margin: 30px auto; padding: 0 18px; color: #243247; }}
header {{ background: #183b63; color: white; padding: 22px; }}
h2 {{ margin-top: 32px; }}
table {{ width: 100%; border-collapse: collapse; }}
th, td {{ padding: 10px; text-align: left; border: 1px solid #ccd4df; }}
th {{ background: #e9eef5; }}
section {{ margin: 24px 0; padding: 14px; border: 1px solid #d6dde7; }}
img {{ max-width: 100%; height: auto; }}
.note {{ background: #f5f2e8; padding: 12px; }}
</style>
</head>
<body>
<header>
<h1>Security Governance Executive Dashboard</h1>
<p>Generated: {report_data['generated_at']}</p>
</header>

<div class="note">
<strong>Assurance status:</strong> Critical and high-severity findings
remain unresolved or unverified. Simulated patch flags are not proof
of technical remediation.
</div>

<h2>Verified Laboratory Findings</h2>
<table>
<thead><tr><th>Issue</th><th>Severity</th><th>Status</th>
<th>Evidence</th></tr></thead>
<tbody>{rows}</tbody>
</table>

<h2>Illustrative Metrics Trends</h2>
<p>The charts below demonstrate a possible reporting format using
illustrative training data. They do not represent measured company
performance or prove that controls improved.</p>
{charts_html}
</body>
</html>
"""

    dashboard_file = BASE / "executive_dashboard.html"
    dashboard_file.write_text(html)

    # Board report based on the observed lab evidence.
    board_report = f"""# Security Governance Board Report

**Generated:** {report_data['generated_at']}

## Executive Summary

The laboratory verification did not demonstrate successful remediation
of the critical Apache Struts finding or the high-severity MySQL
default-credentials finding. The web container could also reach the
database on TCP port 3306, while the scanner's segmentation check
remained inconclusive due to a decoding error.

The simulated patch-status records were marked complete, but independent
technical checks showed that this status did not equate to effective
remediation.

## Priority Findings

| Finding | Severity | Status |
|---|---|---|
| Apache Struts S2-045 | Critical | Open; retest unsuccessful |
| MySQL default root credentials | High | Open; remediation not verified |
| Web-to-database connectivity | Review required | Connectivity confirmed |
| Network segmentation scanner | Inconclusive | Further testing required |

## Recommended Management Actions

1. Assign an accountable owner and deadline to remediate the critical
   Struts finding or replace the vulnerable application image.
2. Replace default database credentials and review account privileges.
3. Apply least-privilege network restrictions and retest permitted
   and denied connectivity.
4. Correct the scanner's network-checking error and repeat the test.
5. Require independent technical evidence before closing findings.
6. Review the dashboard status logic so that lower-is-better metrics,
   such as remediation time and incident count, are evaluated correctly.

## Metrics and Evidence Limitations

The trend charts use illustrative training data only. They are included
to demonstrate how metrics may be visualised and must not be interpreted
as actual historical performance.

The technical findings above are based on the recorded laboratory
tests. Simulated status flags and generated trend values do not establish
that controls are operating effectively.

## Conclusion

Management should treat the critical and high-severity findings as
unresolved until corrective actions are implemented and independently
retested. Closure should be based on verified technical evidence,
documented ownership and an approved remediation decision.
"""

    board_file = BASE / "board_report.md"
    board_file.write_text(board_report)

    print("Security governance metrics and reports generated.")
    print(f"Executive dashboard: {dashboard_file}")
    print(f"Board report: {board_file}")
    print(f"Metrics data: {data_file}")
    print(f"Visualisations: {len(chart_files)} charts")
    print("Trend data is illustrative; lab findings reflect recorded tests.")


if __name__ == "__main__":
    main()
