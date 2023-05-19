#include <stdio.h>
class X {
public:
	int m;
	int mf(int v) { int old = m; m = v; return old; }
};

X var;
var.m = 7;
int z = var.mf(9);
