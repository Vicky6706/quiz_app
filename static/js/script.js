document.addEventListener('DOMContentLoaded', function() {
    console.log('Quiz App is loaded!');

    let totalTime = 300; 

    function startTimer(duration, display) {
        let timer = duration, minutes, seconds;

        const countdown = setInterval(function () {
            minutes = parseInt(timer / 60, 10);
            seconds = parseInt(timer % 60, 10);

            minutes = minutes < 10 ? "0" + minutes : minutes;
            seconds = seconds < 10 ? "0" + seconds : seconds;

            display.textContent = "Time Remaining: " + minutes + ":" + seconds;

            if (--timer < 0) {
                clearInterval(countdown);
                alert("Time is up! The quiz will now be submitted.");
                document.getElementById("quizForm").submit(); 
            }
        }, 1000);
    }

    const display = document.getElementById('timer');
    startTimer(totalTime, display);
});

