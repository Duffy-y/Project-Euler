from itertools import count
from tkinter import HORIZONTAL
import numpy as np
from enum import Enum
import time

start = time.time_ns()

data = "7 53 183 439 863 497 383 563 79 973 287 63 343 169 583 627 343 773 959 943 767 473 103 699 303 957 703 583 639 913 447 283 463 29 23 487 463 993 119 883 327 493 423 159 743 217 623 3 399 853 407 103 983 89 463 290 516 212 462 350 960 376 682 962 300 780 486 502 912 800 250 346 172 812 350 870 456 192 162 593 473 915 45 989 873 823 965 425 329 803 973 965 905 919 133 673 665 235 509 613 673 815 165 992 326 322 148 972 962 286 255 941 541 265 323 925 281 601 95 973 445 721 11 525 473 65 511 164 138 672 18 428 154 448 848 414 456 310 312 798 104 566 520 302 248 694 976 430 392 198 184 829 373 181 631 101 969 613 840 740 778 458 284 760 390 821 461 843 513 17 901 711 993 293 157 274 94 192 156 574 34 124 4 878 450 476 712 914 838 669 875 299 823 329 699 815 559 813 459 522 788 168 586 966 232 308 833 251 631 107 813 883 451 509 615 77 281 613 459 205 380 274 302 35 805"
data_test = "7 53 183 439 863 497 383 563 79 973 287 63 343 169 583 627 343 773 959 943 767 473 103 699 303"

size = (15, 15)

matrix = [int(val) for val in data.split(" ")]
matrix = np.array(matrix)
matrix = np.reshape(matrix, size)

order = np.zeros(size)

def get_index(value_to_index, arr):
  index = 1
  for val in arr:
    if val > value_to_index:
      index += 1

  return index

for x in range(size[1]):
  for y in range(size[0]):
    order[y, x] = get_index(matrix[y, x], matrix[:,x])

column_delta = [0] * size[1]
value_to_select = [0] * size[1]
row_to_elimate_if_selected = [None] * size[0]
column_to_eliminate_if_selected = [None] * size[0]
eliminated_row = []
eliminated_column = []

selected_values = []

for i in range(size[1]):
    for x in range(size[1]):
        if x in eliminated_column:
            continue

        column: np.ndarray = list(matrix[:, x])

        # Keeps available values
        for row in eliminated_row:
            column[row] = 0 # keeps the order

        arg_max = np.argmax(column)
        row_to_elimate_if_selected[x] = arg_max
        value_to_select[x] = column[arg_max]
        sorted = np.sort(column)
        column_delta[x] = sorted[-1] - sorted[-2]

    column_to_select = np.argmax(column_delta)
    value = value_to_select[column_to_select]
    selected_values.append(value)
    eliminated_row.append(row_to_elimate_if_selected[column_to_select])
    eliminated_column.append(column_to_select)

    # print(eliminated_row)
    # print(eliminated_column)
    # print(column_delta)
    # print(f"Selected value: {selected_values}")
    # print()

    column_delta = [0] * size[1]
    row_to_elimate_if_selected = [None] * size[0]
    column_to_eliminate_if_selected = [None] * size[0]

end = time.time_ns()

print(f"Elapsed time = {(end-start) * 10**(-9)}s")

print(sum(selected_values))





        
