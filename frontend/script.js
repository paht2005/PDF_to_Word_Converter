document.getElementById("uploadForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const files = document.getElementById("fileInput").files;
  const strategy = document.getElementById("strategy").value;
  if (!files.length) return;

  const formData = new FormData();
  for (let f of files) formData.append("files", f);
  formData.append("strategy", strategy);

  document.getElementById("status").innerText = "Converting...";

  try {
    const res = await fetch("/api/convert", { method: "POST", body: formData });
    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.error || "Conversion failed");
    }
    const blob = await res.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = res.headers.get("Content-Disposition").split("filename=")[1];
    document.body.appendChild(a);
    a.click();
    a.remove();
    document.getElementById("status").innerText = "✅ Done!";
  } catch (err) {
    document.getElementById("status").innerText = "❌ " + err.message;
  }
});
