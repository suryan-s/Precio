<script>
    
    
</script>

<button on:click
on:mouseover
on:mouseenter
on:mouseleave
on:focus {...$$props}>
    <slot/>
</button>

<style>
    button{
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
    }
    button:hover{
        cursor: pointer;
    }
</style>
