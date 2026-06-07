import re

def analyze_log(log_text):

    findings = []

    failed_logins = log_text.count(
        "Failed password"
    )

    if failed_logins >= 3:
        findings.append(
            "Brute Force Attack"
        )

    admin_access = len(
        re.findall(
            r"/admin|/wp-admin|/phpmyadmin",
            log_text.lower()
        )
    )

    if admin_access > 0:
        findings.append(
            "Web Reconnaissance"
        )

    if "sql syntax" in log_text.lower():
        findings.append(
            "Possible SQL Injection"
        )

    return findings