<script>
    import { shared } from "$lib/shared.svelte";

</script>

<button onclick={shared.score = 0}>Reset</button>

<style>
    button {
        background-color: rgb(247, 124, 124);
        border: none;
        padding: 10px 20px;
        border-radius: 10000px;
    }

    button:hover {
        background-color: rgb(228, 105, 92);
    }
</style>