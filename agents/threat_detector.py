def detect_threat(findings):

    severity = "Low"

    recommendations = []

    mitre = []

    if "Brute Force Attack" in findings:

        severity = "High"

        mitre.append(
            "T1110 - Brute Force"
        )

        recommendations.extend([
            "Enable MFA",
            "Block Source IP",
            "Implement Account Lockout"
        ])

    if "Web Reconnaissance" in findings:

        severity = "Medium"

        mitre.append(
            "T1595 - Active Scanning"
        )

        recommendations.extend([
            "Enable WAF",
            "Restrict Admin Access"
        ])

    if "Possible SQL Injection" in findings:

        severity = "High"

        mitre.append(
            "T1190 - Exploit Public Facing Application"
        )

        recommendations.extend([
            "Validate Inputs",
            "Use Parameterized Queries"
        ])

    return {
        "severity": severity,
        "mitre": mitre,
        "recommendations": recommendations
    }