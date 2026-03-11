<script>
    import { shared } from "$lib/shared.svelte"

    let running = false

    function autoclicker() {
        if (!running) { // to stejné jako if running === false
            running = true
            setInterval(function() {
                shared.score += 1
            }, 1000)
        }    
    }

</script>

<button onclick={autoclicker}>Autoclicker</button>


<style>

    button {
        background-color: rgb(189, 67, 189);
        border: none;
        padding: 10px 20px;
        border-radius: 10000px;
        color: white;
        display: block;
    }

    button:hover {
        background-color: rgb(226, 151, 226);
    }
</style>