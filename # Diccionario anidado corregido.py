# Diccionario anidado corregido
registro_mpu = {
    "0x3B": {"register_name": "ACCEL_XOUT_H", "bit_mask": "0xFF", "sampling_rate": 1000},
    "0x3D": {"register_name": "ACCEL_YOUT_L", "bit_mask": "0xE0", "sampling_rate": 1000},
    "0x6B": {"register_name": "PWR_MGMT_1", "bit_mask": "0x00 / 0x40", "sampling_rate": 100}
}

print("=== SISTEMA DE CONSULTA - SENSOR MPU6050 ===")

# Control numérico del ciclo
MAX_CONSULTAS = 3
intento = 0

while intento < MAX_CONSULTAS:
    intento += 1
    print(f"\n[Intento {intento} de {MAX_CONSULTAS}]")
    
    entrada = input("Ingrese dirección (ej. 0x3B) o nombre (ej. ACCEL_XOUT_H) o 'salir': ").strip()
    
    if entrada.lower() == 'salir':
        print("Saliendo del sistema...")
        break
        
    if entrada == "":
        print("Error: La entrada no puede estar vacía.")
        continue
        
    # 1. Búsqueda por método seguro .get() para direcciones
    datos = registro_mpu.get(entrada)
    
    if datos:
        print(f" Registro encontrado: {entrada}")
        print(f"- Nombre: {datos.get('register_name')}")
        print(f" - Máscara bits: {datos.get('bit_mask')}")
        print(f" - Frecuencia: {datos.get('sampling_rate')} Hz")
    else:
        # 2. Búsqueda por nombre de registro si no es dirección
        encontrado_por_nombre = False
        for direccion, info in registro_mpu.items():
            if info.get("register_name").lower() == entrada.lower():
                print(f" Registro encontrado por nombre: {entrada}")
                print(f" Dirección: {direccion}")
                print(f"Máscara bits: {info.get('bit_mask')}")
                print(f"Frecuencia: {info.get('sampling_rate')} Hz")
                encontrado_por_nombre = True
                break
                
        # 3. Consulta errónea controlada
        if not encontrado_por_nombre:
            print(f" ERROR: El registro '{entrada}' no existe en el mapa de memoria.")

print("\n FIN DEL SCRIPT")