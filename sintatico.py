import ply.yacc as yacc
from lexico import tokens
from pprint import pprint
import pdb

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
    p[0] = 'Concluido'

def p_principal(p):
    'principal : BEGIN comando lista_com END'

def p_declaracoes(p):
    'declaracoes : def_const def_tipos def_var def_func'

def p_def_const(p):
    '''def_const : constante def_const
                 | empty''' # empty rule
    
def p_def_tipos(p):
    '''def_tipos : tipo def_tipos
                 | empty''' # empty rule

def p_def_var(p):
    '''def_var : variavel def_var
               | empty''' # empty rule

def p_def_func(p):
    '''def_func : funcao def_func
                | empty'''

def p_constante(p):
    '''constante : CONST ID '=' const_valor ';' '''
    print("Constante reconhecido")

def p_const_valor(p):
    '''const_valor : CONST_VALOR
                   | exp_mat'''

def p_tipo(p):
    '''tipo : TYPE ID '=' tipo_dado ';' '''
    if (isinstance(p[4], tuple)):
        if (p[4][0] == 'array'):
            tabela_sim.update({p[2]: {'type': 'type', 'ttype':'array', 'type_array': p[4][2], 'n_indices' : p[4][1]}})
        else: # então é record
            tabela_sim.update({p[2]: {'type': 'type', 'ttype':'record', 'var_record': {}}})
            for i in p[4][1][1]: # Lista vinda da regra campos
                tabela_sim[p[2]]['var_record'].update({i[0] : {'type' : i[1]}})


def p_variavel(p):
    "variavel : VAR ID lista_id ':' tipo_dado ';'"
    
    # Essa linha deve adcionar um registro na tabela de símbolos
    # O registro vai ser uma entrada no dicionário "tabela_sim"
    # Que liga o ID à uma outra tabela, com campos variados como type
    if (isinstance(p[5], tuple)):
        tabela_sim.update({p[2] : {'type': p[5][0], 'type_array' : p[5][1]}})
        
    tabela_sim.update({p[2]: {'type':p[5]}})

    if (p[3]):
        for i in p[3]:
            tabela_sim.update({i: {'type':p[5]}})
    
def p_lista_id(p):
    '''lista_id : ',' ID lista_id
                | empty''' #empty rule

    if (p[1] != None):
        if (p[3]):
            p[0] = p[3] + [p[2]]
        else:
            p[0] = [p[2]]

def p_campos(p):
    "campos : ID ':' tipo_dado lista_campos"

    p[0] = (1 + p[4][0], p[4][1] + [(p[1], p[3])])

def p_lista_campos(p):
    '''lista_campos : ';' campos
                    | empty ''' #empty rule

    if (p[1] == None):
        p[0] = (0, [])
    else:
        p[0] = p[2]
    
def p_tipo_dado(p):
    '''tipo_dado : INTEGER
                 | REAL
                 | ARRAY '[' NUMERO ']' OF tipo_dado
                 | RECORD campos END
                 | ID'''

    if (p[1] == 'array'):
        p[0] = (p[1], p[3], p[6])
    elif (p[1] == 'record'):
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]

def p_funcao(p):
    '''funcao : FUNCTION new_scope nome_funcao bloco_funcao'''
    print("Escopo da função:", p[3][0])
    pprint(tabela_sim)
    print("\n")
    del_scope_pop()
    tabela_sim.update({p[3][0] : {"type" : "function", "return_type" : p[3][1], "n_param" : p[3][2]}})

def p_nome_funcao(p):
    '''nome_funcao : ID param_func ':' tipo_dado'''
    tabela_sim.update({'result' : {'type' : p[4]}, 'nome' : p[1]})
    p[0] = (p[1], p[4], p[2])

def p_param_func(p):
    '''param_func : '(' campos ')' 
                  | empty '''

    if (p[1] == None):
        p[0] = 0
    else: # Retornando o número de parâmetros
        p[0] = p[2][0]

    # Adcionando os parametros como variaveis no escopo interno da função
    if (p[1] != None):
        for i in p[2][1]:
            tabela_sim.update({i[0] : {'type' : i[1]}})

def p_bloco_funcao(p):
    '''bloco_funcao : def_var BEGIN comando lista_com END'''

def p_lista_com(p):
    '''lista_com : ';' comando lista_com
                 | empty''' # empty rule

def p_bloco(p):
    '''bloco : BEGIN comando lista_com END
             | comando''' # empty rule

def p_comando(p):
    '''comando : ID nome ATRIBUICAO exp_mat
               | WHILE exp_logica bloco
               | IF exp_logica THEN bloco else
               | WRITE const_valor
               | READ ID nome'''

    # Primeira e segunda regra semântica
    if (p[1] not in ['while', 'if', 'write', 'read']):
        if (p[1] in tabela_sim):
            for i in p[4][0]:
                tipo_esperado = tabela_sim[p[1]]['type']
                if (tipo_esperado != i[0]):
                    print("\n\nErro semântico!")
                    print("Esperado o tipo: ", tipo_esperado)
                    print("Encontrado o tipo: ", i[0])
                    print("Na variável: ", p[0])
                    try:
                        nome = tabela_sim['nome']
                        print("No escopo da função: ", nome)
                    except:
                        print("No escopo global")
                    print("\n")
        else:
            print("\n\nErro semântico!")
            print("Referência à uma váriavel não declarada: ", p[1], "\n\n")

def p_else(p):
    '''else : ELSE bloco
            | empty''' # empty rule

def p_lista_param(p):
    '''lista_param : parametro lista_param_aux
                   | empty''' # empty rule

    if(p[1] != None):
        p[0] = p[2] + 1
    else:
        p[0] = 0

def p_lista_param_aux(p):
    '''lista_param_aux : ',' lista_param
                       | empty''' # empty rule

    if (p[1] == None):
        p[0] = 0
    else:
        p[0] = p[2]

def p_exp_logica(p):
    '''exp_logica : exp_mat exp_logica_aux'''

def p_exp_logica_aux(p):
    '''exp_logica_aux : op_logico exp_logica
                      | empty''' # empty rule

def p_exp_mat(p):
    '''exp_mat : parametro exp_mat_aux'''
    instrucoes = None

    if (p[1][2] == 'func'): # Chamada de função na expressão matemática
        if (p[2][2] == 'empty'):
            p[2][1][-1] = 'jump ' + p[1][1]
            instrucoes = p[2][1]
        if (p[2][2] == 'OP_MAT'):
            instrucoes = p[2][1][:-1] + [
                'atr temp_aux temp',
                'jump ' + p[1][1], # jump <nome_funcao>
                p[2][1][-1] + 'temp_aux'] # operação temp temp temp_aux
        
        

    elif (p[1][2] == 'variavel' or p[1][2] == 'numero'):
        # Deixando a instrução intermediária
        # correta para parâmetros que sejam
        # variáveis ou números
        p[2][1][-1] = p[2][1][-1] + p[1][1]
        instrucoes = p[2][1]

    p[0] = (p[2][0] + [p[1]], p[2][1])
    p[0] = (p[2][0] + [p[1]], instrucoes)

    pprint(p[0][1])

def p_exp_mat_aux(p):
    '''exp_mat_aux : OP_MAT exp_mat
                   | empty''' # empty rule
    if (p[1] != None):
        if (p[1] == '*'):
            ii = 'mult temp temp ' 
        elif (p[1] == '+'):
            ii = 'add temp temp '
        elif (p[1] == '-'):
            ii = 'sub temp temp '
        elif (p[1] == '/'):
            ii = 'div temp temp '
        p[0] = (p[2][0], p[2][1] + [ii], 'OP_MAT')
    else:
        p[0] = ([], ['atr temp '], 'empty')

def p_parametro(p):
    '''parametro : ID nome
                 | NUMERO'''
    # p[0][1] vai ser sempre nome que vai ser posto na instrução intermediária
    # p[0][2] ?
    # p[0][3] o tipo de parametro (variavel, função, etc

    # Se der erro é porque é numero
    # Estamos retornando o tipo pra faze a segunda regra semantica
    
    try:
        if (isinstance(p[2], str)):
            if(p[2] == 'indice_array'):
                try:
                    if (tabela_sim[p[1]]['type'] == 'array'):
                        p[0] = (tabela_sim[p[1]]['array_type'], p[1], 'array')
                    elif (lista_tab[0][tabela_sim[p[1]]['type']]['ttype'] == 'array'):
                        p[0] = (lista_tab[0][tabela_sim[p[1]]['type']]['type_array'], p[1], 'array')
                except:
                    print(p[1])
                    print("Erro semântico, acessando indice de algo que não é array!!!!")  
            else: # Aqui trata o caso de ser uma variável comum em uma expressão matemática
                p[0] = (tabela_sim[p[1]]['type'], p[1], 'variavel')
        elif (isinstance(p[2], tuple)): # Então é record ou função
            if (p[2][0] == 'record_field'):
                try:
                    var_interna = lista_tab[0][tabela_sim[p[1]]['type']]['var_record']
                    try:
                        p[0] = (var_interna[p[2][1]], 'param', 'record')
                    except:
                        # Ultima regra
                        print("Erro semantico, tentou acessar campo não existente do record")
                except:
                    # penultima regra
                    print("Erro semântico, variável não é do tipo record: ", p[1])
            if (p[2][0] == 'param_func'):
                try:
                    if (lista_tab[0][p[1]]['type'] == 'function'):
                        p[0] = (lista_tab[0][p[1]]['return_type'], p[1], 'func')
                        if(lista_tab[0][p[1]]['n_param'] != p[2][1]):
                            # não tem o mesmo número de parametro do protótipo
                            print("não tem o mesmo número de parametro do protótipo: ", p[1])
                    else:
                        print("não é função declarada", p[1])
                except:
                    # não é função declarada
                    print("não é função declarada")
    except:
         if (p[1].find('.') != -1):
             p[0] = ('real', p[1], 'numero')
         else:
             p[0] = ('integer', p[1], 'numero')

def p_op_logico(p):
    '''op_logico : '<'
                 | '>'
                 | '='
                 | '!' '''

def p_nome(p):
    '''nome : '.' ID nome
            | '[' parametro ']'
            | '(' lista_param ')'
            | empty''' # empty rule

    if (p[1] == '['):
        p[0] = 'indice_array'
    elif (p[1] == '.'):
        p[0] = ('record_field', p[2])
    elif (p[1] == '('):
        p[0] = ('param_func', p[2]) # p[2] contém numero de parametros
    else:
        p[0] = 'string'

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
read result.nota2;
read result.nota3
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
