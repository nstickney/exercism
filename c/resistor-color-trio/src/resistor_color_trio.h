#include <stdint.h>

#ifndef RESISTOR_COLOR_TRIO_H
#define RESISTOR_COLOR_TRIO_H

typedef enum {
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
} resistor_band_t;

typedef enum { OHMS = 1, KILOOHMS = 1000 } ohms;

typedef struct resistor_value_t {
  uint16_t value;
  ohms unit;
} resistor_value_t;

resistor_value_t color_code(const resistor_band_t *c);

#endif
