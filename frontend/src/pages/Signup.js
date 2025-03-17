import React from "react";
import AuthForm from "../components/AuthForm";
import { Link as RouterLink, useNavigate } from "react-router-dom";
import "../css/AuthPage.css";
import axios from "axios";

const Signup = () => {
  const navigate = useNavigate();

  //function to handle signup form submission
  const handleSubmit = async (data) => {
    try {
      const response = await axios.post("http://localhost:5000/signup", data);
      navigate("/login");
      alert("Signup successful!");
    } catch (error) {
      alert(error.response?.data?.error || "Signup failed. Please try again.");
    }
  };

  return (
    <div className="auth-page">
      <AuthForm isLogin={false} onSubmit={handleSubmit} />
      <p className="auth-page-link">
        Already have an account? <RouterLink to="/login">Login</RouterLink>
      </p>
    </div>
  );
};

export default Signup;
