# Funciones 
# Funcion para validar la clave
def validar_clave(clave):
    # validar su largo
    if(len(clave) < 6):
        return False;

    if not any(letra.isupper() for letra in clave):
        return False;
    if not any(letra.isdigit()for letra in clave):
        return False
    # validar espacios
    if(' ' in clave):
        return False;

    return True;           


# Función para inscribir participante
def inscribir_participante(inscripciones):
    nombre = input("Ingrese su nombre: ");
    if(nombre in inscripciones):
        print(f"Ya existe una inscripción del usuario {nombre}.");
        return;
    else:
        nivel = input("Ingrese el nivel (B - Basico, A -Avanzado): ").upper();
        if(nivel not in ['A', 'B']):
            print("Nivel no valido!");
            return;
        else:
            while True:
                clave = input("Ingrese la clave: ");
                if(not validar_clave(clave)):
                    print("Clave no valida. Clave no cumple con los requisitos.");
                    return;
                else:
                    inscripciones[nombre] = {'nivel': nivel, 'clave': clave};
                    print("Inscripcion exitosa!");
                    break;

# Funcion para consultar la inscripcion
def consultar_inscripcion(inscripciones):
    nombre = input("Ingrese su nombre: ");
    if(nombre in inscripciones):
        print(f"Nombre: {nombre}, Nivel: {inscripciones[nombre]['nivel']}, Clave: {inscripciones[nombre]['clave']}");
    else:
        print("Inscripción no encontrada!");

# Funcion para eliminar una inscripcion
def eliminar_inscripcion(inscripciones):
    nombre = input("Ingrese su nombre: ");
    if(nombre in inscripciones):
        del inscripciones[nombre];
        print("Inscripción eliminada exitosamente!");
    else:
        print("Inscripción no encontrada!");


def main():

    inscripciones = {};

    while True:
        print("***** MENU *****");
        print("1) Inscribir participante ");
        print("2) Consultar inscripcion");
        print("3) Eliminar Inscripción");
        print("4) Salir")

        opc = int(input("Ingrese una opción del menu: "));

        if(opc == 1):
            inscribir_participante(inscripciones);
        elif(opc == 2):
            consultar_inscripcion(inscripciones);
        elif(opc == 3):
            eliminar_inscripcion(inscripciones);
        elif(opc == 4):
            print("Programa terminado...");
            break;
        else:
            print("Opción no valida!");

if (__name__ == "__main__"):
    main();