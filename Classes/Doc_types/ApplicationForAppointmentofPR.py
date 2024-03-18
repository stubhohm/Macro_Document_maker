#from ..CaseInformation import CaseInformation
name = 'name'
address = 'Street_address'
city = 'City'
county = 'County' 
state = 'State'
zip = 'Zip' 
bar_no = 'bar_no'
tele = 'telephone'
f_name = 'first_name'
m_name = 'middle_name'
l_name = 'last_name'
rel = 'relation'

court_county = 'Probate_Court_County'
deat_cert_attach = 'death_cert_attached'
death_cert_avail = 'death_cert_available'
MCL = 'MCL_7003311'

death_date = 'date_of_death'
death_time = 'time_of_death'
will_date = 'will_date'

age_if_minor ='AGE_if_minor'
legal_dis = 'Legal_disability'
legal_rep ='REPRESENTED BY Name address and capacity'


class ApplicationForAppointmentofPR:
     
    def __init__(self) -> None:
        pass
        self.name = 'Application for Appointment of PR'
        self.doc_path ='ApplicationForAppointmentofPR.pdf'
        self.fields = {
    'STATE OF MICHIGAN PROBATE COURT COUNTY': {'State'}, 
    'First middle and last name': {'First middle and last name'},
    'Petitioners name address and telephone no': {''}, 
    'Petitioners attorney bar no address and telephone no': {}, 
    'Name of applicant': {'applicant name'}, 
    'Relationship to decedent ie heir devisee child spouse creditor beneficiary etc': {}, 
    'Date of death': {}, 
    'Time if known': {}, 
    'CityTownshipVillage': {}, 
    'County': {}, 
    'State': {},
    'A death certificate has been issued and a copy accompanies this application as a separate document': {}, 
    'No death certificate is available Attached is alternative documentation of the decedents death': {}, 
    'NAMERow1': {}, 
    'Street address': {},
    'City': {}, 
    'State_2': {}, 
    'Zip': {}, 
    'RELATIONSHIPRow1': {}, 
    'AGE if minorRow1': {}, 
    'NAMERow2': {}, 
    'Street address_2': {}, 
    'City_2': {},
    'State_3': {}, 
    'Zip_2': {}, 
    'RELATIONSHIPRow2': {}, 
    'AGE if minorRow2': {}, 
    'NAMERow3': {}, 
    'Street address_3': {}, 
    'City_3': {}, 
    'State_4': {}, 
    'Zip_3': {}, 
    'RELATIONSHIPRow3': {}, 
    'AGE if minorRow3': {}, 
    'NAMERow4': {},
    'Street address_4': {}, 
    'City_4': {}, 
    'State_5': {}, 
    'Zip_4': {}, 
    'RELATIONSHIPRow4': {}, 
    'AGE if minorRow4': {}, 
    'NAMERow1_2': {}, 
    'LEGAL DISABILITYRow1': {}, 
    'REPRESENTED BY Name address and capacityRow1': {},
    'NAMERow2_2': {}, 
    'LEGAL DISABILITYRow2': {}, 
    'REPRESENTED BY Name address and capacityRow2': {}, 
    'NAMERow3_2': {}, 
    'LEGAL DISABILITYRow3': {}, 
    'REPRESENTED BY Name address and capacityRow3': {},
    'a Venue is proper in this county because the decedent was domiciled in this county on the date of death': {}, 
    'b The decedent was not domiciled in Michigan but venue is proper in this county because property of the decedent': {}, 
    'a The decedent died intestate and after exercising reasonable diligence I am unaware of any unrevoked testamentary': {}, 
    'b I am aware of an unrevoked testamentary instrument relating to property located in this state as defined under': {}, 
    'c The decedents will dated': {}, 
    'd An authenticated copy of the will and codicils if any probated in': {}, 
    'application according to MCL 7003311': {}, 
    'is already in the courts possession': {}, 
    'isare offered for probate and': {}, 
    'undefined': {}, 
    'isare attached to this application': {}, 
    'isare already in the courts': {}, 
    'County_2': {}, 
    'State_6': {}, 
    'and the appointment has not been terminated  The personal representatives name and address are': {}, 
    'State_7': {}, 
    '8 A personal representative has been previously appointed in': {}, 
    '9 I nominate': {}, 
    '10 Other persons have prior or equal right to appointment as personal representative They are': {}, 
    'Name': {}, 
    'Address': {}, 
    'City_5': {}, 
    'Name_2': {}, 
    'Hisher address is': {}, 
    'Address_2': {}, 
    'City_6': {}, 
    'Name_3': {}, 
    'Name_4': {}, 
    'Name_5': {}, 
    'Name_6': {}, 
    '11 The will expressly requests that the personal representative serve with bond': {}, 
    '12 A special personal representative is necessary because': {}, 
    'undefined_3': {}, 
    '13 Informal probate of the will': {}, 
    '14 Informal appointment of the nominated personal representative': {}, 
    '15 The appointment of a special personal representative pending the appointment of the nominated personal': {}, 
    'with': {}, 
    'without': {}, 
    'Date': {}, 
    'Date_2': {}, 
    'Judge': {}, 
    'Text2': {}, 
    'Text3': {}, 
    'CASE NO': {}, 
    # Case No '/Kids': [IndirectObject(176, 0, 2986483403712), IndirectObject(121, 0, 2986483403712), IndirectObject(133, 0, 2986483403712)]
    'Text4': {}, 
    'Text5': {},
    }
        
    def update_fields(self, case_information, existing_fields):
        #case_information = CaseInformation()
        existing_fields['STATE OF MICHIGAN PROBATE COURT COUNTY'] = case_information.filing_info[court_county]
        
        first_name = str(case_information.decedent_info[f_name])
        middle_name = str(case_information.decedent_info[m_name])
        last_name = str(case_information.decedent_info[l_name])
        full_name = first_name + ' ' + middle_name + ' ' + last_name 
        existing_fields['First middle and last name'] = full_name

        first_name = case_information.applicant_info[f_name]
        middle_name = case_information.applicant_info[m_name]
        last_name = case_information.applicant_info[l_name]
        app_name = first_name + ' ' + middle_name + ' ' + last_name + '\n'
        # Address
        app_add =  case_information.applicant_info[address]
        app_city = case_information.applicant_info[city] 
        app_state = case_information.applicant_info[state]
        app_zip = case_information.applicant_info[zip]
        app_full_add = app_add + ' ' + app_city + ', ' + app_state + ' ' + app_zip + '\n'
        app_tele = case_information.applicant_info[tele]
        existing_fields['Petitioners name address and telephone no'] = app_name + app_full_add + app_tele
        
        att_name = case_information.attorney_info[name]
        att_bar = case_information.attorney_info[bar_no] + '\n'
        att_full_add = case_information.attorney_info[address] + ' ' + case_information.attorney_info[city] + ', ' + case_information.attorney_info[state] + ' ' + case_information.attorney_info[zip] + '\n'
        att_tele = case_information.attorney_info[tele]
        existing_fields['Petitioners attorney bar no address and telephone no'] =  att_name + att_bar + att_full_add + att_tele 

        existing_fields['Name of applicant']= case_information.applicant_info[f_name] + ' ' + case_information.applicant_info[l_name] 
        existing_fields['Relationship to decedent ie heir devisee child spouse creditor beneficiary etc'] = case_information.applicant_info[rel]
        existing_fields['Date of death'] = case_information.decedent_info[death_date] 
        existing_fields['Time if known'] = case_information.decedent_info[death_time]
        existing_fields['CityTownshipVillage'] = case_information.decedent_info[city]
        existing_fields['County'] = case_information.decedent_info[county]
        existing_fields['State'] = case_information.decedent_info[state]
        existing_fields['A death certificate has been issued and a copy accompanies this application as a separate document'] = ""
        existing_fields['No death certificate is available Attached is alternative documentation of the decedents death'] = ""
        existing_fields['NAMERow1'] = case_information.Interested_persons[0][name]
        existing_fields['Street address'] = case_information.Interested_persons[0][address]
        existing_fields['City'] = case_information.Interested_persons[0][city] 
        existing_fields['State_2'] = case_information.Interested_persons[0][state]  
        existing_fields['Zip'] = case_information.Interested_persons[0][zip]  
        existing_fields['RELATIONSHIPRow1'] = case_information.Interested_persons[0][rel] 
        existing_fields['AGE if minorRow1'] = case_information.Interested_persons[0][age_if_minor]  
        existing_fields['NAMERow2'] = case_information.Interested_persons[1][name]
        existing_fields['Street address_2'] = case_information.Interested_persons[1][address] 
        existing_fields['City_2'] = case_information.Interested_persons[1][city]
        existing_fields['State_3'] = case_information.Interested_persons[1][state]
        existing_fields['Zip_2'] = case_information.Interested_persons[1][zip]
        existing_fields['RELATIONSHIPRow2'] = case_information.Interested_persons[1][rel]
        existing_fields['AGE if minorRow2'] = case_information.Interested_persons[1][age_if_minor]
        existing_fields['NAMERow3'] = case_information.Interested_persons[2][name]
        existing_fields['Street address_3'] = case_information.Interested_persons[2][address]
        existing_fields['City_3'] = case_information.Interested_persons[2][city]
        existing_fields['State_4'] = case_information.Interested_persons[2][state]
        existing_fields['Zip_3'] = case_information.Interested_persons[2][zip]
        existing_fields['RELATIONSHIPRow3'] = case_information.Interested_persons[2][rel]
        existing_fields['AGE if minorRow3'] = case_information.Interested_persons[2][age_if_minor]
        existing_fields['NAMERow4']= case_information.Interested_persons[3][name]
        existing_fields['Street address_4'] = case_information.Interested_persons[3][address]
        existing_fields['City_4'] = case_information.Interested_persons[3][city]
        existing_fields['State_5'] = case_information.Interested_persons[3][state]
        existing_fields['Zip_4'] = case_information.Interested_persons[3][zip]
        existing_fields['RELATIONSHIPRow4'] = case_information.Interested_persons[3][rel]
        existing_fields['AGE if minorRow4'] = case_information.Interested_persons[3][age_if_minor]
        
        disabled_count = 0
        for person in case_information.Interested_persons:
            if person[legal_dis]:
                if disabled_count == 2:
                    existing_fields['NAMERow3_2'] = person[name]
                    existing_fields['LEGAL DISABILITYRow3'] = person[legal_dis]
                    existing_fields['REPRESENTED BY Name address and capacityRow3'] = person[legal_rep]
                    disabled_count = 3
                if disabled_count == 1:
                    existing_fields['NAMERow2_2'] = person[name] 
                    existing_fields['LEGAL DISABILITYRow2'] = person[legal_dis]
                    existing_fields['REPRESENTED BY Name address and capacityRow2'] = person[legal_rep]
                    disabled_count = 2
                if disabled_count == 0:
                    existing_fields['NAMERow1_2'] = person[name] 
                    existing_fields['LEGAL DISABILITYRow1'] = person[legal_dis] 
                    existing_fields['REPRESENTED BY Name address and capacityRow1'] = person[legal_rep]
                    disabled_count = 1
                
             
        existing_fields['a Venue is proper in this county because the decedent was domiciled in this county on the date of death'] = '' 
        existing_fields['b The decedent was not domiciled in Michigan but venue is proper in this county because property of the decedent'] = '' 
        existing_fields['a The decedent died intestate and after exercising reasonable diligence I am unaware of any unrevoked testamentary'] = '' 
        existing_fields['b I am aware of an unrevoked testamentary instrument relating to property located in this state as defined under'] = '' 
        existing_fields['c The decedents will dated'] = case_information.decedent_info[will_date] 
        existing_fields['d An authenticated copy of the will and codicils if any probated in'] = "" 
        existing_fields['application according to MCL 7003311'] = case_information.decedent_info[MCL] 
        existing_fields['is already in the courts possession']  = ''
        existing_fields['isare offered for probate and'] = ''
        existing_fields['undefined'] =case_information.decedent_info[will_date]
        existing_fields['isare attached to this application'] ='' 
        existing_fields['isare already in the courts'] ='' 
        existing_fields['County_2'] ='' 
        existing_fields['State_6'] ='' 
        existing_fields['and the appointment has not been terminated  The personal representatives name and address are'] ='' 
        existing_fields['State_7'] ='' 
        existing_fields['8 A personal representative has been previously appointed in'] ='' 
        existing_fields['9 I nominate'] ='' 
        existing_fields['10 Other persons have prior or equal right to appointment as personal representative They are'] ='' 
        existing_fields['Name'] ='' 
        existing_fields['Address'] ='' 
        existing_fields['City_5'] ='' 
        existing_fields['Name_2'] ='' 
        existing_fields['Hisher address is'] ='' 
        existing_fields['Address_2'] ='' 
        existing_fields['City_6'] ='' 
        existing_fields['Name_3'] ='' 
        existing_fields['Name_4'] ='' 
        existing_fields['Name_5'] ='' 
        existing_fields['Name_6'] ='' 
        existing_fields['11 The will expressly requests that the personal representative serve with bond'] ='' 
        existing_fields['12 A special personal representative is necessary because'] ='' 
        existing_fields['undefined_3'] ='' 
        existing_fields['13 Informal probate of the will'] ='' 
        existing_fields['14 Informal appointment of the nominated personal representative'] ='' 
        existing_fields['15 The appointment of a special personal representative pending the appointment of the nominated personal'] ='' 
        existing_fields['with'] ='' 
        existing_fields['without'] ='' 
        existing_fields['Date'] ='' 
        existing_fields['Date_2'] ='' 
        existing_fields['Judge'] ='' 
        existing_fields['Text2'] ='' 
        existing_fields['Text3'] ='' 
        existing_fields['CASE NO'] ='' 
        # Case No '/Kids'] [IndirectObject(176, 0, 2986483403712), IndirectObject(121, 0, 2986483403712), IndirectObject(133, 0, 2986483403712)]
        existing_fields['Text4'] ='' 
        existing_fields['Text5'] =''
 
'''

{'STATE OF MICHIGAN PROBATE COURT COUNTY': {'/T': 'STATE OF MICHIGAN PROBATE COURT COUNTY', '/FT': '/Tx', '/TU': 'STATE OF MICHIGAN PROBATE COURT COUNTY', '/Ff': 8388608}, 'First middle and last name': {'/T': 'First middle and last name', '/FT': '/Tx', '/TU': 'First, middle, and last name', '/Ff': 8388608}, 'Petitioners name address and telephone no': {'/T': 'Petitioners name address and telephone no', '/FT': '/Tx', '/TU': 'Petitioner’s name, address and telephone no.', '/Ff': 8392704}, 'Petitioners attorney bar no address and telephone no': {'/T': 'Petitioners attorney bar no address and telephone no', '/FT': '/Tx', '/TU': 'Petitioner’s attorney, bar no., address, and telephone no.', '/Ff': 8392704}, 'Name of applicant': {'/T': 'Name of applicant', '/FT': '/Tx', '/TU': 'Name of applicant', '/Ff': 8388608}, 'Relationship to decedent ie heir devisee child spouse creditor beneficiary etc': {'/T': 'Relationship to decedent ie heir devisee child spouse creditor beneficiary etc', 
'/FT': '/Tx', '/TU': 'Relationship to decedent, i.e., heir, devisee, child, spouse, creditor, beneficiary, etc', '/Ff': 8388608}, 'Date of death': {'/T': 'Date of death', '/FT': '/Tx', '/TU': 'Date 
of death', '/Ff': 8388608}, 'Time if known': {'/T': 'Time if known', '/FT': '/Tx', '/TU': 'Time (if known', '/Ff': 8388608}, 'CityTownshipVillage': {'/T': 'CityTownshipVillage', '/FT': '/Tx', '/TU': 'City/Township/Village', '/Ff': 8388608}, 'County': {'/T': 'County', '/FT': '/Tx', '/TU': 'County', '/Ff': 8388608}, 'State': {'/T': 'State', '/FT': '/Tx', '/TU': 'State', '/Ff': 8388608}, 'A death certificate has been issued and a copy accompanies this application as a separate document': {'/T': 'A death certificate has been issued and a copy accompanies this application as a separate document', '/FT': '/Btn', '/TU': 'A death certificate has been issued, and a copy accompanies this application as a separate document'}, 'No death certificate is available Attached is alternative documentation of the decedents death': {'/T': 'No death certificate is available Attached is alternative documentation of the decedents death', '/FT': '/Btn', '/TU': 'No death certificate is available. Attached is alternative documentation of the decedent’s death'}, 'NAMERow1': {'/T': 'NAMERow1', '/FT': '/Tx', '/TU': 'NAME_Row_1', '/Ff': 8392704}, 'Street address': {'/T': 'Street address', '/FT': '/Tx', '/TU': 'Street address', '/Ff': 8388608}, 'City': {'/T': 'City', '/FT': '/Tx', '/TU': 'City', '/Ff': 8388608}, 'State_2': {'/T': 'State_2', '/FT': '/Tx', '/TU': 'State', '/Ff': 8388608}, 'Zip': {'/T': 'Zip', '/FT': '/Tx', '/TU': 'Zip', '/Ff': 8388608}, 'RELATIONSHIPRow1': {'/T': 'RELATIONSHIPRow1', '/FT': '/Tx', '/TU': 'RELATIONSHIP*_Row_1', '/Ff': 8392704}, 'AGE if minorRow1': {'/T': 'AGE 
if minorRow1', '/FT': '/Tx', '/TU': 'AGE (if minor)**_Row_1', '/Ff': 8392704}, 'NAMERow2': {'/T': 'NAMERow2', '/FT': '/Tx', '/TU': 'NAME_Row_2', '/Ff': 8392704}, 'Street address_2': {'/T': 'Street address_2', '/FT': '/Tx', '/TU': 'Street address', '/Ff': 8388608}, 'City_2': {'/T': 'City_2', '/FT': '/Tx', '/TU': 'City', '/Ff': 8388608}, 'State_3': {'/T': 'State_3', '/FT': '/Tx', '/TU': 'State', '/Ff': 8388608}, 'Zip_2': {'/T': 'Zip_2', '/FT': '/Tx', '/TU': 'Zip', '/Ff': 8388608}, 'RELATIONSHIPRow2': {'/T': 'RELATIONSHIPRow2', '/FT': '/Tx', '/TU': 'RELATIONSHIP*_Row_2', '/Ff': 8392704}, 'AGE if minorRow2': {'/T': 'AGE if minorRow2', '/FT': '/Tx', '/TU': 'AGE (if minor)**_Row_2', '/Ff': 8392704}, 'NAMERow3': {'/T': 'NAMERow3', '/FT': '/Tx', '/TU': 'NAME_Row_3', '/Ff': 8392704}, 'Street address_3': {'/T': 'Street address_3', '/FT': '/Tx', '/TU': 'Street address', '/Ff': 8388608}, 'City_3': {'/T': 'City_3', '/FT': '/Tx', '/TU': 'City', '/Ff': 8388608}, 'State_4': {'/T': 'State_4', '/FT': '/Tx', '/TU': 'State', '/Ff': 8388608}, 'Zip_3': {'/T': 'Zip_3', '/FT': '/Tx', '/TU': 'Zip', '/Ff': 8388608}, 'RELATIONSHIPRow3': {'/T': 'RELATIONSHIPRow3', '/FT': '/Tx', '/TU': 'RELATIONSHIP*_Row_3', '/Ff': 8392704}, 'AGE if minorRow3': {'/T': 'AGE if minorRow3', '/FT': '/Tx', '/TU': 'AGE (if minor)**_Row_3', '/Ff': 8392704}, 'NAMERow4': {'/T': 'NAMERow4', '/FT': '/Tx', '/TU': 'NAME_Row_4', '/Ff': 8392704}, 'Street address_4': {'/T': 'Street address_4', '/FT': '/Tx', '/TU': 'Street address', '/Ff': 8388608}, 'City_4': {'/T': 'City_4', '/FT': '/Tx', '/TU': 'City', '/Ff': 8388608}, 'State_5': {'/T': 'State_5', '/FT': '/Tx', '/TU': 'State', '/Ff': 8388608}, 'Zip_4': {'/T': 'Zip_4', '/FT': '/Tx', '/TU': 'Zip', '/Ff': 8388608}, 'RELATIONSHIPRow4': {'/T': 'RELATIONSHIPRow4', '/FT': '/Tx', '/TU': 'RELATIONSHIP*_Row_4', '/Ff': 8392704}, 'AGE if minorRow4': {'/T': 'AGE if minorRow4', '/FT': '/Tx', '/TU': 'AGE (if minor)**_Row_4', '/Ff': 8392704}, 'NAMERow1_2': {'/T': 'NAMERow1_2', '/FT': '/Tx', '/TU': 'NAME_Row_1', '/Ff': 8388608}, 'LEGAL DISABILITYRow1': {'/T': 'LEGAL DISABILITYRow1', '/FT': '/Tx', '/TU': 'LEGAL DISABILITY_Row_1', '/Ff': 8388608}, 'REPRESENTED BY Name 
address and capacityRow1': {'/T': 'REPRESENTED BY Name address and capacityRow1', '/FT': '/Tx', '/TU': 'REPRESENTED BY Name, address, and capacity_Row_1', '/Ff': 8388608}, 'NAMERow2_2': {'/T': 'NAMERow2_2', '/FT': '/Tx', '/TU': 'NAME_Row_2', '/Ff': 8388608}, 'LEGAL DISABILITYRow2': {'/T': 'LEGAL DISABILITYRow2', '/FT': '/Tx', '/TU': 'LEGAL DISABILITY_Row_2', '/Ff': 8388608}, 'REPRESENTED BY Name address and capacityRow2': {'/T': 'REPRESENTED BY Name address and capacityRow2', '/FT': '/Tx', '/TU': 'REPRESENTED BY Name, address, and capacity_Row_2', '/Ff': 8388608}, 'NAMERow3_2': {'/T': 'NAMERow3_2', '/FT': '/Tx', '/TU': 'NAME_Row_3', '/Ff': 8388608}, 'LEGAL DISABILITYRow3': {'/T': 'LEGAL DISABILITYRow3', '/FT': '/Tx', '/TU': 'LEGAL DISABILITY_Row_3', '/Ff': 8388608}, 'REPRESENTED BY Name address and capacityRow3': {'/T': 'REPRESENTED BY Name address and capacityRow3', '/FT': '/Tx', '/TU': 'REPRESENTED BY Name, address, and capacity_Row_3', '/Ff': 8388608}, 'a Venue is proper in this county because the decedent was domiciled in this county on the date of death': {'/T': 'a Venue is proper in this county because the decedent was domiciled in this county on the date of death', '/FT': '/Btn', '/TU': 'a. Venue is proper in this county because the decedent was domiciled in this county on the date of death'}, 'b The decedent was not domiciled in Michigan but venue is proper in this county because property of the decedent': {'/T': 'b The decedent was not domiciled in Michigan but venue is proper in this county because property of the decedent', '/FT': '/Btn', '/TU': 'b. The decedent was not domiciled in Michigan, but venue is proper in this county because property of the decedent'}, 'a The decedent died intestate and after exercising reasonable diligence I am unaware of any unrevoked testamentary': {'/T': 'a The decedent died intestate and after exercising reasonable diligence I am unaware of any unrevoked testamentary', '/FT': '/Btn', '/TU': 'a. The decedent died intestate and after exercising reasonable diligence, I am unaware of any unrevoked testamentary'}, 'b I am aware of an unrevoked testamentary instrument relating to property located in this state as defined under': {'/T': 'b I am aware of an unrevoked testamentary instrument relating to property located in this state as defined under', '/FT': '/Btn', '/TU': 'b. I am aware of an unrevoked testamentary instrument relating to property located in this state as defined under'}, 'c The decedents will dated': {'/T': 'c The decedents will dated', '/FT': '/Btn', '/TU': 'c. The decedent’s will, dated'}, 'd An authenticated copy of the will and codicils if any probated in': {'/T': 'd An authenticated copy of the will and codicils if any probated in', '/FT': '/Btn', '/TU': 'd. An authenticated copy of the will and codicil(s), if any, probated in'}, 'application according to MCL 7003311': {'/T': 'application according to MCL 7003311', '/FT': '/Tx', '/TU': 'application according to MCL 700.3311', '/Ff': 8388608}, 'is attached to this application': {'/T': 'is attached to this application', '/FT': '/Btn', '/TU': 'is attached to this application'}, 'is already in the courts possession': {'/T': 'is already in the courts possession', '/FT': '/Btn', '/TU': 'is already in the court’s possession'}, 'isare offered for probate and': {'/T': 'isare offered for probate and', '/FT': '/Tx', '/TU': 'is/are offered for probate and', '/Ff': 8388608}, 'undefined': {'/T': 'undefined', '/FT': '/Tx', '/TU': 'undefined', '/Ff': 8388608}, 'isare attached to this application': {'/T': 'isare attached to this application', '/FT': '/Btn', '/TU': 'is/are attached to this application'}, 'isare already in the courts': {'/T': 'isare already in the courts', '/FT': '/Btn', '/TU': 'is/are already in the court’s'}, 'County_2': {'/T': 'County_2', '/FT': '/Tx', '/TU': 'County', '/Ff': 8388608}, 'State_6': {'/T': 'State_6', '/FT': '/Tx', '/TU': 'State', '/Ff': 8388608}, 'and the appointment has not been terminated  The personal representatives name and address are': {'/T': 'and the appointment has not been terminated  The personal representatives name and address are', '/FT': '/Tx', 
'/TU': 'and the appointment has not been terminated.  The personal representative’s name and address are', '/Ff': 8388608}, 'State_7': {'/T': 'State_7', '/FT': '/Tx', '/TU': 'State', '/Ff': 8388608}, '8 A personal representative has been previously appointed in': {'/T': '8 A personal representative has been previously appointed in', '/FT': '/Btn', '/TU': '8. A personal representative has been 
previously appointed in'}, '9 I nominate': {'/T': '9 I nominate', '/FT': '/Btn', '/TU': '9. I nominate'}, '10 Other persons have prior or equal right to appointment as personal representative They are': {'/T': '10 Other persons have prior or equal right to appointment as personal representative They are', '/FT': '/Btn', '/TU': '10. Other persons have prior or equal right to appointment as personal representative. They are'}, 'Name': {'/T': 'Name', '/FT': '/Tx', '/TU': 'Name', '/Ff': 8388608}, 'Address': {'/T': 'Address', '/FT': '/Tx', '/TU': 'Address', '/Ff': 8388608}, 'City_5': {'/T': 'City_5', '/FT': '/Tx', '/TU': 'City', '/Ff': 8388608}, 'Name_2': {'/T': 'Name_2', '/FT': '/Tx', '/TU': 'Name', '/Ff': 8388608}, 'Hisher address is': {'/T': 'Hisher address is', '/FT': '/Tx', '/TU': 
'His/her address is', '/Ff': 8388608}, 'Address_2': {'/T': 'Address_2', '/FT': '/Tx', '/TU': 'Address', '/Ff': 8388608}, 'City_6': {'/T': 'City_6', '/FT': '/Tx', '/TU': 'City', '/Ff': 8388608}, 'Name_3': {'/T': 'Name_3', '/FT': '/Tx', '/TU': 'Name', '/Ff': 8388608}, 'Name_4': {'/T': 'Name_4', '/FT': '/Tx', '/TU': 'Name', '/Ff': 8388608}, 'Name_5': {'/T': 'Name_5', '/FT': '/Tx', '/TU': 'Name', 
'/Ff': 8388608}, 'Name_6': {'/T': 'Name_6', '/FT': '/Tx', '/TU': 'Name', '/Ff': 8388608}, '11 The will expressly requests that the personal representative serve with bond': {'/T': '11 The will expressly requests that the personal representative serve with bond', '/FT': '/Btn', '/TU': '11. The will expressly requests that the personal representative serve with bond'}, '12 A special personal representative is necessary because': {'/T': '12 A special personal representative is necessary because', '/FT': '/Btn', '/TU': '12. A special personal representative is necessary because'}, 'undefined_2': {'/T': 'undefined_2', '/FT': '/Tx', '/TU': 'undefined', '/Ff': 8388608}, 'undefined_3': {'/T': 'undefined_3', '/FT': '/Tx', '/TU': 'undefined', '/Ff': 8388608}, '13 Informal probate of the will': {'/T': '13 Informal probate of the will', '/FT': '/Btn', '/TU': '13. Informal probate of the will'}, '14 Informal appointment of the nominated personal representative': {'/T': '14 Informal appointment of the nominated personal representative', '/FT': '/Btn', '/TU': '14. Informal appointment of the nominated personal representative'}, '15 The appointment of a special personal representative 
pending the appointment of the nominated personal': {'/T': '15 The appointment of a special personal representative pending the appointment of the nominated personal', '/FT': '/Btn', '/TU': '15. The appointment of a special personal representative pending the appointment of the nominated personal'}, 'with': {'/T': 'with', '/FT': '/Btn', '/TU': 'with'}, 'without': {'/T': 'without', '/FT': '/Btn', '/TU': 'without'}, 'Date': {'/T': 'Date', '/FT': '/Tx', '/TU': 'Date', '/Ff': 8388608}, 'Date_2': {'/T': 'Date_2', '/FT': '/Tx', '/TU': 'Date', '/Ff': 8388608}, 'Judge': {'/T': 'Judge', '/FT': '/Tx', '/Ff': 8388608}, 'Text2': {'/T': 'Text2', '/FT': '/Tx', '/Ff': 8388608}, 'Text3': {'/T': 'Text3', '/FT': '/Tx', '/Ff': 8388608}, 'CASE NO': {'/T': 'CASE NO', '/FT': '/Tx', '/Ff': 8388608, '/Kids': [IndirectObject(176, 0, 2986483403712), IndirectObject(121, 0, 2986483403712), IndirectObject(133, 0, 2986483403712)]}, 'Text4': {'/T': 'Text4', '/FT': '/Tx', '/Ff': 8388608}, 'Text5': {'/T': 'Text5', '/FT': '/Tx', '/Ff': 8388608}}

'''