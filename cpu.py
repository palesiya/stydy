import psutil
import json


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


def send_times_show(func):
    file_name = "times_show.json"

    def send_file_netw(*args):
        try:
            with open(file_name, "w") as log_file:
                log_file.write(json.dumps(get_times(), indent=4, ensure_ascii=False))
        except:
            print("ошибка при работе с файлом times_show")
    return send_file_netw


@send_times_show
def send_file_cpu():
    try:
        with open("cpu_times.txt", "w", encoding="utf-8") as file:
            file.write(times_show(get_times()))
    except:
        print("ошибка при работе с файлом")


def send_virtual_memory(func):
    file_name = "virtual_memory.json"

    def send_file_netw(*args):
        try:
            with open(file_name, "w") as log_file:
                log_file.write(json.dumps(get_memory(), indent=4, ensure_ascii=False))
        except:
            print("ошибка при работе с файлом virtual_memory")
    return send_file_netw


@send_virtual_memory
def send_file_mem():
    try:
        with open("virtual_memory.txt", "w", encoding="utf-8") as file:
                    file.write((memory_show(get_memory())))
    except:
        print("ошибка при работе с файлом")


def send_percent_mem(func):
    file_name = "percent_mem.json"

    def send_file_netw(*args):
        try:
            with open(file_name, "w") as log_file:
                log_file.write(json.dumps(get_pr_mem(), indent=4, ensure_ascii=False))
        except:
            print("ошибка при работе с файлом percent_mem")
    return send_file_netw


@send_percent_mem
def send_file_per():
    try:
        with open("percent_mem.txt", "w") as file:
                    file.write(proc_mem_show(get_pr_mem()))
    except:
        print("ошибка при работе с файлом")


def send_network_counters(func):
    file_name = "network_counters.json"

    def send_file_netw(*args):
        try:
            with open(file_name, "w") as log_file:
                log_file.write(json.dumps(get_network(), indent=4, ensure_ascii=False))
        except:
            print("ошибка при работе с файлом network_counters")
    return send_file_netw


@send_network_counters
def send_file_netw():
    try:
        with open("network_counters.txt", "w", encoding="utf-8") as file:
                    file.write(network_show(get_network()))
    except:
        print("ошибка при работе с файлом")


def send_process_log(func):
    file_name = "process_iter.json"

    def send_file_netw(*args):
        try:
            with open(file_name, "w", encoding="utf-8") as log_file:
                log_file.write(json.dumps(get_process(), indent=4, ensure_ascii=False))
        except:
            print("ошибка при работе с файлом process_iter")
    return send_file_netw


@send_process_log
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
    send_file_mem(memory_show(get_memory()))
    send_file_per(proc_mem_show(get_pr_mem()))
    send_file_netw(network_show(get_network()))
    send_file_cpu(times_show(get_times()))
    send_file_proc(process_show(get_process()))


if __name__ == '__main__':
    main()
