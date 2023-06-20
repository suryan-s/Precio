import { useLocalStorage } from "usehooks-ts";
import { useEffect, useState } from "react";
import { useLocation } from "wouter";
import { useFetchWithToken } from "@/lib/auth/utils";
import { useProjectStore } from "@/lib/stores/projectStore";

import Navbar from "@/components/dashboard/Navbar";
import AddProject from "@/components/dashboard/AddProject";
import ProjectCard, {
  ProjectCardSkeleton,
} from "@/components/dashboard/ProjectCard";
import { useTour } from "@reactour/tour";

export default function Home() {
  const [token] = useLocalStorage<string | null>("token", null);
  const [__, setLocation] = useLocation();
  const { setIsOpen } = useTour();
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
    if (data && data.status === 200) {
      setProjectStore(data);
    }
    if (data?.result.length === 0) {
      setIsOpen(true);
    }
  }, [data]);
  console.log(error, data);

  return (
    <>
      <Navbar />
      <div className="flex flex-col p-6 px-6 md:px-12 bg-zinc-100 min-h-[calc(100vh-5rem)]">
        <h1 className="text-4xl font-bold">Projects</h1>
        <div className="mt-8 grid gap-8 grid-automatic">
          {projectStore.result.length > 0 ? (
            projectStore.result.map(([name, id]) => (
              <ProjectCard
                name={name}
                status="offline"
                image={`https://picsum.photos/200?random=${id}`}
                key={id}
                id={id}
              />
            ))
          ) : loading ? (
            <>
              <ProjectCardSkeleton />
              <ProjectCardSkeleton />
              <ProjectCardSkeleton />
            </>
          ) : (
            <div className="absolute flex flex-col items-center justify-center inset-0">
              <p className="text-2xl font-bold">No projects found!</p>
              <p className="text-lg">
                Add a project to get started with your dashboard.
              </p>
            </div>
          )}
        </div>
        <AddProject />
      </div>
    </>
  );
}
