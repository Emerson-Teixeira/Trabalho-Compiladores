import ply.yacc as yacc
from lexico import tokens
from pprint import pprint

# Será a tabela de simbolos, implementada como um dicionário aninhado.
tabela_sim = {}

# Lista com a tabelas de símbolos, importante para lidar com escopo.
lista_tab = [tabela_sim]

def new_scope_push():
    global tabela_sim
    global lista_tab

    # Cria o novo escopo
    new_tab = {}

    # Adciona na pilha de escopos
    lista_tab = lista_tab + [new_tab]

    # Atualiza a referência pra tabela de símbolos
    tabela_sim = new_tab

def del_scope_pop():
    global tabela_sim
    global lista_tab

    # Exclui o último elemento da lista
    lista_tab = lista_tab[:-1]

    # Atualiza a referencia pra tabela de símbolos
    tabela_sim = lista_tab[-1]

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
                 | empty''' # empty rule
    print('def_const reconhecido')
    
def p_def_tipos(p):
    '''def_tipos : tipo def_tipos
                 | empty''' # empty rule
    print("Def_tipos reconhecido")

def p_def_var(p):
    '''def_var : variavel def_var
               | empty''' # empty rule
    print("Def_var reconhecido")

def p_def_func(p):
    '''def_func : funcao def_func
                | empty'''
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
    
    # Essa linha deve adcionar um registro na tabela de símbolos
    # O registro vai ser uma entrada no dicionário "tabela_sim"
    # Que liga o ID à uma outra tabela, com campos variados como type
    tabela_sim.update({p[2]: {'type':p[5]}})

    if (p[3]):
        for i in p[3]:
            print(i)
            tabela_sim.update({i: {'type':p[5]}})
    
    print ('Regra variável reconhecida')
    
def p_lista_id(p):
    '''lista_id : ',' ID lista_id
                | empty''' #empty rule

    if (p[1] != None):
        if (p[3]):
            p[0] = p[3] + [p[2]]
        else:
            p[0] = [p[2]]
 
    print("Lista ID reconhecido")

def p_campos(p):
    "campos : ID ':' tipo_dado lista_campos"
    
    tabela_sim.update({p[1]: {'type':p[3]}})

    p[0] = 1 + p[4]
    
    print("campos reconhecido")

def p_lista_campos(p):
    '''lista_campos : ';' campos
                    | empty ''' #empty rule

    if (p[1] == None):
        p[0] = 0
    else:
        p[0] = p[2]
        
    print("lista_campos reconhecido")
    
def p_tipo_dado(p):
    '''tipo_dado : INTEGER
                 | REAL
                 | ARRAY '[' NUMERO ']' OF tipo_dado
                 | RECORD campos END
                 | ID'''

    # Funciona porque o tipo é sempre o primeiro símbolo na parte
    # direita da regra.
    p[0] = p[1]
    
    print("Tipo_dado reconhecido")

def p_funcao(p):
    '''funcao : FUNCTION new_scope nome_funcao bloco_funcao'''
    print("Escopo da função: ", p[3][0], "\n", tabela_sim)
    del_scope_pop()
    tabela_sim.update({p[3][0] : {"type" : "function", "return_type" : p[3][1], "n_param" : p[3][2]}})
    print('Funcao reconhecido')

def p_nome_funcao(p):
    '''nome_funcao : ID param_func ':' tipo_dado'''
    tabela_sim.update({'result' : {'type' : p[4]}, 'nome' : p[1]})
    p[0] = (p[1], p[4], p[2])
    print('Nome_funcao reconhecido')

def p_param_func(p):
    '''param_func : '(' campos ')'
                  | empty '''

    if (p[1] == None):
        p[0] = 0
    else:
        p[0] = p[2]
    
    print('param_func reconhecido')

def p_bloco_funcao(p):
    '''bloco_funcao : def_var BEGIN comando lista_com END'''
    print("Bloco_funcao reconhecido")

def p_lista_com(p):
    '''lista_com : ';' comando lista_com
                 | empty''' # empty rule
    print('Lista_com reconhecido')

def p_bloco(p):
    '''bloco : BEGIN comando lista_com END
             | comando''' # empty rule
    print("Bloco reconhecido")

def p_comando(p):
    '''comando : ID nome ATRIBUICAO exp_mat
               | WHILE exp_logica bloco
               | IF exp_logica THEN bloco else
               | WRITE const_valor
               | READ ID nome'''

    if (p[1] not in ['while', 'if', 'write', 'read']):
        if (p[1] in tabela_sim):
            print( "\n\n Variavel declarada antes do \n\n")
            print( p[4] )
            for i in p[4]:
                if (tabela_sim[p[1]]['type'] == 'real'):
                    if (i not in ['real', 'integer']):
                        print("Erro semântico tipo esperado não encontrado da variável: ", p[1])
                    else:
                        continue
                if (tabela_sim[p[1]]['type'] != i):
                    print("Erro semântico tipo esperado não encontrado da variável: ", p[1])
        else:
            print( "\n\n não foi: ", p[1], " \n\n" )


def p_else(p):
    '''else : ELSE bloco
            | empty''' # empty rule
    print('else reconhecido')

def p_lista_param(p):
    '''lista_param : parametro lista_param_aux
                   | empty''' # empty rule
    print('lista_param reconhecido')

def p_lista_param_aux(p):
    '''lista_param_aux : ',' lista_param
                       | empty''' # empty rule

def p_exp_logica(p):
    '''exp_logica : exp_mat exp_logica_aux'''
    print('exp_logica reconhecida')

def p_exp_logica_aux(p):
    '''exp_logica_aux : op_logico exp_logica
                      | empty''' # empty rule

def p_exp_mat(p):
    '''exp_mat : parametro exp_mat_aux'''
    p[0] = p[2] + [p[1]]
    print('\n\nexp_mat reconhecido: ', p[0], '\n\n')

def p_exp_mat_aux(p):
    '''exp_mat_aux : OP_MAT exp_mat
                   | empty''' # empty rule
    if (p[1] != None):
        p[0] = p[2]
    else:
        p[0] = []

def p_parametro(p):
    '''parametro : ID nome
                 | NUMERO'''
    
    global tabela_sim

    # Se der erro é porque é numero
    # Estamos retornando o tipo pra faze a segunda regra semantica
    try:
        p[2]
        if (tabela_sim[p[1]]['type'] == 'function'):
            p[0] = tabela_sim[p[1]]['return_type']
            print("\n\nRetornou função: ", p[0], "\n\n")
        else:
            p[0] = tabela_sim[p[1]]['type']
            print("\n\nRetornou ", p[0], "\n\n")
    except:
         if (p[1].find('.') != -1):
             p[0] = 'real'
             print("\n\n Retornou float \n\n")
         else:
             p[0] = 'integer'
             print("\n\n Retornou int \n\n")
        
    print('parametro reconhecido')

def p_op_logico(p):
    '''op_logico : '<'
                 | '>'
                 | '='
                 | '!' '''
    print('Operador Logico reconhecido')   

def p_nome(p):
    '''nome : '.' ID nome
            | '[' parametro ']'
            | '(' lista_param ')'
            | empty''' # empty rule
    print('nome reconhecido')

def p_new_scope(p):
    "new_scope :"
    new_scope_push()

def p_empty(p):
     'empty :'
     pass

def p_error(p):
    print("\n\nERRO NA LINHA: ", p.lineno, "!!!!!")
    print("TOKEN COM ERRO: ", p.value, "!!!!!")
    print("TIPO DO TOKEN: ", p.type, "!!!!!!\n\n")

    if not p:
        print("End of File!")
        return
 
    while True:
        tok = parser.token() # Get the next token
        
        if not tok: 
            break
        elif tok.type == 'END':
            return tok
        elif tok.type == ';':
            print("\npulou!!!! : ", tok.type, tok.value, "\n")
            parser.errok()
        print("\npulou!!!! : ", tok.type, tok.value, "\n")

parser = yacc.yacc()

print(parser.parse('''
const TAM = 10;
type vetor = array [15] of integer;
type aluno = record
nota1 : real;
nota2 : real
end;
var A, B, C, D : integer;
var E : vetor;
var F : aluno;
function fatorial(a:integer) : integer
var i : integer;
begin
i := 1;
result:=1;
while i < a
begin
result:=result*i;
i:=i+1
end
end
function exp(a: real; b: real) : real
var i : integer;
begin
i := 1;
result := a;
if b = 0 then
result := 1
else
while i < b
begin
result := a * a;
i := i + 1
end
end
function lerDados : aluno
begin
write "digite as notas do aluno";
read result.nota1;
read result.nota2
end
function maior(a : vetor) : integer
var i : integer;
begin
i := 0;
result := a[0];
while i < 15
if a[i] > result then
result := a[i]
end
function menor(a : vetor) : integer
var i : integer;
begin
i := 0;
result := a[0];
while i < 15
if a[i] < result then
result := a[i]
end
function media(a : vetor) : integer
var m : integer;
begin
m := maior(a) + menor(a);
result := m / 2
end
begin
A:=TAM + 20;
B := fatorial(A);
C := exp(A,B);
D := media(E);
F := lerDados()
end
'''))

pprint(tabela_sim)

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
