import ply.yacc as yacc
from validation_lex import tokens

#####################################################################################
def p_statement(p):
    '''
    statement : assignment
    | if
    | ifelse
    | while
    | for
    | statement statement
    '''
    p[0] = "Valid"


#####################################################################################
# I) Validation of simple variable declarations (integer, float, strings)
def p_assignment(p):
    '''
    assignment : DOLLAR ID EQUAL expression SEMICOLON 
    | DOLLAR ID EQUAL MINUS expression SEMICOLON
    | DOLLAR ID EQUAL PLUS expression SEMICOLON
    | DOLLAR ID EQUAL MINUS expression POINT expression SEMICOLON
    | DOLLAR ID EQUAL PLUS expression POINT expression SEMICOLON
    | DOLLAR ID EQUAL expression POINT expression SEMICOLON
    | DOLLAR ID EQUAL STRING SEMICOLON
    '''
    

#####################################################################################
# II) if-statement syntax validation
def p_if(p):
    '''
    if : IF LPAREN expression CONDITIONAL expression RPAREN LCURLY statement RCURLY
    | IF LPAREN expression RPAREN LCURLY statement RCURLY
    '''


#####################################################################################
# III) if-else statement syntax validation
def p_ifelse(p):
    '''ifelse : if ELSE LCURLY statement RCURLY'''


#####################################################################################
# IV) While loop syntax validation
def p_while(p):
    '''
    while : WHILE LPAREN expression CONDITIONAL expression RPAREN LCURLY statement RCURLY
    | WHILE LPAREN expression RPAREN LCURLY statement RCURLY
    '''


#####################################################################################
# V) For loop syntax validation
def p_for(p):
    '''
    for : FOR LPAREN my DOLLAR ID EQUAL expression SEMICOLON DOLLAR ID CONDITIONAL expression SEMICOLON DOLLAR ID INCDEC RPAREN LCURLY statement RCURLY
    '''

#####################################################################################


# Defining expression
def p_id(p):
    'expression : DOLLAR ID' 

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Syntax error in input!\n")

parser = yacc.yacc()


while True:
    try:
        s = input('perl syntax > ')
    except EOFError:
        break
    if not s: 
        continue
    result = parser.parse(s)
    if(result):
        print("Valid syntax\n")
