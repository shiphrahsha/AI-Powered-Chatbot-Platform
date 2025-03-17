import React from "react";
import { useNavigate, useLocation } from "react-router-dom";
import "../css/OptionsPage.css";

const OptionsPage = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const chatHistory = location.state?.chatHistory || [];

  //function to navigate to the Chat with Users page
  const handleChatWithUsers = () => {
    navigate("/chatbot");
  };

  //function to navigate to the AI Chatbot page with chat history
  const handleChatWithAI = () => {
    navigate("/aichatbot", { state: { chatHistory } });
  };

  const particles = Array.from({ length: 50 }, (_, i) => ({
    id: i,
    left: `${Math.random() * 100}%`,
    top: `${Math.random() * 100}%`,
    animationDuration: `${Math.random() * 5 + 5}s`,
  }));

  return (
    <div className="options-page">
      <h2>Choose an option:</h2>
      <button className="option-button" onClick={handleChatWithUsers}>
        Chat with Users
      </button>
      <button className="option-button" onClick={handleChatWithAI}>
        Chat with AI
      </button>
      <div className="particles">
        {particles.map((p) => (
          <div
            key={p.id}
            className="particle"
            style={{
              left: p.left,
              top: p.top,
              animationDuration: p.animationDuration,
            }}
          />
        ))}
      </div>
    </div>
  );
};

export default OptionsPage;
