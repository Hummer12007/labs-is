#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    game = new Game();
    canvas_widget = new CanvasWidget(ui->frame);
    canvas_widget->setGame(game);
    canvas_widget->setGeometry(0, 0, 500, 500);
}

MainWindow::~MainWindow()
{
    delete ui;
}

