import ply.lex as lex

tokens = ( 'INTEIRO', 'REAL', 'IDENTIFICADOR', 'OPERADOR_MAT', 'SPECIAL_CHARACTERS')

def t_REAL(t):
    r'\d+\.\d+' #Nesse caso será aceito 1.5 mas não 1. nem .5
    print( "O token " + t.value + " é um real" )
    return t

def t_INTEIRO(t):
    r'\d+'
    print( "O token " + t.value + " é um inteiro" )
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    print( "O token " + t.value + " é um identificador" )
    return t

def t_OPERADOR_MAT(t):
    r'\+|-|\*|/'
    print( "O token " + t.value + " é um operador matemático" )
    return t

def t_error(t):
     print("Não é possivel identificar o caractere: '%s'" % t.value[0])
     t.lexer.skip(1)

t_ignore = ' \t'

lexer = lex.lex()

lexer.input(' identificatorator 96 95.0 + algo - * . /')

while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
