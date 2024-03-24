
blank = ''
name = 'Name'
address = 'Street Address'
city = 'City'
county = 'County'
state = 'State'
zip = 'Zip'
bar_no = 'Bar Number'
tele = 'Telephone'
f_name = 'First Name'
m_name = 'Middle Name'
l_name = 'Last Name'
rel = 'Relation'

court_county = 'Probate Court County'
court_address = 'Court Address'
court_tele = 'Court Telephne'
judge ='Judge'
deat_cert_attach = 'Death Cert Attached'
death_cert_avail = 'Death Cert Available'
case_no = 'Case Number'
MCL = 'MCL 7003311' 
codicile_date = 'Codicil Date'
codicile_county = 'Codicile County'

death_date = 'Date of Death'
death_time = 'Time of Death'
will_date = 'Will Date'

age_if_minor ='Age if Minor'
legal_dis = 'Legal Disability'
legal_rep ='REPRESENTED BY Name address and capacity'

class test():
    def __init__(self,) -> None:
        self.name ='test'
        self.doc_path ='Services\Docs\test.pdf'
        self.bool = None

    def update_fields(self, case_information, existing_fields):
        existing_fields['STATE OF MICHIGAN PROBATE COURT COUNTY'].update({'/V': ' '})
        existing_fields['First middle and last name'].update({'/V': ' '})
        existing_fields['Petitioners name address and telephone no'].update({'/V': ' '})
        existing_fields['Petitioners attorney bar no address and telephone no'].update({'/V': ' '})
        existing_fields['Name of applicant'].update({'/V': ' '})
        existing_fields['Relationship to decedent ie heir devisee child spouse creditor beneficiary etc'].update({'/V': ' '})
        existing_fields['Date of death'].update({'/V': ' '})
        existing_fields['Time if known'].update({'/V': ' '})
        existing_fields['CityTownshipVillage'].update({'/V': ' '})
        existing_fields['County'].update({'/V': ' '})
        existing_fields['State'].update({'/V': ' '})
        existing_fields['A death certificate has been issued and a copy accompanies this application as a separate document'] = self.bool(True)#A death certificate has been issued and a copy accompanies this application as a separate document
        existing_fields['No death certificate is available Attached is alternative documentation of the decedents death'] = self.bool(True)#No death certificate is available Attached is alternative documentation of the decedents death
        existing_fields['NAMERow1'].update({'/V': ' '})
        existing_fields['Street address'].update({'/V': ' '})
        existing_fields['City'].update({'/V': ' '})
        existing_fields['State_2'].update({'/V': ' '})
        existing_fields['Zip'].update({'/V': ' '})
        existing_fields['RELATIONSHIPRow1'].update({'/V': ' '})
        existing_fields['AGE if minorRow1'].update({'/V': ' '})
        existing_fields['NAMERow2'].update({'/V': ' '})
        existing_fields['Street address_2'].update({'/V': ' '})
        existing_fields['City_2'].update({'/V': ' '})
        existing_fields['State_3'].update({'/V': ' '})
        existing_fields['Zip_2'].update({'/V': ' '})
        existing_fields['RELATIONSHIPRow2'].update({'/V': ' '})
        existing_fields['AGE if minorRow2'].update({'/V': ' '})
        existing_fields['NAMERow3'].update({'/V': ' '})
        existing_fields['Street address_3'].update({'/V': ' '})
        existing_fields['City_3'].update({'/V': ' '})
        existing_fields['State_4'].update({'/V': ' '})
        existing_fields['Zip_3'].update({'/V': ' '})
        existing_fields['RELATIONSHIPRow3'].update({'/V': ' '})
        existing_fields['AGE if minorRow3'].update({'/V': ' '})
        existing_fields['NAMERow4'].update({'/V': ' '})
        existing_fields['Street address_4'].update({'/V': ' '})
        existing_fields['City_4'].update({'/V': ' '})
        existing_fields['State_5'].update({'/V': ' '})
        existing_fields['Zip_4'].update({'/V': ' '})
        existing_fields['RELATIONSHIPRow4'].update({'/V': ' '})
        existing_fields['AGE if minorRow4'].update({'/V': ' '})
        existing_fields['NAMERow1_2'].update({'/V': ' '})
        existing_fields['LEGAL DISABILITYRow1'].update({'/V': ' '})
        existing_fields['REPRESENTED BY Name address and capacityRow1'].update({'/V': ' '})
        existing_fields['NAMERow2_2'].update({'/V': ' '})
        existing_fields['LEGAL DISABILITYRow2'].update({'/V': ' '})
        existing_fields['REPRESENTED BY Name address and capacityRow2'].update({'/V': ' '})
        existing_fields['NAMERow3_2'].update({'/V': ' '})
        existing_fields['LEGAL DISABILITYRow3'].update({'/V': ' '})
        existing_fields['REPRESENTED BY Name address and capacityRow3'].update({'/V': ' '})
        existing_fields['a Venue is proper in this county because the decedent was domiciled in this county on the date of death'] = self.bool(True)#a Venue is proper in this county because the decedent was domiciled in this county on the date of death
        existing_fields['b The decedent was not domiciled in Michigan but venue is proper in this county because property of the decedent'] = self.bool(True)#b The decedent was not domiciled in Michigan but venue is proper in this county because property of the decedent
        existing_fields['a The decedent died intestate and after exercising reasonable diligence I am unaware of any unrevoked testamentary'] = self.bool(True)#a The decedent died intestate and after exercising reasonable diligence I am unaware of any unrevoked testamentary
        existing_fields['b I am aware of an unrevoked testamentary instrument relating to property located in this state as defined under'] = self.bool(True)#b I am aware of an unrevoked testamentary instrument relating to property located in this state as defined under
        existing_fields['c The decedents will dated'] = self.bool(True)#c The decedents will dated
        existing_fields['d An authenticated copy of the will and codicils if any probated in'] = self.bool(True)#d An authenticated copy of the will and codicils if any probated in
        existing_fields['application according to MCL 7003311'].update({'/V': ' '})
        existing_fields['is attached to this application'] = self.bool(True)#is attached to this application
        existing_fields['is already in the courts possession'] = self.bool(True)#is already in the courts possession
        existing_fields['isare offered for probate and'].update({'/V': ' '})
        existing_fields['undefined'].update({'/V': ' '})
        existing_fields['isare attached to this application'] = self.bool(True)#isare attached to this application
        existing_fields['isare already in the courts'] = self.bool(True)#isare already in the courts
        existing_fields['County_2'].update({'/V': ' '})
        existing_fields['State_6'].update({'/V': ' '})
        existing_fields['and the appointment has not been terminated  The personal representatives name and address are'].update({'/V': ' '})
        existing_fields['State_7'].update({'/V': ' '})
        existing_fields['8 A personal representative has been previously appointed in'] = self.bool(True)#8 A personal representative has been previously appointed in
        existing_fields['9 I nominate'] = self.bool(True)#9 I nominate
        existing_fields['10 Other persons have prior or equal right to appointment as personal representative They are'] = self.bool(True)#10 Other persons have prior or equal right to appointment as personal representative They are
        existing_fields['Name'].update({'/V': ' '})
        existing_fields['Address'].update({'/V': ' '})
        existing_fields['City_5'].update({'/V': ' '})
        existing_fields['Name_2'].update({'/V': ' '})
        existing_fields['Hisher address is'].update({'/V': ' '})
        existing_fields['Address_2'].update({'/V': ' '})
        existing_fields['City_6'].update({'/V': ' '})
        existing_fields['Name_3'].update({'/V': ' '})
        existing_fields['Name_4'].update({'/V': ' '})
        existing_fields['Name_5'].update({'/V': ' '})
        existing_fields['Name_6'].update({'/V': ' '})
        existing_fields['11 The will expressly requests that the personal representative serve with bond'] = self.bool(True)#11 The will expressly requests that the personal representative serve with bond
        existing_fields['12 A special personal representative is necessary because'] = self.bool(True)#12 A special personal representative is necessary because
        existing_fields['undefined_2'].update({'/V': ' '})
        existing_fields['undefined_3'].update({'/V': ' '})
        existing_fields['13 Informal probate of the will'] = self.bool(True)#13 Informal probate of the will
        existing_fields['14 Informal appointment of the nominated personal representative'] = self.bool(True)#14 Informal appointment of the nominated personal representative
        existing_fields['15 The appointment of a special personal representative pending the appointment of the nominated personal'] = self.bool(True)#15 The appointment of a special personal representative pending the appointment of the nominated personal
        existing_fields['with'] = self.bool(True)#with
        existing_fields['without'] = self.bool(True)#without
        existing_fields['Date'].update({'/V': ' '})
        existing_fields['Date_2'].update({'/V': ' '})
        existing_fields['Judge'].update({'/V': ' '})
        existing_fields['Text2'].update({'/V': ' '})
        existing_fields['Text3'].update({'/V': ' '})
        existing_fields['CASE NO'].update({'/V': ' '})
        existing_fields['Text4'].update({'/V': ' '})
        existing_fields['Text5'].update({'/V': ' '})