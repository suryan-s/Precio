<script>
      import Fab from "../components/Fab.svelte";


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
import SidenavComposite from "../composites/Sidenav.svelte";

import CreateProject from "../composites/CreateProject.svelte";
import {newProject,fetchStore} from "../stores.js";
import { text } from "svelte/internal";
import {isSideNavOpen} from "../stores.js";
let open = [false, false];
  let disabled = [true, true];
  let deleteOpen = false;
  let deleteEl = "";
  
  const closeCreateModal = () => {
	open[0] = false;
	newProject.reset();
  };



  const [data,loadng, error, get] = fetchStore('http://127.0.0.1:8000/api/getTableNames');

</script>

<SidenavComposite bind:isSideNavOpen = {$isSideNavOpen} />

<Content>
  <Grid>
    <Row>
      <Column>
        <img src="./precio.png" style="width:100%;max-width:400px;text-align:center;" alt="logo" />
      </Column>
	 </Row>
	 {#if $data}
	 <Row>
		<Column>
	   <h3 style="padding: 2rem 0;">Projects</h3>
	   {#each $data as projectName}
	  	<Tile style="display:flex; justify-content: space-between;">
			<div>
				<h4>{projectName[0]}</h4>
			<p>Status : <span style="color:green">Active</span></p>
			</div>
			<div>
			<Button kind="primary" href="#/{projectName}">View</Button>
			<Button kind="danger" on:click={()=>{
				deleteOpen = true;
				deleteEl = projectName[0];
			}}>Delete</Button>		
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
  primaryButtonText="Create"
  secondaryButtonText="Cancel"
  selectorPrimaryFocus="#CreateName"
  hasScrollingContent
  onRequestClose={closeCreateModal}
  onRequestSubmit={closeCreateModal}
  primaryButtonDisabled={disabled[0]}
  on:click:button--secondary={closeCreateModal}
  on:submit={() =>{
	disabled[0] = true;
	fetch('http://127.0.0.1:8000/api/createProject', {
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

<Modal danger bind:open={deleteOpen} modalHeading="Delete Project?" primaryButtonText="Delete"
secondaryButtonText="Cancel"
on:click:button--secondary={() => (deleteOpen = false)}

on:submit={() => {
	  deleteOpen = false;
	  fetch('http://127.0.0.1:8000/api/deleteProject/'+deleteEl, {
		method: 'POST',
	  });
}}	
>
	  <p>Are you sure you want to delete this project?</p>
</Modal>

