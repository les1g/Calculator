/**
 * Calculator application - handles display updates and keyboard/mouse input
 */

let expression = '';

/**
 * Update the display input field with current expression
 */
function updateDisplay() {
    document.getElementById('display').value = expression;
}

/**
 * Append a value (number, operator, or decimal) to the expression
 * @param {string} value - The value to append
 */
function appendValue(value) {
    expression += value;
    updateDisplay();
}

/**
 * Clear the display and reset expression
 */
function clearDisplay() {
    expression = '';
    updateDisplay();
}

/**
 * Delete the last character from the expression
 */
function deleteLast() {
    expression = expression.slice(0, -1);
    updateDisplay();
}

/**
 * Submit the calculation form to the server
 */
function calculate() {
    if (!expression) return;
    document.getElementById('calculator-form').submit();
}

// Initialize event listeners when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    const display = document.getElementById('display');

    // Sync input field with expression variable and validate input
    display.addEventListener('input', function(e) {
        const value = e.target.value;
        const validValue = value.replace(/[^0-9+\-*/.]/g, '');
        expression = validValue;
        if (value !== validValue) {
            updateDisplay();
        }
    });

    // Global keyboard shortcuts - works without focus on input field
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            e.preventDefault();
            clearDisplay();
        } else if (e.key === 'Backspace') {
            e.preventDefault();
            deleteLast();
        } else if (e.key === 'Enter') {
            e.preventDefault();
            calculate();
        } else if (e.key >= '0' && e.key <= '9') {
            e.preventDefault();
            appendValue(e.key);
        } else if (['+', '-', '*', '/'].includes(e.key)) {
            e.preventDefault();
            appendValue(e.key);
        } else if (e.key === '.') {
            e.preventDefault();
            appendValue('.');
        }
    });

    // Handle paste - filter out invalid characters
    display.addEventListener('paste', function(e) {
        e.preventDefault();
        const pastedText = (e.clipboardData || window.clipboardData).getData('text');
        const validText = pastedText.replace(/[^0-9+\-*/.]/g, '');
        expression += validText;
        updateDisplay();
    });
});