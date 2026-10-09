#!/usr/bin/env python3

import os
import json
import datetime


def load_json(filename):
    """Load a JSON file if it exists."""
    if not os.path.exists(filename):
        return None

    with open(filename, "r") as file:
        return json.load(file)


def load_latest_vulnerability_report():
    """Load the latest generated vulnerability report."""
    reports = sorted(
        filename for filename in os.listdir(".")
        if filename.startswith("vulnerability_report_")
        and filename.endswith(".json")
    )

    if not reports:
        print("No vulnerability reports found.")
        return None

    latest_report = reports[-1]
    print(f"Using vulnerability report: {latest_report}")
    return load_json(latest_report)


def analyze_governance_failures():
    """Identify governance issues from the available lab evidence."""
    vulnerabilities = load_latest_vulnerability_report()
    attack_log = load_json("attack_log.json")
    governance = load_json("governance_data.json")
    patch_status = load_json("patch_status.json") or {
        "struts_patched": False,
        "mysql_secured": False,
        "network_segmented": False
    }

    failures = []

    # Vulnerability and patch management
    if vulnerabilities:
        for item in vulnerabilities.get("vulnerabilities", []):
            if (
                item.get("vulnerable") is True
                and item.get("severity") in ("Critical", "High")
            ):
                failures.append({
                    "category": "Patch Management",
                    "description": (
                        f"Vulnerability identified: "
                        f"{item.get('vulnerability')}"
                    ),
                    "severity": item.get("severity"),
                    "impact": "Potential exposure to exploitation",
                    "recommendation": item.get(
                        "remediation", "Investigate and remediate the finding"
                    )
                })

    # Attack simulation evidence
    if attack_log and attack_log.get("success") is True:
        failures.append({
            "category": "Incident Detection",
            "description": (
                "The Struts simulation returned its expected "
                "vulnerability marker."
            ),
            "impact": (
                "The application condition requires investigation "
                "and detection-control validation."
            ),
            "recommendation": (
                "Review monitoring and alerting coverage, then "
                "validate whether the event would be detected."
            )
        })

    # Governance policies and metrics
    if governance:
        policies = governance.get("policies", [])
        metrics = governance.get("metrics", [])

        has_patch_policy = any(
            "patch" in policy.get("name", "").lower()
            for policy in policies
        )

        has_vulnerability_policy = any(
            "vulnerabilit" in policy.get("name", "").lower()
            for policy in policies
        )

        has_patch_metric = any(
            "patch" in metric.get("name", "").lower()
            for metric in metrics
        )

        if has_patch_policy and not patch_status.get("struts_patched", False):
            failures.append({
                "category": "Policy Implementation",
                "description": (
                    "The patch-management policy exists, but the "
                    "baseline status does not record Struts as patched."
                ),
                "impact": "The policy may not be operating effectively.",
                "recommendation": (
                    "Assign remediation ownership, deadlines and "
                    "management escalation for critical vulnerabilities."
                )
            })

        critical_count = (
            vulnerabilities.get("summary", {}).get("critical", 0)
            if vulnerabilities else 0
        )

        if has_vulnerability_policy and critical_count > 0:
            failures.append({
                "category": "Vulnerability Management",
                "description": (
                    "A critical vulnerability was recorded in the "
                    "baseline assessment."
                ),
                "impact": "Potential exploitation of the vulnerable service.",
                "recommendation": (
                    "Prioritise remediation and independently retest."
                )
            })

        if has_patch_metric and not patch_status.get("struts_patched", False):
            failures.append({
                "category": "Metrics and Measurement",
                "description": (
                    "The recorded patch-compliance metric is below target."
                ),
                "impact": "Remediation performance requires management attention.",
                "recommendation": (
                    "Track overdue items, assign accountable owners "
                    "and report exceptions."
                )
            })

    # Network segmentation
    if not patch_status.get("network_segmented", False):
        failures.append({
            "category": "Security Architecture",
            "description": (
                "Baseline patch status does not record network "
                "segmentation controls as implemented."
            ),
            "impact": "Potential for lateral movement between services.",
            "recommendation": (
                "Apply least-privilege network restrictions and verify "
                "permitted and denied connections."
            )
        })

    # Database authentication
    if not patch_status.get("mysql_secured", False):
        failures.append({
            "category": "Authentication and Access Control",
            "description": (
                "Baseline patch status does not record MySQL security "
                "configuration as implemented."
            ),
            "impact": "Default credentials may permit unauthorised access.",
            "recommendation": (
                "Replace default credentials and review database "
                "permissions and network exposure."
            )
        })

    return failures


def main():
    failures = analyze_governance_failures()

    report = {
        "timestamp": datetime.datetime.now().isoformat(),
        "failures": failures,
        "summary": {
            "total_failures": len(failures),
            "categories": {}
        }
    }

    for failure in failures:
        category = failure["category"]
        report["summary"]["categories"][category] = (
            report["summary"]["categories"].get(category, 0) + 1
        )

    report_file = (
        "governance_failure_report_"
        + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".json"
    )

    with open(report_file, "w") as file:
        json.dump(report, file, indent=2)

    print(f"Governance failure analysis completed: {report_file}")
    print(
        "Governance issues requiring review:",
        report["summary"]["total_failures"]
    )

    for category, count in report["summary"]["categories"].items():
        print(f"  {category}: {count}")


if __name__ == "__main__":
    main()
