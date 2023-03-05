<script>
    import "@carbon/styles/css/styles.css";
    import "carbon-components-svelte/css/g100.css";
 import "@carbon/charts/styles.css";
 import {onMount} from "svelte";

    import {    Header,
    SkipToContent,} from "carbon-components-svelte";

    import {isSideNavOpen} from "../stores.js";
    onMount(async() => {
        document.documentElement.setAttribute('theme', 'g100');
    });
</script>

<Header company="Precio" platformName="Dashboard" bind:isSideNavOpen = {$isSideNavOpen}>
    <svelte:fragment slot="skip-to-content">
      <SkipToContent />
    </svelte:fragment>
  </Header>
 
  <slot/>