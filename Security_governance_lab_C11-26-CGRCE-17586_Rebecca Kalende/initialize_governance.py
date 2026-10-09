#!/usr/bin/env python3

from governance_tracker import GovernanceTracker


def initialize_governance_data():
    tracker = GovernanceTracker()

    # Sample policies
    patch_policy = tracker.add_policy(
        "Patch Management Policy",
        "Policy governing the timely application of security patches",
        "CISO",
        "2023-01-15",
        "2024-01-15"
    )

    vulnerability_policy = tracker.add_policy(
        "Vulnerability Management Policy",
        "Policy governing the identification and remediation of vulnerabilities",
        "Security Director",
        "2023-02-10",
        "2024-02-10"
    )

    incident_policy = tracker.add_policy(
        "Incident Response Policy",
        "Policy governing responses to security incidents",
        "CISO",
        "2023-03-05",
        "2024-03-05"
    )

    # Sample controls
    tracker.add_control(
        "Patch Management Process",
        "Process for identifying, testing and applying security patches",
        patch_policy,
        "IT Manager",
        "2023-01-20"
    )

    tracker.add_control(
        "Vulnerability Scanning",
        "Regular scanning for security vulnerabilities",
        vulnerability_policy,
        "Security Engineer",
        "2023-02-15"
    )

    tracker.add_control(
        "Incident Response Team",
        "Team responsible for responding to security incidents",
        incident_policy,
        "Security Director",
        "2023-03-10"
    )

    # Sample risks
    tracker.add_risk(
        "Unpatched Vulnerabilities",
        "Risk of exploitation due to unpatched vulnerabilities",
        "High",
        "High",
        "Security Engineer",
        "Implement automated patch management"
    )

    tracker.add_risk(
        "Insufficient Network Segmentation",
        "Risk of lateral movement between systems",
        "Medium",
        "High",
        "Network Engineer",
        "Apply network segmentation and least-privilege controls"
    )

    tracker.add_risk(
        "Weak Authentication",
        "Risk of unauthorised access due to weak authentication",
        "Medium",
        "Medium",
        "Identity Manager",
        "Implement strong authentication and access controls"
    )

    # Sample incident
    tracker.add_incident(
        "Web Server Compromise",
        "Simulated compromise involving an unpatched Struts vulnerability",
        "2023-04-15",
        "High",
        "Web Server",
        "Unpatched Struts vulnerability (CVE-2017-5638)",
        "Simulated remediation and recovery"
    )

    # Sample metrics
    tracker.add_metric(
        "Patch Compliance",
        "Percentage of systems with critical patches applied",
        95.0,
        85.0,
        "May 2023",
        "Improving"
    )

    tracker.add_metric(
        "Vulnerability Remediation Time",
        "Average time to remediate critical vulnerabilities in days",
        7.0,
        12.0,
        "May 2023",
        "Declining"
    )

    tracker.add_metric(
        "Security Incidents",
        "Number of security incidents during the reporting period",
        0.0,
        1.0,
        "May 2023",
        "Stable"
    )

    # Sample audit
    tracker.add_audit(
        "Annual Security Audit",
        "Comprehensive review of security controls",
        "2023-05-01",
        "External Auditor",
        "Findings involving patch management and network segmentation",
        "Improve patch management and network segmentation"
    )

    print("Governance tracker initialized with sample data.")


if __name__ == "__main__":
    initialize_governance_data()
