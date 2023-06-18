import { create } from "zustand";

interface ProjectStore {
  status: number;
  result: Array<[string, string]>;
}

export const useProjectStore = create<{
  projectStore: ProjectStore;
  setProjectStore: (projectStore: ProjectStore) => void;
  addProject: (project: [string, string]) => void;
}>()((set) => ({
  projectStore: {
    status: 0,
    result: [],
  },
  setProjectStore: (projectStore) => set({ projectStore }),
  addProject: (project) =>
    set((state) => ({
      projectStore: {
        status: state.projectStore.status,
        result: [...state.projectStore.result, project],
      },
    })),
}));
