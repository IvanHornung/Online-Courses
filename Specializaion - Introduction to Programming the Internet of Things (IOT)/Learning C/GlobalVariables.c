int global_i;

void foo() {
    extern int global_i;
    global_i = a + b - c;
}

/*globals can be dangerous*/
void bar() {
    extern int global_i;
    x = global_i*2;
}
