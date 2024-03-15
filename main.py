import sys
import oracledb
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox 
from ui_login import Ui_login
from ui_cadastro import Ui_Cadastro
from PyQt5.QtCore import pyqtSignal 

class Login (QtWidgets.QWidget, Ui_login):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Sistema de Login")

        self.bnt_logar.clicked.connect(self.Logado)
        self.bt_wRegistrar.clicked.connect(self.abrirRegistrar)

        self.lineEdit_2.returnPressed.connect(self.bnt_logar.click)
        self.lineEdit.returnPressed.connect(self.bnt_logar.click)

    def Logado(self):
        QMessageBox.warning(self, 'Aviso', 'Você foi Logado com sucesso!')

    def abrirRegistrar(self):
        self.w = Cadastro()
        self.w.show()
        self.close()


class Cadastro (QtWidgets.QWidget, Ui_Cadastro):
    def __init__(self, parent=None):
        super(Cadastro, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Sistema de Cadastro")

        self.bnt_Cadastrar.clicked.connect(self.cadastrar)
        self.bt_pgLogar.clicked.connect(self.abrirLogin)

        self.input_confirmaSenha.returnPressed.connect(self.bnt_Cadastrar.click)
        self.input_senha.returnPressed.connect(self.bnt_Cadastrar.click)
        self.input_Email.returnPressed.connect(self.bnt_Cadastrar.click)
        self.input_user.returnPressed.connect(self.bnt_Cadastrar.click)


    def cadastrar(self):
        username = self.input_user.text()
        email = self.input_Email.text()
        senha = self.input_senha.text()
        confirma_senha = self.input_confirmaSenha.text()

        # Verifique se as senhas correspondem
        if senha != confirma_senha:
            QMessageBox.warning(self, 'Aviso', 'As senhas não correspondem!')
            return
        else:
            conn = None
            cursor = None
            # Insira os dados na tabela "cadastros" no banco de dados Oracle
            try:
                conn = oracledb.connect('system/oracle@localhost:1521/Cadastros')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO cadastros (username, email, senha) VALUES (:1, :2, :3)", (username, email, senha))
                conn.commit()
                QMessageBox.warning(self, 'Aviso', 'Cadastro realizado com sucesso!')
            except oracledb.Error as error:
                QMessageBox.warning(self, 'Erro', f'Ocorreu um erro ao cadastrar: {error}')
            finally:
                if cursor:
                    cursor.close()
                if conn:
                    conn.close()
            self.w = Login()
            self.w.show()
            self.close()

    def abrirLogin(self):
        self.w = Login()
        self.w.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    edit = Cadastro()
    login.show()
    sys.exit(app.exec_())