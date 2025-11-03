def load_audio(file_path):
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)

def play_audio():
    import pygame
    pygame.mixer.music.play()

def pause_audio():
    import pygame
    pygame.mixer.music.pause()

def stop_audio():
    import pygame
    pygame.mixer.music.stop()

def set_volume(volume):
    import pygame
    pygame.mixer.music.set_volume(volume)