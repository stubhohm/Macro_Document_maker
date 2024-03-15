tags = [
    ['.date', r'^\d{1,2}/\d{1,2}(/(\d{2}|\d{4}))?$', ],
    ['.name', r'^[A-Za-z]+(?: [A-Za-z\-]+)*$ '],
    ['.number', r'^\d{1,3}(,\d{3})*(\.\d+)?$'],
    ['.pronoun', r'^\w+$'],
    ['.heshe', r'^\w+$'],
    ['.himher', r'^\w+$'],
    ['.w', None]
]

class Query():
    def __init__(self, type, input, description):
        '''
        Type refers to the type in the way such as name, date, number, ect
        '''
        self.type = type
        self.input = input
        self.description = description