import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from Btree import Btree
import matplotlib.pyplot as plt


class AffichageGraphique(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'Arbre B'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 240
        self.initUI()
        
    def initUI(self):
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.label = QLabel(self)
        self.label.setText('Entrez une clé:')
        self.label.move(20, 20)
        
        self.textbox = QLineEdit(self)
        self.textbox.move(120, 20)
        self.textbox.resize(100, 25)
        
        self.insert_button = QPushButton('Insérer', self)
        self.insert_button.move(20, 60)
        self.insert_button.clicked.connect(self.on_insert_click)
        
        self.delete_button = QPushButton('Supprimer', self)
        self.delete_button.move(120, 60)
        self.delete_button.clicked.connect(self.on_delete_click)
        
        self.show()
        
        self.btree = Btree(2, 3) 
        
    def on_insert_click(self):
        value = int(self.textbox.text())
        self.btree.insert(value)
        image = self.btree.display()
        plt.imshow(image)
        plt.pause(1)
        print('Clé insérée:', value)
        
    def on_delete_click(self):
        value = int(self.textbox.text())
        self.btree.delete(value)
        image = self.btree.display()
        plt.imshow(image)
        plt.pause(1)
        print('Clé supprimée:', value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AffichageGraphique()
    sys.exit(app.exec_())
