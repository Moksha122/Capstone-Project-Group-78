document.getElementById('send-btn').addEventListener('click', function() {
    const userQuery = document.getElementById('user-query').value;
    
    if (userQuery.trim() !== "") {
        // Display user message
        displayMessage(userQuery, 'user');
        
        // Clear input field
        document.getElementById('user-query').value = "";
        
        // Simulate a bot response
        const botResponse = getBotResponse(userQuery);
        displayMessage(botResponse, 'bot');
        
        // Scroll to the bottom of the chat
        scrollToBottom();
    }
});

// Function to display messages in the chatbox
function displayMessage(message, sender) {
    const chatBox = document.getElementById('chat-box');
    
    const messageBubble = document.createElement('div');
    messageBubble.classList.add('chat-bubble');
    messageBubble.classList.add(sender === 'user' ? 'user-bubble' : 'bot-bubble');
    messageBubble.innerHTML = `<strong>${sender === 'user' ? 'You' : 'Bot'}:</strong> ${message}`;
    
    chatBox.appendChild(messageBubble);
}

// Function to get bot response (simple example)
function getBotResponse(query) {
    if (query.toLowerCase().includes('refund')) {
        return 'Our refund policy allows you to return products within 30 days for a full refund.';
    }else if (query.toLowerCase().includes('hi')) {
        return 'hello! welcome!, how can i help you?';
    }else if (query.toLowerCase().includes('return')) {
        return 'You can return a product by visiting our Returns page or contacting customer support.';
    }
    else if (query.toLowerCase().includes('offer gift cards?')) {
        return 'Yes, we offer gift cards for various amounts. You can purchase them on our website.';
    }else if (query.toLowerCase().includes('shipping address')) {
        return 'Yes, you can update your shipping address before your order is shipped. Please contact support immediately.';
    } else if (query.toLowerCase().includes('contact customer support')) {
        return 'You can contact customer support by emailing support@company.com or calling 1-800-123-4567.';
    } 
     
    else {
        return "I'm sorry, I don't have an answer for that. Please contact support team.";
    }
}

// Function to scroll chat box to the bottom
function scrollToBottom() {
    const chatBox = document.getElementById('chat-box');
    chatBox.scrollTop = chatBox.scrollHeight;
}
