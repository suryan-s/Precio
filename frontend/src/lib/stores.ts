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

export const isSideNavOpen = writable(false);

export const newProject : Writable<Project> = createNewProject();

export function fetchStore (url:string) {
	const loading = writable(false)
	const error = writable(false)
	const data = writable([[]])
	
	async function get() {
		loading.set(true)
		error.set(false)
		try {
			const response = await fetch(url)
			data.set(await response.json())
		} catch(e) {
			error.set(e)
		}
		loading.set(false)
	}
	
	get()
	
	return [ data, loading, error, get]
}