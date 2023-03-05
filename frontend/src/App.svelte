<script>

 
  import Router from 'svelte-spa-router'
  import routes from './lib/routes/routes.js'
  import Layout from './lib/composites/Layout.svelte';
</script>
<Layout>
  <Router {routes} style="width:100%;height:100%;display:block;" />
</Layout>


<style>
  :global(*) {
    box-sizing: border-box;
  }
  :global(body) {
    margin: 0;
    padding: 0;
	font-family: 'IBM Plex Sans', 'Helvetica Neue', Arial, sans-serif;
    width: 100%;
  }
</style>
