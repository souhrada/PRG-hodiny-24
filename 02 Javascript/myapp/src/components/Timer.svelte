<script>

    let elapsedTime = $state(0)

    setInterval(function() {
        elapsedTime += 1
    }, 1000)


    // alternativní zápis
    // setInterval(() => {elapsedTime += 1}, 1000)


</script>

<p>Time: {elapsedTime}</p>