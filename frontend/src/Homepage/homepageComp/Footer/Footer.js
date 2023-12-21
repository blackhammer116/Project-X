import React from "react";
import { FaFacebook } from "react-icons/fa6";
import { FaXTwitter } from "react-icons/fa6";
import { FaInstagram } from "react-icons/fa6";
import { SiGmail } from "react-icons/si";
import footer from "./footer.css";

export default function Footer() {
  return (
    <div className="footer-container no-decor">
      <h1> PROJ.NOVA</h1>
      <ul>
        <li>
          <FaFacebook size={25} />
        </li>
        <li>
          <FaInstagram size={25} />
        </li>
        <li>
          <FaXTwitter size={25} />
        </li>
        <li>
          <SiGmail size={25} />
        </li>
      </ul>
      <ul>
        <a href="#top">
          <li>Home</li>
        </a>
        <a href="#about">
          <li>About Us</li>
        </a>
        <a href="#services">
          <li>Services</li>
        </a>
        <li>Contact</li>
      </ul>

      <hr className="footer-strip" />

      <p className="copyright">Copyright@2023</p>
    </div>
  );
}
