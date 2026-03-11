<script>
import { shared } from "$lib/shared.svelte"
let { level }  = $props()

let upgradeClicked = $state(false)


function upgrade() {
    if (level === 1) {
        shared.multi = 2
    } else if (level === 2) {
        shared.multi = 5
    } else if (level === 3) {
        shared.multi = 10
    }
    upgradeClicked = true
    
}
</script>

<div>
    {#if upgradeClicked}
        <p>Upgraded</p>
    {:else}
        <p>Upgrade clicker</p>
    {/if}

    <button onclick={upgrade}>Upgrade</button>
</div>




<style>
    button {
        background-color: var(--color);
        border: none;
        padding: 10px 20px;
        border-radius: 10000px;
        color: white;
        font-family: monospace;
    }

    button:hover {
        background-color: rgb(85, 85, 238);
    }

    div {
        border: 2px solid rgb(85, 85, 238);
        border-radius: 5px;
        margin: 5px;
        width: fit-content;
        padding: 15px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 10px;
        background-color: rgba(180, 180, 247, 0.3);
        font-family: monospace;
        display: inline-block;
    }
</style>