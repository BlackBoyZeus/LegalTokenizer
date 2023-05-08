import re

class LegalTokenizer:
    def __init__(self):
        self.patterns = [
            (r'\bSection\s\d+\.\d+\([a-z]\)', 'SECTION_HEADING'),
            (r'\bAgreement\b', 'LEGAL_TERM'),
            (r'\bshall\sbe\samended\b', 'LEGAL_PHRASE'),
            (r'\bto\sread\sas\sfollows\b', 'LEGAL_PHRASE'),
            (r'\"[^\"]+\"', 'LEGAL_CLAUSE'),
            (r'\bConfidential\sInformation\b', 'LEGAL_TERM'),
            (r'\bDisclosing\sParty\b', 'LEGAL_TERM'),
            (r'\bthird\sparty\b', 'LEGAL_TERM'),
        ]
        
        self.regex_patterns = [(re.compile(p[0]), p[1]) for p in self.patterns]
        
    def tokenize(self, text):
        tokens = []
        
        for regex, token_type in self.regex_patterns:
            matches = regex.findall(text)
            for match in matches:
                tokens.append((match, token_type))
                
        return tokens
B
