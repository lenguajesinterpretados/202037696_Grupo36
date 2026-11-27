"""Tarea 2: Simulación de lógica de control de tanque hidroeléctrico."""

# Solicitar nivel inicial al usuario
nivel = int(input("Ingresa el nivel inicial del tanque (0-100): "))

monitoreo = True
ciclo = 0

print(f"\nNivel inicial: {nivel}%")
print("-" * 40)

# Bucle principal con límite de seguridad
while monitoreo and ciclo < 10:
    ciclo += 1
    
    # Caso 1: Interrupción por falla de sensor (0% o 100%)
    if nivel == 0 or nivel == 100:
        print(f"[Ciclo {ciclo}] ERROR: Falla de lectura del sensor")
        monitoreo = False
        break
    
    # Caso 2: Nivel bajo (< 15%) → Activar bomba
    elif nivel < 15:
        print(f"[Ciclo {ciclo}] Control: Bomba encendida - Nivel bajo ({nivel}%)")
        nivel += 5
    
    # Caso 3: Nivel normal (15% - 85%) → Operación normal
    elif nivel >= 15 and nivel <= 85:
        print(f"[Ciclo {ciclo}] Control: Operación hidráulica normal ({nivel}%)")
        nivel += 2
    
    # Caso 4: Nivel alto (> 85%) → Apagar bomba
    else:
        print(f"[Ciclo {ciclo}] Control: Bomba apagada - Tanque lleno ({nivel}%)")
        nivel -= 4

print("-" * 40)
print("Fin del monitoreo")
print(f"Nivel final: {nivel}%")