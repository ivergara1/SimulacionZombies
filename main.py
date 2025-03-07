from simulacion import Simulation, ExpansionStrategy, MigrationStrategy

if __name__ == "__main__":

    def validate_input(mensaje, min_value=0, max_value=None, constructor=False):
        extra_message = "." if constructor else f" y debe ser un número entre {min_value} y {max_value}."
        while True:
            try:
                value = int(input(mensaje))
                if value < min_value or (max_value is not None and value > max_value):
                    raise ValueError
                return value
            except ValueError:
                print(f"Se debe ingresar un número válido{extra_message}")

    def main():
        while True:
            print("Menú principal")
            print("Elegir una opción:")
            print("1. Crear simulación")
            print("2. Cargar simulación")
            print("3. Salir")
            initial_action = input("Ingresar la opción: ")
            if initial_action == "1":
                x = validate_input("Ingresar número de pisos: ", constructor=True)
                m = validate_input("Ingresar número de filas por piso: ", constructor=True)
                n = validate_input("Ingresar número de columnas por piso: ", constructor=True)
                print("Elegir la manera en la que se mueven los zombies:")
                print("1. Expansion: Grupo infinito de zombies que se expande a las habitaciones adyacentes.")
                print("2. Migración: Grupo limitado de zombies en el que cada uno elige una habitación adyacente al azar para moverse.")
                strategy_choice = input("Ingresar la opción: ")
            
                if strategy_choice == "1":
                    strategy = ExpansionStrategy()
                elif strategy_choice == "2":
                    strategy = MigrationStrategy()
                else:
                    print("Input inválido. Se elige expansión por defecto.")
                    strategy = ExpansionStrategy()
                simulation = Simulation(x, m, n, strategy)
            
            elif initial_action == "2":
                nombre_archivo = input("Ingresar nombre del archivo guardado: ")
                nombre_archivo = f"simulaciones/{nombre_archivo}.json"
                try:
                    simulation = Simulation(0, 0, 0, ExpansionStrategy())
                    simulation.load_state(nombre_archivo)
                except FileNotFoundError:
                    print("El archivo con el nombre específicado no existe, volviendo al menú principal.")
                    continue

            elif initial_action == "3":
                print("Saliendo.")
                return
            else:
                print("Comando inválido, intentar de nuevo.")
                continue

            while True:
                print("Elegir una opción:")
                print("1. Mostrar estado")
                print("2. Avanzar turno")
                print("3. Añadir zombie")
                print("4. Eliminar zombies de una habitación")
                print("5. Reiniciar simulación")
                print("6. Guardar simulación")
                print("7. Volver al menú principal")
                
                choice = input("Elegir opción: ")
                
                if choice == "1":
                    simulation.show_state()
                elif choice == "2":
                    simulation.advance_turn()
                    print("Se avanzó un turno.\n")
                elif choice == "3":
                    f = validate_input("Ingresar índice del piso: ", max_value = x - 1)
                    r = validate_input("Ingresar índice de la fila: ", max_value = m - 1)
                    c = validate_input("Ingresar índice de la columns: ", max_value = n - 1)
                    if strategy_choice == "2":
                        count = validate_input("Ingresar número de zombies: ", min_value=1)
                    else:
                        count = 1
                    simulation.building.floors[f][r][c].add_zombie(count)
                    print("Se añadieron los zombies en la habitación.\n")
                elif choice == "4":
                    f = validate_input("Ingresar índice del piso: ", max_value = x - 1)
                    r = validate_input("Ingresar índice de la fila: ", max_value = m - 1)
                    c = validate_input("Ingresar índice de la columns: ", max_value = n - 1)
                    simulation.building.floors[f][r][c].remove_zombies()
                    print("Se eliminaron los zombies de la habitación. \n")
                elif choice == "5":
                    simulation.reset_building()
                    print("Se limpió el edificio.\n")
                elif choice == "6":
                    nombre_archivo = input("Ingresar nombre del archivo: ")
                    nombre_archivo = f"simulaciones/{nombre_archivo}.json"
                    simulation.save_state(nombre_archivo)
                    print("Se guardó la simulación.\n")
                elif choice == "7":
                    print("Volviendo al menú principal.")
                    break
                else:
                    print("Comando inválido, intentar de nuevo.")
    
    main()
