<script>
    import { shared } from "$lib/shared.svelte"
    let { buttonText } = $props()

    function increment() {
        shared.score = shared.score + shared.multi
    }

</script>

<button onclick={increment}>{buttonText}</button>

<style>
    button {
        background-color: rgb(110, 247, 122);
        border: none;
        padding: 10px 20px;
        border-radius: 10000px;
    }

    button:hover {
        background-color: rgb(161, 216, 97);
    }
</style>