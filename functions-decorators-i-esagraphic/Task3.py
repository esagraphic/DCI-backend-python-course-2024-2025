def make_bold(func):
    def wrapper(*args, **kwargs):
        new_text =  func(*args,**kwargs)
        return f'<strong> {new_text} </strong>'
        
    return wrapper

def make_italics(func):
    def wrapper(*args,**kwargs):
        text = func(*args,**kwargs)

        return f'<em>{text}<em>'
    return wrapper

def make_paragraph(func):
    def wrapper(*args,**kwargs):
        text = func(*args,**kwargs)

        return f'<p>{text}</p>'
    return wrapper


@make_bold
def get_html_greeting():
    return f'Hello World'


@make_paragraph
@make_italics
# @make_bold
def get_custom_html_greeting(first, last):
    return f'Hello,<strong>{first} , {last}</strong>'

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
