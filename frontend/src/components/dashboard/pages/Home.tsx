import { useLocalStorage } from "usehooks-ts";
import { useEffect } from "react";
import { useLocation, Link } from "wouter";
import { useFetchWithToken } from "@/lib/auth/utils";
import { useProjectStore } from "@/lib/stores/projectStore";

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

import { MoreVerticalIcon, Settings2, Trash } from "lucide-react";

import Navbar from "@/components/dashboard/Navbar";
import AddProject from "@/components/dashboard/AddProject";

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
    <Card className="hover:shadow-lg relative transition-shadow duration-300 ease-in-out">
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
          className="rounded-sm object-cover w-full h-[200px]"
          src={image}
          // width={200}
          height={200}
          alt={`Image for ${name}`}
        />
      </CardContent>
    </Card>
  );
};

export default function Home() {
  const [token] = useLocalStorage<string | null>("token", null);
  const [__, setLocation] = useLocation();
  const [projectStore, setProjectStore] = useProjectStore((state) => [
    state.projectStore,
    state.setProjectStore,
  ]);

  useEffect(() => {
    if (token === null) {
      setLocation("/Login");
    }
  }, [token]);
  const [error, data, loading] = useFetchWithToken<{
    status: number;
    result: Array<[string, string]>;
  }>("api/getTableNames");
  useEffect(() => {
    if (data) {
      setProjectStore(data);
    }
  }, [data]);
  console.log(error, data);
  return (
    <>
      <Navbar />
      <div className="flex flex-col p-6 px-6 md:px-12 bg-zinc-100 min-h-[calc(100vh-5rem)]">
        <h1 className="text-4xl font-bold">Projects</h1>
        <div className="mt-8 grid gap-8 grid-automatic">
          {projectStore ? (
            projectStore.result.map(([name, id]) => (
              <ProjectCard
                name={name}
                status="offline"
                image={`https://picsum.photos/200?random=${id}`}
                key={id}
              />
            ))
          ) : (
            <div className="flex flex-col items-center justify-center w-full">
              <h1 className="text-4xl font-bold">No Projects</h1>
              <p className="text-gray-500">
                Create a new project to get started!
              </p>
            </div>
          )}
        </div>
        <AddProject />
      </div>
    </>
  );
}
