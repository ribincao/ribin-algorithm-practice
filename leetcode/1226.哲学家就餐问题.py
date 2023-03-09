from threading import Lock, Semaphore


class DiningPhilosophers:

    def __init__(self):
        self.lock = Lock()

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:

        self.lock.acquire()
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        self.lock.release()

from threading import Lock, Semaphore


class DiningPhilosophers:

    def __init__(self):
        self.sem = Semaphore(4)
        self.locks = [Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        left_fork, right_fork = philosopher, (philosopher + 1) % 5

        self.locks[left_fork].acquire()
        self.locks[right_fork].acquire()

        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()

        self.locks[left_fork].release()
        self.locks[right_fork].release()

from threading import Lock, Semaphore


class DiningPhilosophers:

    def __init__(self):
        self.lock = Lock()

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:

        self.lock.acquire()
        if self.lock.locked():
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()
            while self.lock.locked():
                self.lock.release()

