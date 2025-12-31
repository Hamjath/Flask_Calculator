from flask import Flask, render_template, request, redirect, url_for, session, flash
from simpleeval import SimpleEval
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "super-secret-key"  # change in real apps
app.permanent_session_lifetime = timedelta(seconds=30)


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")

        if username:
            session.clear()
            session["user"] = username
            session["expression"] = ""
            session["history"] = []
            session["memory"] = 0
            return redirect(url_for("calculator"))
    else:
        if "user" in session:
            flash("You are already logged in.", "info")
            return redirect(url_for("calculator"))
        
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ---------------- CALCULATOR ----------------

@app.route("/", methods=["GET", "POST"])
def calculator():
    if "user" not in session:
        return redirect(url_for("login"))

    # initialize session keys safely
    session.setdefault("expression", "")
    session.setdefault("history", [])
    session.setdefault("memory", 0)

    if request.method == "POST":
        button = request.form.get("button")

        # ---- CLEAR FUNCTIONS ----
        if button == "AC":
            session["expression"] = ""
            session["history"] = []
            session["memory"] = 0

        elif button == "C":
            session["expression"] = ""

        # ---- MEMORY FUNCTIONS ----
        elif button == "MC":
            session["memory"] = 0

        elif button == "MR":
            session["expression"] = str(session["memory"])

        elif button == "M+":
            try:
                evaluator = SimpleEval()
                value = evaluator.eval(session["expression"])
                session["memory"] += float(value)
            except Exception:
                session["expression"] = "Error"

        # ---- CALCULATION ----
        elif button == "=":
            try:
                evaluator = SimpleEval()
                result = evaluator.eval(session["expression"])

                session["history"].append(
                    f"{session['expression']} = {result}"
                )
                session["expression"] = str(result)

            except Exception:
                session["expression"] = "Error"

        # ---- NORMAL INPUT ----
        else:
            if session["expression"] == "Error":
                session["expression"] = ""
            session["expression"] += button

    return render_template(
        "calculator.html",
        expression=session["expression"],
        history=session["history"],
        memory=session["memory"],
        user=session["user"]
    )


# ---------------- HISTORY PAGE ----------------

@app.route("/history")
def history():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
        "history.html",
        history=session.get("history", []),
        user=session["user"]
    )


@app.route("/clear-history")
def clear_history():
    if "user" in session:
        session["history"] = []
    return redirect(url_for("history"))


# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(debug=True)
