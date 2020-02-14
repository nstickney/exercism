#include "resistor_color.h"

resistor_band_t color_code(resistor_band_t c) { return c; }

resistor_band_t *colors() {
  static resistor_band_t colors[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  return colors;
}
