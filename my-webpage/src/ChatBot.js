// src/Chatbot.js
import React, { useState } from "react";
import "./chatbot.css";

const Chatbot = () => {
  const [messages, setMessages] = useState([{ text: "Hello! How can I help you?", sender: "bot" }]);
  const [input, setInput] = useState("");

  // Predefined responses for demonstration
  const responses = {
    hello: "Hi there! How can I assist you today?",
    help: "I'm here to help! You can ask me about our services, products, or general inquiries.",
    bye: "Goodbye! Have a nice day!",
  };

  const handleSend = () => {
    if (input.trim() === "") return;
    
    // Add user's message
    const userMessage = { text: input, sender: "user" };
    setMessages([...messages, userMessage]);

    // Simple response logic
    const botResponseText = responses[input.toLowerCase()] || "I'm sorry, I don't understand that.";
    const botMessage = { text: botResponseText, sender: "bot" };
    
    setMessages(prevMessages => [...prevMessages, userMessage, botMessage]);
    setInput(""); // Clear input
  };

  return (
    <div className="chatbot-container">
      <div className="chatbot-messages">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>
      <div className="chatbot-input">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
};

export default Chatbot;
