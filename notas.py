import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def obtener_ruta_descargas():
    """Obtiene la ruta de la carpeta de Descargas del usuario."""
    home = os.path.expanduser("~")
    if os.name == "nt": 
        return os.path.join(home, "Downloads")
    else:  
        return os.path.join(home, "Descargas")

def guardar_datos(nombre, cursos_notas):
   
    directorio = obtener_ruta_descargas()

   
    nombre_archivo = os.path.join(directorio, f"{nombre}_Reporte.pdf")
    
    doc = SimpleDocTemplate(nombre_archivo, pagesize=letter)
    elementos = []


    data = [
        ["Reporte de Notas"],
        ["Nombre del Estudiante", nombre],
        ["", "", ""],  
        ["No.", "Curso", "Nota"]
    ]
    

    for idx, (curso, nota) in enumerate(cursos_notas, start=1):
        data.append([str(idx), curso, nota])


    notas = [float(nota) for curso, nota in cursos_notas]
    promedio = sum(notas) / len(notas) if notas else 0
    data.append(["", "Promedio", f"{promedio:.2f}"])
    

    tabla = Table(data)
    

    estilo = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    tabla.setStyle(estilo)
    
    elementos.append(tabla)
    doc.build(elementos)
    
    messagebox.showinfo("Éxito", f"PDF guardado en {nombre_archivo}")

def registrar_notas():
    nombre = entrada_nombre.get()
    curso = entrada_curso.get()
    nota = entrada_nota.get()

    if not nombre or not curso or not nota:
        messagebox.showwarning("Advertencia", "Debe completar todos los campos.")
        return

    cursos_notas.append((curso, nota))
    entrada_curso.delete(0, tk.END)
    entrada_nota.delete(0, tk.END)

def generar_pdf():
    nombre = entrada_nombre.get()
    if not nombre or not cursos_notas:
        messagebox.showwarning("Advertencia", "Debe completar todos los campos y agregar al menos una nota.")
        return

    guardar_datos(nombre, cursos_notas)
    cursos_notas.clear()
    entrada_nombre.delete(0, tk.END)

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Registro de Notas")
ventana.geometry("500x400")
ventana.configure(bg="#e1f0f5")

cursos_notas = []


label_nombre = ttk.Label(ventana, text="Nombre del Estudiante:", background="#e1f0f5", font=("Helvetica", 12))
label_nombre.pack(pady=10)
entrada_nombre = ttk.Entry(ventana, width=30, font=("Helvetica", 12))
entrada_nombre.pack(pady=5)

label_curso = ttk.Label(ventana, text="Curso:", background="#e1f0f5", font=("Helvetica", 12))
label_curso.pack(pady=10)
entrada_curso = ttk.Entry(ventana, width=30, font=("Helvetica", 12))
entrada_curso.pack(pady=5)


label_nota = ttk.Label(ventana, text="Nota:", background="#e1f0f5", font=("Helvetica", 12))
label_nota.pack(pady=10)
entrada_nota = ttk.Entry(ventana, width=30, font=("Helvetica", 12))
entrada_nota.pack(pady=5)


boton_agregar = ttk.Button(ventana, text="Agregar Nota", command=registrar_notas)
boton_agregar.pack(pady=10)


boton_generar = ttk.Button(ventana, text="Generar PDF", command=generar_pdf)
boton_generar.pack(pady=20)

ventana.mainloop()
