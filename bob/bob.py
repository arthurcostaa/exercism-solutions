def response(hey_bob):
    hey_bob = hey_bob.strip()

    if not hey_bob:
        return 'Fine. Be that way!'

    is_shout = hey_bob.isupper()
    is_question = hey_bob.endswith('?')

    if  is_question and is_shout:
        return 'Calm down, I know what I\'m doing!'
    elif is_question:
        return 'Sure.'
    elif is_shout:
        return 'Whoa, chill out!'

    return 'Whatever.'
