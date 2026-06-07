async function uploadLog(){

    let file =
        document.getElementById(
            "logFile"
        ).files[0];

    let formData =
        new FormData();

    formData.append(
        "file",
        file
    );

    let response =
        await fetch(
            "/analyze",
            {
                method:"POST",
                body:formData
            }
        );

    let data =
        await response.json();

    document.getElementById(
        "analysisResult"
    ).innerHTML =

    `
    <b>Threats:</b><br>
    ${data.findings.join("<br>")}
    <br><br>

    <b>Severity:</b>
    ${data.severity}

    <br><br>

    <b>Server Issues:</b><br>
    ${data.issues.join("<br>")}
    `;

    document.getElementById(
        "intelResult"
    ).innerHTML =

    `
    <b>IP:</b>
    ${data.threat_intel.ip}
    <br>

    <b>Country:</b>
    ${data.threat_intel.country}
    <br>

    <b>Organization:</b>
    ${data.threat_intel.org}
    `;

    document.getElementById(
        "mitreResult"
    ).innerHTML =
    data.mitre.join("<br>");

    document.getElementById(
        "severityCard"
    ).innerText =
    data.severity;

    document.getElementById(
        "threatCount"
    ).innerText =
    data.findings.length;

    document.getElementById(
        "issueCount"
    ).innerText =
    data.issues.length;
}


async function askAI(){

    let question =
        document.getElementById(
            "question"
        ).value;

    let response =
        await fetch(
            "/chat",
            {
                method:"POST",

                headers:{
                    "Content-Type":
                    "application/json"
                },

                body:JSON.stringify({
                    question:question
                })
            }
        );

    let data =
        await response.json();

    document.getElementById(
        "chatResult"
    ).innerHTML =
    data.answer;
}