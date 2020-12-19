from pytube import YouTube
import os
from tkinter import *


YouTube('https://youtu.be/iszwuX1AK6A').streams.first().download()
