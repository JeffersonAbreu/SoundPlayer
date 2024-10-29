import pygame
import time
import threading

# Inicializa o mixer de áudio do pygame
pygame.mixer.init()

class SoundPlayer:
    current_sound = None  # Para rastrear o som com maior precedência ativa

    def __init__(self, file_path, precedence):
        self.sound = pygame.mixer.Sound(file_path)
        self.precedence = precedence
        self.intensity = 0.1  # Intensidade inicial mínima
        self.loop_interval = 3  # Intervalo padrão em segundos
        self.playing = False
        self._thread = None

    def set_intensity(self, intensity):
        # Ajusta a intensidade entre 0.0 e 1.0 e calcula o intervalo de loop
        self.intensity = max(0.0, min(intensity, 1.0))
        self.loop_interval = 3 - (2.9 * self.intensity)  # Menor intervalo conforme a intensidade aumenta

    def play(self, intensity = 0.1):
        self.set_intensity(intensity)
        if SoundPlayer.current_sound is None or self.precedence < SoundPlayer.current_sound.precedence:
            if SoundPlayer.current_sound:
                SoundPlayer.current_sound.stop()
            SoundPlayer.current_sound = self
            self.playing = True
            self._thread = threading.Thread(target=self._play_loop)
            self._thread.start()

    def _play_loop(self):
        while self.playing and SoundPlayer.current_sound == self and self.intensity > 0.0:
            self.sound.play()
            time.sleep(self.loop_interval)
            self.sound.stop()

    def stop(self):
        self.playing = False
        if self._thread:
            self._thread.join()
        if SoundPlayer.current_sound == self:
            SoundPlayer.current_sound = None

# Definindo instâncias para cada cor com base na precedência
class RedSound(SoundPlayer):
    def __init__(self):
        super().__init__("tools/sounds/A440.ogg", precedence=1)

class OrangeSound(SoundPlayer):
    def __init__(self):
        super().__init__("tools/sounds/Rhodes.ogg", precedence=2)

class YellowSound(SoundPlayer):
    def __init__(self):
        super().__init__("tools/sounds/Slick.ogg", precedence=3)

# Instancia o controlador dos sons
class SoundController:
    def __init__(self):
        self.red = RedSound()
        self.orange = OrangeSound()
        self.yellow = YellowSound()