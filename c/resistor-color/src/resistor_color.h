#ifndef RESISTOR_COLOR_H
#define RESISTOR_COLOR_H

typedef int resistor_band_t;

enum color {
  BLACK,
  BROWN,
  RED,
  ORANGE,
  YELLOW,
  GREEN,
  BLUE,
  VIOLET,
  GREY,
  WHITE
};

resistor_band_t color_code(resistor_band_t c);

resistor_band_t *colors();

#endif
