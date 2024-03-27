import re

# Define token types
tokens = [
    ('IF', r'if(?=\s|\(|\)|;|$)'),
    ('THEN', r'then(?=\s|$)'),
    ('ID', r'[a-z]+'),
    ('INT', r'\d+'),
    ('ASSIGN', r'='),
    ('OP_PLUS', r'\+'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('SEMICOLON', r';'),
    ('WHITESPACE', r'\s+')
]

# Compile regular expressions for token types
patterns = [(name, re.compile(pattern)) for name, pattern in tokens]

# Function to tokenize the input program
def lexer(program):
    tokens = []
    while program:
        # Skip whitespace
        match = re.search(r'^\s+', program)
        if match:
            program = program[match.end():]
            continue

        # Try to match each token pattern
        found_match = False
        for token_name, pattern in patterns:
            match = pattern.match(program)
            if match:
                value = match.group(0)
                tokens.append((token_name, value))
                program = program[len(value):]
                found_match = True
                break
        if not found_match:
            print("Lexer Error: Unrecognized input:", program[0])
            break

    return tokens

# Sample program
sample_program = """
a = 1  ;
if   (   a    +    1   )   then   b  =  2  ;
b = a +5 ;
"""

# Tokenize the sample program
tokens = lexer(sample_program)
for token in tokens:
    print(token)
