import {
  AlertDialog,
  AlertDialogTrigger,
  AlertDialogContent,
  AlertDialogTitle,
  AlertDialogDescription,
  AlertDialogAction,
  AlertDialogCancel,
} from "@/components/ui/alert-dialog";
import {
  Popover,
  PopoverTrigger,
  PopoverContent,
} from "@/components/ui/popover";
import { MoreVerticalIcon, Settings2, Trash } from "lucide-react";
import { Link, useLocation } from "wouter";
import {
  AlertDialogHeader,
  AlertDialogFooter,
} from "@/components/ui/alert-dialog";
import { Button, buttonVariants } from "@/components/ui/button";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card";
import { Skeleton } from "@/components/ui/skeleton";

import { Icons } from "@/components/icons";
import { fetchWithToken } from "@/lib/auth/utils";
import { useCallback, useState } from "react";
import { useProjectStore } from "@/lib/stores/projectStore";

export const ProjectCardSkeleton = () => {
  return (
    <div className="flex flex-col items-center gap-5">
      <Skeleton className="w-full h-6 rounded-sm bg-slate-300" />
      <Skeleton className="w-full h-6 rounded-sm bg-slate-300" />
      <Skeleton className="w-full h-48 rounded-sm bg-slate-300" />
    </div>
  );
};

interface ProjectCardProps {
  name: string;
  status: "online" | "offline";
  image: string;
  id: string;
}
/**
 * Project Card Component
 * @prop `name` Project Name
 * @prop `status` Project Status (online/offline)
 * @prop `image` Project Image URL
 */
const ProjectCard = ({ name, status, image, id }: ProjectCardProps) => {
  const [loading, setLoading] = useState(false);
  const [open, setOpen] = useState(false);
  const removeProject = useProjectStore((state) => state.removeProject);
  const [, setLocation] = useLocation();
  const deleteHandler = useCallback(
    async (e: React.MouseEvent<HTMLButtonElement, MouseEvent>) => {
      e.preventDefault();
      setLoading(true);
      await fetchWithToken(`api/deleteProject/${id}`, {
        method: "POST",
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.status === 200) {
            setOpen(false);
            removeProject([name, id]);
          }
        })
        .catch((err: Error) => {
          console.error(err);
          if (
            err.message === "Token expired" ||
            err.message === "No token found"
          ) {
            setLocation("/Login");
          }
        });

      setLoading(false);
    },
    [id, name, removeProject]
  );
  return (
    <Card className="hover:shadow-lg relative transition-shadow duration-300 ease-in-out">
      <Link href={`/${encodeURIComponent(id)}`}>
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
          <AlertDialog open={open} onOpenChange={setOpen}>
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
                  onClick={deleteHandler}
                >
                  {loading ? (
                    <Icons.spinner className="animate-spin" />
                  ) : (
                    "Delete"
                  )}
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

export default ProjectCard;
