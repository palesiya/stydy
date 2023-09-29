import psutil


def get_times():
    info_times = psutil.cpu_times()
    info = {
        "user": info_times.user,
        "system": info_times.system,
        "idle": info_times.idle
    }
    return info


def get_memory():
    info_mem = psutil.virtual_memory()
    info = {
        "total": info_mem.total,
        "available": info_mem.available,
        #"percent": info_mem.percent,
        "used": info_mem.used
    }
    mem_1 = info["total"] / 1024
    mem_2 = info["available"] / 1024
    mem_3 = info["used"] / 1024
    return mem_1, mem_2, mem_3


def get_pr_mem():
    info_m = psutil.virtual_memory()
    info = {"percent": info_m.percent}
    return info


def get_network():
    info_network = psutil.net_io_counters()
    network = {
        "bytes_sent": info_network.bytes_sent,
        "bytes_recv": info_network.bytes_recv
    }
    netw_1 = network["bytes_sent"] / 1024
    netw_2 = network["bytes_recv"] / 1024
    return netw_1, netw_2


def get_process():
    procs = {p.pid: p.info for p in psutil.process_iter(['name', 'username'])}
    return procs


def process_show(proc_i):
    template = "\tЗапущенные процессы:"
    for pid in proc_i:
        if pid < 2000:
            #template += f"\n\tPid: {pid:<15} \n\tUsername: {proc_i[pid]['username']} \tName: {proc_i[pid]['name']}"
            template += "\n\tPid: {:<10} Name: {:<22} Username: {}".format(pid, proc_i[pid]["name"], proc_i[pid]['username'])
            pid +=1

    return template


def times_show(times_i):
    tmpl = """\t----------------------------------
    Время работы системного процессора (сек.):
    User time{0:<16}{user:.2f}
    System time{0:<14}{system:.2f}
    Idle time{0:<16}{idle:.2f}
    ----------------------------------"""
    return tmpl.format(" ", **times_i)


def memory_show(memory_i):
    tmpl = """\tИспользование системной памяти (килобайт):
    Total memory{0:<13}{1:.2f}
    Available memory{0:<9}{2:.2f} 
    Used memory{0:<14}{3:.2f}
    ----------------------------------"""
    return tmpl.format(" ", *memory_i)


def proc_mem_show(mem_i):
    tmpl = """\tПроцент использования памяти (%):
    Percent memory{0:<11}{percent}
    ----------------------------------"""
    return tmpl.format(" ", **mem_i)


def network_show(network_i):
    tmpl = """\tКоличество отправленных и полученных килобайтов:
    Kilobytes sent{0:<11}{1:.2f}
    Kilobytes received{0:<7}{2:.2f}
    ----------------------------------"""
    return tmpl.format("", *network_i)


def main():
    print(times_show(get_times()))
    print(network_show(get_network()))
    print(memory_show(get_memory()))
    print(proc_mem_show(get_pr_mem()))
    print(process_show(get_process()))


if __name__ == '__main__':
    main()
