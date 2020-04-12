importar  numpy  como  np

classe  MultilayerPerceptron ():
    
    # Objeto inicial configurando os pesos dos neurônios
    def  __init__ ( auto , entrada , oculto , saída ):
        se  len ( oculto ) ==  0 :
             raise  TypeError ( 'Neural Net MLP inválido!' )

        np . aleatório . semente ( 1 )
        eu . pesos  = [ 2  *  np . aleatório . aleatório (( entrada , oculto [ 0 ])) -  1 ]
        se  len ( oculto ) >  1 :
            para  i  no  intervalo ( 1 , len ( oculto )):
                eu . pesos . anexar ( 2  *  np . aleatório . aleatório (( oculto [ i  -  1 ], oculto [ i ])) -  1 )
            eu . pesos . anexar ( 2  *  np . aleatório . aleatório (( oculto [ len ( oculto ) -  1 ], saída )) -  1 )
        mais :
            eu . pesos . acrescentar ( 2  *  np . aleatório . aleatório (( oculto [ 0 ], saída )) -  1 )

    # Método para ajustar o peso dos neurônios
    def  __sigmoid_derivative ( self , inputs ):
        retornar  entradas  * ( 1  -  entradas )

    # Método de ativação
    def  __sigmoid ( auto , entradas ):
        retornar  1  / ( 1  +  np . exp ( - entradas ))

    # Processo para calcular o resultado final de cada neurônio
    def  __forward ( auto , entradas ):
        w  = [ entradas , auto . __sigmoid ( np . dot ( entradas , auto . pesos [ 0 ]))]
        para  i  na  gama ( 1 , len ( auto . pesos )):
            w . acrescentar ( self . __sigmoid ( np . ponto ( w [ len ( w ) -  1 ], self . pesos [ i ])))
        retorno  w

    # Este método treinará os neurônios para prever novos valores
    def  train ( auto , entradas , saídas , iterações ):
        para  iteração  no  intervalo ( iterações ):
            # propagação direta
            w  =  auto . __forward ( entradas )

            # Verificando erro
            erro  =  saídas  -  w [ len ( w ) -  1 ]
            if ( iteração  %  1000 ) ==  0 :
                print ( "Erro: {}" . formato ( np . média ( np . abs ( erro ))))

            # propagação traseira
            w_delta  = [ erro  *  próprio . __sigmóide ( w [ len ( w ) -  1 ])]
            para  i  na  faixa ( len ( w ) -  1 , - 1 , - 1 ):
                se  i  >  1 :
                    w_error  =  w_delta [ len ( w_delta ) -  1 ]. ponto ( auto . pesos [ i  -  1 ]. T )
                    w_delta . anexar ( w_error  *  self . __sigmoid_derivative ( w [ i  -  1 ]))

            # Atualizando pesos
            eu . pesos [ 0 ] + =  np . ponto ( entradas . T , w_delta [ len ( w_delta ) -  1 ])
            j  =  len ( w_delta ) -  2
            para  i  na  gama ( 1 , len ( auto . pesos )):
                eu . pesos [ i ] + =  np . ponto ( w [ i ]. T , w_delta [ j ])
                j  - =  1

    # Este método executará a rede neural
    def  run ( auto , entradas ):
        w  =  auto . __forward ( entradas )
        retorno  w [ len ( w ) -  1 ]

se  __name__  ==  "__main__" :
    nn  =  MultilayerPerceptron ( 2 , [ 4 , 3 , 3 ], 1 )
    X  =  np . matriz ([[ 0 , 0 ], [ 0 , 1 ], [ 1 , 0 ], [ 1 , 1 ]])
    y  =  np . matriz ([[ 0 , 1 , 1 , 0 ]]). T
    nn . trem ( X , y , 40000 )
    print ( "Resultado final: {}" . formato ( nn . run ( np . array ([ 1 , 0 ]))))
