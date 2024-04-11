from Classes.Case_fields import case_name, attorney_info, applicant_info, filing_info, decedent_info, interested_person

class CaseInformation:
    def __init__(self):
        self.case_name = case_name
        self.attorney_info = attorney_info
        self.applicant_info = applicant_info
        self.filing_info = filing_info
        self.decedent_info = decedent_info
        self.interested_person = interested_person
        self.interested_persons = []

        
    def add_interested_person(self, person):
        self.interested_persons.append(person)
        
    def get_full_address(self, person):
        address_k = 'Street Address'
        city_k = 'City'
        state_k = 'State'
        zip_k = 'Zip' 
        add =  person[address_k]
        city = person[city_k] 
        state = person[state_k]
        zip = person[zip_k]
        full_add = add + ' \n' + city + ', ' + state + ' ' + zip
        return full_add

    def get_full_name(self, person):
        f_name = 'First Name'
        m_name = 'Middle Name'
        l_name = 'Last Name'
        name = 'Name'
        if f_name in person.keys():
            first_name = str(person[f_name])
            middle_name = str(person[m_name])
            last_name = str(person[l_name])
            full_name = first_name + ' ' + middle_name + ' ' + last_name
        elif name in person.keys():
            full_name = str(person['Name'])
        else:
            full_name = ''
        return full_name
        
    def get_name_address_phone(self, person, bar = False):
        phone_k = 'Telephone'
        bar_k = 'Bar Number'
        full_name = self.get_full_name(person) + '\n'
        address = self.get_full_address(person) + '\n'
        bar_no = ''
        if bar:
            bar_no = person[bar_k] + '\n'
        full_name + bar_no + address + person[phone_k]

    def get_attorney_info(self, attorney):
        self.attorney_info = attorney.attorney_info

    # Editable Below This Comment