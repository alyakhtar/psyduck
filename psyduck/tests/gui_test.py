from PyQt4 import QtGui, QtCore, uic
import sys

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	app.setStyle("cleanlooks")

	listwidget = QtGui.QListWidget()
	listwidget.show()

	sys.exit(app.exec_())