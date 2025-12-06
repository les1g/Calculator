#  Calculator

A simple web-based calculator built with Flask. It supports basic arithmetic operations, tracks recent calculations, and features a clean pink-themed interface.

## 📁 Project Structure

```
Calculator/
├── app.py                    # Flask web application
├── calculator/               # Calculator module
│   ├── __init__.py
│   └── core.py              # Core calculation logic
├── static/
│   ├── images/              # Custom images
│   └── js/
│       └── calculator.js    # Client-side functionality
├── templates/
│   └── index.html           # Web interface
├── venv/                    # Python virtual environment
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```
## 🚀 Live Demo 
You don’t need to install anything to try the calculator — it’s already deployed on PythonAnywhere:
👉 View the Calculator [here](https://calcles1g.pythonanywhere.com/)

## 🚀 Installation 
If you’d like to run it locally:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Calculator.git
cd Calculator
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Running the Application

```bash
python app.py
```

Open browser to `http://localhost:5000`

### Keyboard Shortcuts

- **0-9** — Input numbers
- **+, -, *, /** — Input operators
- **.** — Input decimal point
- **Enter** — Calculate result
- **Backspace** — Delete last character
- **ESC** — Clear display

### Mouse Controls

- Click any button to input values
- Click **=** to calculate
- Click **C** to clear
- Click **DEL** to delete last character

## 🧪 Testing

Run the built-in tests:

```bash
python calculator/core.py
```

Output: `All tests passed!`

## 📚 API Reference

### `add(a, b)`
Returns the sum of two numbers.

**Parameters:**
- `a` (int/float): First number
- `b` (int/float): Second number

**Returns:** `int/float` — Sum of a and b

---

### `subtract(a, b)`
Returns the difference of two numbers (a - b).

**Parameters:**
- `a` (int/float): First number
- `b` (int/float): Second number

**Returns:** `int/float` — Difference

---

### `multiply(a, b)`
Returns the product of two numbers.

**Parameters:**
- `a` (int/float): First number
- `b` (int/float): Second number

**Returns:** `int/float` — Product

---

### `divide(a, b)`
Returns the quotient of two numbers (a / b).

**Parameters:**
- `a` (int/float): Dividend
- `b` (int/float): Divisor

**Returns:** `float` — Quotient

**Raises:** `ValueError` — If divisor is zero

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details

## 👤 Author

Gisel Garrido
