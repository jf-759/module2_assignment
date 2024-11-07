from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/>
        What toppings would you like on your Fro-Yo?
        <input type="text" name="toppings"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/froyo_results')
def show_froyo_results():
    users_froyo_flavor = request.args.get('flavor')
    users_froyo_toppings = request.args.get('toppings')
    return f'You ordered {users_froyo_flavor} flavored Fro-Yo with {users_froyo_toppings} on top!'

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color?
        <input type="text" name="color"><br/>
        What is your favorite animal?
        <input type="text" name="animal"><br/>
        What is your favorite city?
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    users_color = request.args.get('color')
    users_animal = request.args.get('animal')
    users_city = request.args.get('city')
    return f"Wow, I didn't know {users_color} {users_animal} lived in {users_city}!"

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    
    <form action = "message_results" method = "POST">
        Please enter your secret message:
        <input type = "text" name = "message" required><br/>
        <button type = "submit">Submit</button>
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    message = request.form['message']
    sorted_message = sort_letters(message)
    return f"Here's your secret message! <br/> {sorted_message}" 

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    operand1 = request.args.get('operand1', type = int)
    operand2 = request.args.get('operand2', type = int)
    operation = request.args.get('operation')

    if operation == 'add':
        result = operand1 + operand2
        op_symbol = '+'
    elif operation == 'subtract':
        result = operand1 - operand2
        op_symbol = '_'
    elif operation == 'multiply':
        result = operand1 * operand2
        op_symbol = '*'
    elif operation == 'divide':
        if operand2 == 0:
            return "Error: Division by zero is not allowed."
        result = operand1 / operand2
        op_symbol = '/'
    else:
        return "Error: Invalid operation."

    
    return render_template('calculator_results.html', operand1 = operand1, operand2 = operand2, operation = operation, op_symbol = op_symbol, result = result)


HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope_results', methods=['GET'])
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""

    # Get the user's name and the selected horoscope sign from the query string
    users_name = request.args.get('users_name')
    horoscope_sign = request.args.get('horoscope_sign')

    # Look up the user's personality in the HOROSCOPE_PERSONALITIES dictionary
    users_personality = HOROSCOPE_PERSONALITIES.get(horoscope_sign, "Personality not found.")

    # Generate a random lucky number from 1 to 99
    lucky_number = random.randint(1, 99)

    # Prepare context to pass to the template
    context = {
        'users_name': users_name,
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number
    }

    # Render the results in the horoscope_results.html template
    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
