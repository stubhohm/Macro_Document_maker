
blank = ''
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

class test():
    def __init__(self,) -> None:
        self.name ='test'
        self.doc_path ='Services\Docs\test.pdf'
        self.bool = None

    def update_fields(self, case_information, existing_fields):
        existing_fields['STATE OF MICHIGAN PROBATE COURT COUNTY'] = 'field: STATE OF MICHIGAN PROBATE COURT COUNTY'
        existing_fields['First middle and last name'] = 'field: First middle and last name'
        existing_fields['Petitioners name address and telephone no'] = 'field: Petitioners name address and telephone no'
        existing_fields['Petitioners attorney bar no address and telephone no'] = 'field: Petitioners attorney bar no address and telephone no'
        existing_fields['Name of applicant'] = 'field: Name of applicant'
        existing_fields['Relationship to decedent ie heir devisee child spouse creditor beneficiary etc'] = 'field: Relationship to decedent ie heir devisee child spouse creditor beneficiary etc'
        existing_fields['Date of death'] = 'field: Date of death'
        existing_fields['Time if known'] = 'field: Time if known'
        existing_fields['CityTownshipVillage'] = 'field: CityTownshipVillage'
        existing_fields['County'] = 'field: County'
        existing_fields['State'] = 'field: State'
        existing_fields['A death certificate has been issued and a copy accompanies this application as a separate document'] = self.bool(True)#A death certificate has been issued and a copy accompanies this application as a separate document
        existing_fields['No death certificate is available Attached is alternative documentation of the decedents death'] = self.bool(True)#No death certificate is available Attached is alternative documentation of the decedents death
        existing_fields['NAMERow1'] = 'field: NAMERow1'
        existing_fields['Street address'] = 'field: Street address'
        existing_fields['City'] = 'field: City'
        existing_fields['State_2'] = 'field: State_2'
        existing_fields['Zip'] = 'field: Zip'
        existing_fields['RELATIONSHIPRow1'] = 'field: RELATIONSHIPRow1'
        existing_fields['AGE if minorRow1'] = 'field: AGE if minorRow1'
        existing_fields['NAMERow2'] = 'field: NAMERow2'
        existing_fields['Street address_2'] = 'field: Street address_2'
        existing_fields['City_2'] = 'field: City_2'
        existing_fields['State_3'] = 'field: State_3'
        existing_fields['Zip_2'] = 'field: Zip_2'
        existing_fields['RELATIONSHIPRow2'] = 'field: RELATIONSHIPRow2'
        existing_fields['AGE if minorRow2'] = 'field: AGE if minorRow2'
        existing_fields['NAMERow3'] = 'field: NAMERow3'
        existing_fields['Street address_3'] = 'field: Street address_3'
        existing_fields['City_3'] = 'field: City_3'
        existing_fields['State_4'] = 'field: State_4'
        existing_fields['Zip_3'] = 'field: Zip_3'
        existing_fields['RELATIONSHIPRow3'] = 'field: RELATIONSHIPRow3'
        existing_fields['AGE if minorRow3'] = 'field: AGE if minorRow3'
        existing_fields['NAMERow4'] = 'field: NAMERow4'
        existing_fields['Street address_4'] = 'field: Street address_4'
        existing_fields['City_4'] = 'field: City_4'
        existing_fields['State_5'] = 'field: State_5'
        existing_fields['Zip_4'] = 'field: Zip_4'
        existing_fields['RELATIONSHIPRow4'] = 'field: RELATIONSHIPRow4'
        existing_fields['AGE if minorRow4'] = 'field: AGE if minorRow4'
        existing_fields['NAMERow1_2'] = 'field: NAMERow1_2'
        existing_fields['LEGAL DISABILITYRow1'] = 'field: LEGAL DISABILITYRow1'
        existing_fields['REPRESENTED BY Name address and capacityRow1'] = 'field: REPRESENTED BY Name address and capacityRow1'
        existing_fields['NAMERow2_2'] = 'field: NAMERow2_2'
        existing_fields['LEGAL DISABILITYRow2'] = 'field: LEGAL DISABILITYRow2'
        existing_fields['REPRESENTED BY Name address and capacityRow2'] = 'field: REPRESENTED BY Name address and capacityRow2'
        existing_fields['NAMERow3_2'] = 'field: NAMERow3_2'
        existing_fields['LEGAL DISABILITYRow3'] = 'field: LEGAL DISABILITYRow3'
        existing_fields['REPRESENTED BY Name address and capacityRow3'] = 'field: REPRESENTED BY Name address and capacityRow3'
        existing_fields['a Venue is proper in this county because the decedent was domiciled in this county on the date of death'] = self.bool(True)#a Venue is proper in this county because the decedent was domiciled in this county on the date of death
        existing_fields['b The decedent was not domiciled in Michigan but venue is proper in this county because property of the decedent'] = self.bool(True)#b The decedent was not domiciled in Michigan but venue is proper in this county because property of the decedent
        existing_fields['a The decedent died intestate and after exercising reasonable diligence I am unaware of any unrevoked testamentary'] = self.bool(True)#a The decedent died intestate and after exercising reasonable diligence I am unaware of any unrevoked testamentary
        existing_fields['b I am aware of an unrevoked testamentary instrument relating to property located in this state as defined under'] = self.bool(True)#b I am aware of an unrevoked testamentary instrument relating to property located in this state as defined under
        existing_fields['c The decedents will dated'] = self.bool(True)#c The decedents will dated
        existing_fields['d An authenticated copy of the will and codicils if any probated in'] = self.bool(True)#d An authenticated copy of the will and codicils if any probated in
        existing_fields['application according to MCL 7003311'] = 'field: application according to MCL 7003311'
        existing_fields['is attached to this application'] = self.bool(True)#is attached to this application
        existing_fields['is already in the courts possession'] = self.bool(True)#is already in the courts possession
        existing_fields['isare offered for probate and'] = 'field: isare offered for probate and'
        existing_fields['undefined'] = 'field: undefined'
        existing_fields['isare attached to this application'] = self.bool(True)#isare attached to this application
        existing_fields['isare already in the courts'] = self.bool(True)#isare already in the courts
        existing_fields['County_2'] = 'field: County_2'
        existing_fields['State_6'] = 'field: State_6'
        existing_fields['and the appointment has not been terminated  The personal representatives name and address are'] = 'field: and the appointment has not been terminated  The personal representatives name and address are'
        existing_fields['State_7'] = 'field: State_7'
        existing_fields['8 A personal representative has been previously appointed in'] = self.bool(True)#8 A personal representative has been previously appointed in
        existing_fields['9 I nominate'] = self.bool(True)#9 I nominate
        existing_fields['10 Other persons have prior or equal right to appointment as personal representative They are'] = self.bool(True)#10 Other persons have prior or equal right to appointment as personal representative They are
        existing_fields['Name'] = 'field: Name'
        existing_fields['Address'] = 'field: Address'
        existing_fields['City_5'] = 'field: City_5'
        existing_fields['Name_2'] = 'field: Name_2'
        existing_fields['Hisher address is'] = 'field: Hisher address is'
        existing_fields['Address_2'] = 'field: Address_2'
        existing_fields['City_6'] = 'field: City_6'
        existing_fields['Name_3'] = 'field: Name_3'
        existing_fields['Name_4'] = 'field: Name_4'
        existing_fields['Name_5'] = 'field: Name_5'
        existing_fields['Name_6'] = 'field: Name_6'
        existing_fields['11 The will expressly requests that the personal representative serve with bond'] = self.bool(True)#11 The will expressly requests that the personal representative serve with bond
        existing_fields['12 A special personal representative is necessary because'] = self.bool(True)#12 A special personal representative is necessary because
        existing_fields['undefined_2'] = 'field: undefined_2'
        existing_fields['undefined_3'] = 'field: undefined_3'
        existing_fields['13 Informal probate of the will'] = self.bool(True)#13 Informal probate of the will
        existing_fields['14 Informal appointment of the nominated personal representative'] = self.bool(True)#14 Informal appointment of the nominated personal representative
        existing_fields['15 The appointment of a special personal representative pending the appointment of the nominated personal'] = self.bool(True)#15 The appointment of a special personal representative pending the appointment of the nominated personal
        existing_fields['with'] = self.bool(True)#with
        existing_fields['without'] = self.bool(True)#without
        existing_fields['Date'] = 'field: Date'
        existing_fields['Date_2'] = 'field: Date_2'
        existing_fields['Judge'] = 'field: Judge'
        existing_fields['Text2'] = 'field: Text2'
        existing_fields['Text3'] = 'field: Text3'
        #CASE NO
        existing_fields['Text4'] = 'field: Text4'
        existing_fields['Text5'] = 'field: Text5'



'''{'STATE OF MICHIGAN PROBATE COURT COUNTY': {'/T': 'STATE OF MICHIGAN PROBATE COURT COUNTY', '/FT': '/Tx', '/TU': 'STATE OF MICHIGAN PROBATE COURT COUNTY', '/Ff': 8388608}, 'First middle and last name': {'/T': 'First middle and last name', '/FT': '/Tx', '/TU': 'First, middle, and last name', '/Ff': 8388608}, 'Petitioners name address and telephone no': {'/T': 'Petitioners name address and telephone no', '/FT': '/Tx', '/TU': 'Petitioner’s name, address and telephone no.', '/Ff': 8392704}, 'Petitioners attorney bar no address and telephone no': {'/T': 'Petitioners attorney bar no address and telephone no', '/FT': '/Tx', '/TU': 'Petitioner’s attorney, bar no., address, and telephone no.', '/Ff': 8392704}, 'Name of applicant': {'/T': 'Name of applicant', '/FT': '/Tx', '/TU': 'Name of applicant', '/Ff': 8388608}, 'Relationship to decedent ie heir devisee child spouse creditor beneficiary etc': {'/T': 'Relationship to decedent ie heir devisee child spouse creditor beneficiary etc', '/FT': '/Tx', '/TU': 'Relationship to decedent, i.e., heir, devisee, child, spouse, creditor, beneficiary, etc', '/Ff': 8388608}, 'Date of death': {'/T': 'Date of death', '/FT': '/Tx', '/TU': 'Date of death', '/Ff': 8388608}, 'Time if known': {'/T': 'Time if known', '/FT': '/Tx', '/TU': 'Time (if known', '/Ff': 8388608}, 'CityTownshipVillage': {'/T': 'CityTownshipVillage', '/FT': '/Tx', '/TU': 'City/Township/Village', '/Ff': 8388608}, 'County': {'/T': 'County', '/FT': '/Tx', '/TU': 'County', '/Ff': 8388608}, 'State': {'/T': 'State', '/FT': '/Tx', '/TU': 'State', '/Ff': 8388608}, 'A death certificate has been issued and a copy accompanies this application as a separate document': {'/T': 'A death certificate has been issued and a copy accompanies this application as a separate document', '/FT': '/Btn', '/TU': 'A death certificate has been issued, and a copy accompanies this application as a separate document'}, 'No death certificate is available Attached is alternative documentation of the decedents death': {'/T': 'No death certificate is available Attached is alternative documentation of the decedents death', '/FT': '/Btn', '/TU': 'No death certificate is available. Attached is alternative documentation of the decedent’s death'}, 'NAMERow1': {'/T': 'NAMERow1', '/FT': '/Tx', '/TU': 'NAME_Row_1', '/Ff': 8392704}, 'Street address': {'/T': 'Street address', '/FT': '/Tx', '/TU': 'Street address', '/Ff': 8388608}, 'City': {'/T': 'City', '/FT': '/Tx', '/TU': 'City', '/Ff': 8388608}, 'State_2': {'/T': 'State_2', '/FT': '/Tx', '/TU': 'State', '/Ff': 8388608}, 'Zip': {'/T': 'Zip', '/FT': '/Tx', '/TU': 'Zip', '/Ff': 8388608}, 'RELATIONSHIPRow1': {'/T': 'RELATIONSHIPRow1', '/FT': '/Tx', '/TU': 'RELATIONSHIP*_Row_1', '/Ff': 8392704}, 'AGE if minorRow1': {'/T': 'AGE if minorRow1', '/FT': '/Tx', '/TU': 'AGE (if minor)**_Row_1', '/Ff': 8392704}, 'NAMERow2': {'/T': 'NAMERow2', '/FT': '/Tx', '/TU': 'NAME_Row_2', '/Ff': 8392704}, 'Street address_2': {'/T': 'Street address_2', '/FT': '/Tx', '/TU': 'Street address', '/Ff': 8388608}, 'City_2': {'/T': 'City_2', '/FT': '/Tx', '/TU': 'City', '/Ff': 8388608}, 'State_3': {'/T': 'State_3', '/FT': '/Tx', '/TU': 'State', '/Ff': 8388608}, 'Zip_2': {'/T': 'Zip_2', '/FT': '/Tx', '/TU': 'Zip', '/Ff': 8388608}, 'RELATIONSHIPRow2': {'/T': 'RELATIONSHIPRow2', '/FT': '/Tx', '/TU': 'RELATIONSHIP*_Row_2', '/Ff': 8392704}, 'AGE if minorRow2': {'/T': 'AGE if minorRow2', '/FT': '/Tx', '/TU': 'AGE (if minor)**_Row_2', '/Ff': 8392704}, 'NAMERow3': {'/T': 'NAMERow3', '/FT': '/Tx', '/TU': 'NAME_Row_3', '/Ff': 8392704}, 'Street address_3': {'/T': 'Street address_3', '/FT': '/Tx', '/TU': 'Street address', '/Ff': 8388608}, 'City_3': {'/T': 'City_3', '/FT': '/Tx', '/TU': 'City', '/Ff': 8388608}, 'State_4': {'/T': 'State_4', '/FT': '/Tx', '/TU': 'State', '/Ff': 8388608}, 'Zip_3': {'/T': 'Zip_3', '/FT': '/Tx', '/TU': 'Zip', '/Ff': 8388608}, 'RELATIONSHIPRow3': {'/T': 'RELATIONSHIPRow3', '/FT': '/Tx', '/TU': 'RELATIONSHIP*_Row_3', '/Ff': 8392704}, 'AGE if minorRow3': {'/T': 'AGE if minorRow3', '/FT': '/Tx', '/TU': 'AGE (if minor)**_Row_3', '/Ff': 8392704}, 'NAMERow4': {'/T': 'NAMERow4', '/FT': '/Tx', '/TU': 'NAME_Row_4', '/Ff': 8392704}, 'Street address_4': {'/T': 'Street address_4', '/FT': '/Tx', '/TU': 'Street address', '/Ff': 8388608}, 'City_4': {'/T': 'City_4', '/FT': '/Tx', '/TU': 'City', '/Ff': 8388608}, 'State_5': {'/T': 'State_5', '/FT': '/Tx', '/TU': 'State', '/Ff': 8388608}, 'Zip_4': {'/T': 'Zip_4', '/FT': '/Tx', '/TU': 'Zip', '/Ff': 8388608}, 'RELATIONSHIPRow4': {'/T': 'RELATIONSHIPRow4', '/FT': '/Tx', '/TU': 'RELATIONSHIP*_Row_4', '/Ff': 8392704}, 'AGE if minorRow4': {'/T': 'AGE if minorRow4', '/FT': '/Tx', '/TU': 'AGE (if minor)**_Row_4', '/Ff': 8392704}, 'NAMERow1_2': {'/T': 'NAMERow1_2', '/FT': '/Tx', '/TU': 'NAME_Row_1', '/Ff': 8388608}, 'LEGAL DISABILITYRow1': {'/T': 'LEGAL DISABILITYRow1', '/FT': '/Tx', '/TU': 'LEGAL DISABILITY_Row_1', '/Ff': 8388608}, 'REPRESENTED BY Name address and capacityRow1': {'/T': 'REPRESENTED BY Name address and capacityRow1', '/FT': '/Tx', '/TU': 'REPRESENTED BY Name, address, and capacity_Row_1', '/Ff': 8388608}, 'NAMERow2_2': {'/T': 'NAMERow2_2', '/FT': '/Tx', '/TU': 'NAME_Row_2', '/Ff': 8388608}, 'LEGAL DISABILITYRow2': {'/T': 'LEGAL DISABILITYRow2', '/FT': '/Tx', '/TU': 'LEGAL DISABILITY_Row_2', '/Ff': 8388608}, 'REPRESENTED BY Name address and capacityRow2': {'/T': 'REPRESENTED BY Name address and capacityRow2', '/FT': '/Tx', '/TU': 'REPRESENTED BY Name, address, and capacity_Row_2', '/Ff': 8388608}, 'NAMERow3_2': {'/T': 'NAMERow3_2', '/FT': '/Tx', '/TU': 'NAME_Row_3', '/Ff': 8388608}, 'LEGAL DISABILITYRow3': {'/T': 'LEGAL DISABILITYRow3', '/FT': '/Tx', '/TU': 'LEGAL DISABILITY_Row_3', '/Ff': 8388608}, 'REPRESENTED BY Name address and capacityRow3': {'/T': 'REPRESENTED BY Name address and capacityRow3', '/FT': '/Tx', '/TU': 'REPRESENTED BY Name, address, and capacity_Row_3', '/Ff': 8388608}, 'a Venue is proper in this county because the decedent was domiciled in this county on the date of death': {'/T': 'a Venue is proper in this county because the decedent was domiciled in this county on the date of death', '/FT': '/Btn', '/TU': 'a. Venue is proper in this county because the decedent was domiciled in this county on the date of death'}, 'b The decedent was not domiciled in Michigan but venue is proper in this county because property of the decedent': {'/T': 'b The decedent was not domiciled in Michigan but venue is proper in this county because property of the decedent', '/FT': '/Btn', '/TU': 'b. The decedent was not domiciled in Michigan, but venue is proper in this county because property of the decedent'}, 'a The decedent died intestate and after exercising reasonable diligence I am unaware of any unrevoked testamentary': {'/T': 'a The decedent died intestate and after exercising reasonable diligence I am unaware of any unrevoked testamentary', '/FT': '/Btn', '/TU': 'a. The decedent died intestate and after exercising reasonable diligence, I am unaware of any unrevoked testamentary'}, 'b I am aware of an unrevoked testamentary instrument relating to property located in this state as defined under': {'/T': 'b I am aware of an unrevoked testamentary instrument relating to property located in this state as defined under', '/FT': '/Btn', '/TU': 'b. I am aware of an unrevoked testamentary instrument relating to property located in this state as defined under'}, 'c The decedents will dated': {'/T': 'c The decedents will dated', '/FT': '/Btn', '/TU': 'c. The decedent’s will, dated'}, 'd An authenticated copy of the will and codicils if any probated in': {'/T': 'd An authenticated copy of the will and codicils if any probated in', '/FT': '/Btn', '/TU': 'd. An authenticated copy of the will and codicil(s), if any, probated in'}, 'application according to MCL 7003311': {'/T': 'application according to MCL 7003311', '/FT': '/Tx', '/TU': 'application according to MCL 700.3311', '/Ff': 8388608}, 'is attached to this application': {'/T': 'is attached to this application', '/FT': '/Btn', '/TU': 'is attached to this application'}, 'is already in the courts possession': {'/T': 'is already in the courts possession', '/FT': '/Btn', '/TU': 'is already in the court’s possession'}, 'isare offered for probate and': {'/T': 'isare offered for probate and', '/FT': '/Tx', '/TU': 'is/are offered for probate and', '/Ff': 8388608}, 'undefined': {'/T': 'undefined', '/FT': '/Tx', '/TU': 'undefined', '/Ff': 8388608}, 'isare attached to this application': {'/T': 'isare attached to this application', '/FT': '/Btn', '/TU': 'is/are attached to this application'}, 'isare already in the courts': {'/T': 'isare already in the courts', '/FT': '/Btn', '/TU': 'is/are already in the court’s'}, 'County_2': {'/T': 'County_2', '/FT': '/Tx', '/TU': 'County', '/Ff': 8388608}, 'State_6': {'/T': 'State_6', '/FT': '/Tx', '/TU': 'State', '/Ff': 8388608}, 'and the appointment has not been terminated  The personal representatives name and address are': {'/T': 'and the appointment has not been terminated  The personal representatives name and address are', '/FT': '/Tx', '/TU': 'and the appointment has not been terminated.  The personal representative’s name and address are', '/Ff': 8388608}, 'State_7': {'/T': 'State_7', '/FT': '/Tx', '/TU': 'State', '/Ff': 8388608}, '8 A personal representative has been previously appointed in': {'/T': '8 A personal representative has been previously appointed in', '/FT': '/Btn', '/TU': '8. A personal representative has been previously appointed in'}, '9 I nominate': {'/T': '9 I nominate', '/FT': '/Btn', '/TU': '9. I nominate'}, '10 Other persons have prior or equal right to appointment as personal representative They are': {'/T': '10 Other persons have prior or equal right to appointment as personal representative They are', '/FT': '/Btn', '/TU': '10. Other persons have prior or equal right to appointment as personal representative. They are'}, 'Name': {'/T': 'Name', '/FT': '/Tx', '/TU': 'Name', '/Ff': 8388608}, 'Address': {'/T': 'Address', '/FT': '/Tx', '/TU': 'Address', '/Ff': 8388608}, 'City_5': {'/T': 'City_5', '/FT': '/Tx', '/TU': 'City', '/Ff': 8388608}, 'Name_2': {'/T': 'Name_2', '/FT': '/Tx', '/TU': 'Name', '/Ff': 8388608}, 'Hisher address is': {'/T': 'Hisher address is', '/FT': '/Tx', '/TU': 'His/her address is', '/Ff': 8388608}, 'Address_2': {'/T': 'Address_2', '/FT': '/Tx', '/TU': 'Address', '/Ff': 8388608}, 'City_6': {'/T': 'City_6', '/FT': '/Tx', '/TU': 'City', '/Ff': 8388608}, 'Name_3': {'/T': 'Name_3', '/FT': '/Tx', '/TU': 'Name', '/Ff': 8388608}, 'Name_4': {'/T': 'Name_4', '/FT': '/Tx', '/TU': 'Name', '/Ff': 8388608}, 'Name_5': {'/T': 'Name_5', '/FT': '/Tx', '/TU': 'Name', '/Ff': 8388608}, 'Name_6': {'/T': 'Name_6', '/FT': '/Tx', '/TU': 'Name', '/Ff': 8388608}, '11 The will expressly requests that the personal representative serve with bond': {'/T': '11 The will expressly requests that the personal representative serve with bond', '/FT': '/Btn', '/TU': '11. The will expressly requests that the personal representative serve with bond'}, '12 A special personal representative is necessary because': {'/T': '12 A special personal representative is necessary because', '/FT': '/Btn', '/TU': '12. A special personal representative is necessary because'}, 'undefined_2': {'/T': 'undefined_2', '/FT': '/Tx', '/TU': 'undefined', '/Ff': 8388608}, 'undefined_3': {'/T': 'undefined_3', '/FT': '/Tx', '/TU': 'undefined', '/Ff': 8388608}, '13 Informal probate of the will': {'/T': '13 Informal probate of the will', '/FT': '/Btn', '/TU': '13. Informal probate of the will'}, '14 Informal appointment of the nominated personal representative': {'/T': '14 Informal appointment of the nominated personal representative', '/FT': '/Btn', '/TU': '14. Informal appointment of the nominated personal representative'}, '15 The appointment of a special personal representative pending the appointment of the nominated personal': {'/T': '15 The appointment of a special personal representative pending the appointment of the nominated personal', '/FT': '/Btn', '/TU': '15. The appointment of a special personal representative pending the appointment of the nominated personal'}, 'with': {'/T': 'with', '/FT': '/Btn', '/TU': 'with'}, 'without': {'/T': 'without', '/FT': '/Btn', '/TU': 'without'}, 'Date': {'/T': 'Date', '/FT': '/Tx', '/TU': 'Date', '/Ff': 8388608}, 'Date_2': {'/T': 'Date_2', '/FT': '/Tx', '/TU': 'Date', '/Ff': 8388608}, 'Judge': {'/T': 'Judge', '/FT': '/Tx', '/Ff': 8388608}, 'Text2': {'/T': 'Text2', '/FT': '/Tx', '/Ff': 8388608}, 'Text3': {'/T': 'Text3', '/FT': '/Tx', '/Ff': 8388608}, 'CASE NO': {'/T': 'CASE NO', '/FT': '/Tx', '/Ff': 8388608, '/Kids': [IndirectObject(176, 0, 1801930251568), IndirectObject(121, 0, 1801930251568), IndirectObject(133, 0, 1801930251568)]}, 'Text4': {'/T': 'Text4', '/FT': '/Tx', '/Ff': 8388608}, 'Text5': {'/T': 'Text5', '/FT': '/Tx', '/Ff': 8388608}}'''