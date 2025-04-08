function sendMessage() {
    const input = document.getElementById("user-input");
    const msg = input.value.trim();
    if (!msg) return;

    addMessage("user", msg);
    input.value = "";

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
    })
    .then(response => response.json())
    .then(data => {
        addMessage("bot", data.reply);
    })
    .catch(err => {
        addMessage("bot", "Oops! Server error: " + err);
    });
}

function addMessage(sender, message) {
    const box = document.getElementById("chat-box");
    const div = document.createElement("div");
    div.className = sender;
    div.textContent = (sender === "user" ? "You: " : "MindMate: ") + message;
    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
}
