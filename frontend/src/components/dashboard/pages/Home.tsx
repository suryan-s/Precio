import { useLocalStorage } from "usehooks-ts";
import { useEffect } from "react";
import { useLocation } from "wouter";

import Navbar from "@/components/dashboard/Navbar";

export default function Home() {
  const [token] = useLocalStorage<string | null>("token", null);
  const [__, setLocation] = useLocation();

  useEffect(() => {
    if (token === null) {
      setLocation("/Login");
    }
  }, [token]);
  return (
    <>
      <Navbar />
    </>
  );
}
