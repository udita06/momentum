from playsound import playsound
import os

class FocusSounds:
    def __init__(self):
        self.current_sound = None

    def play_sound(self, sound_file):
        if self.current_sound:
            self.stop_sound()
        self.current_sound = sound_file
        playsound(sound_file)

    def stop_sound(self):
        if self.current_sound:
            # Stopping sound is not directly supported by playsound,
            # so we can implement a workaround or use another library.
            # Here we just reset the current sound.
            self.current_sound = None

    def pause_sound(self):
        # Pausing functionality would require a different audio library
        # that supports pause and resume. This is a placeholder.
        pass

    def list_sounds(self):
        # List available sounds in a predefined directory
        sound_directory = "sounds"  # Adjust the path as necessary
        return [f for f in os.listdir(sound_directory) if f.endswith('.mp3') or f.endswith('.wav')]