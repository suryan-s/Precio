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
import { Link } from "wouter";
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

export default ProjectCard;
