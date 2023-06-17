import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Icons } from "@/components/icons";
import { AlertCircle } from "lucide-react";
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";
import { useState, HTMLAttributes, SyntheticEvent } from "react";
import { useLocation } from "wouter";
import { Link } from "@/components/ui/Link";
import { useLocalStorage } from "usehooks-ts";
import { apiUrlBase } from "@/lib/config";
interface UserAuthFormProps extends HTMLAttributes<HTMLDivElement> {}

interface ResponseType {
  access_token: string;
  token_type: string;
}
interface ResponseRegisterType {
  status: number;
  access_token: string;
  token_type: string;
}
/**
 * Login form component
 */

export function LoginForm({ className, ...props }: UserAuthFormProps) {
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [_, setLocation] = useLocation();
  const [error, setError] = useState<string | null>(null);
  const [__, setToken] = useLocalStorage<string | null>("token", null);

  /**
   * Function to log in a user using the API in login form
   */
  async function onSubmit(event: SyntheticEvent) {
    event.preventDefault();
    setIsLoading(true);
    const data = new URLSearchParams({
      username: (document.getElementById("username") as HTMLInputElement).value,
      password: (document.getElementById("password") as HTMLInputElement).value,
    });
    let response: Response | undefined;
    try {
      response = await fetch(apiUrlBase + "auth/login", {
        method: "POST",
        body: data,
      });
    } catch (e) {
      console.log("Error connecting to server");
      setError("Error connecting to server");
      setIsLoading(false);
    }
    const json: ResponseType = await response?.json();
    if (response?.status === 200) {
      console.log("User logged in successfully.");
      setToken(json.access_token);
      setLocation("/");
    } else if (response?.status === 401) {
      setError("Invalid username or password.");
    } else {
      setError("An error occurred in the server.");
    }
    setIsLoading(false);
  }

  return (
    <div className={cn("grid gap-6", className)} {...props}>
      <form onSubmit={onSubmit}>
        <div className="grid gap-2">
          <div className="grid gap-1">
            <Label className="sr-only" htmlFor="email">
              Email
            </Label>
            <Input
              id="username"
              placeholder="Your Username"
              autoCapitalize="none"
              autoComplete="username"
              autoCorrect="off"
              required
              disabled={isLoading}
            />
            <Label className="sr-only" htmlFor="password">
              Password
            </Label>
            <Input
              id="password"
              placeholder="*****************"
              type="password"
              required
              autoComplete="current-password"
              disabled={isLoading}
            />
          </div>
          <Button disabled={isLoading}>
            {isLoading && (
              <Icons.spinner className="mr-2 h-4 w-4 animate-spin" />
            )}
            Log In
          </Button>
        </div>
        {error && (
          <Alert variant="destructive" className="mt-8">
            <AlertCircle className="h-4 w-4" />
            <AlertTitle>Error</AlertTitle>
            <AlertDescription>{error}</AlertDescription>
          </Alert>
        )}
      </form>
      <div className="relative">
        <div className="absolute inset-0 flex items-center">
          <span className="w-full border-t" />
        </div>
      </div>
      <Link
        className="underline text-zinc-700 underline-offset-4 hover:text-primary text-center"
        href="/signup"
      >
        Or Sign Up instead
      </Link>
    </div>
  );
}

export function SignupForm({ className, ...props }: UserAuthFormProps) {
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [_, setLocation] = useLocation();
  const [error, setError] = useState<string | null>(null);
  const [__, setToken] = useLocalStorage<string | null>("token", null);

  async function onSubmit(event: SyntheticEvent) {
    event.preventDefault();
    setIsLoading(true);
    let response: Response | undefined;
    try {
      response = await fetch(apiUrlBase + "auth/register", {
        method: "POST",
        body: JSON.stringify({
          username: (document.getElementById("username") as HTMLInputElement)
            .value,
          password: (document.getElementById("password") as HTMLInputElement)
            .value,
          email: (document.getElementById("email") as HTMLInputElement).value,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      });
    } catch (e) {
      console.log("Error connecting to server");
      setError("Error connecting to server");
      setIsLoading(false);
    }
    const data: ResponseRegisterType = await response?.json();
    if (data.status === 200) {
      console.log("User created successfully.");
      setToken(data.access_token);
      setLocation("/");
    } else if (data.status === 409) {
      setError("Username already exists.");
    } else {
      setError("An error occurred in the server.");
    }
    setIsLoading(false);
  }

  return (
    <div className={cn("grid gap-6", className)} {...props}>
      <form onSubmit={onSubmit}>
        <div className="grid gap-2">
          <div className="grid gap-1">
            <Label className="sr-only" htmlFor="username">
              Username
            </Label>
            <Input
              id="username"
              placeholder="Your Username"
              autoCapitalize="none"
              autoComplete="username"
              autoCorrect="off"
              required
              disabled={isLoading}
            />

            <Label className="sr-only" htmlFor="email">
              Email
            </Label>
            <Input
              id="email"
              placeholder="name@example.com"
              type="email"
              autoCapitalize="none"
              autoComplete="email"
              autoCorrect="off"
              required
              disabled={isLoading}
            />
            <Label className="sr-only" htmlFor="password">
              Password
            </Label>
            <Input
              id="password"
              placeholder="*****************"
              type="password"
              required
              autoComplete="new-password"
              disabled={isLoading}
            />
          </div>
          <Button disabled={isLoading}>
            {isLoading && (
              <Icons.spinner className="mr-2 h-4 w-4 animate-spin" />
            )}
            Sign Up
          </Button>
        </div>
        {error && (
          <Alert variant="destructive" className="mt-8">
            <AlertCircle className="h-4 w-4" />
            <AlertTitle>Error</AlertTitle>
            <AlertDescription>{error}</AlertDescription>
          </Alert>
        )}
      </form>
      <div className="relative">
        <div className="absolute inset-0 flex items-center">
          <span className="w-full border-t" />
        </div>
      </div>
      <Link
        className="underline text-zinc-700 underline-offset-4 hover:text-primary text-center"
        href="/login"
      >
        Or Log In instead
      </Link>
    </div>
  );
}
