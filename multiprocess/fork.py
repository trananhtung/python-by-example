import os

pid_list = []


def main():
    pid_list.append(os.getpid())
    print("this is parent process, pid: ", pid_list[0])
    pid_child = os.fork()
    print("after fork, pid: ", os.getpid())

    print("pid_list: ", pid_list)
    print("pid_child: ", pid_child)


if __name__ == "__main__":
    main()
