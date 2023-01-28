const mf = document.getElementById('answer');

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
function rollQuestion() {
    mf.disabled = false
    let problem = choose(questions)
    $('.hideOnLoad').hide()
    $('#randQuestion').text(problem.q)
    answer = problem.a
}

// fetch the questions
let questions = []
let answer = null
let guesses = new Set()

fetch("./sample_questions.json").then(res => res.json()).then(qs => {
    questions = qs
    guesses.clear()
    rollQuestion()
    $('#everything').show()
})

$('#submit').click(function() {
    let ans = mf.value
    if (!ans || guesses.has(ans)) return
    else if (ans == answer) { // if correct
        $('#wronglol').hide()
        $('#correctgg').show()
        mf.disabled = true
        return $('#nextQ').show()
    }
    else { // if correct
        guesses.add(ans)
        mf.executeCommand("selectAll")
        return $('#wronglol').show()
    }
})

$('#nextQ').click(function() {
    rollQuestion()
    mf.value = ""
})