def check_server_issues(log_text):

    issues = []

    lower_log = log_text.lower()

    if "memory error" in lower_log:
        issues.append(
            "Memory Issue"
        )

    if "cpu overload" in lower_log:
        issues.append(
            "CPU Overload"
        )

    if "database connection failed" in lower_log:
        issues.append(
            "Database Failure"
        )

    if "service unavailable" in lower_log:
        issues.append(
            "Service Outage"
        )

    return issues