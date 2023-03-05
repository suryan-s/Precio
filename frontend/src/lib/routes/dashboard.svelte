<script>
   import {location} from 'svelte-spa-router';

    
    import { Content, Grid, Row, Column } from "carbon-components-svelte";
    import { LineChart } from "@carbon/charts-svelte";
    import { onMount } from "svelte";
    let query = $location.slice(1);
    let graphData;
      let gaugeData;
    onMount(async () => {
      graphData = await fetch("http://127.0.0.1:8000/api/getLineGraph/"+query).then((res) =>
        res.json()
      );
      console.log(graphData); 
      gaugeData = await fetch("http://127.0.0.1:8000/api/getGauge/"+query).then((res) =>
        res.json()
      );
      console.log(gaugeData);
    });
  
  </script>
  
  <Content>
    <Grid>
      <Row>
        <Column>
          
        </Column>
      </Row>
      <Row>
        <Column>
          
        </Column>
      </Row>
    </Grid>
  </Content>
  