<script>
import Button from "../components/Button.svelte"
import Timer from "../components/Timer.svelte"
import ResetButton from "../components/ResetButton.svelte";
import Upgrade from "../components/Upgrade.svelte";
import { shared } from "$lib/shared.svelte"



</script>

<p>{shared.score}</p>
<Button buttonText={"Click me"}/>
<Button buttonText={"Hello?"}/>
<Timer />
<ResetButton />
<Upgrade />



<style>

</style>