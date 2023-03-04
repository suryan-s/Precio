<script>
    export let text = "+";
    let opened = false;
    const toggleOpen = ()=>{
        opened = !opened;
    }
    
    </script>
<button on:click={toggleOpen}>
    {text}
</button>
{#if opened}
 <div  id="Fab-Toggle-Div">
    <slot/>
</div>
{/if}
<style>
    button{
    position: absolute;
    bottom: 20px;
    right: 20px;
    width: 3rem;
    height:3rem;
    display: grid;
    place-content: center;
    background-color: cadetblue;
    border-radius: 50%;
    font-size: 2rem;
        margin: 0;
        border:none;
    }
    button:hover{
        cursor: pointer;
        background-color: rgb(111, 187, 190);
    }
    div{
        position: absolute;
        bottom: 20px;
        right: 5rem;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
   
</style>
