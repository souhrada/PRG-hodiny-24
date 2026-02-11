function factorial(n) {
    let result = 1

    for (let i = n; i >= 1; i--) {
        // result = result * i
        result *= i
    }
    console.log(result)
    return result
}

factorial(5)



const squareBtn = document.querySelector(".square-btn")
const body = document.querySelector("body")

squareBtn.addEventListener("click", createSquares)

function createSquares() {
    for (let i = 0; i < 3; i++) {
        let square = document.createElement("div")

        square.style.width = "50px"
        square.style.height = "50px"
        square.style.backgroundColor = "green"
        square.style.margin = "5px"

        body.append(square)
    }
}