# Controle de Campeonato

Descrição da atividade de construção de um sistema de controle de campeonatos.

## Sobre a Atividade

O objetivo desta atividade é produzir um sistema de controle de campeonatos, com uma tabela de controle de resultados, detalhes de partidas por equipes, e todo o controle de cadastros de novas equipes e partidas.

Neste campeonato, um time consegue 3 pontos para cada vitória, 1 ponto para cada empate e 0 pontos por derrota. O número de vitórias é o primeiro critério de desempate e o de empates o segundo.

## Tecnologias Utilizadas

O sistema será web, usando o microframework Flask no _backend_, com cadastros em um banco de dados SQLite3. No _frontend_ pode ser utilizada quaisquer bilbiotecas que vocês queiram usar.

## Modelos de Dados

Para facilitarmos a atividade, vamos usar dados todos em memória, presentes em váriaveis dentro do script **dados.py**. Todas as manipulações devem ser feitas por manipulações destes vetores.

Temos três entidades apenas, representados por suas respecitvas classes: _Equipes_, _Partidas_ e _Usuarios_ (todas presentes no script **classes.py**).

## Itens da Atividade

###### A atividade será divida em duas grandes partes: navegação e páginas principais do _frontend_ e parte de cadastros (admin).

### Parte 1 - Navegação e Páginas Principais

Para a primeira parte deve ser criada um _Blueprint_ do flask chamado **website** que terá as seguintes rotas configuradas nos seus respectivos _controllers_:

- Home (/): A página inicial que mostrará o resultado atual do campeonato, mostrando as equipes ordenadas pelo número de pontos (e sua posição nesse caso), mostrando também: número de jogos, vitórias, empates e derrotas. Para cada equipe haverá um link para os detalhes de partidas deste time.
- Detalhes da Equipe (/detalhes/{equipe}): Mostra uma lista de todas as partidas que o time apareceu, com o resultado e estilos diferentes para partidas ganhas, empatadas e perdidas.
- Entrar (/entrar): O formulário de login, que receberá um e-mail e uma senha para fazer o login.

Todos as páginas devem possuir uma identidade visual com botões de navegação (preferencialmente no cabeçalho).

### Parte 2 - Área Administrativa

Na segunda parte deve ser feito outro _Blueprint_ chamado **admin** que terá as seguintes rotas:

- Admin (/admin): Área administrativa, que só pode ser acessada com o login feito, com caminhos para os cadastros de equipes e partidas, além do botão de sair (logout).
- Equipes (/equipes): Listagem de todas as equipes cadastradas, mostrando o nome, sigla e local da equipe na lista, e botões de alteração e remoção da equipe. Além disso, na tela deve haver um botão de inclusão de nova equipe.
  - Nova Equipe (/equipes/criar): Formulário de criação de nova equipe, para coletar o nome, sigla e local da equipe. Botão salvar e limpar. Ao salvar, deve voltar para a listagem.
  - Aletar Equipe (/equipes/alterar/{equipe}): Formulário de alteração da equipe, com os campos de nome, sigla e local já preenchidos e prontos para alteração. Botão salvar e limpar. Ao salvar, deve voltar para a listagem.
  - Remover Equipe (/equipes/deletar/{equipe}): Mostar uma janela de confirmação ao clicar em remover a equipe e, se confirmado, entrar nessa url para remover mesmo a equipe e voltar para a tela de listagem.
- Partidas (/partidas): Listagem de todas as partidas cadastradas, mostrando o nome, sigla e local de ambas as equipes na lista, com o resultados, e botões de alteração e remoção da partida. Além disso, na tela deve haver um botão de inclusão de nova partida.
  - Nova Partida (/partidas/criar): Formulário de criação de nova partida, para coletar o time da casa, o visitante e os pontos de cada um. Botão salvar e limpar. Ao salvar, deve voltar para a listagem.
  - Aletar Partida (/partidas/alterar/{partida}): Formulário de alteração da partida, com os campos de time da casa, visitante e pontos de ambos já preenchidos e prontos para alteração. Botão salvar e limpar. Ao salvar, deve voltar para a listagem.
  - Remover Partida (/partidas/deletar/{partida}): Mostar uma janela de confirmação ao clicar em remover a partida e, se confirmado, entrar nessa url para remover mesmo a partida e voltar para a tela de listagem.

## Correção

A nota será proporcional ao número de testes que passarem, de acordo com os arquivos de testes. A parte de layout só será considerado na apresentação (não nos testes).