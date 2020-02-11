#include <math.h>
#include "armstrong_numbers.h"

int is_armstrong_number(int candidate) {
	int digits = 0;
	int sum = 0;
	for (int c = candidate; c > 0; c /= 10) {
		digits += 1;
	}
	for (int c = candidate; c > 0; c /= 10) {
		sum += (int) pow(c % 10, digits);
	}
	return sum == candidate;
}
