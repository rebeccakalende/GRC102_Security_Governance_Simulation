#!/usr/bin/env python3

import json
import datetime
import argparse


def get_available_patches():
    """Return the simulated patches available in the lab."""
    return [
        {
            "id": "PATCH-001",
            "name": "Apache Struts2 S2-045 Patch",
            "description": "Fixes CVE-2017-5638 in Apache Struts2",
            "severity": "Critical",
            "affected_system": "web_server",
            "status": "Available"
        },
        {
            "id": "PATCH-002",
            "name": "MySQL Security Configuration",
            "description": "Improves MySQL authentication and access controls",
            "severity": "High",
            "affected_system": "database_server",
            "status": "Available"
        },
        {
            "id": "PATCH-003",
            "name": "Network Segmentation Rules",
            "description": "Simulates segmentation controls between services",
            "severity": "Medium",
            "affected_system": "all",
            "status": "Available"
        }
    ]


def apply_patch(patch_id):
    """Record a simulated patch application."""
    patches = get_available_patches()
    patch = next((item for item in patches if item["id"] == patch_id), None)

    if not patch:
        print(f"Error: Patch {patch_id} not found")
        return False

    print(f"Applying simulated patch: {patch['name']} ({patch['id']})")
    print(f"Description: {patch['description']}")
    print(f"Affected system: {patch['affected_system']}")

    status_key = {
        "PATCH-001": "struts_patched",
        "PATCH-002": "mysql_secured",
        "PATCH-003": "network_segmented"
    }[patch_id]

    try:
        try:
            with open("patch_status.json", "r") as file:
                status = json.load(file)
        except FileNotFoundError:
            status = {}

        status[status_key] = True
        status.setdefault("updated_at", datetime.datetime.now().isoformat())

        with open("patch_status.json", "w") as file:
            json.dump(status, file, indent=2)

        print("Simulated patch status recorded successfully.")
        print("Note: This records a simulation status; it does not patch the software or enforce network rules.")
        return True

    except (OSError, json.JSONDecodeError) as error:
        print(f"Error recording simulated patch status: {error}")
        return False


def list_patches():
    """List all available simulated patches."""
    print("Available simulated patches:")
    print("----------------------------")

    for patch in get_available_patches():
        print(f"ID: {patch['id']}")
        print(f"Name: {patch['name']}")
        print(f"Description: {patch['description']}")
        print(f"Severity: {patch['severity']}")
        print(f"Affected system: {patch['affected_system']}")
        print(f"Status: {patch['status']}")
        print()


def main():
    parser = argparse.ArgumentParser(
        description="Security Governance Patch Management Simulation"
    )
    parser.add_argument("--list", action="store_true",
                        help="List available simulated patches")
    parser.add_argument("--apply", metavar="PATCH_ID",
                        help="Record a simulated patch application")

    args = parser.parse_args()

    if args.list:
        list_patches()
    elif args.apply:
        apply_patch(args.apply)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
