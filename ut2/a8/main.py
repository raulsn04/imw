from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from vm import VirtualMachine

app = Flask(__name__)
vmachine = VirtualMachine('Azkaban', 16, 3.7, 1000, 'debian')


@app.route('/')
def index():
    return render_template('index.html', vmachine=vmachine)


@app.route('/change_status/<new_status>')
def change_status(new_status):
    vmachine.status = new_status()

    return redirect('/')


@app.route('/run_process', methods=['GET', 'POST'])
def run_process():
    if request.method == 'POST':
        do_the_run_process(
            request.form["PID"],
            request.form["RAM"],
            request.form["CPU"],
            request.form["HDD"]
        )
        return redirect('/')
    else:
        return render_template('run_process.html')
