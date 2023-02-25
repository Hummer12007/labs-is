#ifndef CANVASWIDGET_H
#define CANVASWIDGET_H

#include <QWidget>
#include "labyrinthstate.h"
#include "game.h"
#include "utils/HelperStructs.h"

class CanvasWidget : public QWidget
{
    Q_OBJECT
public:
    explicit CanvasWidget(QWidget *parent = nullptr);
    void paintEvent(QPaintEvent * Event) override;
    void setGeometry(int ax, int ay, int aw, int ah);

    void setGame(Game* game) {
        this->game = game;
    }

private:
    Game* game;
    QColor wall_color;
    QColor coin_color;
    QColor cherry_color;
    QColor blank_color;
    QColor player_color;
    QColor ghost_color;

    Dimensions cell_dimensions;
    Dimensions field_dimensions;

signals:

};

#endif // CANVASWIDGET_H
