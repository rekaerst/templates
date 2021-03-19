#include <qapplication.h>
#include <qboxlayout.h>
#include <qfile.h>
#include <qstylefactory.h>
#include <qlineedit.h>
#include <qmainwindow.h>
#include <qpushbutton.h>

int main(int argc, char* argv[]) {
	QApplication app(argc, argv);

	QMainWindow window;
	QWidget center;
	QHBoxLayout layout;
	QPushButton quit_btn("Quit");
	QLineEdit line_edit("Hello World!");

	QFile style_sheet("./style.css");
	style_sheet.open(QFile::ReadOnly);
	app.setStyleSheet(style_sheet.readAll());

	window.resize(320, 60);
	window.setWindowTitle("Greeting");

	line_edit.setReadOnly(true);
	layout.addWidget(&line_edit);

	QObject::connect(&quit_btn, &QPushButton::pressed, &QApplication::quit);
	layout.addWidget(&quit_btn);

	center.setLayout(&layout);
	window.setCentralWidget(&center);

	window.show();

	return app.exec();
}
