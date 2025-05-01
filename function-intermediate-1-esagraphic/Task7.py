def update_settings(**kwargs):
    setting = {'theme':'light','notifications':'true','language':'Eng'}

    for key, value in kwargs.items():
        if key in setting:
            setting[key] = value
    
    return setting

# Test cases
# print(update_settings(theme="dark"))
print(update_settings(notifications=False, language="Spanish"))