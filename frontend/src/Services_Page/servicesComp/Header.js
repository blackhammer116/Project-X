import React, { useRef } from "react";
import header from "./header.css";
import { Link } from "react-router-dom";

export default function Header() {
  //   use state to manipulate the horizontal rules
  return (
    <div className="header-container">
      <Link to={"/home"}>
        <h1>PROJ.NOVA</h1>
      </Link>

      <div className="header-menu-list ">
        {/* <hr className="header-strip" /> */}
        <ul>
          <Link to={"/home"}>
            <li>Home</li>
          </Link>
          <Link to={"/about"}>
            <li>About</li>
          </Link>
          <li>Contact Us</li>
          <li>Sign Out</li>
        </ul>
      </div>
    </div>
  );
}
