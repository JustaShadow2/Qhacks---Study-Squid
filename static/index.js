const mf = document.getElementById('answer');
let saveData = JSON.parse(localStorage.mathSquid || "{}")
let xp = saveData.xp || 0

// random number generator, might be useful idk
function rng(min, max) {
    if (max == undefined && +min) { max = min; min = 1 } // rng(5) is the same as rng(1, 5)
    return Math.floor(Math.random() * (max - min + 1)) + min
}

// randomly pick from array
function choose(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

// pick and display a question
function makeQuestion(q) {
    mf.disabled = false
    $('.hideOnLoad').hide()
    $('#randQuestion').text(q)
    answer = 69
}

// fetch the questions
let answer = null
let guesses = new Set()

async function rollQuestion() {
    let qs = await fetch("./api").then(res => res.json())
    guesses.clear()
    makeQuestion(qs.question)
    $('#maths').show()
}
// rollQuestion()

$('#submit').click(function() {
    let ans = mf.value
    if (!ans || mf.disabled || guesses.has(ans)) return
    else if (ans == answer) { // if correct
        $('#wronglol').hide()
        $('#correctgg').show()
        mf.disabled = true
        addXP(Math.max(0, 5 - guesses.size))
        return $('#nextQ').show()
    }
    else { // if not correct
        guesses.add(ans)
        mf.executeCommand("selectAll")
        return $('#wronglol').show()
    }
})

$('#nextQ').click(function() {
    rollQuestion()
    mf.value = ""
})

document.body.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        if (mf.disabled) $("#nextQ").click();
        else $("#submit").click();
        event.preventDefault();
    }
});

///// XP SHIT BECAUSE I AM FIVE YEARS OLD /////
function getXPForLevel(x) {
    return Math.round(((x ** 2) + (x * 7)) / 2)
}

function getLevel(exp) {
    let lvl = 1
    while (getXPForLevel(lvl) <= exp) lvl++
    return lvl
}

function loadXP() {
    let lvl = getLevel(xp)
    let nextXP = getXPForLevel(lvl)
    let prev = getXPForLevel(lvl - 1)
    let progress = ((xp - prev) / (nextXP - prev)) * 100
    $('#xpProgress').css("width", progress + "%")
    // $('#xpProgress').css("background-color", `hsl(${(lvl * 5) % 360}, 100%, 50%)`)
    $('#xpCount').text(`${xp} / ${nextXP} · · · · · Level ${lvl}`)
    saveData.xp = xp
    localStorage.mathSquid = JSON.stringify(saveData)
}
loadXP()

function addXP(amt) {
    let oldLevel = getLevel(xp)
    xp += amt
    let newLevel = getLevel(xp)
    if (oldLevel < newLevel) {
        $('#xpProgress').css("width", "100%")
        setTimeout(() => {
            $('#xpProgress').css("transition-duration", "0s")
            $('#xpProgress').css("width", "0%")
            setTimeout(() => {
                $('#xpProgress').css("transition-duration", "")
                loadXP() 
            }, 10);
        }, 105);
    }
    else loadXP()
}