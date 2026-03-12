const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

sendBtn.addEventListener("click", handleSendMessage);

userInput.addEventListener("keypress", function (e) {
  if (e.key === "Enter") {
    handleSendMessage();
  }
});

async function sendMessageToServer(message) {
  if (!message) return;

  const response = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ question: message }),
  });

  const data = await response.json();
  console.log(data.response);
  return data.response;
}

async function getMockAIResponse(userText) {
  const reply = await sendMessageToServer(userText);
  appendMessage("ai", reply);
  return reply;
}

function handleSendMessage() {
  const text = userInput.value.trim();
  if (text === "") return;

  appendMessage("user", text);
  userInput.value = "";

  showTypingIndicator();

  setTimeout(async () => {
    removeTypingIndicator();
    await getMockAIResponse(text);
  }, 1500);
}

function appendMessage(sender, text) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", `${sender}-message`);

  const contentDiv = document.createElement("div");
  contentDiv.classList.add("message-content");
  contentDiv.textContent = text;

  messageDiv.appendChild(contentDiv);
  chatBox.appendChild(messageDiv);

  scrollToBottom();
}

function showTypingIndicator() {
  const typingDiv = document.createElement("div");
  typingDiv.classList.add("typing-indicator");
  typingDiv.id = "typing-indicator";
  typingDiv.innerHTML = "<span></span><span></span><span></span>";

  chatBox.appendChild(typingDiv);
  scrollToBottom();
}

function removeTypingIndicator() {
  const typingDiv = document.getElementById("typing-indicator");
  if (typingDiv) {
    typingDiv.remove();
  }
}

function scrollToBottom() {
  chatBox.scrollTop = chatBox.scrollHeight;
}

const logoutBtn = document.getElementById("logout-btn");

if (logoutBtn) {
  logoutBtn.addEventListener("click", function () {
    const confirmLogout = confirm(
      "Bạn có chắc chắn muốn đăng xuất khỏi AISawsn?",
    );
    if (confirmLogout) {
      window.location.href = "landing.html";
    }
  });
}
