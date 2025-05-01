

def wrap_with(tag):
    def add_new_tag(func):
        def wrapper(*args, **kwargs):
           
            return f'<p><em>Hello,<{tag}>James Brown</{tag}>!</em></p>'
        
        return wrapper
    return add_new_tag




@wrap_with(tag="strong")
def get_custom_html_greeting(first, last):
    return f'Hello,{first} , {last}'

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
