#include "canvaswidget.h"
#include <QPainter>
#include <QDebug>

CanvasWidget::CanvasWidget(QWidget *parent) : QWidget(parent)
{
    wall_color = QColor(0, 0, 255, 255);
    coin_color = QColor(223, 201, 56, 255);
    cherry_color = QColor(255, 0, 0, 255);
    blank_color = QColor(0, 0, 0, 255);
    player_color = QColor(255, 255, 0, 255);
    ghost_color = QColor(255, 102, 255, 255);
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
    painter.fillRect(0, 0, field_dimensions.w, field_dimensions.h, wall_color);

   if(!game) return;
   auto* state = game->labyrinth_state;
   for (int y = 0; y < game->getHeight(); y++) {
       for (int x = 0; x < game->getWidth(); x++) {
           QColor color = state->isWall(x, y)? wall_color : blank_color;
           painter.fillRect(x * cell_dimensions.w, y * cell_dimensions.h,
                            cell_dimensions.w, cell_dimensions.h, color);
       }
   }
}
