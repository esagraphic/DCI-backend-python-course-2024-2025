


def make_bold(func):
    def wrapper(*args):
        new_text =  func(*args)
        return f'<strong> {new_text} </strong>'
    return wrapper

@make_bold
def get_html_greeting():
    return f'Hello World'



print(get_html_greeting())
