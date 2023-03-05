<script>
      import "carbon-components-svelte/css/g100.css";
  
    import {    Header,
    SkipToContent,} from "carbon-components-svelte";

    import {isSideNavOpen} from "$lib/stores.ts";

</script>

<Header company="Precio" platformName="Dashboard" bind:isSideNavOpen = {$isSideNavOpen}>
    <svelte:fragment slot="skip-to-content">
      <SkipToContent />
    </svelte:fragment>
  </Header>
 
  <slot/>