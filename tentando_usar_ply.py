import ply.lex as lex

reservado = {
    'begin': 'BEGIN',
    'end': 'END',
    'const': 'CONST',
    'type': 'TYPE',
    'var': 'VAR',
    'while':'WHILE',
    'if': 'IF',
    'then': 'THEN',
    'read': 'READ',
    'else': 'ELSE',
}

tokens = ['NUMERO', 'ID', 'OPERADOR_MAT'] + list(reservado.values())

def t_NUMERO(t):
    r'(\d+\.\d+)|(\d+)' #Nesse caso será aceito 1.5 mas não 1. nem .5
    print( "O token " + t.value + " é um real" )
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reservado.get(t.value,'ID')
    print( t.type)
    return t

def t_error(t):
     print("Não é possivel identificar o caractere: '%s'" % t.value[0])
     t.lexer.skip(1)

t_ignore = ' \t'

lexer = lex.lex()

lexer.input('else')

while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok.type, tok.value, tok.lineno, tok.lexpos)      # No more input
