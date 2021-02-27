import ply.yacc as yacc
from lexico import tokens

"""
def p_funcao(p):
    'funcao : FUNCTION nome_funcao bloco_funcao'

def p_nome_funcao(p):
    "nome_funcao : ID param_func ':' tipo_dado" 
"""

def p_variavel(p):
    "variavel : VAR ID lista_id ':' tipo_dado ';'"
    p[0] = 'pomarola' # so para conseguir checar se chegou aqui

def p_lista_id(p):
    '''lista_id : ',' ID lista_id
                |''' #empty rule
    pass

def p_tipo_dado(p):
    '''tipo_dado : INTEGER
                 | REAL
                 | ARRAY '[' NUMERO ']' OF tipo_dado
                 | RECORD campos END
                 | ID'''
    pass

def p_campos(p):
    "campos : ID ':' tipo_dado lista_campos"
    pass

def p_lista_campos(p):
    '''lista_campos : ';' campos lista_campos
                    |''' #empty rule
    pass

def p_error(p):
    print("Erro de sintax")

parser = yacc.yacc()

print(parser.parse('var I : integer;'))

"""
while True:
    try:
        s = 'var I : integer;'
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
"""
