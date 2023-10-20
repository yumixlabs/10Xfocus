import pygame


# Initialize the pygame mixer
class Sound:
    def __init__(self):
        pygame.mixer.init()
        # Load a sound file
        sound_file = "ring1.mp3"
        sound = pygame.mixer.Sound(sound_file)
        # sound.set_volume(0.9)
        # Play the sound
        sound.play()
        # Wait for the sound to finish playing Below line must be applied
        pygame.time.wait(int(sound.get_length() * 1000))



