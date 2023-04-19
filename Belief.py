
def reverse_inquiry(belief):
    return "I am " + "not "*(belief.endswith("enough")) + "enough"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        belief = request.form['belief']
        reverse_belief = reverse_inquiry(belief)
        return f"Original belief: {belief}<br>Flipped belief: {reverse_belief}"
    else:
        return '''
            <form method="post">
                <label for="belief">Enter the belief or thought that causes you distress or discomfort:</label>
                <input type="text" id="belief" name="belief">
                <br>
                <input type="submit" value="Flip Belief">
            </form>
        '''

@app.route('/observe')
def observe():
    return '''
        <form method="post" action="/observe">
            <p>Continue observing and witnessing your thoughts and feelings as they arise. Press Enter when you're ready to move on...</p>
            <input type="submit" value="Next">
        </form>
    '''

@app.route('/shift', methods=['POST'])
def shift():
    answer = request.form['answer']
    if answer.lower() == 'y':
        return "Congratulations!"
    elif answer.lower() == 'n':
        return '''
            <form method="post" action="/observe">
                <p>Have you noticed a shift in your perception of yourself? (y/n)</p>
                <input type="text" id="answer" name="answer">
                <input type="submit" value="Submit">
            </form>
        '''
    else:
        return "Invalid input. Please enter 'y' or 'n'."

if __name__ == '__main__':
    app.run()
