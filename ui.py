from PyQt5.QtWidgets import QApplication, QFileDialog, QPushButton, QVBoxLayout, QWidget

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Konwerter plików')
        layout = QVBoxLayout()
        
        self.btn_convert = QPushButton('Konwertuj', self)
        self.btn_convert.clicked.connect(self.convert)
        layout.addWidget(self.btn_convert)
        
        self.setLayout(layout)
    
    def convert(self):
        input_file, _ = QFileDialog.getOpenFileName(self, "Wybierz plik wejściowy")
        output_file, _ = QFileDialog.getSaveFileName(self, "Zapisz plik wyjściowy")
        if input_file and output_file:
            print(f"Konwersja: {input_file} -> {output_file}")

if __name__ == '__main__':
    app = QApplication([])
    ex = ConverterApp()
    ex.show()
    app.exec_()