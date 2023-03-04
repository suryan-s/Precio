//stores
import { writable } from 'svelte/store';
import {customAlphabet} from "nanoid";

export const newProject = writable({
    id: customAlphabet("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 10)(),
	name: "",
	type: "Arable",
	available: "",
	stationParameters: [],
	pmsParameters: [],
});
