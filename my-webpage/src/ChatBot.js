// src/Chatbot.js
import React, { useState } from "react";
import "./chatbot.css";
import axios from "axios";


const Chatbot = () => {
  const [messages, setMessages] = useState([{ text: "Hello! How can I help you?", sender: "bot" }]);
  const [input, setInput] = useState("");

  // Predefined responses for demonstration
  const responses = {
    hello: "Hi there! How can I assist you today?",
    help: "I'm here to help! You can ask me about our services, products, or general inquiries.",
    bye: "Goodbye! Have a nice day!",
  };

  const handleSend = async () => {
    if (input.trim() === "") return;
  
    const userMessage = { text: input, sender: "user" };
    setMessages([...messages, userMessage]);
  
    try {
      const response = await axios.post("https://api.openai.com/v1/engines/davinci-codex/completions", {
        prompt: input,
        max_tokens: 50,
        temperature: 0.7,
      }, {
        headers: {
          "Authorization": `Bearer YOUR_OPENAI_API_KEY`
        }
      });
  
      const botResponseText = response.data.choices[0].text.trim();
      const botMessage = { text: botResponseText, sender: "bot" };
  
      setMessages(prevMessages => [...prevMessages, userMessage, botMessage]);
    } catch (error) {
      console.error("Error fetching response:", error);
    }
    
    setInput("");
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
