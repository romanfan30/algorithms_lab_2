import BST
import AVL
import RB
import matplotlib.pyplot as plt
import random
import math

x_bst = []
y_bst = []
Tree1 = BST.BST()

x_avl = []
y_avl = []
Tree2 = AVL.AVL()

x_rb = []
y_rb = []
Tree_rb = RB.RB()

number_of_elements = 30000
unique_random_numbers = random.sample(range(number_of_elements), number_of_elements)


#ГРАФИК BST
print("Заполнение BST дерева...")
for n in range(number_of_elements):
    x_bst.append(n)
    Tree1.insert(unique_random_numbers[n])
    y_bst.append(Tree1.getheight())

plt.figure(figsize=(10, 5))
plt.plot(x_bst, y_bst, label="h(n) BST", color='blue', alpha=0.7)
plt.xlabel("n - количество элементов")
plt.ylabel("h - высота дерева")
plt.title("BST дерево (случайные элементы)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()


#ГРАФИК AVL RANDOM
print("Заполнение AVL дерева...")
for n in range(number_of_elements):
    x_avl.append(n)
    Tree2.insert(unique_random_numbers[n])
    y_avl.append(Tree2.get_tree_height())

h_min_avl = []
h_max_avl = []
for n in range(1, number_of_elements + 1):
    h_min_avl.append(math.log2(n + 1))
    h_max_avl.append(1.44 * math.log2(n + 1))

plt.figure(figsize=(10, 5))
plt.plot(x_avl, y_avl, label="h(n) AVL", color='green', alpha=0.7)
plt.plot(x_avl, h_min_avl, label="Нижняя граница", color='orange', linestyle='--')
plt.plot(x_avl, h_max_avl, label="Верхняя граница", color='orange', linestyle='--')
plt.xlabel("n - количество элементов")
plt.ylabel("h - высота дерева")
plt.title("AVL дерево (случайные элементы)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()


#ГРАФИК AVL SORTED
Tree3 = AVL.AVL()
x_avl_sorted = []
y_avl_sorted = []

print("Заполнение AVL дерева возрастающими ключами...")
for n in range(number_of_elements):
    x_avl_sorted.append(n)
    Tree3.insert(n)
    y_avl_sorted.append(Tree3.get_tree_height())

plt.figure(figsize=(10, 5))
plt.plot(x_avl_sorted, y_avl_sorted,
         label="h(n) AVL (sorted insert)", color='green')
plt.plot(x_avl_sorted, h_min_avl,
         label="Нижняя граница", color='orange', linestyle='--')
plt.plot(x_avl_sorted, h_max_avl,
         label="Верхняя граница", color='orange', linestyle='--')

plt.xlabel("n - количество элементов")
plt.ylabel("h - высота дерева")
plt.title("AVL дерево при монотонно возрастающей последовательности вставки")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()


#ГРАФИК RB RANDOM
print("Заполнение RB дерева случайными элементами...")
for n in range(number_of_elements):
    x_rb.append(n)
    Tree_rb.insert(unique_random_numbers[n])
    y_rb.append(Tree_rb.get_tree_height())

h_min_rb = []
h_max_rb = []
for n in range(1, number_of_elements + 1):
    h_min_rb.append(math.log2(n + 1))
    h_max_rb.append(2 * math.log2(n + 1))

plt.figure(figsize=(10, 5))
plt.plot(x_rb, y_rb, label="h(n) RB", color='green', alpha=0.7)
plt.plot(x_rb, h_min_rb, label="Нижняя граница", color='orange', linestyle='--')
plt.plot(x_rb, h_max_rb, label="Верхняя граница", color='orange', linestyle='--')
plt.xlabel("n - количество элементов")
plt.ylabel("h - высота дерева")
plt.title("Красно-чёрное дерево (случайные элементы)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()


#ГРАФИК RB SORTED
Tree_rb_sorted = RB.RB()
x_rb_sorted = []
y_rb_sorted = []

print("Заполнение RB дерева возрастающими ключами...")
for n in range(number_of_elements):
    x_rb_sorted.append(n)
    Tree_rb_sorted.insert(n)
    y_rb_sorted.append(Tree_rb_sorted.get_tree_height())

plt.figure(figsize=(10, 5))
plt.plot(x_rb_sorted, y_rb_sorted,
         label="h(n) RB (sorted insert)", color='green')
plt.plot(x_rb_sorted, h_min_rb,
         label="Нижняя граница", color='orange', linestyle='--')
plt.plot(x_rb_sorted, h_max_rb,
         label="Верхняя граница", color='orange', linestyle='--')

plt.xlabel("n - количество элементов")
plt.ylabel("h - высота дерева")
plt.title("Красно-чёрное дерево при монотонно возрастающей последовательности вставки")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()