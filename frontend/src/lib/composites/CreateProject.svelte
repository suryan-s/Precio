<script>
  import {
    TextInput,
    Select,
    SelectItem,
    RadioButtonGroup,
    RadioButton,
    Checkbox,
  } from "carbon-components-svelte";

  export let disabled = true;
  import { newProject } from "../stores.js";

  const stationParameters = [
    "Temperature",
    "Humidity",
    "Pressure",
    "Wind",
    "Light",
    "UV",
    "Rain",
    "Battery Status",
  ];
  const pmsParameters = ["Soil Moisture", "Soil Temperature/Humidity"];
  $: console.log(JSON.stringify($newProject));
  $: if (
    $newProject.name.trim() === "" ||
    $newProject.type.trim() === "" ||
    $newProject.available.trim() === "" ||
    [...$newProject.stationParameters, ...$newProject.pmsParameters].length === 0||
	["Organic", "Horticulture", "Aquaponics", "Vertical Farming"].includes($newProject.type)||
	["Actuators"].includes($newProject.available)
  ) {
	disabled = true;
  } else {
	disabled = false;
  }
</script>

<TextInput
  id="CreateName"
  invalidText="A valid value is required"
  labelText="Project Name"
  placeholder="A Cool Project"
  bind:value={$newProject.name}
/>
<br />
<Select
  labelText="Project Type"
  on:change={(e) => ($newProject.type = e.target.value)}
>
  <SelectItem value="Arable" />
  <SelectItem value="Hydroponics" />
  <SelectItem value="Organic" />
  <SelectItem value="Horticulture" />
  <SelectItem value="Aquaponics" />
  <SelectItem value="Vertical Farming" />
  <!-- <SelectItem value="Other" /> -->
</Select>
<br />

<p class="bx--label">Do you have a weather station or PMS?</p>

<RadioButtonGroup
  name="radio-button-group"
  value="Weather Station"
  bind:selected={$newProject.available}
>
  <RadioButton value="Weather Station" labelText="Weather Station" />
  <RadioButton value="PMS" labelText="PMS" />
  <RadioButton value="Actuators" labelText="Actuators" />
</RadioButtonGroup>
<br />
{#if $newProject.available === "Weather Station"}
  <!-- loop over station stationParameters -->
  <p class="bx--label">Select the parameters you want to track</p>
  <div style="display:flex; flex-wrap: wrap;">
    {#each stationParameters as parameter}
      <Checkbox
        bind:group={$newProject.stationParameters}
        labelText={parameter}
        value={parameter}
      />
    {/each}
  </div>
{/if}
{#if $newProject.available === "PMS"}
  <!-- loop over pmsParameters -->
  <p class="bx--label">Select the parameters you want to track</p>
  <div style="display:flex; flex-wrap: wrap;">
    {#each pmsParameters as parameter}
      <Checkbox
        bind:group={$newProject.pmsParameters}
        labelText={parameter}
        value={parameter}
      />
    {/each}
  </div>
{/if}
