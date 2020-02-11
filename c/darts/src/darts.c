#include <math.h>
#include "darts.h"

uint8_t score(coordinate_t point) {
	float p = sqrt(pow(point.x, 2) + pow(point.y, 2));
	if (p > 10) {
		return 0;
	} else if (p > 5) {
		return 1;
	} else if (p > 1) {
		return 5;
	} else {
		return 10;
	}
}
