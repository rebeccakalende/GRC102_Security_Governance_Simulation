#!/usr/bin/env python3

import os
import json
import datetime
import argparse


class GovernanceTracker:
    def __init__(self, data_file="governance_data.json"):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                self.data = json.load(f)
        else:
            self.data = {
                "policies": [],
                "controls": [],
                "risks": [],
                "incidents": [],
                "metrics": [],
                "audits": []
            }

    def save_data(self):
        with open(self.data_file, "w") as f:
            json.dump(self.data, f, indent=2)

    def add_policy(self, name, description, owner, approval_date, review_date):
        item = {
            "id": f"POL-{len(self.data['policies']) + 1:03d}",
            "name": name,
            "description": description,
            "owner": owner,
            "approval_date": approval_date,
            "review_date": review_date,
            "status": "Active"
        }
        self.data["policies"].append(item)
        self.save_data()
        return item["id"]

    def add_control(self, name, description, policy_id, owner, implementation_date):
        item = {
            "id": f"CTL-{len(self.data['controls']) + 1:03d}",
            "name": name,
            "description": description,
            "policy_id": policy_id,
            "owner": owner,
            "implementation_date": implementation_date,
            "status": "Implemented"
        }
        self.data["controls"].append(item)
        self.save_data()
        return item["id"]

    def add_risk(self, name, description, likelihood, impact, owner, mitigation_plan):
        risk_matrix = {
            "High": {"High": "Critical", "Medium": "High", "Low": "Medium"},
            "Medium": {"High": "High", "Medium": "Medium", "Low": "Low"},
            "Low": {"High": "Medium", "Medium": "Low", "Low": "Very Low"}
        }
        risk_level = risk_matrix.get(likelihood, {}).get(impact, "Unknown")

        item = {
            "id": f"RISK-{len(self.data['risks']) + 1:03d}",
            "name": name,
            "description": description,
            "likelihood": likelihood,
            "impact": impact,
            "risk_level": risk_level,
            "owner": owner,
            "mitigation_plan": mitigation_plan,
            "status": "Open"
        }
        self.data["risks"].append(item)
        self.save_data()
        return item["id"]

    def add_incident(self, name, description, date, severity,
                     affected_systems, root_cause, resolution):
        item = {
            "id": f"INC-{len(self.data['incidents']) + 1:03d}",
            "name": name,
            "description": description,
            "date": date,
            "severity": severity,
            "affected_systems": affected_systems,
            "root_cause": root_cause,
            "resolution": resolution,
            "status": "Closed"
        }
        self.data["incidents"].append(item)
        self.save_data()
        return item["id"]

    def add_metric(self, name, description, target, actual, period, trend):
        item = {
            "id": f"MET-{len(self.data['metrics']) + 1:03d}",
            "name": name,
            "description": description,
            "target": target,
            "actual": actual,
            "period": period,
            "trend": trend,
            "status": "Active"
        }
        self.data["metrics"].append(item)
        self.save_data()
        return item["id"]

    def add_audit(self, name, description, date, auditor, findings, recommendations):
        item = {
            "id": f"AUD-{len(self.data['audits']) + 1:03d}",
            "name": name,
            "description": description,
            "date": date,
            "auditor": auditor,
            "findings": findings,
            "recommendations": recommendations,
            "status": "Completed"
        }
        self.data["audits"].append(item)
        self.save_data()
        return item["id"]

    def list_policies(self):
        return self.data["policies"]

    def list_controls(self):
        return self.data["controls"]

    def list_risks(self):
        return self.data["risks"]

    def list_incidents(self):
        return self.data["incidents"]

    def list_metrics(self):
        return self.data["metrics"]

    def list_audits(self):
        return self.data["audits"]

    def generate_dashboard(self):
        return {
            "generated_date": datetime.datetime.now().isoformat(),
            "summary": {
                key: len(self.data[key])
                for key in (
                    "policies", "controls", "risks",
                    "incidents", "metrics", "audits"
                )
            },
            "risk_summary": {
                level.lower().replace(" ", "_"): sum(
                    1 for risk in self.data["risks"]
                    if risk["risk_level"] == level
                )
                for level in ("Critical", "High", "Medium", "Low", "Very Low")
            },
            "incident_summary": {
                level.lower(): sum(
                    1 for incident in self.data["incidents"]
                    if incident["severity"] == level
                )
                for level in ("Critical", "High", "Medium", "Low")
            },
            "metrics_summary": [
                {
                    "name": metric["name"],
                    "target": metric["target"],
                    "actual": metric["actual"],
                    "status": (
                        "Green" if metric["actual"] >= metric["target"] else "Red"
                    )
                }
                for metric in self.data["metrics"]
            ]
        }


def main():
    parser = argparse.ArgumentParser(description="Security Governance Tracker")

    actions = [
        "add-policy", "add-control", "add-risk", "add-incident",
        "add-metric", "add-audit", "list-policies", "list-controls",
        "list-risks", "list-incidents", "list-metrics", "list-audits",
        "dashboard"
    ]

    for action in actions:
        parser.add_argument(f"--{action}", action="store_true")

    args = parser.parse_args()
    tracker = GovernanceTracker()

    if args.add_policy:
        policy_id = tracker.add_policy(
            input("Policy Name: "),
            input("Description: "),
            input("Owner: "),
            input("Approval Date (YYYY-MM-DD): "),
            input("Review Date (YYYY-MM-DD): ")
        )
        print(f"Policy added with ID: {policy_id}")

    elif args.add_control:
        control_id = tracker.add_control(
            input("Control Name: "),
            input("Description: "),
            input("Policy ID: "),
            input("Owner: "),
            input("Implementation Date (YYYY-MM-DD): ")
        )
        print(f"Control added with ID: {control_id}")

    elif args.add_risk:
        risk_id = tracker.add_risk(
            input("Risk Name: "),
            input("Description: "),
            input("Likelihood (High/Medium/Low): "),
            input("Impact (High/Medium/Low): "),
            input("Owner: "),
            input("Mitigation Plan: ")
        )
        print(f"Risk added with ID: {risk_id}")

    elif args.add_incident:
        incident_id = tracker.add_incident(
            input("Incident Name: "),
            input("Description: "),
            input("Date (YYYY-MM-DD): "),
            input("Severity (Critical/High/Medium/Low): "),
            input("Affected Systems: "),
            input("Root Cause: "),
            input("Resolution: ")
        )
        print(f"Incident added with ID: {incident_id}")

    elif args.add_metric:
        metric_id = tracker.add_metric(
            input("Metric Name: "),
            input("Description: "),
            float(input("Target Value: ")),
            float(input("Actual Value: ")),
            input("Period (e.g., May 2023): "),
            input("Trend (Improving/Stable/Declining): ")
        )
        print(f"Metric added with ID: {metric_id}")

    elif args.add_audit:
        audit_id = tracker.add_audit(
            input("Audit Name: "),
            input("Description: "),
            input("Date (YYYY-MM-DD): "),
            input("Auditor: "),
            input("Findings: "),
            input("Recommendations: ")
        )
        print(f"Audit added with ID: {audit_id}")

    else:
        list_actions = {
            "list_policies": "policies",
            "list_controls": "controls",
            "list_risks": "risks",
            "list_incidents": "incidents",
            "list_metrics": "metrics",
            "list_audits": "audits"
        }
        matched = False

        for argument, category in list_actions.items():
            if getattr(args, argument):
                print(json.dumps(getattr(tracker, f"list_{category}")(), indent=2))
                matched = True
                break

        if args.dashboard:
            print(json.dumps(tracker.generate_dashboard(), indent=2))
            matched = True

        if not matched:
            parser.print_help()


if __name__ == "__main__":
    main()
