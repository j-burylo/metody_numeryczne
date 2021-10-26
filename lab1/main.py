import numpy as np
def cylinder_area(r:float,h:float):
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca
    """
    if r <= 0 or h <= 0:
        return np.NaN
    else:
        area = np.pi*r**2*h
    return area

def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    fib = [0, 1]
    if n <= 0:
        return None
    if isinstance(n, int):
        for i in range(2, n):
            fib.append(fib[i-1]+fib[i-2])
    else:
        return None
    return fib


def matrix_calculations(a:float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    if isinstance(a, int) or isinstance(a, float):
        a = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
        Mdet = np.linalg.det(a)
        if Mdet == 0:
            Minv = np.NaN
            return Minv
        else:
            Minv = np.invert(a)
            Mt = np.transpose(a)
            return Minv, Mdet, Mt
    else:
        return None

def custom_matrix(m:int, n:int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie 
    z opisem zadania 7.  
    
    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy  
    
    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if isinstance(m, int) and isinstance(n, int):
        if m <= 0 or n <= 0:
            return None
        else:
            custom_matrix = np.zeros((m, m))
            for i in range(m):
                for j in range(n):
                    if i > j:
                        custom_matrix[1][j] = i
                    else:
                        custom_matrix[i][j] = j
            return custom_matrix

    else:
        return None
