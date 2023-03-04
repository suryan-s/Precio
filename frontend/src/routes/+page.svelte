<script>
  import Fab from "$lib/components/Fab.svelte";
  import "@fontsource/open-sans";
  import "carbon-components-svelte/css/g100.css";
  import SidenavComposite from "../lib/composites/Sidenav.svelte";
  import {
    Header,
    SkipToContent,
    Content,
    Grid,
    Row,
    Column,
    Modal,
    TextInput,
    Button,
  } from "carbon-components-svelte";

  import CreateProject from "../lib/composites/CreateProject.svelte";

  let isSideNavOpen = false;

  let open = [false, false];
  let disabled = [true, true];
</script>

<Header company="Precio" platformName="Dashboard" bind:isSideNavOpen>
  <svelte:fragment slot="skip-to-content">
    <SkipToContent />
  </svelte:fragment>
</Header>
<SidenavComposite bind:isSideNavOpen />

<Content>
  <Grid>
    <Row>
      <Column>
        <h1>Welcome!</h1>
      </Column>
    </Row>
  </Grid>
</Content>

<Fab text="+">
  <Button on:click={
	() => {
	  open[0] = !open[0];
	}
  }>Create Project</Button>
  <Button>Import Project</Button>
</Fab>

<Modal

  bind:open={open[0]}
  modalHeading="New Project"
  primaryButtonText="Save"
  secondaryButtonText="Cancel"
  selectorPrimaryFocus="#CreateName"
  hasScrollingContent
  onRequestClose={() => (open = false)}
  onRequestSubmit={() => (open = false)}
  primaryButtonDisabled={disabled[0]}
  on:click:button--secondary={() => (open = false)}

>
 <CreateProject bind:disabled={disabled[0]} />
</Modal>



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
