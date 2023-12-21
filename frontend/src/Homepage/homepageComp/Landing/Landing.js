import React from "react";
import { Link } from "react-router-dom";
import logo from "./pic/logo2.png";
import landing from "./landing.css";

export default function Landing() {
  return (
    <div className="header" id="top">
      <div className="nav-items">
        <div className="logo-name">
          {/* <img src={logo} className="logo" /> */}
          <Link to={"/home"} className="no-decor">
            <h1>PROJ.NOVA</h1>
          </Link>
        </div>
        <div className="menu-items">
          <ul>
            <a href="#about">
              <li>About</li>
            </a>

            <a href="#services">
              <li>Services</li>
            </a>
            <li>Contact Us</li>

            <li>Sign In</li>
          </ul>
        </div>
      </div>
      <div className="message">
        <h1>where your catch phrases go </h1>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat.
        </p>
        <a href="#about">
          <button>Read More</button>
        </a>
      </div>
    </div>
  );
}
