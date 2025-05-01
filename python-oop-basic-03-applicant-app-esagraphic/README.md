## Exercise Covers
- Access Modifiers
- Method types
- Getters and Setters

## Applicant App

Imagine that you are the object applying for a job and the recruiters are other objects interacting with you. You as the applicant wants a clear definitions of your responsibility and have very strong preference for privacy.

You won't let other objects(recruiters) have access to sensitive information about you unless you feel it is in your best interest for them to have it.

You won't give them the impression that you can do something, when you can't, or you won't allow them to abuse you by giving you tasks that are not specific to your responsibility. Hence, you will provide an interface that is specific to your responsibility.

**NB**: All your code should be in the `applicant.py` file.

1. Create a class called `Applicant`

### Access Modifiers
Now, You want to control access to some of your attributes. Implement the following in the `__init__` method

2. Which of your attributes would you like to make `public`? Add two more to the list below
    - first_name: `str`
    - last_name: `str`
    - bio: `str`
    - phone_numbers: `list[str]`
    - applied_company_name: `str`
    - hired: `bool`
    
3. Which of your attributes would you like to keep `private` or you think is not necessary for your interviewer to know. Add two more to the list below
    - marital_status: `str`
4. Which of your attributes would you like to `protect`, so that you only give it if employed. Add two more to the list below
    - bank_account_number: `str`

### Method Types

5. **Instance Methods**
- Introduce a method `get_names` that will return the concatination of the first and last name.
- Your `bio` is too long, you want your interviewer to receive the first 50 characters of your bio. Introduce a method `get_short_bio`
-  The attribute `phone_numbers` happens to be a list of phone numbers. But you want to display it in a good looking format. Introduce a method `get_phone_numbers` and format it however you want.
- `Get inspired`: Introduce two more methods

6. **Class Methods**
- You need a method that will enable you to create applicant objects for all the companies you provide. Call the method `from_all_company`. This method should take an argument `company_names: list[str]` which is a list of company names to create objects for. It should also take all the arguments neccessary to create an applicant object

```python
def company_names(cls, company_names: list[str], first_name: str, last_name: str, .....) -> list[Applicant]:
    ...
```
- Given that you have a `cv` that looks like the dictionary below. Intrduce a class method `apply_from_cv` that will take in the `cv` as an argument and extract information from the `cv` and create an applicant object.

```python
cv = {
    'first_name': 'John', 
    'last_name': 'Piet',
    'bio': 'I am a software engineer with over 5 years of experience. I am specialized in web and mobile application. My languages are Python, JavsScript and PHP'
    'phone_numbers': ['23434324', '74736648', '282737647']
    # TODO: add the two more attributes you completed in quest 2 above
}
```

- `Gets inspired`: Intoduce one more class methods of your choice


7. **Static Methods**
    - Your phone numbers do not have country code. You need a helper function that will take in two arguments. `country_code` and `phone_number`. The helper function should concatinate the strings and return a phone number with the country code

```python
def add_country_code_to_number(country_code, phone_number):
    # TODO: Your code goes here
    

# Example
add_country_code_to_number('237', '647364834') # output: '(+237) 647364834'
```
- Use this helper function to help you better format your phone numbers in the `get_phone_numbers` method of question 5.

### Getters and Setters

8. Using the Pythonic way, create getters and setters for the protected attribute `bank_account_number`. 
- The getter should return bank account only if `hired` is set to `True`. Else, raise a custom exception called `Prohibited` or any built-in exception that makes sense.
- The setter should make sure the bank account number is a string of exactly 15 numbers. Else, raise a custom exception called `InvalidAccountNumberError` or any built-in exception that makes sense.

9. Using the Pythonic way, create a getter, setter and deleter for the private attribute `marital_status`.

- The getter will return a nice message when a recruiter tries to access this attribute. The message will be: `Sorry, but I won't be disclosing this information`.
- The setter should check that the value to be assigned to `marital_status` is either `Married`, `Divorced` or `Single`. Riase the built-in exception `ValueError` otherwise.
- The deleter should prompt(using the `input` function) the applicant if he/she wants to delete this value. If yes, then the `marital_status` should be set to an empty string.