import React from "react";
import Landing from "./Landing/Landing";
import About from "./About_Section/About0";
import Separator from "./SecSep/Separator";
import Services from "./Services/Services";
import Footer from "./Footer/Footer";

export default function HomePage() {
  return (
    <>
      <Landing />
      <About />
      <Separator />
      <Services />
      <Footer />
    </>
  );
}
