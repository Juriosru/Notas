import tkinter as tk
import statistics

class EstadisticasNotas:
    def calcular_promedio(notas):
        return sum(notas) / len(notas)

    def calcular_desviacion(notas):
        return statistics.stdev(notas)

    def obtener_mayor(notas):
        return max(notas)

    def obtener_menor(notas):
        return min(notas)


class Notas:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Notas")
        self.ventana.geometry("280x380")
        self.ventana.configure(bg="gainsboro")
        self.ventana.resizable(False, False)

        self.entradas = []
        self.resultado_promedio = None
        self.resultado_desviacion = None
        self.resultado_mayor = None
        self.resultado_menor = None

        self.crear_interfaz()
        self.ventana.mainloop()

    def crear_interfaz(self):
        for i in range(5):
            etiqueta = tk.Label(self.ventana, text=f"Nota {i+1}:", bg="gainsboro")
            etiqueta.grid(row=i+2, column=0, pady=5)
            
            entrada = tk.Entry(self.ventana)
            entrada.grid(row=i+2, column=1, pady=5)
            self.entradas.append(entrada)

        boton_calcular = tk.Button(self.ventana, text="Calcular", command=self.calcular, bg="lime green")
        boton_calcular.grid(row=10, column=0, pady=20)

        boton_limpiar = tk.Button(self.ventana, text="Limpiar", command=self.limpiar, bg="red")
        boton_limpiar.grid(row=10, column=1, pady=20)

        self.resultado_promedio = tk.Label(self.ventana, text="Promedio:", bg="gainsboro")
        self.resultado_promedio.grid(row=14, column=0)

        self.resultado_desviacion = tk.Label(self.ventana, text="Desviación estándar:", bg="gainsboro")
        self.resultado_desviacion.grid(row=15, column=0)

        self.resultado_mayor = tk.Label(self.ventana, text="Valor mayor:", bg="gainsboro")
        self.resultado_mayor.grid(row=16, column=0)

        self.resultado_menor = tk.Label(self.ventana, text="Valor menor:", bg="gainsboro")
        self.resultado_menor.grid(row=17, column=0)

    def calcular(self):
        try:
            notas = [float(entry.get()) for entry in self.entradas]
            promedio = EstadisticasNotas.calcular_promedio(notas)
            desviacion = EstadisticasNotas.calcular_desviacion(notas)
            mayor = EstadisticasNotas.obtener_mayor(notas)
            menor = EstadisticasNotas.obtener_menor(notas)

            self.resultado_promedio.config(text=f"Promedio: {promedio:.2f}")
            self.resultado_desviacion.config(text=f"Desviación estándar: {desviacion:.2f}")
            self.resultado_mayor.config(text=f"Nota mayor: {mayor}")
            self.resultado_menor.config(text=f"Nota menor: {menor}")
        except ValueError:
            self.resultado_promedio.config(text="Error: ingrese solo números")

    def limpiar(self):
        for entry in self.entradas:
            entry.delete(0, tk.END)
        self.resultado_promedio.config(text="Promedio:")
        self.resultado_desviacion.config(text="Desviación estándar:")
        self.resultado_mayor.config(text="Valor mayor:")
        self.resultado_menor.config(text="Valor menor:")

class principal:
    def iniciar():
        if __name__ == "__main__":
            Notas()

principal.iniciar()