import {
  Popover,
  PopoverTrigger,
  PopoverContent,
} from "@/components/ui/popover";
import { Plus } from "lucide-react";
import { Button } from "../ui/button";

const AddProject = () => {
  return (
    <Popover>
      <PopoverTrigger
        title="Add new..."
        className="absolute bg-primary bottom-6 right-6 text-white hover:outline outline-1 rounded-full p-4"
      >
        <Plus size={25} />
      </PopoverTrigger>
      <PopoverContent className="flex flex-col gap-4">
        <Button className="w-full">Import project</Button>
        <Button className="w-full">Create new project</Button>
      </PopoverContent>
    </Popover>
  );
};

export default AddProject;
