settings = {'Title':'Afghanistan'}

def change_site_title(new_title):
    settings['Title']=new_title


print(settings)
change_site_title("A new fancy title")
print(settings)