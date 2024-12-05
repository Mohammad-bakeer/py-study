
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

# Regular expression for ignoring comments
comment_pattern = r'\/\/.*|\"{3}[\s\S]*?\"{3}|#.*|\/\*[\s\S]*?\*\/'

# Compile regular expressions for token types and comments
patterns = [(name, re.compile(pattern)) for name, pattern in tokens]
comment_regex = re.compile(comment_pattern)

# Function to tokenize the input program
def lexer(program):
    tokens = []
    while program:
        # Skip comments
        match = comment_regex.match(program)
        if match:
            program = program[match.end():]
            continue

        # Skip whitespace
        match = re.match(r'^\s+', program)
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
//comment
a = 1  ;
if   (   a    +    1   )   then   b  =  2  ;
b = a +5 ; #commet
/*
comment
*/
"""

# Tokenize the sample program
tokens = lexer(sample_program)
for token in tokens:
    print(token)
