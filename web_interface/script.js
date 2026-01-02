document.addEventListener('DOMContentLoaded', () => {
    // Configuration
    // Assumes Rasa is running on localhost:5005
    const RASA_URL = 'http://localhost:5005';

    // Connect to Socket.IO
    const socket = io(RASA_URL, {
        transports: ['websocket', 'polling']
    });

    const chatWidget = document.getElementById('chat-widget-messages');
    const inputForm = document.getElementById('chat-input-form');
    const inputField = document.getElementById('chat-input');

    // Connection events
    socket.on('connect', () => {
        console.log('Connected to Rasa server');
        // Optional: Send initial payload to trigger a greeting if your bot expects it
        // socket.emit('user_uttered', { message: '/start' });
    });

    socket.on('disconnect', () => {
        console.log('Disconnected from Rasa server');
    });

    socket.on('connect_error', (error) => {
        console.error('Connection error:', error);
    });

    // Handle incoming messages from bot
    socket.on('bot_uttered', (data) => {
        console.log('Bot uttered:', data);
        if (data.text) {
            appendMessage(data.text, 'bot');
        }
        if (data.image) {
            appendImage(data.image, 'bot');
        }
    });

    // Send message to bot
    inputForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const message = inputField.value.trim();

        if (message) {
            // Display user message
            appendMessage(message, 'user');

            // Send to Rasa
            // The event name 'user_uttered' matches the keys configured in credentials.yml
            socket.emit('user_uttered', {
                message: message,
                session_id: socket.id
            });

            inputField.value = '';
        }
    });

    function appendMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);

        const contentDiv = document.createElement('div');
        contentDiv.classList.add('message-content');
        contentDiv.textContent = text;

        messageDiv.appendChild(contentDiv);
        chatWidget.appendChild(messageDiv);

        scrollToBottom();
    }

    function appendImage(imageUrl, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);

        const contentDiv = document.createElement('div');
        contentDiv.classList.add('message-content');

        const img = document.createElement('img');
        img.src = imageUrl;
        img.style.maxWidth = '100%';
        img.style.borderRadius = '8px';
        img.onload = scrollToBottom; // Scroll when image loads

        contentDiv.appendChild(img);
        messageDiv.appendChild(contentDiv);
        chatWidget.appendChild(messageDiv);

        scrollToBottom();
    }

    function scrollToBottom() {
        chatWidget.scrollTop = chatWidget.scrollHeight;
    }
});
