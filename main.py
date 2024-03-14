import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox

from ui_home import Ui_Form

class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui_home.ui', self)
        self.setWindowTitle("Bloqueador de Sites") 

        # Conectar os botões aos slots
        self.bt_adicionar.clicked.connect(self.adicionaUrl)
        self.bt_bloquear.clicked.connect(self.bloqueiaUrl)
        self.bt_desbloquear.clicked.connect(self.desbloqueiaUrl)
        self.bt_excluir.clicked.connect(self.excluiUrl)

        self.treeWidget.itemSelectionChanged.connect(self.selecionaUrl)

    def adicionaUrl(self):
        # Obter a URL do QLineEdit
        url = self.input_site.text()


        if url:
            item = QtWidgets.QTreeWidgetItem([url])
            item.setText(0, url)
            self.treeWidget.addTopLevelItem(item)
            self.input_site.clear()

        else:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Por favor, insira uma URL válida")

    
    def selecionaUrl(self):
        selected_item = self.treeWidget.currentItem()

        if selected_item:
            self.input_site.setText(selected_item.text(0))



    def bloqueiaUrl(self):
        selected_item = self.treeWidget.currentItem()

        if selected_item:
            with open(r'C:\\Windows\\System32\\drivers\\etc\\hosts', 'a') as file:
                file.write(f'\n127.0.0.1 {url}')

            bloquearUrl('exemplo.com')

    def desbloqueiaUrl(self):
        pass

    def excluiUrl(self):
        selected_item = self.treeWidget.currentItem()

        if selected_item:
            
            index = self.treeWidget.indexOfTopLevelItem(selected_item)

            self.treeWidget.takeTopLevelItem(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())