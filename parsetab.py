
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ARRAY ATRIBUICAO BEGIN CONST CONST_VALOR ELSE END FUNCTION ID IF INTEGER NUMERO OF OP_MAT READ REAL RECORD THEN TYPE VAR WHILE WRITEprograma : declaracoes principalprincipal : BEGIN comando lista_com ENDdeclaracoes : def_const def_tipos def_var def_funcdef_const : constante def_const\n                 | emptydef_tipos : tipo def_tipos\n                 | emptydef_var : variavel def_var\n               | emptydef_func : funcao def_func\n                | emptyconstante : CONST ID '=' const_valor ';' const_valor : CONST_VALOR\n                   | exp_mattipo : TYPE ID '=' tipo_dado ';' variavel : VAR ID lista_id ':' tipo_dado ';'lista_id : ',' ID lista_id\n                | emptycampos : ID ':' tipo_dado lista_camposlista_campos : ';' campos lista_campos\n                    | empty tipo_dado : INTEGER\n                 | REAL\n                 | ARRAY '[' NUMERO ']' OF tipo_dado\n                 | RECORD campos END\n                 | IDfuncao : FUNCTION nome_funcao bloco_funcaonome_funcao : ID param_func ':' tipo_dadoparam_func : '(' campos ')' bloco_funcao : def_var BEGIN comando lista_com ENDlista_com : ';' comando lista_com\n                 | emptybloco : BEGIN comando lista_com END\n             | emptycomando : nome ATRIBUICAO exp_mat\n               | WHILE exp_logica bloco\n               | IF exp_logica THEN bloco else\n               | WRITE const_valor\n               | READ nomeelse : ELSE bloco\n            | emptylista_param : parametro lista_param_aux\n                   | emptylista_param_aux : ',' lista_param\n                       | emptyexp_logica : exp_mat exp_logica_auxexp_logica_aux : op_logico exp_logica\n                      | emptyexp_mat : parametro exp_mat_auxexp_mat_aux : OP_MAT exp_mat\n                   | emptyparametro : ID nome\n                 | NUMEROop_logico : '<'\n                 | '>'\n                 | '='\n                 | '!' nome : '.' ID nome\n            | '[' parametro ']'\n            | '(' lista_param ')'\n            | emptyempty :"
    
_lr_action_items = {'CONST':([0,4,95,],[6,6,-12,]),'TYPE':([0,3,4,5,10,13,95,108,],[-62,12,-62,-5,12,-4,-12,-15,]),'VAR':([0,3,4,5,9,10,11,13,26,29,84,89,91,92,95,108,122,127,129,138,],[-62,-62,-62,-5,28,-62,-7,-4,28,-6,28,-26,-22,-23,-12,-15,-25,-28,-16,-24,]),'FUNCTION':([0,3,4,5,9,10,11,13,25,26,27,29,52,55,95,102,108,129,137,],[-62,-62,-62,-5,-62,-62,-7,-4,54,-62,-9,-6,54,-8,-12,-27,-15,-16,-30,]),'BEGIN':([0,2,3,4,5,9,10,11,13,24,25,26,27,29,36,37,38,39,40,46,51,52,53,55,65,67,72,74,75,76,77,78,79,83,84,89,91,92,95,98,99,102,103,108,114,122,127,129,137,138,],[-62,8,-62,-62,-5,-62,-62,-7,-4,-61,-62,-62,-9,-6,63,-62,-62,-62,-53,-62,-3,-62,-11,-8,-46,-48,-49,-51,-52,63,-58,-59,-60,-10,-62,-26,-22,-23,-12,-47,-50,-27,116,-15,63,-25,-28,-16,-30,-24,]),'$end':([1,7,59,],[0,-1,-2,]),'ID':([6,12,17,18,19,21,22,23,28,31,35,54,57,66,68,69,70,71,73,81,87,94,105,106,117,123,133,135,],[14,30,39,39,39,46,39,39,56,39,39,85,89,39,-54,-55,-56,-57,39,39,107,111,111,89,89,89,89,111,]),'WHILE':([8,33,63,116,],[17,17,17,17,]),'IF':([8,33,63,116,],[18,18,18,18,]),'WRITE':([8,33,63,116,],[19,19,19,19,]),'READ':([8,33,63,116,],[20,20,20,20,]),'.':([8,20,33,39,46,63,116,],[21,21,21,21,21,21,21,]),'[':([8,20,33,39,46,63,93,116,],[22,22,22,22,22,22,109,22,]),'(':([8,20,33,39,46,63,85,116,],[23,23,23,23,23,23,105,23,]),'ATRIBUICAO':([8,16,24,33,46,63,77,78,79,116,],[-62,35,-61,-62,-62,-62,-58,-59,-60,-62,]),'=':([14,24,30,37,38,39,40,46,72,74,75,77,78,79,99,],[31,-61,57,70,-62,-62,-53,-62,-49,-51,-52,-58,-59,-60,-50,]),';':([15,20,24,36,37,38,39,40,42,43,44,45,46,58,60,61,62,64,65,67,72,74,75,76,77,78,79,89,90,91,92,97,98,99,100,113,114,115,119,122,124,125,126,131,134,136,138,139,140,],[33,-62,-61,-62,-62,-62,-62,-53,-38,-13,-14,-39,-62,95,33,-35,-36,-34,-46,-48,-49,-51,-52,-62,-58,-59,-60,-26,108,-22,-23,33,-47,-50,-62,-37,-62,-41,129,-25,-33,-40,33,135,-19,-21,-24,135,-20,]),'END':([15,20,24,32,34,36,37,38,39,40,42,43,44,45,46,60,61,62,64,65,67,72,74,75,76,77,78,79,89,91,92,96,97,98,99,100,110,112,113,114,115,122,124,125,126,131,132,134,136,138,139,140,],[-62,-62,-61,59,-32,-62,-62,-62,-62,-53,-38,-13,-14,-39,-62,-62,-35,-36,-34,-46,-48,-49,-51,-52,-62,-58,-59,-60,-26,-22,-23,-31,-62,-47,-50,-62,122,124,-37,-62,-41,-25,-33,-40,-62,-62,137,-19,-21,-24,-62,-20,]),'NUMERO':([17,18,19,22,23,31,35,66,68,69,70,71,73,81,109,],[40,40,40,40,40,40,40,40,-54,-55,-56,-57,40,40,121,]),'CONST_VALOR':([19,31,],[43,43,]),')':([23,24,39,40,46,48,49,50,75,77,78,79,80,81,82,89,91,92,101,118,122,131,134,136,138,139,140,],[-62,-61,-62,-53,-62,79,-62,-43,-52,-58,-59,-60,-42,-62,-45,-26,-22,-23,-44,128,-25,-62,-19,-21,-24,-62,-20,]),'OP_MAT':([24,38,39,40,46,75,77,78,79,],[-61,73,-62,-53,-62,-52,-58,-59,-60,]),'<':([24,37,38,39,40,46,72,74,75,77,78,79,99,],[-61,68,-62,-62,-53,-62,-49,-51,-52,-58,-59,-60,-50,]),'>':([24,37,38,39,40,46,72,74,75,77,78,79,99,],[-61,69,-62,-62,-53,-62,-49,-51,-52,-58,-59,-60,-50,]),'!':([24,37,38,39,40,46,72,74,75,77,78,79,99,],[-61,71,-62,-62,-53,-62,-49,-51,-52,-58,-59,-60,-50,]),'THEN':([24,37,38,39,40,41,46,65,67,72,74,75,77,78,79,98,99,],[-61,-62,-62,-62,-53,76,-62,-46,-48,-49,-51,-52,-58,-59,-60,-47,-50,]),']':([24,39,40,46,47,75,77,78,79,121,],[-61,-62,-53,-62,78,-52,-58,-59,-60,130,]),',':([24,39,40,46,49,56,75,77,78,79,107,],[-61,-62,-53,-62,81,87,-52,-58,-59,-60,87,]),':':([56,86,88,104,107,111,120,128,],[-62,106,-18,117,-62,123,-17,-29,]),'INTEGER':([57,106,117,123,133,],[91,91,91,91,91,]),'REAL':([57,106,117,123,133,],[92,92,92,92,92,]),'ARRAY':([57,106,117,123,133,],[93,93,93,93,93,]),'RECORD':([57,106,117,123,133,],[94,94,94,94,94,]),'ELSE':([64,76,100,124,],[-34,-62,114,-33,]),'OF':([130,],[133,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'declaracoes':([0,],[2,]),'def_const':([0,4,],[3,13,]),'constante':([0,4,],[4,4,]),'empty':([0,3,4,8,9,10,15,20,23,25,26,33,36,37,38,39,46,49,52,56,60,63,76,81,84,97,100,107,114,116,126,131,139,],[5,11,5,24,27,11,34,24,50,53,27,24,64,67,74,24,24,82,53,88,34,24,64,50,27,34,115,88,64,24,34,136,136,]),'principal':([2,],[7,]),'def_tipos':([3,10,],[9,29,]),'tipo':([3,10,],[10,10,]),'comando':([8,33,63,116,],[15,60,97,126,]),'nome':([8,20,33,39,46,63,116,],[16,45,16,75,77,16,16,]),'def_var':([9,26,84,],[25,55,103,]),'variavel':([9,26,84,],[26,26,26,]),'lista_com':([15,60,97,126,],[32,96,112,132,]),'exp_logica':([17,18,66,],[36,41,98,]),'exp_mat':([17,18,19,31,35,66,73,],[37,37,44,44,61,37,99,]),'parametro':([17,18,19,22,23,31,35,66,73,81,],[38,38,38,47,49,38,38,38,38,49,]),'const_valor':([19,31,],[42,58,]),'lista_param':([23,81,],[48,101,]),'def_func':([25,52,],[51,83,]),'funcao':([25,52,],[52,52,]),'bloco':([36,76,114,],[62,100,125,]),'exp_logica_aux':([37,],[65,]),'op_logico':([37,],[66,]),'exp_mat_aux':([38,],[72,]),'lista_param_aux':([49,],[80,]),'nome_funcao':([54,],[84,]),'lista_id':([56,107,],[86,120,]),'tipo_dado':([57,106,117,123,133,],[90,119,127,131,138,]),'bloco_funcao':([84,],[102,]),'param_func':([85,],[104,]),'campos':([94,105,135,],[110,118,139,]),'else':([100,],[113,]),'lista_campos':([131,139,],[134,140,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> declaracoes principal','programa',2,'p_programa','sintatico.py',5),
  ('principal -> BEGIN comando lista_com END','principal',4,'p_principal','sintatico.py',9),
  ('declaracoes -> def_const def_tipos def_var def_func','declaracoes',4,'p_declaracoes','sintatico.py',13),
  ('def_const -> constante def_const','def_const',2,'p_def_const','sintatico.py',17),
  ('def_const -> empty','def_const',1,'p_def_const','sintatico.py',18),
  ('def_tipos -> tipo def_tipos','def_tipos',2,'p_def_tipos','sintatico.py',22),
  ('def_tipos -> empty','def_tipos',1,'p_def_tipos','sintatico.py',23),
  ('def_var -> variavel def_var','def_var',2,'p_def_var','sintatico.py',27),
  ('def_var -> empty','def_var',1,'p_def_var','sintatico.py',28),
  ('def_func -> funcao def_func','def_func',2,'p_def_func','sintatico.py',32),
  ('def_func -> empty','def_func',1,'p_def_func','sintatico.py',33),
  ('constante -> CONST ID = const_valor ;','constante',5,'p_constante','sintatico.py',37),
  ('const_valor -> CONST_VALOR','const_valor',1,'p_const_valor','sintatico.py',41),
  ('const_valor -> exp_mat','const_valor',1,'p_const_valor','sintatico.py',42),
  ('tipo -> TYPE ID = tipo_dado ;','tipo',5,'p_tipo','sintatico.py',46),
  ('variavel -> VAR ID lista_id : tipo_dado ;','variavel',6,'p_variavel','sintatico.py',50),
  ('lista_id -> , ID lista_id','lista_id',3,'p_lista_id','sintatico.py',55),
  ('lista_id -> empty','lista_id',1,'p_lista_id','sintatico.py',56),
  ('campos -> ID : tipo_dado lista_campos','campos',4,'p_campos','sintatico.py',60),
  ('lista_campos -> ; campos lista_campos','lista_campos',3,'p_lista_campos','sintatico.py',64),
  ('lista_campos -> empty','lista_campos',1,'p_lista_campos','sintatico.py',65),
  ('tipo_dado -> INTEGER','tipo_dado',1,'p_tipo_dado','sintatico.py',69),
  ('tipo_dado -> REAL','tipo_dado',1,'p_tipo_dado','sintatico.py',70),
  ('tipo_dado -> ARRAY [ NUMERO ] OF tipo_dado','tipo_dado',6,'p_tipo_dado','sintatico.py',71),
  ('tipo_dado -> RECORD campos END','tipo_dado',3,'p_tipo_dado','sintatico.py',72),
  ('tipo_dado -> ID','tipo_dado',1,'p_tipo_dado','sintatico.py',73),
  ('funcao -> FUNCTION nome_funcao bloco_funcao','funcao',3,'p_funcao','sintatico.py',77),
  ('nome_funcao -> ID param_func : tipo_dado','nome_funcao',4,'p_nome_funcao','sintatico.py',81),
  ('param_func -> ( campos )','param_func',3,'p_param_func','sintatico.py',85),
  ('bloco_funcao -> def_var BEGIN comando lista_com END','bloco_funcao',5,'p_bloco_funcao','sintatico.py',89),
  ('lista_com -> ; comando lista_com','lista_com',3,'p_lista_com','sintatico.py',93),
  ('lista_com -> empty','lista_com',1,'p_lista_com','sintatico.py',94),
  ('bloco -> BEGIN comando lista_com END','bloco',4,'p_bloco','sintatico.py',98),
  ('bloco -> empty','bloco',1,'p_bloco','sintatico.py',99),
  ('comando -> nome ATRIBUICAO exp_mat','comando',3,'p_comando','sintatico.py',103),
  ('comando -> WHILE exp_logica bloco','comando',3,'p_comando','sintatico.py',104),
  ('comando -> IF exp_logica THEN bloco else','comando',5,'p_comando','sintatico.py',105),
  ('comando -> WRITE const_valor','comando',2,'p_comando','sintatico.py',106),
  ('comando -> READ nome','comando',2,'p_comando','sintatico.py',107),
  ('else -> ELSE bloco','else',2,'p_else','sintatico.py',111),
  ('else -> empty','else',1,'p_else','sintatico.py',112),
  ('lista_param -> parametro lista_param_aux','lista_param',2,'p_lista_param','sintatico.py',116),
  ('lista_param -> empty','lista_param',1,'p_lista_param','sintatico.py',117),
  ('lista_param_aux -> , lista_param','lista_param_aux',2,'p_lista_param_aux','sintatico.py',121),
  ('lista_param_aux -> empty','lista_param_aux',1,'p_lista_param_aux','sintatico.py',122),
  ('exp_logica -> exp_mat exp_logica_aux','exp_logica',2,'p_exp_logica','sintatico.py',125),
  ('exp_logica_aux -> op_logico exp_logica','exp_logica_aux',2,'p_exp_logica_aux','sintatico.py',129),
  ('exp_logica_aux -> empty','exp_logica_aux',1,'p_exp_logica_aux','sintatico.py',130),
  ('exp_mat -> parametro exp_mat_aux','exp_mat',2,'p_exp_mat','sintatico.py',133),
  ('exp_mat_aux -> OP_MAT exp_mat','exp_mat_aux',2,'p_exp_mat_aux','sintatico.py',137),
  ('exp_mat_aux -> empty','exp_mat_aux',1,'p_exp_mat_aux','sintatico.py',138),
  ('parametro -> ID nome','parametro',2,'p_parametro','sintatico.py',141),
  ('parametro -> NUMERO','parametro',1,'p_parametro','sintatico.py',142),
  ('op_logico -> <','op_logico',1,'p_op_logico','sintatico.py',146),
  ('op_logico -> >','op_logico',1,'p_op_logico','sintatico.py',147),
  ('op_logico -> =','op_logico',1,'p_op_logico','sintatico.py',148),
  ('op_logico -> !','op_logico',1,'p_op_logico','sintatico.py',149),
  ('nome -> . ID nome','nome',3,'p_nome','sintatico.py',153),
  ('nome -> [ parametro ]','nome',3,'p_nome','sintatico.py',154),
  ('nome -> ( lista_param )','nome',3,'p_nome','sintatico.py',155),
  ('nome -> empty','nome',1,'p_nome','sintatico.py',156),
  ('empty -> <empty>','empty',0,'p_empty','sintatico.py',160),
]
