<script>
  export let data;
  
  import { Content, Grid, Row, Column } from "carbon-components-svelte";
  import { LineChart } from "@carbon/charts-svelte";
  import { onMount } from "svelte";
    let graphData;
    let gaugeData;
  onMount(async () => {
    graphData = await fetch("http://127.0.0.1:8000/api/getLineGraph/"+data.slug).then((res) =>
      res.json()
    );
    console.log(graphData); 
    gaugeData = await fetch("http://127.0.0.1:8000/api/getGauge/"+data.slug).then((res) =>
      res.json()
    );
    console.log(gaugeData);
  });

</script>

<Content>
  <Grid>
    <Row>
      <Column>
        <h1>{data.slug}</h1>
      </Column>
    </Row>
    <Row>
      <Column>
        
      </Column>
    </Row>
  </Grid>
</Content>
