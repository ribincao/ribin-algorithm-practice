#include <semaphore.h>

class FooBar {
private:
    int n;
    sem_t fooDone, barDone;

public:
    FooBar(int n) {
        this->n = n;
        sem_init(&fooDone, 0, 0);
        sem_init(&barDone, 0, 1);
    }

    void foo(function<void()> printFoo) {
        
        for (int i = 0; i < n; i++) {
            sem_wait(&barDone);
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
            sem_post(&fooDone);
        }
    }

    void bar(function<void()> printBar) {
        
        for (int i = 0; i < n; i++) {
            sem_wait(&fooDone);
        	// printBar() outputs "bar". Do not change or remove this line.
        	printBar();
            sem_post(&barDone);
        }
    }
};