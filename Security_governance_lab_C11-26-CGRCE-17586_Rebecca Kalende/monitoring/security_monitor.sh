#!/usr/bin/env bash

set -u

BASE_DIR="$HOME/security_governance_lab/monitoring/output"
mkdir -p "$BASE_DIR"

STAMP=$(date '+%Y%m%d_%H%M%S')
ALERTS="$BASE_DIR/security_alerts_${STAMP}.log"

echo "Security monitoring run: $(date -Is)" | tee "$ALERTS"

echo
echo "=== Container status ==="
sudo docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}' \
    | tee "$BASE_DIR/container_status_${STAMP}.txt"

echo
echo "=== Suspicious web log patterns ==="
sudo docker logs --since 30m web_server 2>&1 \
    | grep -Ei 'multipart/form-data|exception|error|X-Vulnerable' \
    > "$BASE_DIR/suspicious_web_events_${STAMP}.log" || true

if [ -s "$BASE_DIR/suspicious_web_events_${STAMP}.log" ]; then
    echo "ALERT: Matching web log patterns found." | tee -a "$ALERTS"
else
    echo "No matching patterns found in collected web logs." | tee -a "$ALERTS"
fi

echo
echo "=== Web-to-database reachability ==="
if sudo docker exec web_server bash -c \
    'timeout 3 bash -c "</dev/tcp/database_server/3306"' 2>/dev/null
then
    echo "ALERT: Web container can reach database port 3306." | tee -a "$ALERTS"
else
    echo "Database TCP reachability was not confirmed." | tee -a "$ALERTS"
fi

echo
echo "Monitoring evidence saved under: $BASE_DIR"
