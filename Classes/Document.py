class Document():
    
    def __init__(self,) -> None:
        self.document_name = None
        self.template_name = None
        self.document_path = None
        self.queries = []
        self.valid_tags = []
        self.valid_descriptions = []
        self.text = None
        self.max_description_lenth = 250
        self.qry_cls = None
        self.tags = None

    def get_queries(self):
        self.queries = []

    def get_text(self):
        self.text = ''

    def format_queries(self):
        self.queries = [match.split('#') for match in self.queries]

    def validate_tags(self, i=0):
        self.valid_queries = [0] * len(self.queries)
        for query in self.queries:
            if query[0] in self.tags[0]:
                self.valid_tags[i] = True
                i += 1
                continue
            self.valid_tags[i] = False
            i += 1

    def validate_descriptions(self, i=0):
        self.valid_descriptions = [0] * len(self.queries)
        for query in self.queries:
            if len(query[1]) > self.max_description_lenth:
                self.valid_descriptions[i] = False
                i +=1
                continue
            i += 1

    def validate_queries(self):
        self.validate_tags()
        self.validate_descriptions()

        
            
