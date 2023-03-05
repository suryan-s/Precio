<script>
    export let isSideNavOpen = false;
    import {
        SideNav,
    SideNavItems,
    SideNavMenu,
    SideNavMenuItem,
    SideNavLink,
    SideNavDivider
    } from "carbon-components-svelte";
</script>


<SideNav bind:isOpen={isSideNavOpen} style="padding:1rem;">
  <p>
    <a href="https://github.com/suryan-s/precio">Precio</a> is a comprehensive solution designed to assist modern farmers in optimizing their agricultural operations by incorporating precision farming practices. This document serves as a guide for developers and users of Precio, providing information on the project's features, functionality, and usage.

  </p>
  </SideNav>
