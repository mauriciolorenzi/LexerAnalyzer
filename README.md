# LexerAnalyzer

This is the lexer analyzer for the language Anicca, which will be explained below, for the discipline called Compilers.

# Anicca

Em Páli, língua antiga indiana, Anicca (Links para um site externo) significa impermanência. Um nome adequado para uma linguagem de programação que talvez só existira no curto tempo percorrido neste curso.

Nossa tímida linguagem de programação será composta de funções, variáveis, condições, repetiçoes, operadores, e uma biblioteca de poucas funções nativas. O compilador de Anicca irá traduzir seus Programas Fonte para Programas em Python. Vamos tomar como inspiração LearnXinYminutes (Links para um site externo), e definir a linguagem através de um Programa Fonte exemplo.

-- Dois traços iniciam uma linha de comentário.

----------------------------------------------------
-- Funções.
----------------------------------------------------

-- Somente funções podem ser declaradas diretamente
-- em um programa. Os outros elementos devem ser
-- declarados dentro de alguma função.

-- Todo programa inicia da função `inicio`, ela é 
-- obrigatória. Os parâmetros (`(valor:Logica)`) e 
-- o retorno (`Numero`) são opcionais nas funções.
-- Os parâmetros são considerados variáveis como 
-- as declaradas dentro da função.
inicio:Funcao(valor:Logica,item:Texto):Numero::{ }

----------------------------------------------------
-- Variáveis e Tipos.
----------------------------------------------------

-- A atribuição é representada pelo símbolo `::`.
-- As variáveis devem receber um valor inicial. O
-- escopo das variáveis está associado a função
-- que ela foi definida. Não existe escopo de 
-- blocos internos a função como `se` e `enquanto`.

-- Funções são do tipo `Funcao`, a linguagem não
-- permite atribuir funções a variáveis. Isso 
-- simplifica a implementação.

tiposDeVariaveis:Funcao::{
  -- O carácter ' deve ser precedido por #, e
  -- # deve ser representada por ##.
  textoVar:Texto::'#'exemplo##'

  -- Só serão permitidos valores tipo inteiro,
  -- os valores reais devem ser arredondados; 
  -- acima ou igual a .5 para cima, e abaixo de
  -- .5 para baixo.
  numeroVar:Numero::1234

  -- Tipos Logico podem receber Sim e Nao.
  logicoVar:Logico::Sim
}

----------------------------------------------------
-- Fluxo de Controle. 
----------------------------------------------------

tiposDeFluxoDeControle:Funcao:Logico::{
  resultado:Logico::Nao

  se(1 = 2){
    -- O fluxo condicional é definido pela palavra 
    -- `se` e uma condição se que atendida 
    -- direciona o fluxo para esse trecho do 
    -- Programa.
    resultado::Nao
  } se nao se('a' != 'a'){
    -- Caso a condição de `se` não for atendida,
    -- o fluxo é direcionado para a próxima 
    -- condição `se nao se`.
    resultado::Nao
  } se nao {
    -- Caso nenhuma condição anterior seja atendida,
    -- o fluxo é direcionado para esse trecho do
    -- Programa. 
    resultado::Sim
  }

  contador:Numero::0
  -- O fluxo de repetição é representado pela 
  -- palavra `enquanto` e uma codição de parada.
  enquanto(contador < 10){
    contador::contador + 1
  }

  retorna resultado
}
Os operadores + (soma), - (subtração), / (divisão), * (multiplicação), :: (atribuição), = (igual), != (diferente), > (maior), < (menor), <= (menor igual), >=(maior igual), & (e), | (ou), e ! (negação); devem ser associados com os tipos: Logico, Texto, e Numero. Caso alguma associação operador-tipo não fizer sentido ela pode ser ignorada (não será permitida), exemplo operador / e o tipo Logico.

Os nomes das variáveis e das funções devem iniciar com letra minúscula e devem ser formados apenas por letras.  Os nomes que iniciam com letra maiúscula são exclusivos dos tipos: Logico, Texto, Numero, e Funcao. As palavras reservadas como `retorna` devem ser escritas em minúsculo.
