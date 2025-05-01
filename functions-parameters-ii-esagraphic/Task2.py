settings = {'Title': 'My original title'}
default_settings = {'Title': 'My original title'}

def change_site_title(new_title):
    global settings
    settings['Title'] = new_title

def get_title(my_dic=None):
    if my_dic is None:
        my_dic = default_settings
    return my_dic['Title']

print(get_title(settings))  
print(get_title())       
change_site_title("A new fancy title")
print(get_title(settings))  
print(get_title())         
