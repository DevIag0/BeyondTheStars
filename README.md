  Beyond the Stars - Space Shooter Game

  Sobre o Projeto

Este é um projeto acadêmico desenvolvido para a disciplina de **Linguagem de Programação** da faculdade. O jogo "Beyond the Stars" é um space shooter clássico desenvolvido em Python utilizando a biblioteca Pygame, implementando diversos padrões de projeto e conceitos de programação orientada a objetos.

  Características do Jogo

- **Modo Single Player**: Jogue sozinho contra ondas de inimigos
- **Modo Cooperativo**: Jogue com um amigo (2 jogadores)
- **Sistema de Pontuação**: Ganhe pontos eliminando inimigos e meteoros
- **Sistema de Vida**: Jogadores têm vida limitada
- **Diferentes Tipos de Inimigos**: Enemy1, Enemy2 e meteoros com comportamentos únicos
- **Sistema de Score**: Top 10 melhores pontuações salvas em banco de dados
- **Modos de Tempo**: 60 segundos, 120 segundos ou ilimitado
- **Configurações Avançadas**: FPS (60/90), volume, tempo de jogo e listagem de comandos
- **Efeitos Sonoros**: Música de fundo e efeitos sonoros
- **Animações**: Sprites animados para jogadores e inimigos
- **Menu de Pausa**: Pause o jogo a qualquer momento
- **Background Parallax**: Efeito de profundidade nos backgrounds

    Tecnologias Utilizadas

- **Python 3.13**: Linguagem principal do projeto
- **Pygame 2.6.1**: Biblioteca para desenvolvimento de jogos
- **SQLite3**: Banco de dados para sistema de pontuação
- **Programação Orientada a Objetos**: Base arquitetural do projeto

 Arquitetura do Projeto

O projeto segue uma arquitetura bem estruturada com separação de responsabilidades:

```
SpaceShooter/
├── main.py                 # Ponto de entrada da aplicação
├── requirements.txt        # Dependências do projeto
├── asset/                  # Recursos gráficos e sonoros
└── code/                  # Código fonte
    ├── Game.py           # Controlador principal
    ├── Entity.py         # Classe base abstrata
    ├── Player.py         # Classe do jogador
    ├── Enemy.py          # Classe dos inimigos
    ├── Meteor.py         # Classe dos meteoros
    ├── Level.py          # Gerenciamento de níveis
    ├── Menu.py           # Interface do menu
    ├── Opcoes.py         # Menu de configurações
    └── ...
```

 Padrões de Projeto Implementados

 1. **Factory Pattern** (`EntityFactory.py`)
- Responsável pela criação de diferentes tipos de entidades
- Centraliza a lógica de instanciação de jogadores, inimigos, meteoros e backgrounds
- Facilita a adição de novos tipos de entidades
- Permite a criação dinâmica de entidades com base em configurações

 2. **Mediator Pattern** (`EntityMediator.py`)
- Gerencia a comunicação entre diferentes entidades
- Centraliza a lógica de colisões e interações
- Desacopla as entidades umas das outras

 3. **Template Method Pattern** (`Entity.py`)
- Classe abstrata que define a estrutura comum para todas as entidades
- Método abstrato `move()` implementado pelas subclasses
- Garante consistência na interface das entidades

 4. **Proxy Pattern** (`DatabaseProxy.py`)
- Controla o acesso ao banco de dados SQLite3
- Gerencia operações de leitura e escrita do sistema de score
- Abstrai a complexidade das operações de banco de dados
- Fornece interface simplificada para o sistema de pontuação

 5. **Strategy Pattern** (implícito)
- Diferentes comportamentos de movimento para jogadores e inimigos
- Diferentes tipos de tiro para cada entidade

 🎨 Estrutura de Classes

 Hierarquia de Entidades
```
Entity (ABC)
├── Player
├── Enemy
├── Meteor
├── Background
├── PlayerShot
└── EnemyShot
```

### Classes Principais

#### `Entity` (Classe Abstrata)
- Classe base para todas as entidades do jogo
- Define propriedades comuns: posição, sprite, vida, velocidade
- Método abstrato `move()` para implementação específica

#### `Player`
- Controla o jogador com animações
- Implementa sistema de tiro
- Gerencia entrada do teclado
- Suporte para 2 jogadores com controles diferentes

#### `Enemy`
- Movimento vertical
- Sistema de tiro automático
- Diferentes tipos de inimigos com características únicas

#### `Meteor`
- Novos tipos de obstáculos (Meteor1 e Meteor2)
- Movimento vertical simples
- Colisão com jogadores e projéteis
- Spawn automático durante o gameplay

#### `Game`
- Controlador principal da aplicação
- Gerencia transições entre estados (menu, jogo, opções)
- Mantém configurações globais (volume, etc.)

#### `Level`
- Gerencia o gameplay
- Sistema de spawn de inimigos
- Controle de pontuação e vida
- Menu de pausa integrado

#### `Score`
- Sistema completo de pontuação
- Integração com banco de dados SQLite3
- Separação por modos de tempo (60s/120s)
- Display de top 10 melhores scores
- Entrada de nome do jogador

#### `DatabaseProxy`
- Gerenciamento de conexões com SQLite3
- Operações CRUD para sistema de score
- Consultas otimizadas para rankings

##  Controles

### Jogador 1
- **Movimento**: Setas do teclado
- **Atirar**: Espaço
- **Pausar**: P
- **Sair**: ESC

### Jogador 2 (Modo Cooperativo)
- **Movimento**: W, A, S, D
- **Atirar**: G

### Menu
- **Navegar**: Setas ↑/↓
- **Selecionar**: Enter
- **Voltar**: ESC

### Lista Completa de Comandos
Acesse no menu "Opções" → "Comandos" para ver todos os controles disponíveis.

##  Como Executar

1. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

2. **Execute o jogo**:
```bash
python main.py
```

##  Dependências

- `pygame==2.6.1`: Biblioteca principal para desenvolvimento do jogo

##  Funcionalidades Implementadas

### Sistema de Entidades
- ✅ Criação dinâmica de entidades via Factory
- ✅ Gerenciamento de vida e colisões
- ✅ Animações sprite-based
- ✅ Sistema de tiro para jogadores e inimigos
- ✅ Meteoros como obstáculos adicionais

### Sistema de Gameplay
- ✅ Múltiplos modos de jogo (Single Player e Cooperativo)
- ✅ Sistema de pontuação com banco de dados
- ✅ Modos de tempo (60s, 120s, ilimitado)
- ✅ Spawn dinâmico de inimigos e meteoros
- ✅ Detecção de colisões
- ✅ Game Over com entrada de nome
- ✅ Countdown timer

### Interface de Usuário
- ✅ Menu principal interativo
- ✅ Menu de configurações completo
- ✅ Sistema de score com rankings
- ✅ Listagem de comandos
- ✅ Sistema de pausa
- ✅ HUD com informações do jogo

### Configurações
- ✅ Controle de FPS (60/90)
- ✅ Controle de volume
- ✅ Seleção de tempo de jogo
- ✅ Visualização de comandos

### Áudio e Gráficos
- ✅ Música de fundo
- ✅ Sprites animados
- ✅ Backgrounds paralaxe (múltiplas camadas)
- ✅ Controle de volume
- ✅ Diferentes velocidades de parallax para menu e jogo

### Sistema de Dados
- ✅ Banco de dados SQLite3 integrado
- ✅ Sistema de score persistente
- ✅ Rankings separados por modo de tempo
- ✅ Estatísticas dos top 3 jogadores

##  Conceitos de Programação Aplicados

### Programação Orientada a Objetos
- **Encapsulamento**: Propriedades e métodos encapsulados nas classes
- **Herança**: Hierarquia de classes Entity -> Player/Enemy
- **Polimorfismo**: Método `move()` implementado diferentemente em cada classe
- **Abstração**: Classe abstrata Entity define interface comum

### Padrões de Projeto
- **Factory**: Criação centralizada de entidades
- **Mediator**: Gerenciamento de interações entre entidades
- **Template Method**: Estrutura comum para entidades
- **Proxy**: Controle de acesso ao banco de dados

### Boas Práticas
- **Separação de Responsabilidades**: Cada classe tem uma responsabilidade específica
- **Constantes Centralizadas**: Arquivo `Const.py` com todas as configurações
- **Modularização**: Código organizado em módulos específicos
- **Documentação**: Comentários explicativos no código

##  Desenvolvimento Acadêmico

Este projeto foi desenvolvido como parte do currículo da disciplina de Linguagem de Programação, demonstrando:

- Aplicação prática de conceitos de POO
- Implementação de padrões de projeto
- Estruturação de código em projetos médios
- Uso de bibliotecas externas (Pygame)
- Desenvolvimento de jogos em Python

##  Aprendizados

Durante o desenvolvimento deste projeto, foram aplicados e consolidados os seguintes conceitos:

1. **Padrões de Projeto**: Implementação prática de Factory, Mediator, Template Method e Proxy
2. **Arquitetura de Software**: Organização de código em camadas e módulos
3. **Programação Orientada a Objetos**: Uso intensivo de herança, polimorfismo e encapsulamento
4. **Desenvolvimento de Jogos**: Conceitos fundamentais de game loops, sprites e colisões
5. **Gerenciamento de Estado**: Controle de diferentes estados do jogo (menu, gameplay, pausa)
6. **Interação com Usuário**: Implementação de menus e controles de entrada
7. **Banco de Dados**: Integração com SQLite3 para persistência de dados
8. **Sistema de Ranking**: Implementação de sistema de pontuação e rankings

---

**Desenvolvido para fins acadêmicos - Disciplina de Linguagem de Programação**
