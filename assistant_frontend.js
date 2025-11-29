const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const micBtn = document.getElementById('mic-btn');

function appendMessage(sender, text) {
    const msgRow = document.createElement('div');
    msgRow.className = `chat-msg ${sender}`;
    const bubble = document.createElement('div');
    bubble.className = `bubble ${sender}`;
    if (sender === 'user') {
        bubble.innerHTML = `<div style="font-size:0.95em;font-weight:bold;margin-bottom:2px;">You</div>${text}`;
    } else {
        bubble.innerHTML = `<div style="font-size:0.95em;font-weight:bold;margin-bottom:2px;">Assistant</div>${text}`;
    }
    msgRow.appendChild(bubble);
    chatBox.appendChild(msgRow);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendToBackend(text) {
    appendMessage('user', text);
    userInput.value = '';
    appendMessage('assistant', '...thinking...');
    try {
        const res = await fetch('http://localhost:5000/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: text })
        });
        const data = await res.json();
        // Remove the '...thinking...' message
        chatBox.removeChild(chatBox.lastChild);
        appendMessage('assistant', data.reply);
        // Speak the assistant's reply using browser TTS
        if ('speechSynthesis' in window) {
            const utterance = new SpeechSynthesisUtterance(data.reply);
            utterance.lang = 'en-US';
            window.speechSynthesis.speak(utterance);
        }
    } catch (err) {
        chatBox.removeChild(chatBox.lastChild);
        appendMessage('assistant', 'Error contacting backend.');
    }
}

userInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        const text = userInput.value.trim();
        if (!text) return;
        sendToBackend(text);
    }
});

// Optional: Add speech recognition for mic button
micBtn.onclick = () => {
    if (!('webkitSpeechRecognition' in window)) {
        alert('Speech recognition not supported in this browser.');
        return;
    }
    const recognition = new webkitSpeechRecognition();
    recognition.lang = 'en-US';
    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        userInput.value = transcript;
        // Automatically send to backend when speech is recognized
        if (transcript.trim()) {
            sendToBackend(transcript);
        }
    };
    recognition.start();
};
