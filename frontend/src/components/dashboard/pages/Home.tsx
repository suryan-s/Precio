import { useLocalStorage } from "usehooks-ts";
import { useEffect } from "react";
import { useLocation } from "wouter";

import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

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
      <div className="flex flex-col justify-center p-6 px-6 md:px-12">
        <h1 className="text-4xl font-bold">Projects</h1>
        <div className="mt-8 flex flex-wrap gap-8">
          <Card>
            <CardHeader>
              <CardTitle>Project Name</CardTitle>
              <CardDescription>
                <span className="font-black text-xl leading-3">•</span> Offline
              </CardDescription>
            </CardHeader>
            <CardContent>
              <img
                src="https://via.placeholder.com/200"
                width={200}
                height={200}
                alt="Project Image"
              />
            </CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle>Project Name</CardTitle>
              <CardDescription>
                <span className="font-black text-xl leading-3 text-green-600">
                  •
                </span>{" "}
                Online
              </CardDescription>
            </CardHeader>
            <CardContent>
              <img
                src="https://via.placeholder.com/200"
                width={200}
                height={200}
                alt="Project Image"
              />
            </CardContent>
          </Card>
        </div>
      </div>
    </>
  );
}
