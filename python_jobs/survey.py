class AnonymousSurvey:
    """Collect anonymous answers to a survey question"""

    def __init__(self, question): #1
        """Store a question, and preapre to store responses."""
        self.question = question
        self.responses = []

    def show_question(self): #2
        """Show the survey question."""
        print(self.question)

    def store_responses(self, new_response): #3
        """Store a single response to the survey."""
        self.responses.append(new_response)
    
    def show_results(self): #4
        """Show all the respones that have been given."""
        print("Survey Results:")
        for response in self.responses:
            print(f"- {response}")

# 1 
    # The class starts with a survey question that you provide and includes
    # An empty list to store responses
            
# 2
    # The class has methods to print the survey question

# 3
    # Add a new response to the list
            
# 4
    # And print all the reponses stored in the list
            
# To create an instance, all you have to provide is a question and display using show_question()
# Once that's created, you can store a response using store_response()
# And show results using show_results()
            

            
