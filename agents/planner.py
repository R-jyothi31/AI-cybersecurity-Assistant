from agents.log_analyzer import (
    analyze_log
)

from agents.threat_detector import (
    detect_threat
)

from agents.server_monitor import (
    check_server_issues
)

from agents.threat_intel import (
    extract_ip,
    check_ip_reputation
)

from agents.report_generator import (
    generate_pdf
)


def run_agent(log_text):

    findings = analyze_log(
        log_text
    )

    threat = detect_threat(
        findings
    )

    issues = check_server_issues(
        log_text
    )

    ip = extract_ip(
        log_text
    )

    intel = check_ip_reputation(
        ip
    )

    result = {

        "findings": findings,

        "severity": threat[
            "severity"
        ],

        "mitre": threat[
            "mitre"
        ],

        "recommendations": threat[
            "recommendations"
        ],

        "issues": issues,

        "threat_intel": intel
    }

    generate_pdf(result)

    return result