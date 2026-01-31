import re
from zxcvbn import zxcvbn

class PasswordChecker:
    def __init__(self):
        # Traditional criteria for detailed feedback
        self.criteria = {
            "length": lambda p: len(p) >= 12,
            "uppercase": lambda p: any(c.isupper() for c in p),
            "lowercase": lambda p: any(c.islower() for c in p),
            "digit": lambda p: any(c.isdigit() for c in p),
            "special": lambda p: any(not c.isalnum() for c in p)
        }

    def assess(self, password):
        # 1. Get the Advanced Strength Score (0 to 4)
        # zxcvbn checks patterns, keyboard paths, and dictionaries
        results = zxcvbn(password)
        score = results['score']
        crack_time = results['crack_times_display']['offline_fast_hashing_1e10_per_second']
        
        # 2. Check traditional complexity rules
        failed_criteria = [name for name, check in self.criteria.items() if not check(password)]
        
        # 3. Generate Feedback
        strength_map = {0: "⚠️ Dangerous", 1: "❌ Weak", 2: "🟠 Fair", 3: "🟢 Good", 4: "💎 Very Strong"}
        
        print(f"--- Password Assessment ---")
        print(f"Overall Strength: {strength_map[score]}")
        print(f"Estimated time to crack (Brute Force): {crack_time}")
        
        if failed_criteria:
            print("\nSuggestions to improve:")
            for item in failed_criteria:
                print(f" - Add more {item}" if item != "length" else " - Make it longer (12+ chars)")
        
        # zxcvbn also provides specific warnings (e.g., "This is a common name")
        if results['feedback']['warning']:
            print(f"Warning: {results['feedback']['warning']}")

# --- Execution ---
if __name__ == "__main__":
    checker = PasswordChecker()
    user_pw = input("Enter a password to test: ")
    checker.assess(user_pw)