def profile(name, age, *skills, location="Unknown", **additional_info):
    print(f'Name: {name}')
    print(f'Age : {age}')
    skills_str = ", ".join(skills)
    print(f'Skills: {skills_str}')  
    print(f'Location: {location}')
    for key , value in additional_info.items():
        print(f'{key}: {value}')

# profile("Maxim", 35, "C++", "SQL")

profile("Simona", 28, "Python", "Java", location="New York", hobby="Painting", job="Developer")
