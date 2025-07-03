# 🚀 Beyond the Stars - Space Shooter Game

## 📋 Sobre o Projeto

(Ainda em desenvolvimento)
Este é um projeto acadêmico desenvolvido para a disciplina de **Linguagem de Programação** da faculdade. O jogo "Beyond the Stars" é um space shooter clássico desenvolvido em Python utilizando a biblioteca Pygame, implementando diversos padrões de projeto e conceitos de programação orientada a objetos.

## 🎮 Características do Jogo

- **Modo Single Player**: Jogue sozinho contra ondas de inimigos
- **Modo Cooperativo**: Jogue com um amigo (2 jogadores)
- **Modo Player vs Player**: Enfrente outro jogador
- **Sistema de Pontuação**: Ganhe pontos eliminando inimigos
- **Sistema de Vida**: Jogadores têm vida limitada
- **Efeitos Sonoros**: Música de fundo e efeitos sonoros
- **Animações**: Sprites animados para jogadores e inimigos
- **Menu de Pausa**: Pause o jogo a qualquer momento
- **Configurações**: Ajuste volume e outras opções

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**: Linguagem principal do projeto
- **Pygame 2.6.1**: Biblioteca para desenvolvimento de jogos
- **Programação Orientada a Objetos**: Base arquitetural do projeto

## 🏗️ Arquitetura do Projeto

O projeto segue uma arquitetura bem estruturada com separação de responsabilidades:

```
SpaceShooter/
├── main.py                 # Ponto de entrada da aplicação
├── requirements.txt        # Dependências do projeto
├── asset/                  # Recursos gráficos e sonoros
│   ├── sprites/           # Imagens dos personagens
│   ├── backgrounds/       # Imagens de fundo
│   └── sounds/           # Arquivos de áudio
└── code/                  # Código fonte
    ├── Game.py           # Controlador principal
    ├── Entity.py         # Classe base abstrata
    ├── Player.py         # Classe do jogador
    ├── Enemy.py          # Classe dos inimigos
    ├── Level.py          # Gerenciamento de níveis
    ├── Menu.py           # Interface do menu
    ├── Opcoes.py         # Menu de configurações
    └── ...
```

## 🎯 Padrões de Projeto Implementados

### 1. **Factory Pattern** (`EntityFactory.py`)
- Responsável pela criação de diferentes tipos de entidades
- Centraliza a lógica de instanciação de jogadores, inimigos e backgrounds
- Facilita a adição de novos tipos de entidades
- Permite a criação dinâmica de entidades com base em configurações

### 2. **Mediator Pattern** (`EntityMediator.py`)
- Gerencia a comunicação entre diferentes entidades
- Centraliza a lógica de colisões e interações
- Desacopla as entidades umas das outras

### 3. **Template Method Pattern** (`Entity.py`)
- Classe abstrata que define a estrutura comum para todas as entidades
- Método abstrato `move()` implementado pelas subclasses
- Garante consistência na interface das entidades

### 4. **Strategy Pattern** (implícito)
- Diferentes comportamentos de movimento para jogadores e inimigos
- Diferentes tipos de tiro para cada entidade

## 🎨 Estrutura de Classes

### Hierarquia de Entidades
```
Entity (ABC)
├── Player
├── Enemy
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

#### `Game`
- Controlador principal da aplicação
- Gerencia transições entre estados (menu, jogo, opções)
- Mantém configurações globais (volume, etc.)

#### `Level`
- Gerencia o gameplay
- Sistema de spawn de inimigos
- Controle de pontuação e vida
- Menu de pausa integrado

## 🎮 Controles

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

## 🚀 Como Executar

1. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

2. **Execute o jogo**:
```bash
python main.py
```

## 📦 Dependências

- `pygame==2.6.1`: Biblioteca principal para desenvolvimento do jogo

## 🎯 Funcionalidades Implementadas

### Sistema de Entidades
- ✅ Criação dinâmica de entidades via Factory
- ✅ Gerenciamento de vida e colisões
- ✅ Animações sprite-based
- ✅ Sistema de tiro para jogadores e inimigos

### Sistema de Gameplay
- ✅ Múltiplos modos de jogo
- ✅ Sistema de pontuação
- ✅ Spawn dinâmico de inimigos
- ✅ Detecção de colisões
- ✅ Game Over e reinício

### Interface de Usuário
- ✅ Menu principal interativo
- ✅ Menu de configurações
- ✅ Sistema de pausa
- ✅ HUD com informações do jogo

### Áudio e Gráficos
- ✅ Música de fundo
- ✅ Sprites animados
- ✅ Backgrounds paralaxe
- ✅ Controle de volume

## 🧠 Conceitos de Programação Aplicados

### Programação Orientada a Objetos
- **Encapsulamento**: Propriedades e métodos encapsulados nas classes
- **Herança**: Hierarquia de classes Entity -> Player/Enemy
- **Polimorfismo**: Método `move()` implementado diferentemente em cada classe
- **Abstração**: Classe abstrata Entity define interface comum

### Padrões de Projeto
- **Factory**: Criação centralizada de entidades
- **Mediator**: Gerenciamento de interações entre entidades
- **Template Method**: Estrutura comum para entidades

### Boas Práticas
- **Separação de Responsabilidades**: Cada classe tem uma responsabilidade específica
- **Constantes Centralizadas**: Arquivo `Const.py` com todas as configurações
- **Modularização**: Código organizado em módulos específicos
- **Documentação**: Comentários explicativos no código

## 👥 Desenvolvimento Acadêmico

Este projeto foi desenvolvido como parte do currículo da disciplina de Linguagem de Programação, demonstrando:

- Aplicação prática de conceitos de POO
- Implementação de padrões de projeto
- Estruturação de código em projetos médios
- Uso de bibliotecas externas (Pygame)
- Desenvolvimento de jogos em Python

## 🎓 Aprendizados

Durante o desenvolvimento deste projeto, foram aplicados e consolidados os seguintes conceitos:

1. **Padrões de Projeto**: Implementação prática de Factory, Mediator e Template Method
2. **Arquitetura de Software**: Organização de código em camadas e módulos
3. **Programação Orientada a Objetos**: Uso intensivo de herança, polimorfismo e encapsulamento
4. **Desenvolvimento de Jogos**: Conceitos fundamentais de game loops, sprites e colisões
5. **Gerenciamento de Estado**: Controle de diferentes estados do jogo (menu, gameplay, pausa)
6. **Interação com Usuário**: Implementação de menus e controles de entrada

---

**Desenvolvido para fins acadêmicos - Disciplina de Linguagem de Programação**
