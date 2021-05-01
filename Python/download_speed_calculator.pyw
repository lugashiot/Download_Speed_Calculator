import sys, locale
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QFont, QKeyEvent
from PyQt5.Qt import Qt, QStyle, QStyleFactory
from darktheme.widget_template import DarkPalette

global x, y, speicherplatz, speed
locale.setlocale(locale.LC_ALL, 'de_AT')

class MainWindow(QWidget):
    def __init__(self, *__args):
        super().__init__()
        self.setWindowTitle('Download-Speed-Rechner')
        self.setFont(QFont('Verdana', 14))
        self.setWindowIcon(QIcon('icon.png'))
        self.setStyle(QStyleFactory.create('Fusion'))
        self.setPalette(DarkPalette())
        self.setStyleSheet("QToolTip { color: #ffffff; background-color: grey; border: 1px solid white; }")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter: 
            onCalculateClick()
        elif event.key() == Qt.Key_Return:
            onCalculateClick()

#def
def gb(): global x; x = 1024
def mb(): global x; x = 1
def mbit(): global y; y = 8
def mbyte(): global y; y = 1
def getspeicherpl(): global speicherplatz; speicherplatz = speicheredit.text()
def getspeed(): global speed; speed = speededit.text()
def onCalculateClick():
    try:
        dauersec = locale.atof(speicherplatz) * x / locale.atof(speed) * y
        dauermin = dauersec / 60
        dauerstd = dauermin / 60
        sekundenlabel.setText('{:.2f} Sekunden'.format(dauersec))
        minutenlabel.setText('{:.2f} Minuten'.format(dauermin))
        stundenlabel.setText('{:.2f} Stunden'.format(dauerstd))
    except:
        sekundenlabel.setText('Check your input!')

app = QApplication([])

#Buttons
rdbtn1 = QRadioButton('GB')
rdbtn2 = QRadioButton('MB')
rdbtn3 = QRadioButton('Mbit/s')
rdbtn4 = QRadioButton('MB/s')
rdbtn1.toggled.connect(lambda:gb())
rdbtn2.toggled.connect(lambda:mb())
rdbtn3.toggled.connect(lambda:mbit())
rdbtn4.toggled.connect(lambda:mbyte())
rdbtn1.setChecked(True)
rdbtn3.setChecked(True)
calculate = QPushButton('Calculate')
calculate.clicked.connect(onCalculateClick)

#Input Lines
speicheredit = QLineEdit()
speededit = QLineEdit()
speicheredit.editingFinished.connect(lambda:getspeicherpl())
speededit.editingFinished.connect(lambda:getspeed())

#Labels
outputlabel = QLabel('Verbleibende Zeit: ')
sekundenlabel = QLabel('0 Sekunden')
minutenlabel = QLabel('0 Minuten')
stundenlabel = QLabel('0 Stunden')

speicherwidg = QWidget()
speicherlay = QHBoxLayout()
dspeedwidg = QWidget()
dspeedlay = QHBoxLayout()

speicherlay.addWidget(speicheredit)
speicherlay.addWidget(rdbtn1)
speicherlay.addWidget(rdbtn2)
dspeedlay.addWidget(speededit)
dspeedlay.addWidget(rdbtn3)
dspeedlay.addWidget(rdbtn4)

speicherwidg.setLayout(speicherlay)
dspeedwidg.setLayout(dspeedlay)

#final construction
window = MainWindow()
vlayout = QVBoxLayout()
vlayout.addWidget(speicherwidg)
vlayout.addWidget(dspeedwidg)
vlayout.addWidget(calculate)
vlayout.addWidget(outputlabel)
vlayout.addWidget(sekundenlabel)
vlayout.addWidget(minutenlabel)
vlayout.addWidget(stundenlabel)
window.setLayout(vlayout)
#window.setGeometry(0, 0, 500, 300)
window.show()

sys.exit(app.exec())