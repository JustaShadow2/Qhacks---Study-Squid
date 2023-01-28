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
}

let loading = true
let answerID = 0
let guesses = new Set()

let category = null
let categoryName = null

$('.subjectOption').click(function() {
    category = $(this).attr('category')
    categoryName = $(this).find("p").text()
    rollQuestion()
    $('#home').hide()
})
$('.subjectOption:first').trigger("click")

async function rollQuestion() {
    let qs = await fetch("./api/" + category).then(res => res.json())
    guesses.clear()
    makeQuestion(qs.question)
    answerID = qs.id
    $('#maths').show()
    loading = false
}

$('#submit').click(function() {
    let ans = mf.value
    if (!ans || loading || mf.disabled || guesses.has(ans)) return
    loading = true

    $.ajax({
        url: "./api/solve", type: "post",
        data: JSON.stringify({ id: answerID, answer: ans }),
        headers: { 'Content-Type': 'application/json'}
    })
    .done(function(res) {
        if (res == true || res == "true") { // if correct
            $('#wronglol').hide()
            $('#correctgg').show()
            mf.disabled = true
            addXP(Math.max(0, 5 - guesses.size))
            $('#nextQ').show()
            return loading = false
        }
        else { // if not correct
            guesses.add(ans)
            mf.executeCommand("selectAll")
            $('#steps').show()
            $('#wronglol').show()
            return loading = false
        }
    })
    .fail(function (e) {
        loading = false
        return alert("Something went wrong!")
    })
})

$('#steps').click(async function() {
    $('#steps').hide()
    $('#loadingHint').text("Loading steps...")
    $('#loadingHint').show()
    let steps = await fetch("./api/steps/" + answerID).then(res => res.json())
    console.log(steps)
    if (!steps || !steps.queryresult || !steps.queryresult.pods) return $('#loadingHint').text("No steps availible!.")
    let img = steps.queryresult.pods.map(x => x.subpods).flat().sort((a, b) => b.img.height - a.img.height)[0].img
    console.log(img)
    $('#stepsImg').attr("src", img.src)
    $('#stepsImg').attr("alt", img.alt)
    $('#hintImage').show()
    $('#loadingHint').hide()
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