document.addEventListener('DOMContentLoaded', () => {
    const chatBox = document.getElementById('chatBox');
    const messageForm = document.getElementById('messageForm');
    const userMessage = document.getElementById('userMessage');

    messageForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const message = userMessage.value.trim();

        if (message) {
            appendMessage('user', message);
            userMessage.value = '';

            try {
                const response = await fetch('https://3h2gghij55venpvyb7jfvimgfe0httbo.lambda-url.us-east-1.on.aws/', { 
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ question: message })
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const data = await response.json();
                const answer = data.answer || "I couldn't get a response from the server.";
                appendMessage('bot', answer);
            } catch (error) {
                console.error("Error fetching response:", error);
                appendMessage('bot', "There was an error processing your request.");
            }
        }
    });


    function appendMessage(sender, text) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('chat-message', sender === 'user' ? 'user-message' : 'bot-message');
    messageDiv.innerHTML = `<p>${text}</p>`;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

});
