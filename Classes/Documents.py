db_path = 'documents.db'

docs_table = 'DocumentsTable'
id_sql = 'id'
name_sql = 'doc_name'
doc_path_sql = 'doc_path'
script_path_sql = 'script_path'

case_table = 'Case_Table'
client_name_sql = 'Client_Name'
case_info_path_sql = 'Case_File_Path'

attorney_table = 'Attorney_Table'
attorney_name_sql = 'Attorney_Name'
attorney_info_path_sql = 'Attorney_info_path'



c1 = "\nblank = ''\nname = 'Name'\naddress = 'Street Address'\ncity = 'City'"
c2 = "\ncounty = 'County'\nstate = 'State'\nzip = 'Zip'\nbar_no = 'Bar Number'\ntele = 'Telephone'\nf_name = 'First Name'\nm_name = 'Middle Name'"
c3 = "\nl_name = 'Last Name'\nrel = 'Relation'\n\ncourt_county = 'Probate Court County'\ncourt_address = 'Court Address'"
c4 ="\ncourt_tele = 'Court Telephne'\njudge ='Judge'\ndeat_cert_attach = 'Death Cert Attached'\ndeath_cert_avail = 'Death Cert Available'"
c5 ="\ncase_no = 'Case Number'\nMCL = 'MCL 7003311' \ncodicile_date = 'Codicil Date'\ncodicile_county = 'Codicile County'"
c6 = "\n\ndeath_date = 'Date of Death'\ndeath_time = 'Time of Death'\nwill_date = 'Will Date'\n\nage_if_minor ='Age if Minor'"
c7 = "\nlegal_dis = 'Legal Disability'\nlegal_rep ='REPRESENTED BY Name address and capacity'"
constants = ''
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
            {name_sql} TEXT NOT NULL UNIQUE,
            {doc_path_sql} TEXT NOT NULL,
            {script_path_sql} TEXT NOT NULL
            )                
        ''')
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {case_table} (
            {id_sql} INTEGER PRIMARY KEY,
            {client_name_sql} TEXT NOT NULL UNIQUE,
            {case_info_path_sql} TEXT NOT NULL
            )                
        ''')
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {attorney_table} (
            {id_sql} INTEGER PRIMARY KEY,
            {attorney_name_sql} TEXT NOT NULL UNIQUE,
            {attorney_info_path_sql} TEXT NOT NULL
            )                
        ''')

        self.connection.commit()
    
    def close_db(self):
        self.cursor.close()
        self.connection.close()

    def get_local_doc_path(self, name):
        get_query = f'SELECT {doc_path_sql} FROM {docs_table} WHERE {name_sql} = ?'
        self.cursor.execute(get_query, (name,))
        self.destination_file = self.cursor.fetchone()[0]

    def get_local_py_path(self, name):
        get_query = f'SELECT {script_path_sql} FROM {docs_table} WHERE {name_sql} = ?'
        self.cursor.execute(get_query, (name,))
        self.destination_file_py = self.cursor.fetchone()[0]

    def get_template_names(self):
        self.cursor.execute(f'SELECT {name_sql} FROM {docs_table}')
        return self.cursor.fetchall()

    def get_case_names(self):
        self.cursor.execute(f'SELECT {client_name_sql} from {case_table}')
        return self.cursor.fetchall()
    
    def get_attorney_names(self):
        self.cursor.execute(f'SELECT {attorney_name_sql} from {attorney_table}')
        return self.cursor.fetchall()

    def add_to_doc_db(self, name):
        insert_query = f'INSERT OR REPLACE INTO {docs_table} ({name_sql}, {doc_path_sql}, {script_path_sql}) VALUES (?, ?, ?)'
        self.cursor.execute(insert_query, (name, self.destination_file, self.destination_file_py,))
        print('doc db added doc paths to db')
        self.connection.commit()

    def add_to_case_db(self, name):
        insert_query = f'INSERT INTO {case_table} ({client_name_sql}, {case_info_path_sql}) VALUES (?, ?)'
        self.cursor.execute(insert_query, (name, self.destination_file_py,))
        self.connection.commit()

    def add_attorney_to_db(self, name, path):
        insert_query = f'INSERT INTO {attorney_table} ({attorney_name_sql}, {attorney_info_path_sql}) VALUES (?, ?)'
        self.cursor.execute(insert_query, (name, path,))
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
        self.add_to_doc_db(template_name)
        print('added to db')

    '''
    TODO
    def remove_from_db(self):
    

    def rename(self):
        self.set_to_db(new_name, file_path)
        self.empty_new_py()
        self.populate_new_py()
        self.remove_from_db()'''

    

    
