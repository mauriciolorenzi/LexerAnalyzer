import json 

def analisadorLexico(programa):
    operadores = ['+', '-', '*', '/']
    reservado = ['Funcao', 'Logica', 'Texto', 'Numero', 'Logico', 'se', 'se nao se', 'se nao', 'enquanto', 'retorna']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    lexer = {

      '-': {
        '-': 'comentario',
        ' ': 'operador-menos'
      },
      '\\': {
        'n': 'quebra-linha'        
      },
      ':': 'dois-pontos',
      ''

    }

    regras = {
        '-' : 'operador-menos',
        '--' : 'comentario',
        '\n': 'quebra-linha',
        #'inicio' : 'identificador',
        ':' : 'dois-pontos',
        'Funcao' : 'reservado',
        '(' : 'abre-parenteses',
        ')' : 'fecha-parenteses',
        #'valor' : 'identificador',
        'Logica' : 'reservado',
        ',' : 'virgula',
        #'item' : 'identificador',
        'Texto' : 'reservado',
        'Numero' : 'reservado',
        '::' : 'atribuicao',
        '{' : 'abre-chaves',
        '}' : 'fecha-chaves',
        #'tiposDeVariaveis' : 'identificador',
        #'textoVar' : 'identificador',
        '\'#\'exemplo##\'' : 'texto',
        #'numeroVar' : 'identificador',
        '1234' : 'numero',
        #'logicoVar' : 'identificador',
        'Logico' : 'reservado',
        'Sim' : 'logico',
        #'tiposDeFluxoDeControle' : 'identificador',
        #'resultado' : 'identificador',
        'Nao' : 'logico',
        'se' : 'reservado',
        '1' : 'numero',
        '=' : 'operador-igual',
        '2' : 'numero',
        'se nao se' : 'reservado',
        '\'a\'' : 'texto',
        '!=' : 'operador-diferente',
        'se nao' : 'reservado',
        '@' : 'desconhecido',
        #'contador' : 'identificador',
        '0' : 'numero',
        'enquanto' : 'reservado',
        #'contador' : 'identificador',
        '<' : 'operador-menor',
        '>' : 'operador-maior',
        '10' : 'numero',
        '+' : 'operador-mais',
        'retorna' : 'reservado'
    }

    tokens = []
    erros = []
  # for c in programa:
  #  print c
  return {"tokens":tokens,"erros":erros}

# ALERTA: Nao modificar o codigo fonte apos esse aviso

def testaAnalisadorLexico(programa, teste):
  # Caso o resultado nao seja igual ao teste
  # ambos sao mostrados e a execucao termina  
  resultado = json.dumps(analisadorLexico(programa), indent=2)
  teste = json.dumps(teste, indent=2)
  if resultado != teste:
    # Mostra o teste e o resultado lado a lado  
    resultadoLinhas = resultado.split('\n')
    testeLinhas = teste.split('\n')
    if len(resultadoLinhas) > len(testeLinhas):
      testeLinhas.extend(
        [' '] * (len(resultadoLinhas)-len(testeLinhas))
      )
    elif len(resultadoLinhas) < len(testeLinhas):
      resultadoLinhas.extend(
        [' '] * (len(testeLinhas)-len(resultadoLinhas))
      )
    linhasEmPares = enumerate(zip(testeLinhas, resultadoLinhas))
    maiorTextoNaLista = str(len(max(testeLinhas, key=len)))
    maiorIndice = str(len(str(len(testeLinhas))))
    titule = '{:<'+maiorIndice+'} + {:<'+maiorTextoNaLista+'} + {}'
    objeto = '{:<'+maiorIndice+'} | {:<'+maiorTextoNaLista+'} | {}'
    print(titule.format('', 'teste', 'resultado'))
    print(objeto.format('', '', ''))
    for indice, (esquerda, direita) in linhasEmPares:
      print(objeto.format(indice, esquerda, direita))
    # Termina a execucao
    print("\n): falha :(")
    quit()

# Programa que passdo para a funcao analisadorLexico
programa = """-- funcao inicial

inicio:Funcao(valor:Logica,item:Texto):Numero::{
}

tiposDeVariaveis:Funcao::{
  textoVar:Texto::'#'exemplo##'
  numeroVar:Numero::1234
  logicoVar:Logico::Sim
}

tiposDeFluxoDeControle:Funcao:Logico::{
  resultado:Logico::Nao

  se(1 = 2){
    resultado::Nao
  } se nao se('a' != 'a'){
    resultado::Nao
  } se nao @ {
    resultado::Sim
  }

  contador:Numero::0
  enquanto(contador < 10){
    contador::contador + 'a'
  }

  retorna resultado
}"""

# Resultado esperado da execucao da funcao analisadorLexico
# passando paea ela o programa anterior
teste = {
  "tokens":[
    # Comentario    
    {
      "grupo":"comentario", "texto": "-- funcao inicial", 
      "local":{"linha":1,"indice":0}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":1,"indice":17}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":2,"indice":0}
    },
    # Funcao inicio
    {
      "grupo":"identificador", "texto": "inicio", 
      "local":{"linha":3,"indice":0}
    },
    {
      "grupo":"dois-pontos", "texto": ":", 
      "local":{"linha":3,"indice":6}
    },
    {
      "grupo":"reservado", "texto": "Funcao", 
      "local":{"linha":3,"indice":7}
    },
    {
      "grupo":"abre-parenteses", "texto": "(", 
      "local":{"linha":3,"indice":13}
    },
    {
      "grupo":"identificador", "texto": "valor", 
      "local":{"linha":3,"indice":14}
    },
    {
      "grupo":"dois-pontos", "texto": ":", 
      "local":{"linha":3,"indice":19}
    },
    {
      "grupo":"reservado", "texto": "Logica", 
      "local":{"linha":3,"indice":20}
    },
    {
      "grupo":"virgula", "texto": ",", 
      "local":{"linha":3,"indice":26}
    },
    {
      "grupo":"identificador", "texto": "item", 
      "local":{"linha":3,"indice":27}
    },
    {
      "grupo":"dois-pontos", "texto": ":", 
      "local":{"linha":3,"indice":31}
    },
    {
      "grupo":"reservado", "texto": "Texto", 
      "local":{"linha":3,"indice":32}
    },
    {
      "grupo":"fecha-parenteses", "texto": ")", 
      "local":{"linha":3,"indice":37}
    },
    {
      "grupo":"dois-pontos", "texto": ":", 
      "local":{"linha":3,"indice":38}
    },
    {
      "grupo":"reservado", "texto": "Numero", 
      "local":{"linha":3,"indice":39}
    },
    {
      "grupo":"atribuicao", "texto": "::", 
      "local":{"linha":3,"indice":45}
    },
    {
      "grupo":"abre-chaves", "texto": "{", 
      "local":{"linha":3,"indice":47}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":3,"indice":48}
    },
    {
      "grupo":"fecha-chaves", "texto": "}", 
      "local":{"linha":4,"indice":0}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":4,"indice":1}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":5,"indice":0}
    },
    # Funcao tiposDeVariaveis
    {
      "grupo":"identificador", "texto": "tiposDeVariaveis", 
      "local":{"linha":6,"indice":0}
    },
    {
      "grupo":"dois-pontos", "texto": ":", 
      "local":{"linha":6,"indice":16}
    },
    {
      "grupo":"reservado", "texto": "Funcao", 
      "local":{"linha":6,"indice":17}
    },
    {
      "grupo":"atribuicao", "texto": "::", 
      "local":{"linha":6,"indice":23}
    },
    {
      "grupo":"abre-chaves", "texto": "{", 
      "local":{"linha":6,"indice":25}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":6,"indice":26}
    },
    # textoVar:Texto::'#'exemplo##'
    {
      "grupo":"identificador", "texto": "textoVar", 
      "local":{"linha":7,"indice":2}
    },
    {
      "grupo":"dois-pontos", "texto": ":", 
      "local":{"linha":7,"indice":10}
    },
    {
      "grupo":"reservado", "texto": "Texto", 
      "local":{"linha":7,"indice":11}
    },
    {
      "grupo":"atribuicao", "texto": "::", 
      "local":{"linha":7,"indice":16}
    },
    {
      "grupo":"texto", "texto": "'#'exemplo##'", 
      "local":{"linha":7,"indice":18}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":7,"indice":31}
    },
    # numeroVar:Numero::1234
    {
      "grupo":"identificador", "texto": "numeroVar", 
      "local":{"linha":8,"indice":2}
    },
    {
      "grupo":"dois-pontos", "texto": ":", 
      "local":{"linha":8,"indice":11}
    },
    {
      "grupo":"reservado", "texto": "Numero", 
      "local":{"linha":8,"indice":12}
    },
    {
      "grupo":"atribuicao", "texto": "::", 
      "local":{"linha":8,"indice":18}
    },
    {
      "grupo":"numero", "texto": "1234", 
      "local":{"linha":8,"indice":20}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":8,"indice":24}
    },
    # logicoVar:Logico::Sim
    {
      "grupo":"identificador", "texto": "logicoVar", 
      "local":{"linha":9,"indice":2}
    },
    {
      "grupo":"dois-pontos", "texto": ":", 
      "local":{"linha":9,"indice":11}
    },
    {
      "grupo":"reservado", "texto": "Logico", 
      "local":{"linha":9,"indice":12}
    },
    {
      "grupo":"atribuicao", "texto": "::", 
      "local":{"linha":9,"indice":18}
    },
    {
      "grupo":"logico", "texto": "Sim", 
      "local":{"linha":9,"indice":20}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":9,"indice":23}
    },
    # Fecha Funcao
    {
      "grupo":"fecha-chaves", "texto": "}", 
      "local":{"linha":10,"indice":0}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":10,"indice":1}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":11,"indice":0}
    },
    # Funcao tiposDeFluxoDeControle
    {
      "grupo":"identificador", "texto": "tiposDeFluxoDeControle", 
      "local":{"linha":12,"indice":0}
    },
    {
      "grupo":"dois-pontos", "texto": ":", 
      "local":{"linha":12,"indice":22}
    },
    {
      "grupo":"reservado", "texto": "Funcao", 
      "local":{"linha":12,"indice":23}
    },
    {
      "grupo":"dois-pontos", "texto": ":", 
      "local":{"linha":12,"indice":29}
    },
    {
      "grupo":"reservado", "texto": "Logico", 
      "local":{"linha":12,"indice":30}
    },
    {
      "grupo":"atribuicao", "texto": "::", 
      "local":{"linha":12,"indice":36}
    },
    {
      "grupo":"abre-chaves", "texto": "{", 
      "local":{"linha":12,"indice":38}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":12,"indice":39}
    },
    # resultado:Logico::Nao
    {
      "grupo":"identificador", "texto": "resultado", 
      "local":{"linha":13,"indice":2}
    },
    {
      "grupo":"dois-pontos", "texto": ":", 
      "local":{"linha":13,"indice":11}
    },
    {
      "grupo":"reservado", "texto": "Logico", 
      "local":{"linha":13,"indice":12}
    },
    {
      "grupo":"atribuicao", "texto": "::", 
      "local":{"linha":13,"indice":18}
    },
    {
      "grupo":"logico", "texto": "Nao", 
      "local":{"linha":13,"indice":20}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":13,"indice":23}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":14,"indice":0}
    },
    # se(1 = 2){
    {
      "grupo":"reservado", "texto": "se", 
      "local":{"linha":15,"indice":2}
    },
    {
      "grupo":"abre-parenteses", "texto": "(", 
      "local":{"linha":15,"indice":4}
    },
    {
      "grupo":"numero", "texto": "1", 
      "local":{"linha":15,"indice":5}
    },
    {
      "grupo":"operador-igual", "texto": "=", 
      "local":{"linha":15,"indice":7}
    },
    {
      "grupo":"numero", "texto": "2", 
      "local":{"linha":15,"indice":9}
    },
    {
      "grupo":"fecha-parenteses", "texto": ")", 
      "local":{"linha":15,"indice":10}
    },
    {
      "grupo":"abre-chaves", "texto": "{",
      "local":{"linha":15,"indice":11}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":15,"indice":12}
    },
    {
      "grupo":"identificador", "texto": "resultado", 
      "local":{"linha":16,"indice":4}
    },
    {
      "grupo":"atribuicao", "texto": "::", 
      "local":{"linha":16,"indice":13}
    },
    {
      "grupo":"logico", "texto": "Nao", 
      "local":{"linha":16,"indice":15}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":16,"indice":18}
    },
    # } se nao se('a' != 'a'){
    {
      "grupo":"fecha-chaves", "texto": "}",
      "local":{"linha":17,"indice":2}
    },
    {
      "grupo":"reservado", "texto": "se nao se", 
      "local":{"linha":17,"indice":4}
    },
    {
      "grupo":"abre-parenteses", "texto": "(", 
      "local":{"linha":17,"indice":13}
    },
    {
      "grupo":"texto", "texto": "'a'", 
      "local":{"linha":17,"indice":15}
    },
    {
      "grupo":"operador-diferente", "texto": "!=", 
      "local":{"linha":17,"indice":18}
    },
    {
      "grupo":"texto", "texto": "'a'", 
      "local":{"linha":17,"indice":21}
    },
    {
      "grupo":"fecha-parenteses", "texto": ")", 
      "local":{"linha":17,"indice":24}
    },
    {
      "grupo":"abre-chaves", "texto": "{",
      "local":{"linha":17,"indice":25}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":17,"indice":26}
    },
    {
      "grupo":"identificador", "texto": "resultado", 
      "local":{"linha":18,"indice":4}
    },
    {
      "grupo":"atribuicao", "texto": "::", 
      "local":{"linha":18,"indice":13}
    },
    {
      "grupo":"logico", "texto": "Nao", 
      "local":{"linha":18,"indice":15}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":18,"indice":18}
    },
    # } se nao @ {
    {
      "grupo":"fecha-chaves", "texto": "}",
      "local":{"linha":19,"indice":2}
    },
    {
      "grupo":"reservado", "texto": "se nao", 
      "local":{"linha":19,"indice":4}
    },
    {
      "grupo":"desconhecido", "texto": "@", 
      "local":{"linha":19,"indice":11}
    },
    {
      "grupo":"abre-chaves", "texto": "{",
      "local":{"linha":19,"indice":13}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":19,"indice":14}
    },
    {
      "grupo":"identificador", "texto": "resultado", 
      "local":{"linha":20,"indice":4}
    },
    {
      "grupo":"atribuicao", "texto": "::", 
      "local":{"linha":20,"indice":13}
    },
    {
      "grupo":"logico", "texto": "Sim", 
      "local":{"linha":20,"indice":15}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":20,"indice":18}
    },
    {
      "grupo":"fecha-chaves", "texto": "}", 
      "local":{"linha":21,"indice":2}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":21,"indice":3}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":22,"indice":0}
    },
    # contador:Numero::0
    {
      "grupo":"identificador", "texto": "contador", 
      "local":{"linha":23,"indice":2}
    },
    {
      "grupo":"dois-pontos", "texto": ":", 
      "local":{"linha":23,"indice":10}
    },
    {
      "grupo":"reservado", "texto": "Numero", 
      "local":{"linha":23,"indice":11}
    },
    {
      "grupo":"atribuicao", "texto": "::", 
      "local":{"linha":23,"indice":17}
    },
    {
      "grupo":"numero", "texto": "0", 
      "local":{"linha":23,"indice":19}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":23,"indice":20}
    },
    # enquanto(contador < 10){
    {
      "grupo":"reservado", "texto": "enquanto", 
      "local":{"linha":24,"indice":2}
    },
    {
      "grupo":"abre-parenteses", "texto": "(", 
      "local":{"linha":24,"indice":10}
    },
    {
      "grupo":"identificador", "texto": "contador", 
      "local":{"linha":24,"indice":11}
    },
    {
      "grupo":"operador-menor", "texto": "<", 
      "local":{"linha":24,"indice":20}
    },
    {
      "grupo":"numero", "texto": "10", 
      "local":{"linha":24,"indice":22}
    },
    {
      "grupo":"fecha-parenteses", "texto": ")", 
      "local":{"linha":24,"indice":24}
    },
    {
      "grupo":"abre-chaves", "texto": "{",
      "local":{"linha":24,"indice":25}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":24,"indice":26}
    },
    {
      "grupo":"identificador", "texto": "contador", 
      "local":{"linha":25,"indice":4}
    },
    {
      "grupo":"atribuicao", "texto": "::", 
      "local":{"linha":25,"indice":12}
    },
    {
      "grupo":"identificador", "texto": "contador", 
      "local":{"linha":25,"indice":14}
    },
    {
      "grupo":"operador-mais", "texto": "+", 
      "local":{"linha":25,"indice":23}
    },
    {
      "grupo":"texto", "texto": "'a'", 
      "local":{"linha":25,"indice":25}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":25,"indice":28}
    },
    {
      "grupo":"fecha-chaves", "texto": "}", 
      "local":{"linha":26,"indice":2}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":26,"indice":3}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":27,"indice":0}
    },
    # Fecha Funcao
    {
      "grupo":"reservado", "texto": "retorna", 
      "local":{"linha":28,"indice":2}
    },    
    {
      "grupo":"identificador", "texto": "resultado", 
      "local":{"linha":28,"indice":10}
    },
    {
      "grupo":"quebra-linha", "texto": "\n", 
      "local":{"linha":28,"indice":19}
    },
    {
      "grupo":"fecha-chaves", "texto": "}", 
      "local":{"linha":29,"indice":0}
    }
  ], "erros":[
    {
      "texto":"simbolo, @, desconhecido",
      "local":{"linha":19,"indice":11}
    }
  ]
}

# Execucao do teste que valida a funcao analisadorLexico
testaAnalisadorLexico(programa, teste)

print("(: sucesso :)")