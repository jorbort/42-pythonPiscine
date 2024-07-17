import time
import sys

def display_progress(count, start_time, total) :
    """funcion para calcular y mostrar por antalla el porcentaje de la barra de carga"""
    elapsed_time = time.time() - start_time
    if elapsed_time > 0 :
        rate = count / elapsed_time
        eta = (total - count) / rate
    else:
        rate, eta = 0, 0
    bar_length = 50
    filled_length = int(bar_length * count // total)
    bar = '=' * filled_length + '>' + ' ' * (bar_length - filled_length -1)
    sys.stdout.write(f"\r{filled_length * 2}%|[{bar}]| {count}/{total} - ETA: {eta:.2f}s - {rate:.2f}it/s")
    sys.stdout.flush()

def ft_tqdm(lst : range) -> None:
    """funcion que muestra por consola un barrra de progreso"""
    total = len(lst)
    start_time = time.time()
    for count, item in enumerate(lst, 1):
        yield item
        display_progress(count, start_time,total)
    display_progress(total, start_time, total)
    sys.stdout.write('\n')
    sys.stdout.flush()

