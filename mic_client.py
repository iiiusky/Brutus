import pyaudio
import socket
import select


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 4096

#HOST = "192.168.2.100"
HOST = "80.142.80.200"
PORT = 8082

audio = pyaudio.PyAudio()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def callback(in_data, frame_count, time_info, status):
    try:
        s.send(in_data)
        return (None, pyaudio.paContinue)
    except:
        return

try:
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, stream_callback=callback)
    while 1:
        pass
except:
    stream.close()
    audio.terminate()
    s.close()



