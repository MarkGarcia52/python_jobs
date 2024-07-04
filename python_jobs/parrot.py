# How the input() function works

# Pauses your program and waits for the user to enter some text

# Python receives user input, it assigns that input to a vairbale ot make it conveinant for you to work with

#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)

# It takes one argument: the prompt, that we want to display to the user
# So they know kind of information to enter

# It literally pauses and you enter in the terminal

# Writing clear prompts

# Each time you use the input() function, you should include a clear, easy-to-follow
# prompt that tells the user exactly what kind of information you're looking for

# Letting the user choose when to quit:

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

