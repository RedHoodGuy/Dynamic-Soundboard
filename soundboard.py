from winsound import *
from tkinter import *
import sys
import os
import glob

top = Tk()
top.title('Mel Soundboard')
class MainWindow(Frame):
	
	def __init__(self, parent=None):
		Frame.__init__(self,parent)
		self.parent = parent
		#self.pack()
		self.convert_mp3_wav('mp3_files/')
		self.dynam_buttons()

	def dynam_buttons(self):
		m_buttons = []
		sounds = []
		y = 0
		x = 1
		i = 0
		for file in glob.glob(os.path.join("wav_files/", '*.wav')):
			#print (file)
			#print(resource_path(file))
			def get_sound(file):
				return lambda: PlaySound(resource_path(file), SND_FILENAME | SND_ASYNC)
			sound = get_sound(file)
			m_buttons.append(Button(top, text = file[10:-4], command = sound).grid(row=i, column=x, sticky=W, pady=(10,10), padx=(10,10)))
			if(x == 10):
				i = i + 1
				x = 0
			x = x + 1

	def convert_mp3_wav(self, path):
		for filename in glob.glob(os.path.join(path, '*.mp3')):
			"""Find every file in the directory "mp3" and convert 
			them to wav files and send them to "wav_files" directory"""
			name = str(filename)
			mp3_audio = AudioSegment.from_file(name)
			mp3_audio.export('wav_files/' + name[10:-4] + ".wav", format="wav")
			
def resource_path(relative_path):
		""" Get absolute path to resource, works for dev and for PyInstaller """
		try:
			# PyInstaller creates a temp folder and stores path in _MEIPASS
			base_path = sys._MEIPASS
		except Exception:
			#returns the cwd, for dev.
			base_path = os.path.abspath(".")

		return os.path.join(base_path, relative_path)

soundboard = MainWindow(top)
soundboard.mainloop()