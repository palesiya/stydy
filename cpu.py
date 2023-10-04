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
        "total": (info_mem.total / 1024),
        "available": (info_mem.available / 1024),
        "used": (info_mem.used / 1024)
    }
    # mem_1 = info["total"] / 1024
    # mem_2 = info["available"] / 1024
    # mem_3 = info["used"] / 1024
    # mem = {
    #     "total": mem_1,
    #     "available": mem_2,
    #     "used": mem_3
    # }
    return info


def get_pr_mem():
    info_m = psutil.virtual_memory()
    info = {"percent": info_m.percent}
    return info


def get_network():
    info_network = psutil.net_io_counters()
    network = {
        "bytes_sent": (info_network.bytes_sent / 1024),
        "bytes_recv": (info_network.bytes_recv / 1024)
    }
    # netw_1 = network["bytes_sent"] / 1024
    # netw_2 = network["bytes_recv"] / 1024
    # netw = {
    #     "bytes_sent": netw_1,
    #     "bytes_recv": netw_2
    # }
    return network


def get_process():
    procs = {p.pid: p.info for p in psutil.process_iter(['name', 'username'])}
    return procs


def process_show(proc_i):
    template = "\tЗапущенные процессы:"
    for pid in proc_i:
        if pid < 2000:
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
    Total memory{0:<13}{total:.2f}
    Available memory{0:<9}{available:.2f} 
    Used memory{0:<14}{used:.2f}
    ----------------------------------"""
    return tmpl.format(" ", **memory_i)


def proc_mem_show(mem_i):
    tmpl = """\tПроцент использования памяти (%):
    Percent memory{0:<11}{percent}
    ----------------------------------"""
    return tmpl.format(" ", **mem_i)


def network_show(network_i):
    tmpl = """\tКоличество отправленных и полученных килобайтов:
    Kilobytes sent{0:<11}{bytes_sent:.2f}
    Kilobytes received{0:<7}{bytes_recv:.2f}
    ----------------------------------"""
    return tmpl.format(" ", **network_i)


def send_file_cpu():
    try:
        with open("cpu_times.txt", "w", encoding="utf-8") as file:
            file.write(times_show(get_times()))
    except:
        print("ошибка при работе с файлом")


def send_file_mem():
    try:
        with open("virtual_memory.txt", "w", encoding="utf-8") as file:
                    file.write((memory_show(get_memory())))
    except:
        print("ошибка при работе с файлом")


def send_file_per():
    try:
        with open("percent_mem.txt", "w", encoding="utf-8") as file:
                    file.write(proc_mem_show(get_pr_mem()))
    except:
        print("ошибка при работе с файлом")


def send_file_netw():
    try:
        with open("network_counters.txt", "w", encoding="utf-8") as file:
                    file.write(network_show(get_network()))
    except:
        print("ошибка при работе с файлом")


def send_file_proc():
    try:
        with open("process_iter.txt", "w", encoding="utf-8") as file:
                    file.write(process_show(get_process()))
    except:
        print("ошибка при работе с файлом")


def main():
    print(times_show(get_times()))
    print(network_show(get_network()))
    print(memory_show(get_memory()))
    print(proc_mem_show(get_pr_mem()))
    print(process_show(get_process()))
    send_file_mem()
    send_file_per()
    send_file_netw()
    send_file_cpu()
    send_file_proc()

if __name__ == '__main__':
    main()


