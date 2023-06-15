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

interface ProjectCardProps {
  name: string;
  status: "online" | "offline";
  image: string;
}
const ProjectCard = ({ name, status, image }: ProjectCardProps) => {
  return (
    <Card>
      <CardHeader>
        <CardTitle>{name}</CardTitle>
        <CardDescription>
          {status === "online" && (
            <>
              <span className="font-black text-xl leading-3 text-green-600">
                •
              </span>
              Online
            </>
          )}
          {status === "offline" && (
            <>
              <span className="font-black text-xl leading-3 text-gray-600">
                •
              </span>
              Offline
            </>
          )}
        </CardDescription>
      </CardHeader>
      <CardContent>
        <img src={image} width={200} height={200} alt="Project Image" />
      </CardContent>
    </Card>
  );
};

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
      <div className="flex flex-col p-6 px-6 md:px-12 bg-slate-100 min-h-[calc(100vh-5rem)]">
        <h1 className="text-4xl font-bold">Projects</h1>
        <div className="mt-8 flex flex-wrap gap-8">
          <ProjectCard
            name="Project Name"
            status="offline"
            image="https://via.placeholder.com/200"
          />
          <ProjectCard
            name="Project Name"
            status="online"
            image="https://via.placeholder.com/200"
          />
        </div>
      </div>
    </>
  );
}
