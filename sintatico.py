import ply.yacc as yacc
from lexico import tokens

def p_programa(p):
    'programa : declaracoes principal'
    print('Programa reconhecido')

def p_principal(p):
    'principal : BEGIN comando lista_com END'
    print('Principal reconhecido')

def p_declaracoes(p):
    'declaracoes : def_const def_tipos def_var def_func'
    print('Declarações reconhecido')

def p_def_const(p):
    '''def_const : constante def_const
                 | ''' # empty rule
    print('def_const reconhecido')
    
def p_def_tipos(p):
    '''def_tipos : tipo def_tipos
                 | ''' # empty rule
    print("Def_tipos reconhecido")

def p_def_var(p):
    '''def_var : variavel def_var
               | ''' # empty rule
    print("Def_var reconhecido")

def p_def_func(p):
    '''def_func : funcao def_func
                | '''
    print("Def_func reconhecido")

def p_constante(p):
    '''constante : CONST ID '=' const_valor ';' '''
    print("Constante reconhecido")

def p_const_valor(p):
    '''const_valor : CONST_VALOR
                   | exp_mat'''
    print('const_valor reconhecido')

def p_tipo(p):
    '''tipo : TYPE ID '=' tipo_dado ';' '''
    print('Tipo reconhecido')

def p_variavel(p):
    "variavel : VAR ID lista_id ':' tipo_dado ';'"
    print ('Regra variável reconhecida')
    p[0] = 'pomarola' # so para conseguir checar se chegou aqui

def p_lista_id(p):
    '''lista_id : ',' ID lista_id
                |''' #empty rule
    print("Lista ID reconhecido")

def p_campos(p):
    "campos : ID ':' tipo_dado lista_campos"
    print("campos reconhecido")

def p_lista_campos(p):
    '''lista_campos : ';' campos lista_campos
                    |''' #empty rule
    print("lista_campos reconhecido")
    
def p_tipo_dado(p):
    '''tipo_dado : INTEGER
                 | REAL
                 | ARRAY '[' NUMERO ']' OF tipo_dado
                 | RECORD campos END
                 | ID'''
    print("Tipo_dado reconhecido")

def p_funcao(p):
    '''funcao : FUNCTION nome_funcao bloco_funcao'''
    print('Funcao reconhecido')

def p_nome_funcao(p):
    '''nome_funcao : ID param_func ':' tipo_dado'''
    print('Nome_funcao reconhecido')

def p_param_func(p):
    '''param_func : '(' campos ')' '''
    print('param_func reconhecido')

def p_bloco_funcao(p):
    '''bloco_funcao : def_var BEGIN comando lista_com END'''
    print("Bloco_funcao reconhecido")

def p_lista_com(p):
    '''lista_com : ';' comando lista_com
                 | ''' # empty rule
    print('Lista_com reconhecido')

def p_bloco(p):
    '''bloco : BEGIN comando lista_com END
             | ''' # empty rule
    print("Bloco reconhecido")

def p_comando(p):
    '''comando : nome ATRIBUICAO exp_mat
               | WHILE exp_logica bloco
               | IF exp_logica THEN bloco else
               | WRITE const_valor
               | READ nome'''
    print('comando reconhecido')

def p_else(p):
    '''else : ELSE bloco
            | ''' # empty rule
    print('else reconhecido')

def p_lista_param(p):
    '''lista_param : parametro lista_param_aux
                   | ''' # empty rule
    print('lista_param reconhecido')

def p_lista_param_aux(p):
    '''lista_param_aux : ',' lista_param
                       | ''' # empty rule

def p_exp_logica(p):
    '''exp_logica : exp_mat exp_logica_aux'''
    print('exp_logica reconhecida')

def p_exp_logica_aux(p):
    '''exp_logica_aux : OP_LOGICO exp_logica
                      | ''' # empty rule

def p_exp_mat(p):
    '''exp_mat : parametro exp_mat_aux'''
    print('exp_mat reconhecido')

def p_exp_mat_aux(p):
    '''exp_mat_aux : OP_MAT exp_mat
                   | ''' # empty rule

def p_parametro(p):
    '''parametro : ID nome
                 | NUMERO'''
    print('parametro reconhecido')

def p_nome(p):
    '''nome : '.' ID nome
            | '[' parametro ']'
            | '(' lista_param ')'
            | ''' # empty rule
    print('nome reconhecido')
    
def p_error(p):
    print("Erro de sintax")

parser = yacc.yacc()

print(parser.parse('''

const TAM = 10;
type vetor = array[15] of integer;
type aluno = record;
    nota1 :real;
    nota2 :real;
  end;
var A, B, C, D : integer;
var E:vetor;
var F:aluno;

'''))

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