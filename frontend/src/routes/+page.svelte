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

  let isSideNavOpen = false;

  let open = [false, false];
</script>

<Header company="Precio" platformName="Dashboard" bind:isSideNavOpen>
  <svelte:fragment slot="skip-to-content">
    <SkipToContent />
  </svelte:fragment>
  <SidenavComposite bind:isSideNavOpen />
</Header>

<Content>
  <Grid>
    <Row>
      <Column>
        <h1>Welcome</h1>
      </Column>
    </Row>
  </Grid>
</Content>
<Fab text="+">
  <Button on:click={
	() => {
	  open[0] = true;
	}
  }>Create Project</Button>
  <Button>Import Project</Button>
</Fab>

<Modal
  bind:open={open[0]}
  modalHeading="New Project"
  primaryButtonText="Save"
  secondaryButtonText="Cancel"
  onRequestClose={() => (open = false)}
  onRequestSubmit={() => (open = false)}
>
  <TextInput
	id="test2"
	invalidText="A valid value is required"
	labelText="Text Input label"
	placeholder="Placeholder text"
  />
</Modal>



<style>
  :global(*) {
    box-sizing: border-box;
  }
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: "Open Sans", sans-serif;
    width: 100%;
  }
</style>
