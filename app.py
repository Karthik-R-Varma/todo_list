from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for tasks (use a database in a real application)
tasks = []

# Add enumerate to Jinja2 globals
app.jinja_env.globals.update(enumerate=enumerate)

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append({'task': task, 'status': 'pending'})
    return redirect(url_for('home'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    tasks[task_id]['status'] = 'completed'
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
