
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ARRAY ATRIBUICAO BEGIN CONST CONST_VALOR ELSE END FUNCTION ID IF INTEGER NUMERO OF OP_MAT READ REAL RECORD THEN TYPE VAR WHILE WRITEprograma : declaracoes principalprincipal : BEGIN comando lista_com ENDdeclaracoes : def_const def_tipos def_var def_funcdef_const : constante def_const\n                 | emptydef_tipos : tipo def_tipos\n                 | emptydef_var : variavel def_var\n               | emptydef_func : funcao def_func\n                | emptyconstante : CONST ID '=' const_valor ';' const_valor : CONST_VALOR\n                   | exp_mattipo : TYPE ID '=' tipo_dado ';' variavel : VAR ID lista_id ':' tipo_dado ';'lista_id : ',' ID lista_id\n                | emptycampos : ID ':' tipo_dado lista_camposlista_campos : ';' campos\n                    | empty tipo_dado : INTEGER\n                 | REAL\n                 | ARRAY '[' NUMERO ']' OF tipo_dado\n                 | RECORD campos END\n                 | IDfuncao : FUNCTION new_scope nome_funcao bloco_funcaonome_funcao : ID param_func ':' tipo_dadoparam_func : '(' campos ')' \n                  | empty bloco_funcao : def_var BEGIN comando lista_com ENDlista_com : ';' comando lista_com\n                 | emptybloco : BEGIN comando lista_com END\n             | comandocomando : ID nome ATRIBUICAO exp_mat\n               | WHILE exp_logica bloco\n               | IF exp_logica THEN bloco else\n               | WRITE const_valor\n               | READ ID nomeelse : ELSE bloco\n            | emptylista_param : parametro lista_param_aux\n                   | emptylista_param_aux : ',' lista_param\n                       | emptyexp_logica : exp_mat exp_logica_auxexp_logica_aux : op_logico exp_logica\n                      | emptyexp_mat : parametro exp_mat_auxexp_mat_aux : OP_MAT exp_mat\n                   | emptyparametro : ID nome\n                 | NUMEROop_logico : '<'\n                 | '>'\n                 | '='\n                 | '!' nome : '.' ID nome\n            | '[' parametro ']'\n            | '(' lista_param ')'\n            | emptynew_scope :empty :"
    
_lr_action_items = {'CONST':([0,4,89,],[6,6,-12,]),'TYPE':([0,3,4,5,10,13,89,106,],[-64,12,-64,-5,12,-4,-12,-15,]),'VAR':([0,3,4,5,9,10,11,13,22,25,83,85,86,89,102,106,123,130,134,141,],[-64,-64,-64,-5,24,-64,-7,-4,24,-6,-26,-22,-23,-12,24,-15,-25,-16,-28,-24,]),'FUNCTION':([0,3,4,5,9,10,11,13,21,22,23,25,47,50,89,106,115,130,143,],[-64,-64,-64,-5,-64,-64,-7,-4,49,-64,-9,-6,49,-8,-12,-15,-27,-16,-31,]),'BEGIN':([0,2,3,4,5,9,10,11,13,21,22,23,25,35,36,37,38,39,40,46,47,48,50,57,65,67,72,74,75,76,78,83,85,86,89,92,93,94,99,100,102,106,113,115,116,123,130,134,141,143,],[-64,8,-64,-64,-5,-64,-64,-7,-4,-64,-64,-9,-6,-62,63,-64,-64,-64,-54,-3,-64,-11,-8,-64,-47,-49,-50,-52,-53,63,-10,-26,-22,-23,-12,-59,-60,-61,-48,-51,-64,-15,63,-27,127,-25,-16,-28,-24,-31,]),'$end':([1,7,54,],[0,-1,-2,]),'ID':([6,8,12,17,18,19,20,24,27,29,32,33,34,35,36,37,38,39,40,49,52,56,57,63,65,66,67,68,69,70,71,72,73,74,75,76,79,81,88,92,93,94,96,99,100,104,113,118,124,127,128,136,138,],[14,16,26,39,39,39,45,51,39,16,57,39,39,-62,16,-64,-64,-64,-54,-63,83,39,-64,16,-47,39,-49,-55,-56,-57,-58,-50,39,-52,-53,16,103,105,109,-59,-60,-61,39,-48,-51,83,16,109,83,16,83,83,109,]),'WHILE':([8,29,35,36,37,38,39,40,57,63,65,67,72,74,75,76,92,93,94,99,100,113,127,],[17,17,-62,17,-64,-64,-64,-54,-64,17,-47,-49,-50,-52,-53,17,-59,-60,-61,-48,-51,17,17,]),'IF':([8,29,35,36,37,38,39,40,57,63,65,67,72,74,75,76,92,93,94,99,100,113,127,],[18,18,-62,18,-64,-64,-64,-54,-64,18,-47,-49,-50,-52,-53,18,-59,-60,-61,-48,-51,18,18,]),'WRITE':([8,29,35,36,37,38,39,40,57,63,65,67,72,74,75,76,92,93,94,99,100,113,127,],[19,19,-62,19,-64,-64,-64,-54,-64,19,-47,-49,-50,-52,-53,19,-59,-60,-61,-48,-51,19,19,]),'READ':([8,29,35,36,37,38,39,40,57,63,65,67,72,74,75,76,92,93,94,99,100,113,127,],[20,20,-62,20,-64,-64,-64,-54,-64,20,-47,-49,-50,-52,-53,20,-59,-60,-61,-48,-51,20,20,]),'=':([14,26,35,37,38,39,40,57,72,74,75,92,93,94,100,],[27,52,-62,70,-64,-64,-54,-64,-50,-52,-53,-59,-60,-61,-51,]),';':([15,35,38,39,40,42,43,44,45,53,55,57,62,64,72,74,75,77,83,84,85,86,91,92,93,94,98,100,101,112,114,120,123,125,126,132,133,141,],[29,-62,-64,-64,-54,-39,-13,-14,-64,89,29,-64,-37,-35,-50,-52,-53,-40,-26,106,-22,-23,-36,-59,-60,-61,29,-51,-64,-38,-42,130,-25,-34,-41,138,29,-24,]),'END':([15,28,30,35,38,39,40,42,43,44,45,55,57,62,64,72,74,75,77,83,85,86,90,91,92,93,94,98,100,101,108,111,112,114,123,125,126,132,133,137,139,140,141,142,],[-64,54,-33,-62,-64,-64,-54,-39,-13,-14,-64,-64,-64,-37,-35,-50,-52,-53,-40,-26,-22,-23,-32,-36,-59,-60,-61,-64,-51,-64,123,125,-38,-42,-25,-34,-41,-64,-64,-19,-21,143,-24,-20,]),'.':([16,39,45,57,],[32,32,32,32,]),'[':([16,39,45,57,87,],[33,33,33,33,107,]),'(':([16,39,45,57,103,],[34,34,34,34,118,]),'ATRIBUICAO':([16,31,35,57,92,93,94,],[-64,56,-62,-64,-59,-60,-61,]),'NUMERO':([17,18,19,27,33,34,56,66,68,69,70,71,73,96,107,],[40,40,40,40,40,40,40,40,-55,-56,-57,-58,40,40,122,]),'CONST_VALOR':([19,27,],[43,43,]),')':([34,35,39,40,57,59,60,61,75,83,85,86,92,93,94,95,96,97,110,123,129,132,137,139,141,142,],[-64,-62,-64,-54,-64,94,-64,-44,-53,-26,-22,-23,-59,-60,-61,-43,-64,-46,-45,-25,135,-64,-19,-21,-24,-20,]),'OP_MAT':([35,38,39,40,57,75,92,93,94,],[-62,73,-64,-54,-64,-53,-59,-60,-61,]),'<':([35,37,38,39,40,57,72,74,75,92,93,94,100,],[-62,68,-64,-64,-54,-64,-50,-52,-53,-59,-60,-61,-51,]),'>':([35,37,38,39,40,57,72,74,75,92,93,94,100,],[-62,69,-64,-64,-54,-64,-50,-52,-53,-59,-60,-61,-51,]),'!':([35,37,38,39,40,57,72,74,75,92,93,94,100,],[-62,71,-64,-64,-54,-64,-50,-52,-53,-59,-60,-61,-51,]),'THEN':([35,37,38,39,40,41,57,65,67,72,74,75,92,93,94,99,100,],[-62,-64,-64,-64,-54,76,-64,-47,-49,-50,-52,-53,-59,-60,-61,-48,-51,]),'ELSE':([35,38,39,40,42,43,44,45,57,62,64,72,74,75,77,91,92,93,94,100,101,112,114,125,126,],[-62,-64,-64,-54,-39,-13,-14,-64,-64,-37,-35,-50,-52,-53,-40,-36,-59,-60,-61,-51,113,-38,-42,-34,-41,]),']':([35,39,40,57,58,75,92,93,94,122,],[-62,-64,-54,-64,93,-53,-59,-60,-61,131,]),',':([35,39,40,51,57,60,75,92,93,94,105,],[-62,-64,-54,81,-64,96,-53,-59,-60,-61,81,]),':':([51,80,82,103,105,109,117,119,121,135,],[-64,104,-18,-64,-64,124,128,-30,-17,-29,]),'INTEGER':([52,104,124,128,136,],[85,85,85,85,85,]),'REAL':([52,104,124,128,136,],[86,86,86,86,86,]),'ARRAY':([52,104,124,128,136,],[87,87,87,87,87,]),'RECORD':([52,104,124,128,136,],[88,88,88,88,88,]),'OF':([131,],[136,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'declaracoes':([0,],[2,]),'def_const':([0,4,],[3,13,]),'constante':([0,4,],[4,4,]),'empty':([0,3,4,9,10,15,16,21,22,34,37,38,39,45,47,51,55,57,60,96,98,101,102,103,105,132,133,],[5,11,5,23,11,30,35,48,23,61,67,74,35,35,48,82,30,35,97,61,30,114,23,119,82,139,30,]),'principal':([2,],[7,]),'def_tipos':([3,10,],[9,25,]),'tipo':([3,10,],[10,10,]),'comando':([8,29,36,63,76,113,127,],[15,55,64,98,64,64,133,]),'def_var':([9,22,102,],[21,50,116,]),'variavel':([9,22,102,],[22,22,22,]),'lista_com':([15,55,98,133,],[28,90,111,140,]),'nome':([16,39,45,57,],[31,75,77,92,]),'exp_logica':([17,18,66,],[36,41,99,]),'exp_mat':([17,18,19,27,56,66,73,],[37,37,44,44,91,37,100,]),'parametro':([17,18,19,27,33,34,56,66,73,96,],[38,38,38,38,58,60,38,38,38,60,]),'const_valor':([19,27,],[42,53,]),'def_func':([21,47,],[46,78,]),'funcao':([21,47,],[47,47,]),'lista_param':([34,96,],[59,110,]),'bloco':([36,76,113,],[62,101,126,]),'exp_logica_aux':([37,],[65,]),'op_logico':([37,],[66,]),'exp_mat_aux':([38,],[72,]),'new_scope':([49,],[79,]),'lista_id':([51,105,],[80,121,]),'tipo_dado':([52,104,124,128,136,],[84,120,132,134,141,]),'lista_param_aux':([60,],[95,]),'nome_funcao':([79,],[102,]),'campos':([88,118,138,],[108,129,142,]),'else':([101,],[112,]),'bloco_funcao':([102,],[115,]),'param_func':([103,],[117,]),'lista_campos':([132,],[137,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> declaracoes principal','programa',2,'p_programa','sintatico.py',39),
  ('principal -> BEGIN comando lista_com END','principal',4,'p_principal','sintatico.py',44),
  ('declaracoes -> def_const def_tipos def_var def_func','declaracoes',4,'p_declaracoes','sintatico.py',48),
  ('def_const -> constante def_const','def_const',2,'p_def_const','sintatico.py',52),
  ('def_const -> empty','def_const',1,'p_def_const','sintatico.py',53),
  ('def_tipos -> tipo def_tipos','def_tipos',2,'p_def_tipos','sintatico.py',57),
  ('def_tipos -> empty','def_tipos',1,'p_def_tipos','sintatico.py',58),
  ('def_var -> variavel def_var','def_var',2,'p_def_var','sintatico.py',62),
  ('def_var -> empty','def_var',1,'p_def_var','sintatico.py',63),
  ('def_func -> funcao def_func','def_func',2,'p_def_func','sintatico.py',70),
  ('def_func -> empty','def_func',1,'p_def_func','sintatico.py',71),
  ('constante -> CONST ID = const_valor ;','constante',5,'p_constante','sintatico.py',79),
  ('const_valor -> CONST_VALOR','const_valor',1,'p_const_valor','sintatico.py',82),
  ('const_valor -> exp_mat','const_valor',1,'p_const_valor','sintatico.py',83),
  ('tipo -> TYPE ID = tipo_dado ;','tipo',5,'p_tipo','sintatico.py',86),
  ('variavel -> VAR ID lista_id : tipo_dado ;','variavel',6,'p_variavel','sintatico.py',96),
  ('lista_id -> , ID lista_id','lista_id',3,'p_lista_id','sintatico.py',120),
  ('lista_id -> empty','lista_id',1,'p_lista_id','sintatico.py',121),
  ('campos -> ID : tipo_dado lista_campos','campos',4,'p_campos','sintatico.py',132),
  ('lista_campos -> ; campos','lista_campos',2,'p_lista_campos','sintatico.py',140),
  ('lista_campos -> empty','lista_campos',1,'p_lista_campos','sintatico.py',141),
  ('tipo_dado -> INTEGER','tipo_dado',1,'p_tipo_dado','sintatico.py',149),
  ('tipo_dado -> REAL','tipo_dado',1,'p_tipo_dado','sintatico.py',150),
  ('tipo_dado -> ARRAY [ NUMERO ] OF tipo_dado','tipo_dado',6,'p_tipo_dado','sintatico.py',151),
  ('tipo_dado -> RECORD campos END','tipo_dado',3,'p_tipo_dado','sintatico.py',152),
  ('tipo_dado -> ID','tipo_dado',1,'p_tipo_dado','sintatico.py',153),
  ('funcao -> FUNCTION new_scope nome_funcao bloco_funcao','funcao',4,'p_funcao','sintatico.py',163),
  ('nome_funcao -> ID param_func : tipo_dado','nome_funcao',4,'p_nome_funcao','sintatico.py',181),
  ('param_func -> ( campos )','param_func',3,'p_param_func','sintatico.py',191),
  ('param_func -> empty','param_func',1,'p_param_func','sintatico.py',192),
  ('bloco_funcao -> def_var BEGIN comando lista_com END','bloco_funcao',5,'p_bloco_funcao','sintatico.py',214),
  ('lista_com -> ; comando lista_com','lista_com',3,'p_lista_com','sintatico.py',225),
  ('lista_com -> empty','lista_com',1,'p_lista_com','sintatico.py',226),
  ('bloco -> BEGIN comando lista_com END','bloco',4,'p_bloco','sintatico.py',237),
  ('bloco -> comando','bloco',1,'p_bloco','sintatico.py',238),
  ('comando -> ID nome ATRIBUICAO exp_mat','comando',4,'p_comando','sintatico.py',251),
  ('comando -> WHILE exp_logica bloco','comando',3,'p_comando','sintatico.py',252),
  ('comando -> IF exp_logica THEN bloco else','comando',5,'p_comando','sintatico.py',253),
  ('comando -> WRITE const_valor','comando',2,'p_comando','sintatico.py',254),
  ('comando -> READ ID nome','comando',3,'p_comando','sintatico.py',255),
  ('else -> ELSE bloco','else',2,'p_else','sintatico.py',321),
  ('else -> empty','else',1,'p_else','sintatico.py',322),
  ('lista_param -> parametro lista_param_aux','lista_param',2,'p_lista_param','sintatico.py',330),
  ('lista_param -> empty','lista_param',1,'p_lista_param','sintatico.py',331),
  ('lista_param_aux -> , lista_param','lista_param_aux',2,'p_lista_param_aux','sintatico.py',346),
  ('lista_param_aux -> empty','lista_param_aux',1,'p_lista_param_aux','sintatico.py',347),
  ('exp_logica -> exp_mat exp_logica_aux','exp_logica',2,'p_exp_logica','sintatico.py',355),
  ('exp_logica_aux -> op_logico exp_logica','exp_logica_aux',2,'p_exp_logica_aux','sintatico.py',366),
  ('exp_logica_aux -> empty','exp_logica_aux',1,'p_exp_logica_aux','sintatico.py',367),
  ('exp_mat -> parametro exp_mat_aux','exp_mat',2,'p_exp_mat','sintatico.py',393),
  ('exp_mat_aux -> OP_MAT exp_mat','exp_mat_aux',2,'p_exp_mat_aux','sintatico.py',433),
  ('exp_mat_aux -> empty','exp_mat_aux',1,'p_exp_mat_aux','sintatico.py',434),
  ('parametro -> ID nome','parametro',2,'p_parametro','sintatico.py',454),
  ('parametro -> NUMERO','parametro',1,'p_parametro','sintatico.py',455),
  ('op_logico -> <','op_logico',1,'p_op_logico','sintatico.py',523),
  ('op_logico -> >','op_logico',1,'p_op_logico','sintatico.py',524),
  ('op_logico -> =','op_logico',1,'p_op_logico','sintatico.py',525),
  ('op_logico -> !','op_logico',1,'p_op_logico','sintatico.py',526),
  ('nome -> . ID nome','nome',3,'p_nome','sintatico.py',531),
  ('nome -> [ parametro ]','nome',3,'p_nome','sintatico.py',532),
  ('nome -> ( lista_param )','nome',3,'p_nome','sintatico.py',533),
  ('nome -> empty','nome',1,'p_nome','sintatico.py',534),
  ('new_scope -> <empty>','new_scope',0,'p_new_scope','sintatico.py',551),
  ('empty -> <empty>','empty',0,'p_empty','sintatico.py',555),
]
