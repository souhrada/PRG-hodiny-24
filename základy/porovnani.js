let kresniJmeno = "Hugo"
let cislo = 5
let pravda = true

let seznamStudentu = ["Emil", "Emilie", "Jarmila", "Jarmil", "Hvězdoň"]


console.log(krestniJmeno)

function nahodnaFunkce() {
    console.log("funguje")
}

nahodnaFunkce()

if (cislo > 0)  {
    console.log("číslo je kladné")
} else if (cislo < 0) {
    console.log("číslo je záporné")
} else {
    console.log("číslo je 0")
}


let pocitadlo = 1

while (pocitadlo < 11) {
    console.log(pocitadlo)
    pocitadlo++
}

for (let i = 1; i < 11; i++) {
    console.log(i)
}


for (let i = 0; i < seznamStudentu.length; i++) {
    console.log(seznamStudentu[i])
}