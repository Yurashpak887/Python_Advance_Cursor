import psutil
from enum import Enum
import json, toml
import yaml

from flask import Flask, jsonify


methods = [
    'cpu_stats',
    'cpu_times',
    'cpu_times_percent',
    'datetime',
    'disk_io_counters',
    'disk_partitions',
    'disk_usage',
    'functools',
    'getloadavg',
    'long',
    'net_connections',
    'net_if_stats',
    'net_io_counters',
    'os', 'pid_exists',
    'pids',
    'process_iter',
    'sensors_battery',
    'sensors_fans',
    'sensors_temperatures',
    'signal',
    'subprocess',
    'swap_memory',

    'virtual_memory',
    'wait_procs']

def _parse_spec(spec):
    if hasattr(spec, '_asdict'):
        spec = spec._asdict()
    if isinstance(spec, dict):
        return {k:_parse_spec(v) for k,v in spec.items()}
    if isinstance(spec, list):
        return [_parse_spec(itm) for itm in spec]
    if isinstance(spec, Enum):
        return spec.name

    return spec

def type_to_json(result):
    return json.dumps(result)

def method_api(method, format='json'):
    spec = method()
    ret = _parse_spec(spec)
    if format.lower()=="json":
        result = type_to_json(ret)
    elif format.lower()=='toml':
        result = toml.dumps(ret)
    elif format.lower()=='yaml':
        result = yaml.dump(ret)
    return result

if __name__ == '__main__':
    print("File opened and executed successfully.")

    spec = psutil.sensors_battery()
    res = _parse_spec(spec)
    result = type_to_json(res)


