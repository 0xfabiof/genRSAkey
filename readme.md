## genRSAkey
Python function that generates RSA Keys *(n,p,q,e,d)* for a given input *l* which represents the length of the representation in bits of *n*.

Project done for the course of Cryptography, of the Master's in Information Security

Department of Computer Science

Faculty of Sciences, University of Porto

The full implementation report is below (Portuguese only)

Fábio Freitas - up201505331@fc.up.pt

Nuno Lopes - up201505531@fc.up.pt

--
## genRSAkey
Função em Python que gera chaves RSA *(n,p,q,e,d*) dado um input *l* que representa o comprimento em bits para *n*

Realizado no âmbito da Unidade Curricular de Criptografia do Mestrado em Segurança Informática

Departamento de Ciência de Computadores

Faculdade de Ciências da Universidade do Porto

Fábio Freitas - up201505331@fc.up.pt

Nuno Lopes - up201505531@fc.up.pt

## Relatório de Implementação
No âmbito do trabalho prático 1 da unidade curricular de Criptografia do Mestrado em Segurança Informática da FCUP foi nos proposto que fosse construída uma implementação em Python de uma função de geração de chaves de utilização do esquema criptográfico RSA.

Segundo o enunciado, esta implementação deveria ser feita sem recorrer a importação de quaisquer bibliotecas criptográficas, sendo o único módulo cuja utilização seria permitida seria o módulo random.

O objetivo era que dado um input length  l, a função deveria retornar um tuplo com 5 valores: n, p, q, e, d.

-   n - inteiro longo cuja representação em bits é de tamanho l
    
-   p,q - inteiros primos tal que p*q = n
    
-   e - inteiro coprimo com (p-1)*(q-1) (expoente público)
    
-   d - tal que ed≡1(mod(p−1)(q−1)) (expoente privado)
    

O primeiro passo da nossa implementação passou por construir um protótipo funcional da função de geração de chaves que aceitasse um input length l  de tamanhos relativamente pequenos (16 bits ou 32 bits) para que pudéssemos verificar os p e q gerados comparando-os com listas de números primos já existentes.

Criámos uma função num_gen() que será o gerador de números aleatórios. Esta função será utilizada para gerar p e q. Esta função num_gen aceita como argumento a dimensão em bits do número gerado. Sendo que n resulta da multiplicação entre p e q, o gerador de números para o p e q deve tomar como dimensão em bits a metade da dimensão que é pretendida para o n. (para um n de dimensão 4096 bits, deve ser gerado um par de p e q de 2048 bits cada um, por exemplo).

Em primeiro lugar, é criado um while loop que chama a função num_gen() e o valor retornado nessa função é atribuído a uma variável p e de seguida é feita a verificação se essa variável p se trata ou não de um número primo. Se não se tratar de um número primo, a variável p é incrementada em 2 (para se manter um número ímpar). Quando é atingido um número primo o loop é quebrado e a execução do programa continua.

A geração do q é feita exatamente da mesma forma mas à condição do loop que q tem de ser primo é acrescentada a condição de que também tem ser diferente de p. (já que um dos requisitos do esquema criptográfico RSA é que os primos cuja multiplicação resulta no n sejam diferentes). Além disto, definimos também que a diferença entre p e q teria de ser maior que 2n1/4 para evitar um ataque de Faulty Key Generation.

Numa fase inicial da nossa implementação, quando ainda estávamos a lidar com lengths de tamanho muito reduzido, a nossa verificação de primalidade era feita de uma forma simples que verificava num ciclo for se existe algum número y de 2 até x cujo resto da divisão inteira de x por y fosse 0. Se sim, este ciclo retornaria false, se não o ciclo retornaria true (ou seja, o número é primo).

No entanto, quando percebemos que o nosso protótipo estava de facto funcional e começamos a tentar escalá-lo para números da ordem de grandeza pedida no enunciado, é óbvio que esta verificação de primalidade não possuía os requisitos de eficiência necessários. Para aumentarmos então a eficiência do nosso programa substituímos o nosso algoritmo simples de verificação de primalidade por um algoritmo com base estatística extremamente eficiente conhecido como Miller-Rabin primality test numa função a que chamamos is_probable_prime(). Como é sabido, este teste de primalidade aceita como parâmetros, além do número a testar, o número de iterações do teste probabilístico. Para a nossa implementação decidimos fazer o teste com 64 iterações que nos fornece uma probabilidade de 1-2-128 da verificação estar correta, o que é mais que aceitável em termos práticos. Para melhorar a eficiência deste algoritmo utilizamos uma exponenciação modular, esta baseia-se num algoritmo de exponenciação binária mas retorna o resto da divisão inteira entre o valor da exponenciação (definido na função binpowmod()).

Gerados então p e q com a dimensão em bits pretendida, a definimos então uma variável n que resulta da multiplicação destes dois primos gerados.

O próximo passo será então a geração das últimas duas variáveis que compõem o conjunto de partes necessárias para o esquema criptográfico RSA: o expoente público de cifrar e e o expoente público de decifrar d.

Em relação ao expoente público de cifrar e foi escolhido aquele que é adotado como constante na maioria das implementações RSA que é o número primo 65537, que é um dos números de Fermat e é habitualmente utilizado porque é computado muito rapidamente devido a corresponder a 216+1.

Utilizamos também o Algoritmo de Euclides estendido numa função egcd() que como o nome indica é uma extensão do algoritmo de Euclides onde além de calcular o máximo divisor comum entre (a,b) também obtemos os coeficientes que multiplicando com a e b fornece-nos o máximo divisor comum entre (a,b). Este algoritmo é usado em conjunto com o inverso multiplicativo, quando multiplicamos um valor pelo seu inverso multiplicativo obtemos o valor um com isto podemos calcular o valor de d  pois queremos que e*d ≡1(mod(p−1)(q−1)).

De modo a conseguir melhorar a eficiência do programa usamos um algoritmo de exponenciação binária binpow() , onde em vez de calcular um expoente da maneira tradicional, elevamos sempre o valor a 2 e depois fazemos uma multiplicação de modo a obter o valor do expoente necessário.

Depois da conclusão destas otimizações, realizamos alguns testes e documentamos os seus resultados em termos de tempo de execução e em 100 execuções, obtivemos os seguintes resultados:

![testes](https://i.imgur.com/gArcPRL.png)

  

Referências Bibliográficas:

Algorithm Implementation/Mathematics/Primality Testing - disponível online em [https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Primality_Testing](https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Primality_Testing) (acedido pela última vez em Novembro de 2018)

Algorithm Implementation/Mathematics/Extended Euclidean algorithm - disponível online em [https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm](https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm) (acedido pela última vez em Novembro de 2018)

Binary Exponentiation - disponível online em [https://cp-algorithms.com/algebra/binary-exp.html](https://cp-algorithms.com/algebra/binary-exp.html) (acedido pela última vez em Novembro de 2018)

MENEZES, Alfred; OORSCHOT, Paul; e VANSTONE, Scott; Handbook of Applied Cryptography - 1996
