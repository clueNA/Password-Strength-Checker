import streamlit as st
import re
from datetime import datetime
import json
import time
import string

class PasswordStrengthChecker:
    def __init__(self):
        self.min_length = 8
        # Common passwords list
        self.common_passwords = {
            "password", "123456", "12345678", "qwerty", "admin",
            "letmein", "welcome", "monkey", "password123", "abc123",
            "football", "123456789", "princess", "dragon", "secret"
        }
        # Common patterns
        self.keyboard_patterns = [
            "qwerty", "asdfgh", "zxcvbn", "qwertz", "azerty",
            "123456", "234567", "345678", "456789"
        ]

    def check_keyboard_pattern(self, password):
        password_lower = password.lower()
        for pattern in self.keyboard_patterns:
            if pattern in password_lower:
                return True
        return False

    def check_repeated_patterns(self, password):
        # Check for repeated characters (e.g., 'aaa', '111')
        for i in range(len(password)-2):
            if password[i] == password[i+1] == password[i+2]:
                return True
        return False

    def check_sequential_chars(self, password):
        # Check for sequential characters (e.g., 'abc', '123', 'xyz')
        alpha = string.ascii_lowercase
        digits = string.digits
        
        password_lower = password.lower()
        for i in range(len(password)-2):
            # Check alphabetical sequence
            if password_lower[i:i+3] in alpha:
                return True
            # Check numerical sequence
            if password_lower[i:i+3] in digits:
                return True
        return False

    def check_strength(self, password):
        score = 0
        feedback = []
        
        # Basic checks
        if len(password) >= self.min_length:
            score += 2
            feedback.append("✅ Good length")
        else:
            feedback.append(f"❌ Password should be at least {self.min_length} characters long")
            
        if re.search(r'[A-Z]', password):
            score += 2
            feedback.append("✅ Contains uppercase letters")
        else:
            feedback.append("❌ Add uppercase letters")
            
        if re.search(r'[a-z]', password):
            score += 2
            feedback.append("✅ Contains lowercase letters")
        else:
            feedback.append("❌ Add lowercase letters")
            
        if re.search(r'\d', password):
            score += 2
            feedback.append("✅ Contains numbers")
        else:
            feedback.append("❌ Add numbers")
            
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 2
            feedback.append("✅ Contains special characters")
        else:
            feedback.append("❌ Add special characters")
            
        # Advanced checks
        if password.lower() in self.common_passwords:
            score -= 3
            feedback.append("⚠️ This is a commonly used password")
            
        if self.check_keyboard_pattern(password):
            score -= 2
            feedback.append("⚠️ Contains keyboard pattern")
            
        if self.check_repeated_patterns(password):
            score -= 2
            feedback.append("⚠️ Contains repeated patterns")
            
        if self.check_sequential_chars(password):
            score -= 2
            feedback.append("⚠️ Contains sequential characters")
            
        # Extra points for longer passwords
        if len(password) >= self.min_length + 4:
            score += 2
            feedback.append("✅ Extra length bonus")
            
        # Ensure score doesn't go below 0
        score = max(0, score)
            
        return score, feedback

    def get_strength_level(self, score):
        if score <= 4:
            return "Weak", "#ff4444"
        elif score <= 8:
            return "Moderate", "#ffa700"
        elif score <= 10:
            return "Strong", "#00cc44"
        return "Very Strong", "#00ff00"

def main():
    st.set_page_config(
        page_title="Password Strength Checker",
        page_icon="🔒",
        layout="centered"
    )

    # Custom CSS for animations
    st.markdown("""
    <style>
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .strength-indicator {
        animation: pulse 2s infinite;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .stProgress > div > div > div > div {
        transition: all 500ms ease;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title and description
    st.title("🔒 Password Strength Checker")
    st.markdown("""
    Enter your password below to check its strength in real-time.
    A strong password should include:
    - At least 8 characters
    - Uppercase and lowercase letters
    - Numbers
    - Special characters
    """)

    # Initialize session state for password history
    if 'last_password' not in st.session_state:
        st.session_state.last_password = ''
    if 'animation_key' not in st.session_state:
        st.session_state.animation_key = 0

    # Create password input field
    password = st.text_input("Enter your password", type="password", key="password_input")

    # Initialize the password checker
    checker = PasswordStrengthChecker()

    # Create placeholder for live updates
    strength_placeholder = st.empty()
    progress_placeholder = st.empty()
    score_placeholder = st.empty()
    feedback_placeholder = st.empty()
    stats_placeholder = st.empty()

    if password:
        # Check if password changed
        if password != st.session_state.last_password:
            st.session_state.animation_key += 1
            st.session_state.last_password = password

        # Check password strength
        score, feedback = checker.check_strength(password)
        strength, color = checker.get_strength_level(score)

        # Display strength meter with animation
        strength_placeholder.markdown(
            f"""
            <div class="strength-indicator" style="background-color: {color}20; color: {color}; text-align: center;">
                <h3>Password Strength: {strength}</h3>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Animated progress bar
        progress = (score / 12) * 100  # Max score is 12
        progress_placeholder.progress(progress/100)
        
        # Display score
        score_placeholder.markdown(f"**Score:** {score}/12")

        # Display feedback
        feedback_placeholder.markdown("### Feedback:")
        for item in feedback:
            feedback_placeholder.markdown(item)

        # Display password statistics
        stats_placeholder.markdown("### Password Statistics")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Length:** {len(password)} characters")
        with col2:
            st.markdown(f"**Complexity Score:** {score}")

    # Footer
    st.markdown("---")
    st.markdown("""
    💡 **Tips for creating strong passwords:**
    - Use a mix of characters
    - Avoid common words or phrases
    - Avoid keyboard patterns (e.g., qwerty)
    - Avoid sequential characters (e.g., abc123)
    - Make it memorable but not obvious
    - Don't reuse passwords across different accounts
    """)

    # Current timestamp in footer
    st.markdown(f"*Current Time (UTC): {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}*")
    st.markdown(f"*Current User: {st.session_state.get('user', 'clueNA')}*")

if __name__ == "__main__":
    main()