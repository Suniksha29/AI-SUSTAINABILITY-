import React from 'react';
import './Hero.css';

const Hero = () => {
  return (
    <div className="hero-container">
      <div className="hero-content">
        <h1 className="hero-headline">Welcome to a New Dimension</h1>
        <p className="hero-subheadline">
          Discover a world where creativity meets innovation. Let's build something amazing together.
        </p>
        <button className="hero-button">Get Started</button>
      </div>
    </div>
  );
};

export default Hero;
