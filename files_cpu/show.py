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
