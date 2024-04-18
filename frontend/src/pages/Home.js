import React from "react";
import Button from "@mui/material/Button";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();
  return (
    <div>
      <h1>Home</h1>
      <Button
        variant="contained"
        color="error"
        onClick={() => {
          navigate("/");
        }}
      >
        Logout
      </Button>
    </div>
  );
};

export default Home;
