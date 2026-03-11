<script>
    import { shared } from "$lib/shared.svelte"

    let text = $state("Cheats")
    let color = $state("black")
    let cheat = false

    function runCheat() {
        if (text === "iddqd" && !cheat) {
        shared.score += 100
        cheat = true
        color = "green"
        }
    }
    
</script>


<p style="color:{color}">{text}</p>
<input bind:value={text} oninput={runCheat} type="text">