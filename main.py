import sys
from PyQt6.QtWidgets import QApplication
from models.tv_model import TVModel
from views.tv_view import TVRemoteView
from controllers.tv_controller import TVController

app = QApplication(sys.argv)
model = TVModel()
view = TVRemoteView()
controller = TVController(model, view)
view.show()
sys.exit(app.exec())
