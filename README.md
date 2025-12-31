# Flask Calculator 🧮

A web-based calculator application built with Flask that features session management, calculation history, and memory functions.

## Features

- **User Authentication**: Simple username-based login system
- **Calculator Functions**: Basic arithmetic operations (+, -, *, /)
- **Memory Functions**: MC (Memory Clear), MR (Memory Recall), M+ (Memory Add)
- **Calculation History**: Track all your calculations in the current session
- **Session Management**: Each user has their own isolated session
- **Responsive Design**: Modern UI with Bootstrap 5

## Screenshots

The calculator features a sleek, modern interface with:
- Neon-styled display and buttons
- Real-time calculation history
- Memory indicator
- Dark theme with gradient background

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Hamjath/Flask_Calculator.git
cd Flask_Calculator
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## Usage

1. **Login**: Enter any username to start your session
2. **Calculate**: Use the on-screen buttons to perform calculations
3. **Memory Functions**:
   - M+: Add current result to memory
   - MR: Recall value from memory
   - MC: Clear memory
4. **History**: View your calculation history on the main page or dedicated history page
5. **Clear**: Use C to clear current expression, AC to clear everything

## Project Structure

```
flask-calculator/
│
├── app.py                 # Main Flask application
├── templates/
│   ├── base.html         # Base template
│   ├── calculator.html   # Calculator interface
│   ├── history.html      # History page
│   └── login.html        # Login page
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## Security Notes

⚠️ **Important**: This application uses a simple session-based authentication for demonstration purposes. For production use:
- Change the `secret_key` in `app.py` to a strong, random key
- Implement proper user authentication with password hashing
- Use environment variables for sensitive configuration
- Enable HTTPS
- Implement CSRF protection

## Technologies Used

- **Flask**: Web framework
- **Bootstrap 5**: Frontend styling
- **SimpleEval**: Safe expression evaluation
- **Flask Sessions**: Session management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

HAMJATH KHAN

## Acknowledgments

- Built as a learning project for Flask and web development
- Inspired by classic calculator designs with a modern twist