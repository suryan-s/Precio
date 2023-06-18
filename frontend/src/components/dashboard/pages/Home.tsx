import { useLocalStorage } from "usehooks-ts";
import { useEffect } from "react";
import { useLocation } from "wouter";
import { useFetchWithToken } from "@/lib/auth/utils";
import { useProjectStore } from "@/lib/stores/projectStore";

import Navbar from "@/components/dashboard/Navbar";
import AddProject from "@/components/dashboard/AddProject";
import ProjectCard from "@/components/dashboard/ProjectCard";

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
