#include <math.h>

#include "resistor_color_trio.h"

resistor_value_t color_code(const resistor_band_t *c) {
  uint32_t result = (c[0] * 10 + c[1]) * pow(10, c[2]);
  if (result > KILOOHMS && result % KILOOHMS == 0) {
    return (resistor_value_t){result / KILOOHMS, KILOOHMS};
  }
  return (resistor_value_t){result, OHMS};
}
