

class Applicant:
    def __init__(self, first_name: str, last_name: str, bio: str, 
                 phone_numbers: list[str], applied_company_name: str, 
                 marital_status: str, bank_account_number: str):
        # Public attributes
        self.first_name = first_name
        self.last_name = last_name
        self.bio = bio
        self.phone_numbers = phone_numbers
        self.applied_company_name = applied_company_name
        self.hired = False  # Initially not hired
        
        # Private attribute
        self.__marital_status = marital_status  # Marital status, kept private
        
        # Protected attribute
        self._bank_account_number = bank_account_number  # Bank account number, protected

    def get_names(self):
        
        return f"{self.first_name} {self.last_name}"

    def get_short_bio(self):
        
        return self.bio[:50]  # Return first 50 characters of bio

    def get_phone_numbers(self, country_code: str):
        
        return ', '.join(self.add_country_code_to_number(country_code, num) for num in self.phone_numbers)

    @staticmethod
    def add_country_code_to_number(country_code: str, phone_number: str) -> str:
        
        return f"(+{country_code}) {phone_number}"

    @property
    def bank_account_number(self):
       
        if self.hired:
            return self._bank_account_number
        raise Prohibited("Access Denied: Not employed.")

    @bank_account_number.setter
    def bank_account_number(self, value: str):
       
        if len(value) == 15 and value.isdigit():
            self._bank_account_number = value
        else:
            raise InvalidAccountNumberError("Bank account number must be a string of exactly 15 digits.")

    @property
    def marital_status(self):
        
        return "Sorry, but I won't be disclosing this information."

    @marital_status.setter
    def marital_status(self, status: str):
        
        if status in ["Married", "Divorced", "Single"]:
            self.__marital_status = status
        else:
            raise ValueError("Marital status must be either 'Married', 'Divorced', or 'Single'.")

    @marital_status.deleter
    def marital_status(self):
        
        confirmation = input("Do you want to delete your marital status? (yes/no): ")
        if confirmation.lower() == 'yes':
            self.__marital_status = ""

    @classmethod
    def from_all_company(cls, company_names: list[str], first_name: str, 
                         last_name: str, bio: str, phone_numbers: list[str], 
                         marital_status: str, bank_account_number: str) -> list['Applicant']:
        
        applicants = []
        for company in company_names:
            applicant = cls(first_name, last_name, bio, phone_numbers, company, marital_status, bank_account_number)
            applicants.append(applicant)
        return applicants

    @classmethod
    def apply_from_cv(cls, cv: dict) -> 'Applicant':
        
        return cls(
            first_name=cv['first_name'],
            last_name=cv['last_name'],
            bio=cv['bio'],
            phone_numbers=cv['phone_numbers'],
            applied_company_name="Unknown",  # Default value or can be set later
            marital_status=cv.get('marital_status', "Not specified"),  # Optional attribute
            bank_account_number=cv.get('bank_account_number', "Not specified")  # Optional attribute
        )

    def display_info(self):
       
        print(f"Name: {self.get_names()}")
        print(f"Short Bio: {self.get_short_bio()}")
        print(f"Phone Numbers: {self.get_phone_numbers('237')}")  # Example country code
        print(f"Applied Company: {self.applied_company_name}")
        print(f"Hired: {self.hired}")



if __name__ == "__main__":
    # Creating an applicant using individual attributes
    applicant = Applicant(
        first_name="John",
        last_name="Doe",
        bio="A passionate software developer with a keen interest in artificial intelligence and machine learning.",
        phone_numbers=["1234567890", "0987654321"],
        applied_company_name="Tech Innovations",
        marital_status="Single",
        bank_account_number="123456789012345"
    )

    applicant.display_info()  # Display non-sensitive info
    print("Concatenated Name:", applicant.get_names())  # Display concatenated name

    # Setting and getting marital status
    try:
        applicant.marital_status = "Married"
        print("Marital Status:", applicant.marital_status)  # Get marital status
    except ValueError as e:
        print(e)

    # Deleting marital status
    del applicant.marital_status

    # Attempting to get bank account number
    try:
        print("Bank Account Number:", applicant.bank_account_number)  # Attempt to get bank account number
    except Prohibited as e:
        print(e)

    # Creating multiple applicants for different companies
    company_list = ["Company A", "Company B", "Company C"]
    applicants = Applicant.from_all_company(
        company_names=company_list,
        first_name="Jane",
        last_name="Smith",
        bio="An experienced data scientist.",
        phone_numbers=["3216540987"],
        marital_status="Married",
        bank_account_number="987654321098765"
    )

    for app in applicants:
        app.display_info()  # Display info for each applicant

    # Applying from CV
    cv = {
        'first_name': 'John', 
        'last_name': 'Piet',
        'bio': 'I am a software engineer with over 5 years of experience. I am specialized in web and mobile application. My languages are Python, JavaScript, and PHP.',
        'phone_numbers': ['23434324', '74736648', '282737647'],
        'marital_status': 'Single',
        'bank_account_number': '555555555555555'  # Adding optional attributes
    }

    applicant_from_cv = Applicant.apply_from_cv(cv)
    applicant_from_cv.display_info()  # Display the information from the CV
