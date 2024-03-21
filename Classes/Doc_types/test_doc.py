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

class test_doc():
    def __init__(self,) -> None:
        self.name ='test doc'
        self.doc_path ='Services\Docs\test doc.pdf'
        self.bool = None

    def update_fields(self, case_information, existing_fields):
        existing_fields['county'] = 'field: county'
        existing_fields['fileno'] = 'field: fileno'
        existing_fields['casename'] = 'field: casename'
        existing_fields['adate'] = 'field: adate'
        existing_fields['amount'] = 'field: amount'
        existing_fields['county1'] = 'field: county1'
        existing_fields['address'] = 'field: address'
        existing_fields['item2'] = self.bool(True)#item2
        existing_fields['ndate'] = 'field: ndate'
        existing_fields['aname'] = 'field: aname'
        existing_fields['barno'] = 'field: barno'
        existing_fields['aaddress'] = 'field: aaddress'
        existing_fields['acity'] = 'field: acity'
        existing_fields['atelno'] = 'field: atelno'
        existing_fields['prname'] = 'field: prname'
        existing_fields['praddress'] = 'field: praddress'
        existing_fields['prcity'] = 'field: prcity'
        existing_fields['prtelno'] = 'field: prtelno'
        existing_fields['Check Box1'] = self.bool(True)#Check Box1
        existing_fields['Check Box2'] = self.bool(True)#Check Box2
        existing_fields['Check Box3'] = self.bool(True)#Check Box3
        existing_fields['Check Box4'] = self.bool(True)#Check Box4
        existing_fields['Check Box5'] = self.bool(True)#Check Box5
        existing_fields['Check Box6'] = self.bool(True)#Check Box6



'''{'county': {'/T': 'county', '/FT': '/Tx', '/Ff': 8388608}, 'fileno': {'/T': 'fileno', '/FT': '/Tx', '/Ff': 8388608}, 'casename': {'/T': 'casename', '/FT': '/Tx', '/Ff': 8388608}, 'adate': {'/T': 'adate', '/FT': '/Tx', '/Ff': 8388608, '/AA': {}}, 'amount': {'/T': 'amount', '/FT': '/Tx', '/Ff': 8388608, '/AA': {'/F': IndirectObject(74, 0, 1386587388384), '/K': IndirectObject(75, 0, 1386587388384)}}, 'county1': {'/T': 'county1', '/FT': '/Tx', '/Ff': 8388608}, 'address': {'/T': 'address', '/FT': '/Tx', '/Ff': 8388608}, 'item2': {'/T': 'item2', '/FT': '/Btn'}, 'ndate': {'/T': 'ndate', '/FT': '/Tx', '/Ff': 8388608, '/AA': {}}, 'aname': {'/T': 'aname', '/FT': '/Tx', '/Ff': 8388608}, 'barno': {'/T': 'barno', '/FT': '/Tx', '/Ff': 8388608}, 'aaddress': {'/T': 'aaddress', '/FT': '/Tx', '/Ff': 8388608}, 'acity': {'/T': 'acity', '/FT': '/Tx', '/Ff': 8388608}, 'atelno': {'/T': 'atelno', '/FT': '/Tx', '/Ff': 8388608, '/AA': {}}, 'prname': {'/T': 'prname', '/FT': '/Tx', '/Ff': 8388608}, 'praddress': {'/T': 'praddress', '/FT': '/Tx', '/Ff': 8388608}, 'prcity': {'/T': 'prcity', '/FT': '/Tx', '/Ff': 8388608}, 'prtelno': {'/T': 'prtelno', '/FT': '/Tx', '/Ff': 8388608, '/AA': {}}, 'Check Box1': {'/T': 'Check Box1', '/FT': '/Btn'}, 'Check Box2': {'/T': 'Check Box2', '/FT': '/Btn'}, 'Check Box3': {'/T': 'Check Box3', '/FT': '/Btn'}, 'Check Box4': {'/T': 'Check Box4', '/FT': '/Btn'}, 'Check Box5': {'/T': 'Check Box5', '/FT': '/Btn'}, 'Check Box6': {'/T': 'Check Box6', '/FT': '/Btn'}}'''