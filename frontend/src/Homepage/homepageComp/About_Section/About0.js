import React from "react";
import aboutI from "./pics/about-img1.jpg";
import about0 from "./about0.css";

export default function About0() {
  return (
    <div className="about0-container" id="about">
      <img src={aboutI} />

      <div className="about0-description">
        <h1>Who We Are</h1>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
          <br />
          <br />
          Dui sapien eget mi proin sed libero enim sed faucibus. Luctus
          venenatis lectus magna fringilla urna porttitor rhoncus. Scelerisque
          viverra mauris in aliquam. Ut tellus elementum sagittis vitae.
          Convallis convallis tellus id interdum velit. Donec massa sapien
          faucibus et molestie ac feugiat sed lectus. Id interdum velit laoreet
          id. Leo duis ut diam quam nulla porttitor massa id.
        </p>
      </div>
    </div>
  );
}
