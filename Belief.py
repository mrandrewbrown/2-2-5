

def reverse_inquiry(belief):
    return "I am " + "not "*(belief.endswith("enough")) + "enough"
                    

belief = input("Enter the belief or thought that causes you distress or discomfort: ")
reverse_belief = reverse_inquiry(belief)


input("Now, Pull up VIPs.  Reverse the belief and say it out loud to yourself and press Enter to continue...")

# Wait for the person to press Enter before continuing
input("Sit quietly and observe your thoughts and feelings as they arise in response to the original belief or thought. Press Enter to continue when you're ready...")

# Loop until the person notices a shift in their perception of themselves
while True:
    # Ask the person to observe their thoughts and feelings without judgment or resistance
    input("Continue observing and witnessing your thoughts and feelings as they arise. Press Enter when you're ready to move on...")

    # Check if the person noticed a shift in their perception of themselves
    answer = input("Have you noticed a shift in your perception of yourself? (y/n) ")
    if answer.lower() == "y":
        print("Congratulations!")
        break
    elif answer.lower() == "n":
        continue
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
