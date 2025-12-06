"""
Flask web application for a simple calculator with history tracking.
"""

from flask import Flask, render_template, request, session
from calculator.core import add, subtract, multiply, divide

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # TODO: Change to random string in production
    

@app.route("/", methods=["GET", "POST"])
def calculator():
    """Handle calculator requests and calculations."""
    expression = session.get("expression", "")
    result = ""
    history = session.get("history", [])

    if request.method == "POST":
        expr = request.form.get("expression", "").strip()

        try:
            # Validate input - only allow numbers, operators, and decimals
            if expr and all(c in "0123456789+-*/. " for c in expr):
                operator = None
                operation_display = ""

                # Parse and calculate based on operator
                if "+" in expr:
                    parts = expr.split("+", 1)
                    a, b = float(parts[0]), float(parts[1])
                    result = add(a, b)
                    operator = "+"
                elif "-" in expr and expr.count("-") == 1:
                    parts = expr.split("-", 1)
                    a, b = float(parts[0]), float(parts[1])
                    result = subtract(a, b)
                    operator = "-"
                elif "*" in expr:
                    parts = expr.split("*", 1)
                    a, b = float(parts[0]), float(parts[1])
                    result = multiply(a, b)
                    operator = "*"
                elif "/" in expr:
                    parts = expr.split("/", 1)
                    a, b = float(parts[0]), float(parts[1])
                    result = divide(a, b)
                    operator = "/"
                else:
                    # Just a number entered, store it
                    expression = expr
                    session["expression"] = expression
                    return render_template(
                        "index.html",
                        result=result,
                        expression=expression,
                        history=history,
                    )

                # Format and store calculation in history
                if operator:
                    # Convert floats to ints if they're whole numbers
                    if isinstance(a, float) and a.is_integer():
                        a = int(a)
                    if isinstance(b, float) and b.is_integer():
                        b = int(b)
                    if isinstance(result, float) and result.is_integer():
                        result = int(result)

                    operation_display = f"{a} {operator} {b} = {result}"
                    history.append(operation_display)

                    # Keep only last 10 operations
                    if len(history) > 10:
                        history.pop(0)

                # Clear expression after calculation and store updated session
                expression = ""
                session["expression"] = expression
                session["history"] = history
            else:
                result = "Error"
                expression = ""
                session["expression"] = ""
        except (ValueError, ZeroDivisionError, IndexError):
            result = "Error"
            expression = ""
            session["expression"] = ""

    return render_template(
        "index.html", result=result, expression=expression, history=history
    )


if __name__ == "__main__":
    app.run(debug=True)