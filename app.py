from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Temporary classroom data
classrooms_data = [
    {
        "building": "CB",
        "room": "101",
        "floor": "First Floor",
        "capacity": 60,
        "people": 35,
        "energy": "1.42 kWh",
        "status": "Active"
    },
    {
        "building": "CB",
        "room": "102",
        "floor": "First Floor",
        "capacity": 60,
        "people": 13,
        "energy": "0.86 kWh",
        "status": "Active"
    },
    {
        "building": "CB",
        "room": "201",
        "floor": "Second Floor",
        "capacity": 60,
        "people": 0,
        "energy": "0 kWh",
        "status": "Offline"
    }
]


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "classroom123":
            return redirect(url_for("classrooms"))

        return render_template(
            "login.html",
            error="Invalid username or password"
        )

    return render_template("login.html")


@app.route("/classrooms")
def classrooms():

    return render_template(
        "classrooms.html",
        classrooms=classrooms_data
    )


@app.route("/add-classroom", methods=["GET", "POST"])
def add_classroom():

    if request.method == "POST":

        building = request.form.get("building")
        room = request.form.get("room")
        floor = request.form.get("floor")
        capacity = request.form.get("capacity")

        new_classroom = {
            "building": building,
            "room": room,
            "floor": floor,
            "capacity": capacity,
            "people": 0,
            "energy": "0 kWh",
            "status": "Active"
        }

        classrooms_data.append(new_classroom)

        return redirect(url_for("classrooms"))

    return render_template("add_classroom.html")

@app.route("/classroom/<int:classroom_id>")
def classroom_dashboard(classroom_id):

    classroom = classrooms_data[classroom_id]

    return render_template(
        "classroom_dashboard.html",
        classroom=classroom
    )


if __name__ == "__main__":
    app.run(debug=True)