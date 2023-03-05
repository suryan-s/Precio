//stores
import { writable } from 'svelte/store';
import {customAlphabet} from "nanoid";


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

export const newProject = createNewProject();

export function fetchStore (url) {
	const loading = writable(false)
	const error = writable(false)
	const data = writable([[]])
	
	async function get() {
		loading.set(true)
		error.set(false)
		try {
			const response = await fetch(url).then(r => r.json())
			data.set(JSON.parse(response[0]))
			console.log(response[0])
		} catch(e) {
			error.set(e)
		}
		loading.set(false)
	}
	
	get()
	
	return [ data, loading, error, get]
}

