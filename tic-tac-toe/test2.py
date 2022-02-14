import fnmatch
import os
print([f for f in os.listdir("C:\\Users\\LexaNoN\\PycharmProjects\\Tele-MRWN") if fnmatch.fnmatch(f, 'kino_ep5*')])