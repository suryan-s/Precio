import Home from "./Home.svelte";
import Dashboard from "./dashboard.svelte";

export default {
    // Exact path
    '/': Home,

    // Using named parameters, with last being optional
    '/:id': Dashboard,
}
