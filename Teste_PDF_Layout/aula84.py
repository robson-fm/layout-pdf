from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def mp(mm):
    return mm/0.352777


pastaApp=os.path.dirname(__file__)

def criarPDF():
    try:
        cnv = canvas.Canvas(pastaApp+"\\TesteVisual.pdf",pagesize=A4)
        cnv.drawImage(pastaApp+"\\images.png",mp(2),mp(280),width=100, height=50)#logo superior do lado esquerdo
        # cnv.drawImage(pastaApp+"\\teste_background.png",mp(100),mp(100),width=100, height=200)


        cnv.drawImage(pastaApp+"\\img1.png",mp(175),mp(236),width=100, height=180)#imagem superior do lado direito


        cnv.drawImage(pastaApp+"\\img2.png",mp(182),mp(-1),width=80, height=140)#imagem inferior do lado direito

        cnv.drawImage(pastaApp+"\\img1.png",mp(-2),mp(-1),width=80, height=140)#imagem inferior do lado esquerda

        # cnv.drawImage(pastaApp+"\\img1.png",mp(175),mp(230),width=100, height=200)
        # cnv.drawImage(pastaApp+"\\img1.png",mp(158),mp(212),width=150, height=250)
        # cnv.drawImage(pastaApp+"\\img.jpg",mp(0),mp(207))
        # cnv.circle(mp(100), mp(100), mp(25))
        # cnv.drawString(mp(100),mp(100),"Título PDF")
        cnv.save()        
    except:
        messagebox.showinfo(title="Erro", message="Erro ao criar arquvio PDF")
        return
    messagebox.showinfo(title="PDF", message="PDF Criado")    

app=Tk()
app.title(" Testando Layout PDF")
app.geometry("600x450")

btn_criarPDF =Button(app, text="Criar PDF", command=criarPDF)
btn_criarPDF.pack(side="left", padx=10)

app.mainloop()


  