#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <QTimer>
#include <cassert>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    timer = new QTimer(this);
    connect(timer, SIGNAL(timeout()), this, SLOT(timerTick()));
    timer->start(150);
    game = new Game();
    canvas_widget = new CanvasWidget(ui->frame);
    canvas_widget->setGame(game);
    canvas_widget->setGeometry(0, 0, game->WIDTH * 40, game->HEIGHT * 40);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::timerTick() {
    this->game->flipTile();
    // this->game->labyrinth_state->setTile(0, 0, Tile::Cherry);
    if (this->game->labyrinth_state->num_coins() < 0) {
        if (!this->game->labyrinth_state->spawn_coin({})) {
            assert(false);
        }
    }

    this->game->pacman->nextStep();

    update();
    return;
}

