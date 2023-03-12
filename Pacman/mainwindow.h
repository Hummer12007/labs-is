#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QTime>
#include <QTimer>
#include "canvaswidget.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void timerTick();

private:
    Ui::MainWindow *ui;
    QTimer* timer;
    Game* game;
    CanvasWidget *canvas_widget;
};
#endif // MAINWINDOW_H
