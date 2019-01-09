from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from vm import VirtualMachine
from mysql import DB

app = Flask(__name__)
vmachine = VirtualMachine(1)

db = DB('emmet', 'Brownbrown1+', 'vmweb')

cmd = input('Introduzca el comando: ')
desc = input('Introduzca la descripción: ')

sql = f"insert into commands values ('{cmd}', '{desc}')"
db.run(sql)

sql = 'select * from commands order by name'
print(db.run(sql))

@app.route("/")
def index():
    return render_template("index.html", vmachine=vmachine)


@app.route("/change_status/<new_status>")
def change_status(new_status):
    if new_status == "0":
        vmachine.stop()
    elif new_status == "1":
        vmachine.start()
    else:
        vmachine.suspend()
    return redirect("/")


@app.route("/run_process", methods=["GET", "POST"])
def run_process():
    if request.method == "POST":
        vmachine.run(
            int(request.form["pid"]),
            float(request.form["ram"]),
            float(request.form["cpu"]),
            float(request.form["hdd"]),
        )
        return redirect("/")
    else:
        return render_template("run_process.html")


if __name__ == "__main__":
    app.run(debug=True)
