const $ = (id) => document.getElementById(id);

const healthDot = $("health-dot");
const healthText = $("health-text");

async function checkHealth() {
  try {
    const res = await fetch("/health");
    if (!res.ok) throw new Error("Health check failed");
    healthDot.style.background = "#22c55e";
    healthText.textContent = "Online";
  } catch {
    healthDot.style.background = "#ef4444";
    healthText.textContent = "Offline";
  }
}

function setupTabs() {
  const buttons = document.querySelectorAll(".tab-btn");
  const tabs = document.querySelectorAll(".tab-content");

  buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
      buttons.forEach((b) => b.classList.remove("active"));
      tabs.forEach((t) => t.classList.remove("active"));

      btn.classList.add("active");
      const target = document.getElementById(btn.dataset.tab);
      target.classList.add("active");
    });
  });
}

function riskBadgeClass(level = "unknown") {
  return `risk-${level}`;
}

function renderCandidates(candidates = []) {
  if (!candidates.length) {
    return `<div class="row"><strong>No known hash format detected.</strong></div>`;
  }

  return candidates
    .map((c) => {
      const confidence = `${Math.round(c.confidence * 100)}%`;
      return `
        <div class="result-panel" style="margin-top:0.8rem;">
          <div class="row"><strong>Algorithm:</strong> ${c.algorithm.toUpperCase()}</div>
          <div class="row"><strong>Confidence:</strong> ${confidence}</div>
          <div class="row"><strong>Reason:</strong> ${c.reason}</div>
          <div class="row">
            <strong>Risk:</strong>
            <span class="pill ${riskBadgeClass(c.risk?.level)}">${c.risk?.level || "unknown"}</span>
            ${c.risk?.message || ""}
          </div>
        </div>
      `;
    })
    .join("");
}

function renderDetectResult(data) {
  const panel = $("detectResult");
  panel.classList.remove("hidden");
  panel.innerHTML = `
    <h3>Detection Result</h3>
    ${renderCandidates(data.candidates)}
    <div class="row" style="margin-top:0.8rem;"><strong>Recommendation:</strong> ${data.recommendation}</div>
  `;
}

function renderVerifyResult(data) {
  const panel = $("verifyResult");
  panel.classList.remove("hidden");
  panel.innerHTML = `
    <h3>Verification Result</h3>
    <div class="row"><strong>Status:</strong> ${data.verified ? "✅ Match" : "❌ No Match"}</div>
    <div class="row"><strong>Algorithm:</strong> ${(data.algorithm || "unknown").toUpperCase()}</div>
    <div class="row"><strong>Message:</strong> ${data.message}</div>
    <div class="row" style="margin-top:0.8rem;"><strong>Detection Candidates:</strong></div>
    ${renderCandidates(data.detection?.candidates || [])}
  `;
}

async function detectHash() {
  const hashValue = $("detectHash").value.trim();
  if (!hashValue) {
    alert("Please enter a hash value.");
    return;
  }

  const res = await fetch("/api/detect", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ hash_value: hashValue }),
  });

  const data = await res.json();
  if (!res.ok) {
    alert(data.detail || "Detection failed.");
    return;
  }

  renderDetectResult(data);
}

async function verifyHash() {
  const hashValue = $("verifyHash").value.trim();
  const plaintext = $("verifyPlain").value;

  if (!hashValue || !plaintext) {
    alert("Please provide both hash and plaintext.");
    return;
  }

  const res = await fetch("/api/verify", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ hash_value: hashValue, plaintext }),
  });

  const data = await res.json();
  if (!res.ok) {
    alert(data.detail || "Verification failed.");
    return;
  }

  renderVerifyResult(data);
}

function init() {
  setupTabs();
  checkHealth();

  $("detectBtn").addEventListener("click", detectHash);
  $("verifyBtn").addEventListener("click", verifyHash);
}

init();
