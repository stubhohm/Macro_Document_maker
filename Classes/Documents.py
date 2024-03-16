querry_format = r'\.[^\s#]+#\s*[^#]+#'
db_path = 'documents.db'
docs_table = 'DocumentsTable'

id_sql = 'id'
name_sql = 'doc_name'
text_sql = 'doc_text'



class Documentsdb():
    name = "Documents_DataBase"
    def __init__(self, sql, re, doc_cls):
        self.document = []
        self.sql = sql
        self.re = re
        self.matches = None
        self.connection = sql.connect(db_path)
        self.cursor = self.connection.cursor()
        self.new_doc = None
        self.doc_cls = doc_cls

    def init_db(self):
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {docs_table} (
            {id_sql} INTEGER PRIMARY KEY,
            {name_sql} TEXT NOT NULL,
            {text_sql} TEXT NOT NULL
            )                
        ''')
        self.connection.commit()
    
    def close_db(self):
        self.cursor.close()
        self.connection.close()


    def get_template_names(self):
        self.cursor.execute(f'SELECT {name_sql} FROM {docs_table}')
        return self.cursor.fetchall()

    def find_queries(self, new_doc):
        new_doc.queries = self.re.findall(querry_format, new_doc.template_text)
        a = 0

    def validate_template_for_db(self, template_name, text):
        ## Instance the new document
        self.new_doc = self.doc_cls()
        self.new_doc.template_name = template_name
        self.new_doc.template_text = text
        
        # Regex the entry to find Query Macros
        self.find_queries(self.new_doc)
        
        # Format Queries from text into workable form and ensure there were no errors
        self.new_doc.format_queries()
        self.new_doc.validate_queries()


    

    
