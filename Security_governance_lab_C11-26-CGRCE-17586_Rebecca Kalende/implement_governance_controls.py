#!/usr/bin/env python3

import argparse
import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime

from governance_tracker import GovernanceTracker

BASE = Path(__file__).resolve().parent


def apply_simulated_patch(patch_id):
    """Record a simulated remediation action."""
    subprocess.run(
        [sys.executable, str(BASE / "patch_management.py"),
         "--apply", patch_id],
        cwd=BASE,
        check=True
    )


def add_control_once(name, description, policy_id, owner):
    """Register a control only if it does not already exist."""
    tracker = GovernanceTracker(str(BASE / "governance_data.json"))

    existing = [
        item for item in tracker.list_controls()
        if item["name"] == name
    ]

    if existing:
        print(f"Control already registered: {name}")
        return

    control_id = tracker.add_control(
        name,
        description,
        policy_id,
        owner,
        datetime.now().strftime("%Y-%m-%d")
    )
    print(f"Registered control: {control_id} - {name}")


def implement_patch():
    apply_simulated_patch("PATCH-001")
    add_control_once(
        "Automated Patch Management",
        "Track vulnerability remediation and patch-status evidence.",
        "POL-001",
        "Security Engineer"
    )


def implement_database():
    apply_simulated_patch("PATCH-002")
    add_control_once(
        "Database Security",
        "Track database authentication and access-control remediation.",
        "POL-001",
        "Database Administrator"
    )


def implement_network():
    apply_simulated_patch("PATCH-003")
    add_control_once(
        "Network Segmentation",
        "Track least-privilege network restrictions and connectivity tests.",
        "POL-001",
        "Network Engineer"
    )


def implement_monitoring():
    script = BASE / "monitoring" / "security_monitor.sh"

    if not script.exists():
        print("Monitoring script not found; monitoring control not registered.")
        return

    script.chmod(0o755)

    add_control_once(
        "Security Monitoring",
        "Collect container status, selected web-log events and reachability alerts.",
        "POL-002",
        "Security Engineer"
    )

    print("Existing monitoring script preserved.")


def implement_oversight():
    document = BASE / "governance_oversight.md"

    if not document.exists():
        document.write_text(
            "# Security Governance Oversight\n\n"
            "Define control ownership, risk escalation, management reporting, "
            "remediation accountability and independent retesting.\n"
        )

    tracker = GovernanceTracker(str(BASE / "governance_data.json"))
    policies = [
        item for item in tracker.list_policies()
        if item["name"] == "Security Governance Oversight"
    ]

    if policies:
        policy_id = policies[0]["id"]
    else:
        policy_id = tracker.add_policy(
            "Security Governance Oversight",
            "Defines governance accountability and escalation arrangements.",
            "CEO",
            datetime.now().strftime("%Y-%m-%d"),
            datetime.now().strftime("%Y-%m-%d")
        )

    add_control_once(
        "Executive Security Oversight",
        "Document executive reporting and security-risk escalation.",
        policy_id,
        "CEO"
    )


def verify_controls():
    print("\n=== Control Verification Summary ===")

    status_file = BASE / "patch_status.json"
    if status_file.exists():
        status = json.loads(status_file.read_text())
        for key in (
            "struts_patched",
            "mysql_secured",
            "network_segmented"
        ):
            print(f"{key} recorded: {status.get(key, False)}")
    else:
        print("Patch status file not found.")

    print(
        "Monitoring script exists:",
        (BASE / "monitoring" / "security_monitor.sh").exists()
    )
    print(
        "Governance oversight document exists:",
        (BASE / "governance_oversight.md").exists()
    )

    tracker = GovernanceTracker(str(BASE / "governance_data.json"))
    print("Policies recorded:", len(tracker.list_policies()))
    print("Controls recorded:", len(tracker.list_controls()))
    print("Risks recorded:", len(tracker.list_risks()))
    print("Metrics recorded:", len(tracker.list_metrics()))

    print(
        "\nImportant: recorded status flags indicate simulation state only. "
        "Confirm technical effectiveness through independent tests."
    )


def main():
    parser = argparse.ArgumentParser(
        description="Security Governance Control Implementation Simulation"
    )
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--patch", action="store_true")
    parser.add_argument("--database", action="store_true")
    parser.add_argument("--network", action="store_true")
    parser.add_argument("--monitoring", action="store_true")
    parser.add_argument("--oversight", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    if args.all or args.patch:
        implement_patch()
    if args.all or args.database:
        implement_database()
    if args.all or args.network:
        implement_network()
    if args.all or args.monitoring:
        implement_monitoring()
    if args.all or args.oversight:
        implement_oversight()
    if args.all or args.verify:
        verify_controls()


if __name__ == "__main__":
    main()
