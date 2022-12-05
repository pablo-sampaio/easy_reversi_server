
# Projeto Easy Reversi Server

Projeto criado para a disciplina de Sistemas Multiagentes. Oferece classes
básicas para o jogo **Reversi** modificado.

## Principais arquivos

- **reversi** - funções básicas com a lógica do jogo - criar jogo, listar jogadas válidas, aplicar jogada, calcular score, etc
- **play_offline** - permite jogar, pelo teclado, contra o agente guloso (faz a jogada que dá mais pontos no momento)
- **server_reversi** - criar um servidor que controla a execução de uma quantidade de partidas pré-definidas (no código) entre dois clientes, conectados via socket
- **client_greedy** - cliente (do servidor) que implementa o agente guloso
- **client_human** - cliente (do servidor) que permite um jogador humano conectar ao servidor e jogar pelo teclado

Recomendação para quem fazer uma IA para jogar através do servidor: veja o código de um dos clientes (os dois são parecidos) e aproveite
o "esqueleto" do código, trocando apenas a função que faz a escolha da jogada.


## Regras do Jogo

- O tabuleiro padrão tem tamanho 8x8, mas o código permite tamanhos pares diversos.
- Se você jogar em uma posição ao lado de um adversáio, todas as peças adversárias consecutivas que estiverem entre duas peças suas na mesma linha (horizontal, vertical ou diagonal) se tornam suas.
- Você só pode jogar em posições que conquistam peças adversárias.
- (Variante) O tabuleiro pode iniciar com "pedras", que indicam posições proibidas de jogar.
- Você sempre pode passar a vez.
- Se não tiver mais posições válidas para jogar, é obrigatório passar (mas o servidor aguarda o jogador indicar que passou).
- Se os dois jogadores passarem de forma consecutiva, o jogo encerra.


## PENDÊNCIAS (TODO)

- Ainda falta enviar o tabuleiro do servidor para os clientes (e fazer o parser nos clientes)
- Falta o servidor gerar uma pontuação final de todos os jogos
