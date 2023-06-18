import { useLocalStorage } from "usehooks-ts";
import { Button } from "@/components/ui/button";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import { Command, User, Settings } from "lucide-react";
const UserControls = () => {
  const [_t, setToken] = useLocalStorage<string | null>("token", null);
  return (
    <div className="flex flex-col gap-2">
      <Button
        onClick={() => {
          setToken(null);
        }}
      >
        Logout
      </Button>
    </div>
  );
};
const Navbar = () => {
  return (
    <header className="sticky z-50">
      <nav className="flex items-center justify-between flex-wrap bg-primary p-4 px-6 md:px-12">
        <div className="flex items-center flex-shrink-0 text-white mr-6">
          <Command className="mr-2 h-7 w-7" />
          <span className="font-semibold text-xl tracking-tight">Precio</span>
        </div>
        <div className="flex items-center flex-shrink-0 text-white gap-6">
          <Popover>
            <PopoverTrigger
              title="Your account"
              className="text-white hover:bg-slate-800 transition-colors rounded-sm p-3"
            >
              <User />
            </PopoverTrigger>
            <PopoverContent>
              <UserControls />
            </PopoverContent>
          </Popover>
          <Popover>
            <PopoverTrigger
              title="Settings"
              className="text-white hover:bg-slate-800 transition-colors rounded p-3"
            >
              <Settings />
            </PopoverTrigger>
            <PopoverContent>Settings Controls</PopoverContent>
          </Popover>
        </div>
      </nav>
    </header>
  );
};

export default Navbar;
