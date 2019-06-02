from BackgroundSubtraction import Backgroundsub
from BlobDetection import Blobdetection
from datahandling import writetocsv
from datahandling import redim
from datahandling import datacleanse
from analysis import categorize
from analysis import determine_speed
import os

PATH1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sampledata', 'sync_1_1.mp4')
PATH2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sampledata', 'sync_2_1.mp4')

PATH3 = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sampledata', 'sync_1_1bgs.wmv')
PATH4 = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sampledata', 'sync_2_1bgs.wmv')

PATH5 = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sampledata', 'sync_1_og.csv')
PATH6 = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sampledata', 'sync_1_norm.csv')

''' 
Der folgende Code wurde so zusammengestellt, dass einfach die einzelnen Schritte des Programms nachvollzogen werden 
koennen. Fuer die entsprechenden Schritte koennen einfach die zugehoerigen Code-Segmente auskommentiert und
ausgefuerht werden
'''

# Background Subtraction auf beide Snippets anwenden und Output speichern
# bgs1 = Backgroundsub(PATH1)
# bgs1.savebgs()
# bgs2 = Backgroundsub(PATH2)
# bgs2.savebgs()

# Blob Detection auf beide BackSub Videos anwenden
# bd1 = Blobdetection(PATH3, True, True)
# trajectory1 = bd1.showbd()
# bd2 = Blobdetection(PATH4, True, False)
# trajectory2 = bd2.showbd()

# horizontale Flugbahn in CSV-Datei schreiben
# writetocsv(trajectory1, 'test.csv')
# vertikale Flugbahn kann nur von Hand bestimmt werden
# print(trajectory2)

# leere Frames in CSV ausfuellen
# datacleanse(PATH5)
# redim(PATH5)

# Klassifikation und Geschwindigkeit hinzufuegen
# categorize(PATH6)
# determine_speed(PATH5, PATH6)
