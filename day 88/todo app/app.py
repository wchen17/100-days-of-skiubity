# ============================================================
#  DAY 88 — Portfolio Project
#  PROJECT: Todo / Agenda App
# ============================================================
#
#  SKILLS USED: Flask, SQLAlchemy, Bootstrap, WTForms, due dates
#
#  REQUIREMENTS:
#    - Add tasks with title, description, due date, priority
#    - Mark tasks complete (strikethrough, move to bottom)
#    - Delete tasks
#    - Filter: All / Active / Completed / Overdue
#    - Sort by due date or priority
#    - Data persists in SQLite
#
# ============================================================

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"
db = SQLAlchemy(app)


class Todo(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    due_date    = db.Column(db.Date)
    priority    = db.Column(db.Integer, default=2)   # 1=high, 2=med, 3=low
    completed   = db.Column(db.Boolean, default=False)
    created_at  = db.Column(db.Date, default=date.today)

    @property
    def is_overdue(self):
        return self.due_date and self.due_date < date.today() and not self.completed

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    filter_by = request.args.get("filter", "all")
    query     = db.select(Todo).order_by(Todo.priority, Todo.due_date)
    todos     = db.session.execute(query).scalars().all()

    if filter_by == "active":
        todos = [t for t in todos if not t.completed]
    elif filter_by == "completed":
        todos = [t for t in todos if t.completed]
    elif filter_by == "overdue":
        todos = [t for t in todos if t.is_overdue]

    return render_template("index.html", todos=todos, filter=filter_by, today=date.today())


@app.route("/add", methods=["POST"])
def add_todo():
    title    = request.form.get("title")
    due_str  = request.form.get("due_date")
    priority = int(request.form.get("priority", 2))
    due_date = date.fromisoformat(due_str) if due_str else None

    if title:
        db.session.add(Todo(title=title, due_date=due_date, priority=priority))
        db.session.commit()
    return redirect(url_for("index"))


# --------------------------------------------------
#  TODO 1: /toggle/<id> route → flip completed boolean
# --------------------------------------------------
@app.route("/toggle/<int:todo_id>")
def toggle(todo_id):
    todo = db.get_or_404(Todo, todo_id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for("index"))


# --------------------------------------------------
#  TODO 2: /delete/<id> route
# --------------------------------------------------
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    pass   # TODO


# --------------------------------------------------
#  TODO 3: /edit/<id> route (GET=form, POST=save)
# --------------------------------------------------
@app.route("/edit/<int:todo_id>", methods=["GET", "POST"])
def edit(todo_id):
    pass   # TODO


if __name__ == "__main__":
    app.run(debug=True)
