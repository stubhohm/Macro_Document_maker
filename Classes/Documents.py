db_path = 'documents.db'
docs_table = 'DocumentsTable'

id_sql = 'id'
name_sql = 'doc_name'
doc_path_sql = 'doc_path'
script_path_sql = 'script_path'

case_table = 'Case Table'
client_name_sql = 'Client Name'
case_info_path_sql = 'Case File Path'



c1 = "\nblank = ''\nname = 'name'\naddress = 'Street_address'\ncity = 'City'"
c2 = "\ncounty = 'County'\nstate = 'State'\nzip = 'Zip'\nbar_no = 'bar_no'\ntele = 'telephone'\nf_name = 'first_name'\nm_name = 'middle_name'"
c3 = "\nl_name = 'last_name'\nrel = 'relation'\n\ncourt_county = 'Probate_Court_County'\ncourt_address = 'Court_address'"
c4 ="\ncourt_tele = 'Court_Tele'\njudge ='Judge'\ndeat_cert_attach = 'death_cert_attached'\ndeath_cert_avail = 'death_cert_available'"
c5 ="\ncase_no = 'CASE NO'\nMCL = 'MCL_7003311'\nexisting_appt_rep = 'and the appointment has not been terminated  The personal representatives name and address are'"
c6 = "\n\ndeath_date = 'date_of_death'\ndeath_time = 'time_of_death'\nwill_date = 'will_date'\n\nage_if_minor ='AGE_if_minor'"
c7 = "\nlegal_dis = 'Legal_disability'\nlegal_rep ='REPRESENTED BY Name address and capacity'"
constants = c1 + c2 + c3 + c4 + c5 + c6 + c7
cls = "\n\nclass "
init = "\n    def __init__(self,) -> None:"
name = "\n        self.name ="
path = "\n        self.doc_path ="
bool = "\n        self.bool = None"



class Documentsdb():
    name = "Documents_DataBase"
    def __init__(self, sql, re):
        self.document = []
        self.sql = sql
        self.re = re
        self.matches = None
        self.connection = sql.connect(db_path)
        self.cursor = self.connection.cursor()
        self.destination_dir = 'Services\\Docs'
        self.destination_file = None
        self.destination_dir_py = 'Classes\\Doc_types'
        self.destination_file_py = None

    def init_db(self):
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {docs_table} (
            {id_sql} INTEGER PRIMARY KEY,
            {name_sql} TEXT NOT NULL,
            {doc_path_sql} TEXT NOT NULL,
            {script_path_sql} TEXT NOT NULL
            )                
        ''')
        self.connection.commit()
    
    def close_db(self):
        self.cursor.close()
        self.connection.close()

    def get_template_names(self):
        self.cursor.execute(f'SELECT {name_sql} FROM {docs_table}')
        return self.cursor.fetchall()

    def add_to_db(self, name):
        insert_query = f'INSERT INTO {docs_table} ({name_sql}, {doc_path_sql}, {script_path_sql}) VALUES (?, ?, ?)'
        self.cursor.execute(insert_query, (name, self.destination_file, self.destination_file_py,))
        self.connection.commit()

    def make_local_copy(self, file_name, source_file):
        snake_name = file_name.replace(' ', '_')
        with open(source_file, 'rb') as src_file:
            # Read the contents of the source file
            file_contents = src_file.read()

        # Construct the destination file path
        self.destination_file = self.destination_dir + '\\' + file_name + '.pdf'
        self.destination_file_py = self.destination_dir_py + '\\' + snake_name + '.py'

        # Open the destination file for writing
        with open(self.destination_file, 'wb') as dest_file:
            print(self.destination_file)
            # Write the contents of the source file to the destination file
            dest_file.write(file_contents)

        # Open the destination file for writing of python script
        with open(self.destination_file_py, 'w') as dest_file:
            print(self.destination_file_py)
            # Write the contents of the source file to the destination file
            text = constants + cls + snake_name + '():' + init + name + "'" + file_name + "'" + path + "'" + self.destination_file + "'" + bool
            dest_file.write(text)

    def set_to_db(self, template_name, file_path):
        ## Instance the new document
        self.make_local_copy(template_name, file_path)
        self.add_to_db(template_name)
        print('added to db')

    '''
    TODO
    def remove_from_db(self):
    

    def rename(self):
        self.set_to_db(new_name, file_path)
        self.empty_new_py()
        self.populate_new_py()
        self.remove_from_db()'''

    

    
