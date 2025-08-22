# doc_utils.py
import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtGui

def ensure_document(default_name="NEWFLANG"):
    """
    確保有開啟文件，若無則彈出對話框輸入名稱並建立新文件。
    """
    if App.ActiveDocument is None:
        # 建立輸入對話框
        dialog = QtGui.QInputDialog()
        dialog.setWindowTitle("建立新文件")
        dialog.setLabelText("請輸入新文件名稱：")
        dialog.setTextValue(default_name)
        dialog.resize(300, 100)

        # 顯示對話框並取得輸入值
        if dialog.exec_():
            doc_name = dialog.textValue()
        else:
            doc_name = default_name  # 使用者取消時仍建立預設文件

        App.newDocument(doc_name)
        Gui.activeDocument().activeView().viewAxometric()
        Gui.SendMsgToActiveView("ViewFit")

    return App.ActiveDocument