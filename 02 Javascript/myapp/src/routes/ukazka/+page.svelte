<script>
    import Button from "../../components/Button.svelte"

    let message = "Hello!"
    let src = "https://upload.wikimedia.org/wikipedia/commons/2/28/Golden-retriever-1.jpg"
    let score = $state(0)

    function increment() {
        score += 1
    }
</script>


<h1>Vše funguje</h1>
<ul>
    <li>Vše</li>
    <li>funguje</li>
    <li>bez</li>
    <li>problémů</li>
</ul>

<h2>{message.toUpperCase()} random person</h2>
<img {src} class="image" alt="">

<p>{score >= 5 ? "Good!" : "Neutral"}</p>
<p>Points: {score}</p>
<button onclick={increment}>Click me!</button>
<Button />

<style>
    .image {
        height: 200px;
    }
</style>