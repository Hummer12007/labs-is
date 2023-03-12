#include "canvaswidget.h"
#include <QPainter>
#include <QDebug>

CanvasWidget::CanvasWidget(QWidget *parent) : QWidget(parent)
{
    wall_color = QColor(56, 56, 172, 255);
    coin_color = QColor(223, 201, 56, 255);
    cherry_color = QColor(255, 0, 0, 255);
    blank_color = QColor(56, 56, 56, 255);
    player_color = QColor(255, 255, 0, 255);
    ghost_color = QColor(255, 102, 255, 255);
    padding_color = QColor(56, 56, 128, 255);
}

// override
void CanvasWidget::setGeometry(int ax, int ay, int aw, int ah) {
   QWidget::setGeometry(ax, ay, aw, ah);
   field_dimensions = Dimensions(this->geometry().width(), this->geometry().height());
   qDebug() << "field dims: " << field_dimensions.w << " " << field_dimensions.h;
   cell_dimensions = Dimensions(field_dimensions.w / game->getWidth(),
                                field_dimensions.h / game->getHeight());
}

void CanvasWidget::paintEvent(QPaintEvent*) {
    QPainter painter(this);
    painter.fillRect(0, 0, field_dimensions.w, field_dimensions.h, padding_color);

    if(!game) return;
    auto* state = game->labyrinth_state;
    const auto PADDING = 2;
    for (int y = 0; y < game->getHeight(); y++) {
        for (int x = 0; x < game->getWidth(); x++) {
            QColor color;
            switch (state->getTile(x, y)) {
                case Tile::Wall  : color = wall_color  ; break;
                case Tile::Blank : color = blank_color ; break;
                case Tile::Coin  : color = coin_color  ; break;
                case Tile::Player: color = player_color; break;
                case Tile::Ghost : color = ghost_color ; break;
                case Tile::Cherry: color = cherry_color; break;
                default: assert(false);
            }
            painter.fillRect(PADDING + x * cell_dimensions.w, PADDING + y * cell_dimensions.h,
                            cell_dimensions.w - PADDING, cell_dimensions.h - PADDING, color);
        }
    }
}
