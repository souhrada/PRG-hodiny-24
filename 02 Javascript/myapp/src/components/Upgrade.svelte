<script>
import { shared } from "$lib/shared.svelte"

let upgradeClicked = $state(false)


function upgrade() {
    upgradeClicked = true
    shared.multi = 2
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
        background-color: rgb(113, 113, 236);
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
    }
</style>