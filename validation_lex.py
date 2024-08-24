import ply.lex as lex

# List of tokens
tokens = [
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'ID',
   'EQUAL',
   'DOLLAR',
   'POINT',
   'SEMICOLON',
   'STRING',
   'LCURLY',
   'RCURLY',
   'CONDITIONAL',
   'INCDEC',
   'SINGLEQUOTES',
   'DOUBLEQUOTES',
]


# Dictionary containing reserved values
reserved = {
   'if' : 'IF',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'for' : 'FOR',
   'my' : 'my',
}


# Defining regular expressions for the tokens present in the list above
t_EQUAL = r'\='
t_DOLLAR = r'\$'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_POINT = r'\.'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_STRING = r'\"[a-zA-Z_0-9~!@#$%^&*()_+=-|?{}\s]*"' or r"\'[a-zA-Z_0-9~!@#$%^&*()_+=-|?{}\s]*'"
t_CONDITIONAL = r'>=|<=|<|>|==|!='
t_INCDEC = r'\++|--'
t_SINGLEQUOTES = r"\'"
t_DOUBLEQUOTES = r'\"'


# Appending the values in the "reserved" dictionary to the list of tokens
tokens = tokens + list(reserved.values())


# Defining regular expressions for the tokens 
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
