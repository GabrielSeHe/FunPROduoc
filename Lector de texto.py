def contarcaracteres(textoaleer, resumentexto):
    try:
        with open(textoaleer, 'r') as file:
            contenido = file.read()
            letras = sum(c.isalpha() for c in contenido)
            espacios = sum(c.isspace() for c in contenido)
            total = letras + espacios

        with open(resumentexto, 'w') as resumentext:
            resumentext.write(f"{textoaleer} tiene:\n")
            resumentext.write(f"letras: {letras}\n")
            resumentext.write(f"espacios: {espacios}\n")
            resumentext.write(f"Total: {total}\n")
            resumentext.write(f"ola profe")

        resumen = (
            f"resumen {textoaleer}:\n"
            f"letras: {letras}\n"
            f"espacios: {espacios}\n"
            f"total: {total}"
        )
        print(resumen)
        print(f"{resumentexto} generado")

    except FileNotFoundError:
        print(f"{textoaleer} no fue encontrado")

textoaleer = 'El retrato oval.txt' 
resumentexto = 'RESUMEN El retrato oval.txt'  

contarcaracteres(textoaleer, resumentexto)
