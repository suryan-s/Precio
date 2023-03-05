<script>
  import { location } from "svelte-spa-router";
  import { LineChart, GaugeChart } from "@carbon/charts-svelte";
    import {
        SideNav,
    SideNavItems,
    SideNavLink,
    } from "carbon-components-svelte";
  import { Content, Grid, Row, Column } from "carbon-components-svelte";
  import { onMount } from "svelte";
  import DashNav from "../composites/DashNav.svelte";

  let query = $location.slice(1);
  let graphData = [];
  let gaugeData;
  let isSideNavOpen = true;

  fetch("http://127.0.0.1:8000/api/getLineGraph/" + query + "/0")
    .then((res) => res.json())
    .then((data) => {
      graphData[0] = JSON.parse(data[0]);
      //now we have the data in the form of an array of objects like this:
      //[['2023-03-05 04:05:54.138481', 33, 28, 33], ['2023-03-05 04:05:54.138481', 33, 28, 33], ['2023-03-05 04:05:54.138481', 33, 28, 33]]...]
      //we need to convert it to an array of objects like this:
      //[{"group":"1",date:"2023-03-05 04:05:54.138481",value:33},{"group":"2",date:"2023-03-05 04:05:54.138481",value:28},{"group":"3",date:"2023-03-05 04:05:54.138481",value:33"},{"group":"1",date:"2023-03-05 04:05:54.138481",value:33},{"group":"2",date:"2023-03-05 04:05:54.138481",value:28},{"group":"3",date:"2023-03-05 04:05:54.138481",value:33"},{"group":"1",date:"2023-03-05 04:05:54.138481",value:33},{"group":"2",date:"2023-03-05 04:05:54.138481",value:28},{"group":"3",date:"2023-03-05 04:05:54.138481",value:33"}]
      //we can do this by using the map function

      graphData[0] = graphData[0].map((item) => {
        return [
          {
            group: "maxTempC",
            date: item[0],
            value: item[1],
          },
          {
            group: "minTempC",
            date: item[0],
            value: item[2],
          },
          {
            group: "tempC",
            date: item[0],
            value: item[3],
          },
        ];
      });
      //now we have an array of arrays of objects, we need to flatten it to an array of objects
      graphData[0] = graphData[0].flat();

      console.log(graphData[0]);
    });

  fetch("http://127.0.0.1:8000/api/getLineGraph/" + query + "/1")
    .then((res) => res.json())
    .then((data) => {
      graphData[1] = JSON.parse(data[0]);
      //now we have the data in the form of an array of objects like this:
      //[['2023-03-05 04:05:54.138481', 33], ['2023-03-05 04:05:54.138481', 33], ['2023-03-05 04:05:54.138481', 33]]...]

      graphData[1] = graphData[1].map((item) => {
        return [
          {
            group: "humidity",
            date: item[0],
            value: item[1],
          },
        ];
      });
      //now we have an array of arrays of objects, we need to flatten it to an array of objects
      graphData[1] = graphData[1].flat();
    });

  fetch("http://127.0.0.1:8000/api/getLineGraph/" + query + "/2")
    .then((res) => res.json())
    .then((data) => {
      graphData[2] = JSON.parse(data[0]);
      //now we have the data in the form of an array of objects like this:
      //[['2023-03-05 04:05:54.138481', 33], ['2023-03-05 04:05:54.138481', 33], ['2023-03-05 04:05:54.138481', 33]]...]

      graphData[2] = graphData[2].map((item) => {
        return [
          {
            group: "precipitation",
            date: item[0],
            value: item[1],
          },
        ];
      });
      //now we have an array of arrays of objects, we need to flatten it to an array of objects
      graphData[2] = graphData[2].flat();
    });

  fetch("http://127.0.0.1:8000/api/getLineGraph/" + query + "/3")
    .then((res) => res.json())
    .then((data) => {
      graphData[3] = JSON.parse(data[0]);
      //now we have the data in the form of an array of objects like this:
      //[['2023-03-05 04:05:54.138481', 33], ['2023-03-05 04:05:54.138481', 33], ['2023-03-05 04:05:54.138481', 33]]...]

      graphData[3] = graphData[3].map((item) => {
        return [
          {
            group: "pressure",
            date: item[0],
            value: item[1],
          },
        ];
      });
      //now we have an array of arrays of objects, we need to flatten it to an array of objects
      graphData[3] = graphData[3].flat();
    });

  fetch("http://127.0.0.1:8000/api/getGauge/" + query)
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      let gauges = JSON.parse(data[0]);
      gauges = Object.entries(gauges).map(([key, value]) => {
        return {
          group: key,
          value: value,
        };
      });
      console.log(gauges);
      gaugeData = gauges.slice(1);
    });
</script>
<SideNav bind:isOpen={isSideNavOpen}>
  <SideNavItems>
    <SideNavLink text="Dashboard" href="#{$location}" style="background:#f6f6f6;"  />
    <SideNavLink text="Insight"/>
    <SideNavLink text="Actions" />
   <p style="position:fixed;bottom:1rem;left:5.5rem">Precio</p>
  </SideNavItems>
  </SideNav>
<Content>
  <Grid>
    <Row>
      <Column>
        <h1 style="margin-bottom:2rem;">Dashboard</h1>
      </Column>
    </Row>

    <Row>
      {#if gaugeData}
        {#each gaugeData as gauge}
          <Column padding>
            <GaugeChart
              data={[
                {
                  group: "value",
                  value:
                    gauge.group === "pressure" ? gauge.value / 10 : gauge.value,
                },
              ]}
              options={{
                title: gauge.group,
                theme: "g100",
                resizable: true,
                height: "250px",
                width: "250px",
                gauge: {
                  showPercentageSymbol: false,
                  status: "warning",
                  type: "full",
                },
              }}
            />
          </Column>
        {/each}
      {/if}
    </Row>
    <br />
    <div>
    <Row>
      {#if graphData[0]}
        <Column>
          <LineChart
            data={graphData[0]}
            options={{
              title: "Temperature",
              theme: "g100",
              resizable: true,
              height: "500px",
              curve: "curveNatural",
              zoomBar: {
                top: {
                  enabled: true,
                },
              },
              axes: {
                left: {
                  mapsTo: "value",
                  title: "Temperature (°C)",
                  scaleType: "linear",
                },
                bottom: {
                  mapsTo: "date",
                  title: "Date",
                  scaleType: "time",
                },
              },
              legend: {
                enabled: true,
                position: "bottom",
              },
            }}
          />
        </Column>
      {/if}
    </Row>
    <br />
    <Row>
      {#if graphData[1]}
        <Column>
          <LineChart
            data={graphData[1]}
            options={{
              title: "Humidity",
              theme: "g100",
              resizable: true,
              height: "500px",
              curve: "curveNatural",
              zoomBar: {
                top: {
                  enabled: true,
                },
              },
              axes: {
                left: {
                  mapsTo: "value",
                  title: "Humidity",
                  scaleType: "linear",
                },
                bottom: {
                  mapsTo: "date",
                  title: "Date",
                  scaleType: "time",
                },
              },
              legend: {
                enabled: true,
                position: "bottom",
              },
            }}
          />
        </Column>
      {/if}
    </Row>
    <br />
    <Row>
      {#if graphData[2]}
        <Column>
          <LineChart
            data={graphData[2]}
            options={{
              title: "Precipitation",
              theme: "g100",
              resizable: true,
              height: "500px",
              curve: "curveNatural",
              zoomBar: {
                top: {
                  enabled: true,
                },
              },
              axes: {
                left: {
                  mapsTo: "value",
                  title: "Precipitation (MM)",
                  scaleType: "linear",
                },
                bottom: {
                  mapsTo: "date",
                  title: "Date",
                  scaleType: "time",
                },
              },
              legend: {
                enabled: true,
                position: "bottom",
              },
            }}
          />
        </Column>
      {/if}
    </Row>
    <br />
    <Row>
      {#if graphData[3]}
        <Column>
          <LineChart
            data={graphData[3]}
            options={{
              title: "Pressure",
              theme: "g100",
              resizable: true,
              height: "500px",
              zoomBar: {
                top: {
                  enabled: true,
                },
              },
              animations: {
                enabled: true,
                easing: "ease-in-out",
                speed: 1000,
              },
              curve: "curveNatural",
              axes: {
                left: {
                  mapsTo: "value",
                  title: "Pressure",
                  scaleType: "linear",
                },
                bottom: {
                  mapsTo: "date",
                  title: "Date",
                  scaleType: "time",
                },
              },
              legend: {
                enabled: true,
                position: "bottom",
              },
            }}
          />
        </Column>
      {/if}
    </Row>
  </Grid>
</Content>

<style>

</style>
