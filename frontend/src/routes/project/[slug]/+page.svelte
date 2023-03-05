<script>
    export let data;
    import "carbon-components-svelte/css/g100.css";
    import { Content, Grid, Row, Column } from "carbon-components-svelte";
    
</script>

<Content>
    <Grid>
        <Row>
            <Column>
                <h1>{data.slug}</h1>
            </Column>
        </Row>
    </Grid>
</Content>