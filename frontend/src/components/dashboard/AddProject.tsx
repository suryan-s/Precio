import { useCallback, useState } from "react";
import {
  Popover,
  PopoverTrigger,
  PopoverContent,
} from "@/components/ui/popover";
import { Plus } from "lucide-react";
import { Button, buttonVariants } from "../ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
  DialogFooter,
} from "@/components/ui/dialog";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Icons } from "../icons";

import { fetchWithToken } from "@/lib/auth/utils";
import { useLocation } from "wouter";
import { useProjectStore } from "@/lib/stores/projectStore";

const ImportProject = () => {
  return (
    <Dialog>
      <DialogTrigger className={buttonVariants({ variant: "link" })}>
        Import Project
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Import Project</DialogTitle>
          <DialogDescription>Import Project</DialogDescription>
        </DialogHeader>
        <DialogFooter>
          <Button>Import</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
};
const AddNewProject = () => {
  const [open, setOpen] = useState(false);
  const [loading, setLoading] = useState(false);
  const [selectValue, setSelectValue] = useState<string | undefined>(undefined);
  const [, setLocation] = useLocation();
  const addProject = useProjectStore((state) => state.addProject);
  const submitHandler = useCallback(
    (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault();
      setLoading(true);
      const pname = e.currentTarget.projectName.value;
      const pdesc = e.currentTarget.projectDescription.value;
      const obj = {
        project_name: pname,
        project_description: pdesc,
        project_type: selectValue,
      };
      console.log(JSON.stringify(obj));
      console.log(obj);
      fetchWithToken("api/createProject", {
        method: "POST",
        body: JSON.stringify(obj),
      })
        .then((res) => {
          console.log(res);
          setLoading(false);
          return res.json();
        })
        .then((res) => {
          if (res.status === 401) setLocation("/login");
          addProject([pname, res.project_id]);
        })
        .catch((err) => {
          console.log(err);
          if (err.status === 401) setLocation("/login");
          if (
            err.message === "Token expired" ||
            err.message === "No token found"
          ) {
            localStorage.removeItem("token");
            setLocation("/login");
          }
          setLoading(false);
        });
      setOpen(false);
    },
    [setOpen, setLoading, selectValue]
  );
  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger
        className={buttonVariants({
          variant: "default",
        })}
      >
        Add new project
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>New Project</DialogTitle>
          <DialogDescription>Create a new project</DialogDescription>
        </DialogHeader>
        <form onSubmit={submitHandler}>
          <div className="grid gap-4 py-4">
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="projectName">Project Name*</Label>
              <Input
                id="projectName"
                placeholder="A cool name..."
                minLength={3}
                className="col-span-3"
                required
              />
            </div>
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="projectDescription" className="leading-5">
                Project Description
              </Label>
              <Input
                id="projectDescription"
                placeholder="An amazing project description."
                minLength={3}
                className="col-span-3"
              />
            </div>
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="projectType">Project Type*</Label>
              <Select required onValueChange={setSelectValue}>
                <SelectTrigger className="col-span-3" id="projectType">
                  <SelectValue placeholder="Project Type" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="arable">Arable</SelectItem>
                  <SelectItem value="aquaponics">Aquaponics</SelectItem>
                  <SelectItem value="hydroponics">Hydroponics</SelectItem>
                  <SelectItem value="indoor">Indoor</SelectItem>
                  <SelectItem value="custom">Custom</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>
          <DialogFooter>
            <Button type="submit">
              {loading ? (
                <Icons.spinner className="animate-spin" />
              ) : (
                "Create Project"
              )}
            </Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
};

const AddProject = () => {
  return (
    <Popover>
      <PopoverTrigger
        title="Add new..."
        className="fixed bg-primary bottom-6 right-6 text-white hover:outline outline-1 rounded-full p-4"
      >
        <Plus size={25} />
      </PopoverTrigger>
      <PopoverContent className="flex flex-col gap-4">
        <ImportProject />
        <AddNewProject />
      </PopoverContent>
    </Popover>
  );
};

export default AddProject;
