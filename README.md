# SoundPlayer - Controlador de Loop de Áudio com Prioridade

**SoundPlayer** é uma biblioteca Python para controle de reprodução de áudio em loop, projetada para uso intensivo com gerenciamento automático de precedência. Cada som pode ser ajustado em intensidade, determinando o intervalo de repetição para simular um efeito contínuo. Ideal para aplicações que necessitam de sons com prioridade, como radares ou sistemas de alerta.

## Características

- Controle de intensidade de som: ajuste de 0.0 (silencioso) a 1.0 (intensidade máxima)
- Sistema de loop automático: menor intervalo conforme intensidade aumenta
- Gerenciamento de precedência entre sons (`RED`, `ORANGE`, `YELLOW`), garantindo que apenas o som com maior prioridade esteja ativo
- Baseado em **pygame** para suporte de áudio robusto e threading para reprodução contínua e fluida

## Estrutura de Arquivos

```plaintext
.
├── src
└── tools
    └── sounds
        ├── A440.ogg      # Som RED com prioridade máxima
        ├── Rhodes.ogg    # Som ORANGE com prioridade média
        └── Slick.ogg     # Som YELLOW com prioridade baixa
```

## Interface de Cores para Precedência de Sons

| Som       | Cor       | Prioridade            |
|-----------|-----------|-----------------------|
| 🔴 **RED**    | **Vermelho** | Alta (Prioridade Máxima) |
| 🟠 **ORANGE** | **Laranja**  | Média (Prioridade Intermediária) |
| 🟡 **YELLOW** | **Amarelo**  | Baixa (Prioridade Menor) |

- **RED**: Som de alta prioridade. Interrompe todos os outros sons ao ser ativado.
- **ORANGE**: Som de prioridade intermediária. Toca se **RED** não estiver ativo e interrompe o **YELLOW**.
- **YELLOW**: Som de prioridade baixa. Toca apenas se **RED** e **ORANGE** estiverem inativos.

## Exemplo de instalação e como usar

### Instalar no sistema

```shell
pip install pygame
```

### Instalar em um ambiente virtual

```shell
python3.12 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install pygame
```

### Exemplo de uso

```python
import time

# Instancia o controlador dos sons
sound_player = SoundController()

# Inicia o som YELLOW com intensidade mínima e ajusta gradualmente
for i in range(5):
    intensity = (i + 1) / 10
    sound_player.yellow.play(intensity=intensity)
    time.sleep(1)

# Inicia o som ORANGE com intensidade crescente, substituindo o YELLOW
sound_player.orange.play()
for i in range(5):
    intensity = (i * 1.5 + 1) / 10
    sound_player.orange.set_intensity(intensity)
    time.sleep(1)

# Inicia o som RED com intensidade máxima e substitui o ORANGE
for i in range(5):
    intensity = 0.5 + (i + 1) / 10
    sound_player.red.play(intensity=intensity)
    time.sleep(1)

# Para o som RED
sound_player.red.stop()
```
