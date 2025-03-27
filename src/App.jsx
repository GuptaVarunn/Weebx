import { SignedIn, SignedOut, SignInButton, UserButton } from "@clerk/clerk-react";
import React from "react";
import { BrowserRouter,Routes } from "react-router-dom";
export default function App() {
  return (
    <>
    <header>
      <SignedOut>
        <SignInButton />
      </SignedOut>
      <SignedIn>
        <UserButton />
      </SignedIn>
    </header>
    <BrowserRouter>
    <Routes>
      {/* <Route /> */}
      </Routes>
      </BrowserRouter>
    </>
  );
}