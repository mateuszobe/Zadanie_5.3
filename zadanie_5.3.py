from faker import Faker

# Generator danych
fake = Faker()

# Główna klasa dla wizytówki
class Contact:
    def __init__(self, first_name, last_name, email, company, position):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.company = company
        self.position = position

# Klasa bazowa wizytówki (dziedziczy z Contact)
class BaseContact(Contact):
    def __init__(self, first_name, last_name, email, company, position, private_phone):
        super().__init__(first_name, last_name, email, company, position)
        self.private_phone = private_phone

    def contact(self):
        print(f"Wybieram numer +48 {self.private_phone} i dzwonię do {self.first_name} {self.last_name}")

    @property
    def label_length(self):
        return len(f"{self.first_name} {self.last_name}")

# Klasa biznesowa wizytówki (dziedziczy z Contact)
class BusinessContact(Contact):
    def __init__(self, first_name, last_name, email, company, position, work_phone):
        super().__init__(first_name, last_name, email, company, position)
        self.work_phone = work_phone

    def contact(self):
        print(f"Wybieram numer +48 {self.work_phone} i dzwonię do {self.first_name} {self.last_name}")

    @property
    def label_length(self):
        return len(f"{self.first_name} {self.last_name}")

# Funkcja do generowania wizytówek
def create_contacts(contact_type, quantity):
    contacts = []
    for _ in range(quantity):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        private_phone = fake.phone_number()

        if contact_type == 'base':
            contact = BaseContact(
                first_name=first_name,
                last_name=last_name,
                email=email,
                company=company,
                position=position, 
                private_phone=private_phone
            )
        elif contact_type == 'business':
            work_phone = fake.phone_number()
            company = fake.company()
            position = fake.job()
            contact = BusinessContact(
                first_name=first_name,
                last_name=last_name,
                email=email,
                company=company,
                position=position,
                work_phone=work_phone
            )
        else:
            raise ValueError("Unknown contact type. Use 'base' or 'business'.")
        
        contacts.append(contact)
    return contacts

# Testowanie kodu 
if __name__ == "__main__":
    base_contacts = create_contacts('base', 2)
    business_contacts = create_contacts('business', 2)

    # Wywołanie metody contact oraz label_length (+1 dla spacji) dla przykładowej wizytówki
    for contact in base_contacts + business_contacts:
        contact.contact()
        print("Label length:", contact.label_length)
