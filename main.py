from flask import Flask, render_template, url_for, request
import csv

app = Flask(__name__)

def read_data(filename):
    staff_data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            staff_data.append(row)
    return staff_data

staff_data = read_data("staff.csv")

@app.route("/", methods=["GET"])
def search():
    staff_name = request.args.get("staff_name", "").strip().lower()
    department = request.args.get("department", "").strip().lower()

    results = []
    for staff in staff_data:
        if staff_name != "" and department != "":
            if staff_name in staff["name"].lower() and department in staff["dept"].lower():
                results.append(staff)
        elif staff_name != "":
            if staff_name in staff["name"].lower():
                results.append(staff)
        elif department != "":
            if department in staff["dept"].lower():
                results.append(staff)

    return render_template("search.html", results=results, staff_name=staff_name, department=department)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=6969)
