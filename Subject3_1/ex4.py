from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form.get('name')
    student_number = request.form.get('student_number')
    gender = request.form.get('gender')
    
    return render_template('result.html',
                           name=name,
                           student_number=student_number,
                           gender=gender)

if __name__ == '__main__':
    app.run(debug=True)