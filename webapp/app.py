from flask import Flask, render_template, redirect, url_for, request

from student import Student

students = []

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def students_page():
    '''
    Currently the method should use the GET method only
    as the current task is to display a list of students parsed from
    the studentcsv file. Therefore, the line of code for POST method
    is commented.
    :return:
    '''
    '''
    if request.method == "POST":
        new_student_id = request.form.get("student-id", "")
        new_student_name = request.form.get("name", "")
        new_student_last_name = request.form.get("last-name", "")

        new_student = Student(name=new_student_name, lastname=new_student_last_name, student_id=new_student_id)
        students.append(new_student)

        return redirect(url_for("students_page"))
    '''
    return render_template("index.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)
