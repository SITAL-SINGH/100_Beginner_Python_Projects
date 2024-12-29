import time

def countdown_animation():
    for i in range(3, 0, -1):
        print(i, end='', flush=True)
        time.sleep(1)  # Wait for 1 second
        print('\r', end='', flush=True)  # Carriage return to overwrite the line
    print("Go!")

# Call the function to see the animation
countdown_animation()