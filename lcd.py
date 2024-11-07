from  grove.display.jhd1802 import JHD1802
import time

# Initialize the Grove LCD
lcd = JHD1802()

# Function to display a message on the LCD
def display_message(line1, line2):
    lcd.setCursor(0, 0)   # Set cursor to the first line
    lcd.write(line1)       # Display first line of text
    lcd.setCursor(1, 0)   # Set cursor to the second line
    lcd.write(line2)       # Display second line of text

# lcd.clear()
# Display a message
display_message("Hello, world!", 'Raspberry PI')

# Hold the message for a few seconds
time.sleep(5)

# Clear the display before exiting
lcd.clear()
