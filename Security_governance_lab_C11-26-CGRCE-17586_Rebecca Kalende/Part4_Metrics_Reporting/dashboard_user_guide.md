# Security Governance Dashboard User Guide

## 1. Overview

The Security Governance Dashboard presents security-governance findings and illustrative metric trends. It is intended to support review and decision-making by security teams, executives and Board members.

## 2. Opening the Dashboard

1. Open `executive_dashboard.html` in a web browser.
2. Review the assurance-status notice at the top.
3. Review the verified laboratory findings table.
4. Review the illustrative metrics charts.
5. Use the associated Board report for management recommendations.

Keep the dashboard HTML file and its `metrics_visualizations` folder together so that the chart images can load correctly.

## 3. Understanding the Findings

The dashboard distinguishes recorded laboratory evidence from illustrative metrics.

- **Critical:** Requires immediate prioritisation and accountable remediation.
- **High:** Requires prompt corrective action and appropriate escalation.
- **Review required:** Further assessment is needed to determine the appropriate control action.
- **Inconclusive:** The available test did not establish the control's status.

A simulated patch-status flag is not proof that a technical vulnerability has been fixed.

## 4. Interpreting the Trend Charts

The charts show illustrative examples of patch compliance, vulnerability remediation time, security incidents, monitoring coverage and policy compliance.

These values demonstrate how trends may be displayed. They are not actual organisational measurements and should not be presented as proof of control effectiveness.

Metric direction matters. Higher values generally indicate better performance for compliance and coverage measures, while lower values are generally preferable for remediation time and incident count.

## 5. Using the Dashboard for Decisions

Users should:

1. Identify critical and high-priority findings.
2. Confirm the evidence and current technical status.
3. Assign a responsible owner and remediation deadline.
4. Escalate overdue or material risks.
5. Review corrective-action evidence and independent retest results.
6. Close findings only when the defined closure criteria are met.

## 6. Refreshing the Dashboard

From the laboratory directory, run:

`python3 Part4_Metrics_Reporting/governance_metrics.py`

Open the newly generated dashboard and check that the charts and findings table display correctly.

## 7. Limitations

The dashboard is a laboratory demonstration, not a production SIEM or a live enterprise monitoring service. Its conclusions are limited to the evidence collected in the simulated environment.

## 8. Review

The dashboard, metrics and user guidance should be reviewed periodically to ensure that the information is accurate, relevant and appropriate for its intended audience.
