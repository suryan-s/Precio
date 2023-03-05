<script>
  import Fab from "$lib/components/Fab.svelte";


  import {

    Content,
    Grid,
    Row,
    Column,
    Modal,
    TextInput,
    Button,
	Tile,
  } from "carbon-components-svelte";
  import SidenavComposite from "$lib/composites/Sidenav.svelte";

  import CreateProject from "$lib/composites/CreateProject.svelte";
  import {newProject,fetchStore} from "$lib/stores.ts";
  import { text } from "svelte/internal";
  import {isSideNavOpen} from "$lib/stores.ts";
 
  

  let open = [false, false];
  let disabled = [true, true];

  const closeCreateModal = () => {
	open[0] = false;
	newProject.reset();
  };


  const [data,loadng, error, get] = fetchStore('/api/getProjects');


</script>


<SidenavComposite bind:isSideNavOpen = {$isSideNavOpen} />

<Content>
  <Grid>
    <Row>
      <Column>
        <h1>Precio Dashboard</h1>
      </Column>
	 </Row>
	 {#if $data}
	 <Row>
		<Column>
	   <h3 style="padding: 2rem 0;">Projects</h3>
	   {#each $data[0] as projectName}
	  	<Tile style="display:flex; justify-content: space-between;">
			<div>
				<h4>{projectName}</h4>
			<p>Status : <span style="color:green">Active</span></p>
			</div>
			<div>
			<Button kind="primary" href="/project/{projectName}">View</Button>
			<Button kind="danger">Delete</Button>		
			</div>
		</Tile>
	   {/each}
	</Column>
	</Row>
	{/if}
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
  selectorPrimaryFocus="#CreateName"
  hasScrollingContent
  onRequestClose={closeCreateModal}
  onRequestSubmit={closeCreateModal}
  primaryButtonDisabled={disabled[0]}
  on:click:button--secondary={closeCreateModal}
  on:submit={() =>{
	disabled[0] = true;
	fetch('/api/createProject', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify($newProject)
	})
	.then(response => response.text())
	.then(text => {
		console.log(text);
		get();
		closeCreateModal();
	})
  }}


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
