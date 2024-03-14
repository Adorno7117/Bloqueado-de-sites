# OBIJETIVO: adiconar,bloquear,desbloquear, excluir uma url

import sys
from PyQt5 import QtWidgets
from ui_home import Ui_bloq 
from PyQt5.QtWidgets import QMessageBox

class Princpal (QtWidgets.QMainWindow, Ui_bloq):
    def __init__(self, parent=None):
        super(Princpal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Sistema bloqueador de sites")
        
        #botões
        self.bt_adicionar.clicked.connect(self.adicionaUrl)
        self.bt_bloquear.clicked.connect(self.bloqueiaUrl)
        self.bt_desbloquear.clicked.connect(self.desbloqueiaUrl)
        self.bt_excluir.clicked.connect(self.excluiUrl)



    def adicionaUrl(self):
        url = self.input_site.text()
        if url:
            self.listWidget_urls.addItem(url)
        else:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Por favor, insira uma URL válida")

    
    def bloqueiaUrl(self):
        pass

    
    def desbloqueiaUrl(self):
        pass
    
    def excluiUrl(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Princpal()
    window.show()
    sys.exit(app.exec_())