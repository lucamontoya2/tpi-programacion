# CONSIGNA 1: 


a= {101, 102, 103, 104, 105, 106}
b= {104, 105, 106, 107, 108}
c= {102, 105, 109}

print("Conjunto A:", a)
print("Conjunto B:", b)
print("Conjunto C:", c)

# ================================
# PARTE A - Analisis con conjuntos.
# ================================

# 1. calcular e interpretar:
plataformas2= a and b 
print("Usuarios que utilizan ambas plataformas:",plataformas2)

plataforma1= a or b
print("Usuarios que utilizan al menos una plataforma:", plataforma1)

usuariosSinErrores= ((a and b) - c)
print("Usuarios que utilizan la plataforma, pero no presentan errores:",usuariosSinErrores)

usuariosExclusivos= (a - b) or (b-a)
print("Usuarios que utilizan exclusivamente una sola plataforma:",usuariosExclusivos)

# 2. Expresar al menos dos resultados usando comprensión de conjuntos.

# Guarda los elementos que estan en a y tambien b
ambasPlataformas=[]
for x in a:
    if x in b:
        ambasPlataformas.append(x)
print("Usuarios que utilizan ambas plataformas:",ambasPlataformas)

unicaPlataforma=[]
for x in a:
    if x not in b:
        unicaPlataforma.append(x)
for x in b:
    if x not in a:
        unicaPlataforma.append(x)
print("Usuarios que utilizan al menos una plataforma:",unicaPlataforma)

# 3. Dectectar: Usuarios que aparecen en 𝐶 pero no en 𝐴 ∪ 𝐵

usuariosC= c - plataformas2
print("Usuarios que aparecen en 𝐶 pero no en 𝐴 ∪ 𝐵:",usuariosC)

# =============================
# PARTE B - LOGICA PROPOSICIONAL
# =============================

# 4. definir p, q y r.

todos = a or b or c 

criticos = []
no_criticos = []

for usuario in todos:

    p = usuario in a
    q = usuario in b
    r = usuario in c

    if (p or q) and r:
        criticos.append(usuario)

    else:
        no_criticos.append(usuario)

print("\nUsuarios críticos:")
print(criticos)

print("\nUsuarios no críticos:")
print(no_criticos)

# 5. Construir la tabla de verdad.
print('\nTabla de verdad para (p or q) and r:')
print('p q r | resultado')

tabla_verdad = []
for p in (False, True):
    for q in (False, True):
        for r in (False, True):
            resultado = (p or q) and r
            tabla_verdad.append((p, q, r, resultado))
            print(int(p), int(q), int(r), '|', int(resultado))

# 7. Clasificar los usuarios del dataset en: criticos o no criticos.

# Ya se clasificaron en el punto 4, utilizando la lógica proposicional.

# =========================
# PARTE C - INTERPRETACION
# =========================

# Ya hecho en los puntos anteriores, interpretando cada resultado a medida que se obtenía.




 
