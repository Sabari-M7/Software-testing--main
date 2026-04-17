from flask import Flask, request, render_template

app = Flask(__name__)

# Calculator logic
class Operation:
    def execute(self, a, b):
        raise NotImplementedError

class Add(Operation):
    def execute(self, a, b): return a + b

class Subtract(Operation):
    def execute(self, a, b): return a - b

class Multiply(Operation):
    def execute(self, a, b): return a * b

class Divide(Operation):
    def execute(self, a, b):
        if b == 0: raise ValueError("Cannot divide by zero")
        return a / b

class Calculator:
    def __init__(self):
        self.operations = {
            "add": Add(),
            "subtract": Subtract(),
            "multiply": Multiply(),
            "divide": Divide()
        }

    def calculate(self, op_name, a, b):
        operation = self.operations.get(op_name)
        if not operation:
            raise ValueError("Invalid operation")
        return operation.execute(a, b)

@app.route("/", methods=["GET", "POST"])
def index():
    result, error = "", ""
    if request.method == "POST":
        try:
            a = float(request.form["num1"])
            b = float(request.form["num2"])
            op = request.form["operation"]
            calc = Calculator()
            result = calc.calculate(op, a, b)
        except Exception as e:
            error = str(e)
    return render_template("calculator.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
