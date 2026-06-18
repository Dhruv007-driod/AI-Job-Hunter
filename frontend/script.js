async function uploadResume() {

    let file =
        document.getElementById("resume")
        .files[0];

    let formData = new FormData();

    formData.append("file", file);

    let response = await fetch(
        "http://127.0.0.1:8000/upload",
        {
            method: "POST",
            body: formData
        }
    );

    let data = await response.json();

let jobsHTML = "";

for (let job of data.recommended_jobs) {

    jobsHTML += `
        <div class="card">

            <h4>${job.job}</h4>

            <p>
                Match Score:
                ${job.score}%
            </p>

            <p>
                Missing Skills:
                ${job.missing_skills.join(", ")}
            </p>

        </div>
    `;
}

document.getElementById("result").innerHTML = `
<div class="card">

<h2>Resume Analysis</h2>

<h2>
Resume Score:
${data.resume_score}/100
</h2>

<p><strong>Email:</strong> ${data.email}</p>

<p><strong>Phone:</strong> ${data.phone}</p>

<h3>Skills</h3>
<ul>
${data.skills.map(skill =>
`<li>${skill}</li>`).join("")}
</ul>

<h3>Recommended Jobs</h3>
<ul>
${jobsHTML}
</ul>

</div>
`;
}