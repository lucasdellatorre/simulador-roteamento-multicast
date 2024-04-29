# Simulador de roteamento multicast

O simulador deve receber como parâmetros de execução o nome de um arquivo de descrição de topologia (conforme formato especificado) e um arquivo contendo comandos a serem executados na topologia (conforme formato especificado). O simulador deve apresentar na saída as mensagens enviadas pelos roteadores e subredes da topologia conforme o formato estabelecido, considerando a execução dos comandos indicados no arquivo de entrada.

## Formato do arquivo de descrição de topologia

```
#SUBNET
<sid>,<netaddr/mask>
#ROUTER
<rid>,<numifs>,<ip1/mask>,<ip2/mask>,<ip3/mask>...
#ROUTERTABLE
<rid>,<netaddr/mask>,<nexthop>,<ifnum>
```

## Formato do arquivo de execução

```
<command> <params>
<command> <params>
...
```

## Os comandos que devem ser suportados são:

mjoin <sid> <mgroupid> : indicação do interesse da subrede <sid> para receber mensagens do grupo multicast <mgroupid>

mleave <sid> <mgroupid> : solicitação de retirada de interesse da subrede <sid> em relação ao grupo multicast <mgroupid>

mping <sid> <mgroupid> <msg> : envio de um ping com a mensagem <msg> da subrede <sid> para o grupo multicast <mgroupid>

## Formato de saída

Mensagem mjoin: <sid> => <rid> : mjoin <mgroupid>;

Mensagem mleave: <sid> => <rid> : mleave <mgroupid>;

Mensagem mflood: <rid> >> <rid>, <rid> >> <rid>, ... : mflood <mgroupid>;

Mensagem mprune: <rid> >> <rid> : mprune <mgroupid>;

Mensagem mping: <sid|rid> =>> <sid|rid>, <sid|rid> =>> <sid|rid>: mping <mgroupid> <msg>;

Mensagem mrecv: <sid> box <sid> : <mgroupid>#<msg> from <sid> ;

Funcionamento do mping

## O comando mping é composto por 3 etapas:

Flooding: é enviado um pacote de inundação (mflood) entre os roteadores da rede utilizando RPF (Reverse Path Forwarding) para evitar loops

Pruning: é enviada uma mensagem mprune para "bloquear" o tráfego multicast de um grupo específico para um roteador

Ping: é enviado o pacote de ping contendo a mensagem para o grupo multicast respectivo

Recv: quando a mensagem chega na subrede, a mensagem enviada é apresentada (mrecv)

## Modo de execução do simulador

```
$ simulador <topofile> <cmdfile>
```
