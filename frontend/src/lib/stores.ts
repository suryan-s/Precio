//stores
import { Writable, writable } from 'svelte/store';
import {customAlphabet} from "nanoid";

interface Project {
	id: string;
	name: string;
	type: string;
	available: string;
	stationParameters: string[];
	pmsParameters: string[];
}

function createNewProject() {
	const { subscribe, set, update } = writable({
		id: customAlphabet("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 10)(),
		name: "",
		type: "Arable",
		available: "",
		stationParameters: [],
		pmsParameters: [],
	});

	return {
		subscribe,
		set,
		update,
		reset: () => {
			set({
				id: customAlphabet("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 10)(),
				name: "",
				type: "Arable",
				available: "",
				stationParameters: [],
				pmsParameters: [],
			});
		},
	};
}

export const newProject : Writable<Project> = createNewProject();
