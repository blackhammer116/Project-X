import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./Homepage/homepageComp/HomePage";
import Services from "./Services_Page/Services";
import About0 from "./Homepage/homepageComp/About_Section/About0";

import "./App.css";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route index element={<HomePage />} />
          <Route path="/home" element={<HomePage />} />
          <Route path="/services" element={<Services />} />
          <Route path="/about" element={<About0 />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
