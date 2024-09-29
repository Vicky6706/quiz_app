from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Berlin", "Madrid", "Paris", "Lisbon"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "choices": ["Charles Dickens", "J.K. Rowling", "William Shakespeare", "Mark Twain"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the smallest prime number?",
        "choices": ["1", "2", "3", "5"],
        "answer": "2"
    },
    {
        "question": "What is the chemical symbol for water?",
        "choices": ["O2", "H2O", "CO2", "HO"],
        "answer": "H2O"
    },
    {
        "question": "What is the capital of Bulgaria?",
        "choices": ["Sofia", "Zagreb", "Paris", "London"],
        "answer": "Sofia"
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answers = request.form
        score = 0
        total_questions = len(quiz_questions)
        
        
        for index, question in enumerate(quiz_questions):
            selected_answer = user_answers.get(f"question-{index}")
            if selected_answer == question['answer']:
                score += 1

        return redirect(url_for('result', score=score, total=total_questions))
    
    return render_template('quiz.html', questions=quiz_questions)


@app.route('/result')
def result():
    score = request.args.get('score')
    total = request.args.get('total')
    return render_template('result.html', score=score, total=total)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
