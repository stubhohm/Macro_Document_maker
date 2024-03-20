
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
court_address = 'Court_address'
court_tele = 'Court_Tele'
judge ='Judge'
deat_cert_attach = 'death_cert_attached'
death_cert_avail = 'death_cert_available'
case_no = 'CASE NO'
MCL = 'MCL_7003311'
existing_appt_rep = 'and the appointment has not been terminated  The personal representatives name and address are'

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
        self.doc_path ='Services\Docs\Application for Appointment of PR.pdf'
        
    def update_fields(self, case_information, existing_fields):
        existing_fields['STATE OF MICHIGAN PROBATE COURT COUNTY'] = case_information.filing_info[court_county]
        existing_fields[judge] = case_information.filing_info[judge]
        existing_fields['Text2'] = case_information.filing_info[court_tele]
        existing_fields['Text3'] = case_information.filing_info[court_address]
        existing_fields[case_no] = case_information.filing_info[case_no]
        # Case No '/Kids'] [IndirectObject(176, 0, 2986483403712), IndirectObject(121, 0, 2986483403712), IndirectObject(133, 0, 2986483403712)]
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
        app_full_add = app_add + '\n' + app_city + ', ' + app_state + ' ' + app_zip + '\n'
        app_tele = case_information.applicant_info[tele]
        existing_fields['Petitioners name address and telephone no'] = app_name + app_full_add + app_tele
        
        att_name = case_information.attorney_info[name] + '\n'
        att_bar = case_information.attorney_info[bar_no] + '\n'
        att_full_add = case_information.attorney_info[address] + '\n' + case_information.attorney_info[city] + ', ' + case_information.attorney_info[state] + ' ' + case_information.attorney_info[zip] + '\n'
        att_tele = case_information.attorney_info[tele]
        existing_fields['Petitioners attorney bar no address and telephone no'] =  att_name + att_bar + att_full_add + att_tele 
        existing_fields['Name of applicant']= case_information.applicant_info[f_name] + ' ' + case_information.applicant_info[l_name] 
        existing_fields['Relationship to decedent ie heir devisee child spouse creditor beneficiary etc'] = case_information.applicant_info[rel]
        existing_fields['Date of death'] = case_information.decedent_info[death_date] 
        existing_fields['Time if known'] = case_information.decedent_info[death_time]
        existing_fields['CityTownshipVillage'] = case_information.decedent_info[city]
        existing_fields['County'] = case_information.decedent_info[county]
        existing_fields['State'] = case_information.decedent_info[state]
        #existing_fields['A death certificate has been issued and a copy accompanies this application as a separate document'] = ""
        #existing_fields['No death certificate is available Attached is alternative documentation of the decedents death'] = ""
        for i, person in enumerate(case_information.Interested_persons):
            if i == 0:
                existing_fields['NAMERow1'] = person[name]
                existing_fields['Street address'] = person[address]
                existing_fields['City'] = person[city] 
                existing_fields['State_2'] = person[state]  
                existing_fields['Zip'] = person[zip]  
                existing_fields['RELATIONSHIPRow1'] = person[rel] 
                existing_fields['AGE if minorRow1'] = person[age_if_minor]  
            else:
                existing_fields[f'NAMERow{i+1}'] = person[name]
                existing_fields[f'Street address_{i+1}'] = person[address] 
                existing_fields[f'City_{i+1}'] = person[city]
                existing_fields[f'State_{i+2}'] = person[state]
                existing_fields[f'Zip_{i+1}'] = person[zip]
                existing_fields[f'RELATIONSHIPRow{i+1}'] = person[rel]
                existing_fields[f'AGE if minorRow{i+1}'] = person[age_if_minor]
        for i, person in enumerate(case_information.Interested_persons):
            if person[legal_dis]:
                if i < 3:
                    existing_fields[f'NAMERow{i+1}_2'] = person[name]
                    existing_fields[f'LEGAL DISABILITYRow{i+1}'] = person[legal_dis]
                    existing_fields[f'REPRESENTED BY Name address and capacityRow{i+1}'] = person[legal_rep]
     
        #existing_fields['a Venue is proper in this county because the decedent was domiciled in this county on the date of death'] = '' 
        #existing_fields['b The decedent was not domiciled in Michigan but venue is proper in this county because property of the decedent'] = '' 
        #existing_fields['a The decedent died intestate and after exercising reasonable diligence I am unaware of any unrevoked testamentary'] = '' 
        #existing_fields['b I am aware of an unrevoked testamentary instrument relating to property located in this state as defined under'] = '' 
        
        
         
        
        # 6B MCL700.1301
        existing_fields['application according to MCL 7003311'] = case_information.decedent_info[MCL]
        # 6B boxes
        #existing_fields['is attached to this application'] = T/F
        #existing_fields['is already in the courts possession']  = T/F
        # 6c
        existing_fields['c The decedents will dated'] = case_information.decedent_info[will_date] 

        
        existing_fields['isare offered for probate and'] = case_information.decedent_info[will_date]
        existing_fields['undefined'] = case_information.decedent_info[will_date]
        
        # 6c boxes
        #existing_fields['isare attached to this application'] =T/F 
        #existing_fields['isare already in the courts'] =T/F 
        
        # 6d authenticated copy exists and is on file iwth
        #existing_fields['d An authenticated copy of the will and codicils if any probated in'] = T/F 
        existing_fields['County_2'] ='County_2' 
        existing_fields['State_6'] ='State_6' 
        
        # 8. Existing peronsal rep
        #existing_fields['8 A personal representative has been previously appointed in'] = T/F
        existing_fields[existing_appt_rep] ='existing rep county' 
        existing_fields['State_7'] ='State_7' 
        existing_fields['Name'] ='Name' 
        existing_fields['Address'] ='Address' 
        existing_fields['City_5'] ='City_5'
        existing_fields['Name_2'] ='Name_2'
        
        # 9. Appointing Personal Rep
        #existing_fields['9 I nominate'] =' ' 
        existing_fields['Hisher address is'] ='Hisher address is' 
        existing_fields['Address_2'] ='Address_2'
        existing_fields['City_6'] ='City_6' 
        
        # 10. Other persons have prior or equal right to appointment are:
        #existing_fields['10 Other persons have prior or equal right to appointment as personal representative They are'] =T/F 
        existing_fields['Name_3'] ='Name_3' 
        existing_fields['Name_4'] ='Name_4'
        existing_fields['Name_5'] ='Name_5'
        existing_fields['Name_6'] ='Name_6' 
        
        #existing_fields['11 The will expressly requests that the personal representative serve with bond'] =T/F 
        #existing_fields['12 A special personal representative is necessary because'] =T/F
        
        # These two are for defining the reason need a special rep is needed, and is split across two lines.
        existing_fields['undefined_2'] ='undefined_2' 
        existing_fields['undefined_3'] ='undefined_3' 
        
        #existing_fields['13 Informal probate of the will'] =T/F 
        #existing_fields['14 Informal appointment of the nominated personal representative'] =T/F
        #existing_fields['15 The appointment of a special personal representative pending the appointment of the nominated personal'] =T/F 
        #existing_fields['with'] =T/F 
        #existing_fields['without'] =T/F 
        
        # Applicant and Attorney Signature Fields
        existing_fields['Date'] =' '
        existing_fields['Date_2'] =' '
        existing_fields['Text4'] =' ' 
        existing_fields['Text5'] =' '