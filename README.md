![Password-Strength-Checker](https://socialify.git.ci/clueNA/Password-Strength-Checker/image?font=Raleway&language=1&name=1&owner=1&pattern=Transparent&stargazers=1&theme=Dark)

# 🔒 Password Strength Checker

A real-time password strength analyzer built with Python and Streamlit. This tool provides instant feedback on password security with advanced pattern detection and animated visual feedback.

## 🌐 Live Demo
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://passcheq.streamlit.app/)

## ✨ Features

- **Real-time Strength Analysis**: Instant feedback as you type
- **Advanced Password Checks**:
  - Common password detection
  - Keyboard pattern recognition
  - Repeated character detection
  - Sequential pattern detection
- **Visual Feedback**:
  - Animated strength indicator
  - Dynamic progress bar
  - Color-coded feedback
  - Detailed security recommendations

## 🎯 Password Criteria

The tool evaluates passwords based on:
- Minimum length (8 characters)
- Presence of uppercase letters
- Presence of lowercase letters
- Numbers
- Special characters
- Additional complexity factors

## 🏆 Scoring System

Passwords are scored on a scale of 0-12 points:
- **Weak** (0-4 points): High risk
- **Moderate** (5-8 points): Basic security
- **Strong** (9-10 points): Good security
- **Very Strong** (11-12 points): Excellent security

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Streamlit

### Installation

1. Clone the repository:
```bash
git clone https://github.com/clueNA/Password-Strength-Checker
cd password-strength-checker
```

2. Install required packages:
```bash
pip install streamlit
```

3. Run the application:
```bash
streamlit run main.py
```

## 💻 Usage

1. Visit the application URL or run locally
2. Enter your password in the input field
3. Receive instant feedback on your password's strength
4. Follow the recommendations to improve security

## 📊 Security Scoring Details

Points are awarded as follows:
- +2 points: Meeting minimum length
- +2 points: Containing uppercase letters
- +2 points: Containing lowercase letters
- +2 points: Containing numbers
- +2 points: Containing special characters
- +2 points: Extra length bonus

Points are deducted for:
- -3 points: Common password detection
- -2 points: Keyboard patterns
- -2 points: Repeated characters
- -2 points: Sequential characters

## 🛡️ Security Tips

- Use a mix of different character types
- Avoid common words or phrases
- Avoid keyboard patterns (e.g., "qwerty")
- Avoid sequential characters (e.g., "abc123")
- Create unique passwords for each account
- Consider using a password manager


## ⭐ Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Password security best practices from [NIST](https://www.nist.gov/)
- Common password list from security research
