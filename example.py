import time
from sound_player import SoundController

# Exemplo de uso
sound_player = SoundController()

# Inicia o som amarelo com intensidade mínima
for i in range(5):
    intensity = (i + 1) / 10
    sound_player.yellow.play(intensity=intensity)
    time.sleep(1)  # Espera para simular o loop inicial

time.sleep(1)

# Inicia o som laranja com intensidade mínima
sound_player.orange.play()

for i in range(5):
    intensity = (i*1.5 + 1) / 10
    sound_player.orange.set_intensity(intensity)
    time.sleep(1)  # Espera para simular o loop inicial
    
# Ajusta a intensidade para 1.0 (maior intensidade)
time.sleep(2)  # Espera para simular o loop inicial

intensity = 0.5
for i in range(5):
    intensity += (i + 1) / 10
    sound_player.red.play(intensity=intensity)
    time.sleep(1)  # Espera para simular o loop inicial

time.sleep(2)  # Espera para simular o loop inicial
# Parando o som vermelho
sound_player.red.stop()
