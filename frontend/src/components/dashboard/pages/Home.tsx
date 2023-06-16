import { useLocalStorage } from "usehooks-ts";
import { useEffect } from "react";
import { useLocation, Link } from "wouter";

import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Button, buttonVariants } from "@/components/ui/button";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog";

import { Plus, MoreVerticalIcon, Settings2, Trash } from "lucide-react";

import Navbar from "@/components/dashboard/Navbar";

interface ProjectCardProps {
  name: string;
  status: "online" | "offline";
  image: string;
}
/**
 * Project Card Component
 * @prop `name` Project Name
 * @prop `status` Project Status (online/offline)
 * @prop `image` Project Image URL
 */
const ProjectCard = ({ name, status, image }: ProjectCardProps) => {
  return (
    <Card className="w-64 hover:shadow-lg relative transition-shadow duration-300 ease-in-out">
      <Link href={`/${encodeURIComponent(name)}`}>
        <CardHeader className="flex flex-col pb-5 cursor-pointer">
          <CardTitle className="break-words">{name}</CardTitle>
          <CardDescription>
            {status === "online" && (
              <>
                <span className="font-black text-2xl leading-3 text-green-600">
                  •
                </span>{" "}
                Online
              </>
            )}
            {status === "offline" && (
              <>
                <span className="font-black text-2xl leading-3 text-gray-600">
                  •
                </span>{" "}
                Offline
              </>
            )}
          </CardDescription>
        </CardHeader>
      </Link>
      <Popover>
        <PopoverTrigger className="absolute right-3 top-5 p-1 hover:bg-slate-200 rounded-sm transition-all">
          <MoreVerticalIcon size={20} />
        </PopoverTrigger>
        <PopoverContent className=" flex flex-col gap-4 w-56">
          <Button className="gap-2 justify-evenly">
            <Settings2 size={20} /> Project Settings
          </Button>
          <AlertDialog>
            <AlertDialogTrigger
              className={buttonVariants({
                variant: "destructive",
                class: "gap-2 justify-evenly",
              })}
            >
              <Trash size={20} /> Delete Project
            </AlertDialogTrigger>
            <AlertDialogContent>
              <AlertDialogHeader>
                <AlertDialogTitle>
                  Are you sure you want to delete this project?
                </AlertDialogTitle>
              </AlertDialogHeader>
              <AlertDialogDescription>
                You will not be able to reverse this! Make sure you know what
                you are doing before you proceed.
              </AlertDialogDescription>
              <AlertDialogFooter>
                <AlertDialogAction
                  className={buttonVariants({ variant: "destructive" })}
                >
                  Yes, delete this project
                </AlertDialogAction>
                <AlertDialogCancel>Cancel</AlertDialogCancel>
              </AlertDialogFooter>
            </AlertDialogContent>
          </AlertDialog>
        </PopoverContent>
      </Popover>
      <CardContent className="pt-0">
        <img
          className="rounded-sm"
          src={image}
          width={200}
          height={200}
          alt={`Image for ${name}`}
        />
      </CardContent>
    </Card>
  );
};

const AddProject = () => {
  return (
    <Popover>
      <PopoverTrigger className="absolute bg-primary bottom-6 right-6 text-white hover:outline outline-1 rounded-full p-4">
        <Plus size={25} />
      </PopoverTrigger>
      <PopoverContent>
        <div />
      </PopoverContent>
    </Popover>
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
      <div className="flex flex-col p-6 px-6 md:px-12 bg-zinc-100 min-h-[calc(100vh-5rem)]">
        <h1 className="text-4xl font-bold">Projects</h1>
        <div className="mt-8 flex flex-wrap gap-8">
          <ProjectCard
            name="Project Name"
            status="offline"
            image="https://picsum.photos/200"
          />
          <ProjectCard
            name="Project Name"
            status="online"
            image="https://picsum.photos/200?random=1"
          />
        </div>
        <AddProject />
      </div>
    </>
  );
}
