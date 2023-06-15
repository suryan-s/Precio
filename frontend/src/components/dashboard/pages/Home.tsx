import { useLocalStorage } from "usehooks-ts";
import { useEffect } from "react";
import { useLocation } from "wouter";
import { Button } from "@/components/ui/button";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";
import { Command, User, Settings } from "lucide-react";

function UserControls() {
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
}
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
      <header>
        <nav className="flex items-center justify-between flex-wrap bg-primary p-4 px-6 md:px-12">
          <div className="flex items-center flex-shrink-0 text-white mr-6">
            <Command className="mr-2 h-7 w-7" />
            <span className="font-semibold text-xl tracking-tight">Precio</span>
          </div>
          <div className="flex items-center flex-shrink-0 text-white gap-6">
            <Popover>
              <PopoverTrigger className="text-white hover:outline outline-1 rounded-sm p-3">
                <User />
              </PopoverTrigger>
              <PopoverContent>
                <UserControls />
              </PopoverContent>
            </Popover>
            <Popover>
              <PopoverTrigger className="text-white hover:outline outline-1 rounded p-3">
                <Settings />
              </PopoverTrigger>
              <PopoverContent>Settings Controls</PopoverContent>
            </Popover>
          </div>
        </nav>
      </header>
    </>
  );
}
