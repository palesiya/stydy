from files_cpu import show
from files_cpu import parsing


def main():
    print(show.times_show(parsing.get_times()))
    print(show.network_show(parsing.get_network()))
    print(show.memory_show(parsing.get_memory()))
    print(show.proc_mem_show(parsing.get_pr_mem()))
    print(show.process_show(parsing.get_process()))


if __name__ == '__main__':
    main()
