# ch 4.2.1 main.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget
# 어플리케이션 핸들러와 빈 GUI 위젯

# QWidget 클래스를 상속받아서 클래스를 정의
class Calculator(QWidget):

    def __init__(self):
        super().__init__()      # 부모 클래스 QWidget을 초기화
        self.initUI()           

    def initUI(self):
        self.setWindowTitle('Calculator')   # 윈도우에 표시되는 타이틀
        self.resize(256, 256)               # 윈도우 사이즈
        self.show()                     # 윈도우 화면이 표시되도록 호출


if __name__ == "__main__":          # pypt는 어플리케이션당 1개의 QApplication이 필요함
    app = QApplication(sys.argv)    # QApplication 윈도우 인스턴스 생성
    view = Calculator()             # Calculator 윈도우 인스턴스 생성
    sys.exit(app.exec_())           # 어플리케이션 이벤트 처리를 하도록 루프 구동