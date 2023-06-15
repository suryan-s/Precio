import { lazy, Suspense } from "react";
import { Command } from "lucide-react";
const Quote = lazy(() => import("@/components/ui/quotes"));

export default function PrettyWrapper({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <>
      <div className="container relative h-screen flex-col items-center justify-center grid lg:max-w-none lg:grid-cols-2 lg:px-0">
        <div className="relative hidden h-full flex-col bg-muted p-10 text-white dark:border-r lg:flex">
          <div
            className="absolute inset-0 bg-cover"
            style={{
              backgroundImage:
                "url(https://images.unsplash.com/photo-1599138900450-3d06e89ad309?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&fm=jpg&w=1080&fit=max), linear-gradient(315deg, rgba(13,28,25,1) 0%, rgba(39,64,40,1) 23%, rgba(79,93,40,1) 50%, rgba(23,80,38,1) 100%)",
            }}
          />
          <div className="relative z-20 flex items-center text-lg font-medium">
            <Command className="mr-2 h-8 w-8" /> <p className="text-2xl">Precio</p>
          </div>
          <Suspense fallback={<div>Loading...</div>}>
            <Quote />
          </Suspense>
        </div>
        <div className="lg:p-8">
          <div className="mx-auto flex w-full flex-col justify-center space-y-6 sm:w-[350px]">
            {children}
            <p className="px-8 text-center text-sm text-muted-foreground">
              By clicking continue, you agree to our{" "}
              <a
                href="/terms"
                className="underline underline-offset-4 hover:text-primary"
              >
                Terms of Service
              </a>{" "}
              and{" "}
              <a
                href="/privacy"
                className="underline underline-offset-4 hover:text-primary"
              >
                Privacy Policy
              </a>
              .
            </p>
          </div>
        </div>
      </div>
    </>
  );
}
