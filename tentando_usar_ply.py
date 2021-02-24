import ply.lex as lex

reservado = {
    'begin': 'BEGIN',
    'end': 'END',
    'const': 'CONST',
    'type': 'TYPE',
    'var': 'VAR',
    'while':'WHILE',
    'write': 'WRITE',
    'if': 'IF',
    'then': 'THEN',
    'read': 'READ',
    'else': 'ELSE',
    'integer': 'INTEGER',
    'real':'REAL',
    'array':'ARRAY',
    'record':'RECORD',
    'function':'FUNCTION',
    'of':'OF',
}

tokens = ['NUMERO', 'ID', 'OP_MAT', 'OP_LOGICO','ATRIBUICAO','CONST_VALOR'] + list(reservado.values())

literals = ";.,[]():"

def t_NUMERO(t):
    r'(\d+\.\d+)|(\d+)' #Nesse caso será aceito 1.5 mas não 1. nem .5
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reservado.get(t.value,'ID')
    return t

def t_OP_LOGICO(t):
    r'>|<|=|!'
    return t

def t_OP_MAT(t):
    r'\+|-|\*|/'
    return t

def t_error(t):
     print("Não é possivel identificar o caractere: '%s'" % t.value[0])
     t.lexer.skip(1)

def t_ATRIBUICAO(t):
    r'\:='
    return t

def t_CONST_VALOR(t):
    r'\"[a-zA-Z0-9]*\"'
    return t

t_ignore = ' \t \n'

lexer = lex.lex()

lexer.input('"asdasdasd"')

while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok.type)      # No more input
