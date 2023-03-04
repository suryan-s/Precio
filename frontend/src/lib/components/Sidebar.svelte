<script>
    export let title = "";
</script>
<aside>
    <h1>{title}</h1>
<slot/>
</aside>

<style>
    aside{
        background-color: #222;
        width:100%;
        max-width:400px;
        min-height: 100vh;
        height:100%;
        color: aliceblue;
        padding:20px 30px;
    }
    h1{
        padding:0;
        margin:0;
    }
</style>