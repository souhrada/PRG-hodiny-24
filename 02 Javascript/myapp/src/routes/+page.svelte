<script>
import Button from "../components/Button.svelte"
import Timer from "../components/Timer.svelte"
import ResetButton from "../components/ResetButton.svelte"
import Upgrade from "../components/Upgrade.svelte"
import { shared } from "$lib/shared.svelte"
import Autoclicker from "../components/Autoclicker.svelte"
import Cheats from "../components/Cheats.svelte"


let animScore = $state()

$effect( () => {
    if (shared.score > 0) {
        animScore = "anim-score"
        setTimeout(() => animScore = "", 100)
    }
    
})

</script>

<div>
    <p class={animScore}>{shared.score}</p>
</div>

<Button buttonText={"Click me"}/>
<Timer />
<ResetButton />
<Upgrade level={1} --color="rgb(113, 113, 236)"/>
<Upgrade level={2} --color="rgb(236, 113, 113)"/>
<Upgrade level={3} --color="rgb(113, 236, 113)"/>
<Autoclicker />
<Cheats />




<style>

    div {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .anim-score {
        animation: popout 0.1s;
    }

    @keyframes popout {
        50% {
            scale: 2;
        }

        100% {
            scale: 1;
        }
    }
</style>