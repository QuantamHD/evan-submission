#include <stdio.h>
#include <stdint.h>

void xorshift32(uint32_t *state)
{
	/* Algorithm "xor" from p. 4 of Marsaglia, "Xorshift RNGs" */
	uint32_t x = *state;
	x ^= x << 13;
	x ^= x >> 17;
	x ^= x << 5;
	*state = x;
}

int main() {
    uint32_t seed = 1;
    for (int i = 0; i < 9; i++) {
        xorshift32(&seed);
        printf("state: %u, digit: %u\n", seed, seed % 10);
    }
    return 0;
}