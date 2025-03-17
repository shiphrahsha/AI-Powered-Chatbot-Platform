import React from "react";
import Chat from "../components/Chat";
import "../css/Chatbot.css";

const Chatbot = () => {
  //retrieve the user ID from the  localStorage
  const userId = localStorage.getItem("userId");

  if (!userId) {
    return (
      <div className="chatbot-container">
        User not logged in. Please log in to access the chatbot.
      </div>
    );
  }

  //generate random particles
  const particles = Array.from({ length: 40 }, (_, i) => ({
    id: i,
    left: `${Math.random() * 100}%`,
    top: `${Math.random() * 100}%`,
    animationDuration: `${Math.random() * 5 + 5}s`,
  }));

  return (
    <div className="chatbot-container">
      <Chat userId={userId} />
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

export default Chatbot;