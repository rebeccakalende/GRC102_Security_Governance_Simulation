# Security Governance Controls Implementation Report

## 1. Overview

This report documents the governance control activities performed to address the weaknesses identified in the laboratory's initial security assessment. The control areas were patch management, database security, network segmentation, security monitoring and governance oversight.

## 2. Control Implementation

### 2.1 Patch Management

The patch-management simulation recorded `PATCH-001` for the critical Apache Struts S2-045 vulnerability. The resulting status file recorded `struts_patched: true`.

The post-control vulnerability scan continued to identify the critical Struts finding. Therefore, the simulated status change did not demonstrate that the vulnerable software had been remediated.

### 2.2 Database Security

The workflow recorded `PATCH-002` as the simulated MySQL security-configuration action. However, a subsequent technical test successfully authenticated to MySQL using the configured default root password. The database-security control therefore did not pass independent verification.

### 2.3 Network Segmentation

The workflow recorded `PATCH-003` as the simulated network-segmentation action. Independent testing confirmed that the web container could still reach the database on TCP port 3306. The network-segmentation control therefore requires further implementation and retesting.

### 2.4 Security Monitoring

A local monitoring script was created to collect Docker container status, search web-container logs for configured patterns and test web-to-database reachability. During the recorded run, no matching web-log patterns were found, but the script generated an alert for database connectivity.

This evidence demonstrates basic monitoring activity. It does not establish centralised SIEM capability or continuous enterprise-level detection.

### 2.5 Governance Oversight

A governance-oversight document was prepared to describe proposed responsibilities, risk escalation, management reporting and accountability. The document supports the governance design but does not, by itself, prove formal adoption by an organisation.

## 3. Verification Results

The verification script confirmed that the simulated status flags were recorded and that the monitoring script and governance-oversight document existed.

However, independent tests found that the critical Struts marker remained present, MySQL accepted the configured default root password, and the web container retained TCP connectivity to the database. The latest vulnerability report also contained an inconclusive network-segmentation result due to a decoding error.

## 4. Outstanding Actions

1. Remediate or replace the vulnerable Struts application and repeat the vulnerability assessment.
2. Replace default database credentials, review account privileges and retest database authentication.
3. Apply appropriate network restrictions and retest permitted and denied connectivity.
4. Correct the scanner's network-checking error and repeat that check.
5. Preserve evidence, assign remediation owners and retest all changes before declaring the controls effective.

## 5. Conclusion

The laboratory control workflow and supporting governance records were created. However, independent technical verification did not demonstrate that the critical Struts vulnerability, weak MySQL authentication or web-to-database connectivity weaknesses had been resolved.

The simulation highlights the importance of validating technical changes, maintaining accurate control status, escalating unresolved risks and requiring evidence-based retesting before closure.

**Report limitation:** This is a report on a simulated laboratory environment. Recorded patch-status flags and proposed governance arrangements are not evidence of actual production remediation or organisational approval.
