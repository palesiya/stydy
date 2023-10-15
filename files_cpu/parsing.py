import psutil
from files_cpu import decors


@decors.log("cpu_times.json")
def get_times():
    info_times = psutil.cpu_times()
    info = {
        "user": info_times.user,
        "system": info_times.system,
        "idle": info_times.idle
    }
    return info


@decors.log("virtual_memory.json")
def get_memory():
    info_mem = psutil.virtual_memory()
    info = {
        "total": (info_mem.total / 1024),
        "available": (info_mem.available / 1024),
        "used": (info_mem.used / 1024)
    }
    return info


@decors.log("percent_mem.json")
def get_pr_mem():
    info_m = psutil.virtual_memory()
    info = {"percent": info_m.percent}
    return info


@decors.log("network_counters.json")
def get_network():
    info_network = psutil.net_io_counters()
    network = {
        "bytes_sent": (info_network.bytes_sent / 1024),
        "bytes_recv": (info_network.bytes_recv / 1024)
    }
    return network


@decors.log("process_iter.json")
def get_process():
    procs = {p.pid: p.info for p in psutil.process_iter(['name', 'username'])}
    return procs
