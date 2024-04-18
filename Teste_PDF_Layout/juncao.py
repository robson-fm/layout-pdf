from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle
import datetime
import numpy as np

def gerar_pdf(tipo):
    styles = getSampleStyleSheet()
    GRID_STYLE = TableStyle(
                [('GRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('ALIGN', (1, 0), (-1, -1), 'RIGHT')])
    
    GRID_STYLE2 = TableStyle(
                [('GRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('ALIGN', (1, 0), (-1, -1), 'RIGHT')])
    
    GRID_STYLE3 = TableStyle(
                [('GRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('ALIGN', (1, 0), (-1, -1), 'RIGHT')])
    
    # Resto do seu código...
    # (Coloquei o restante do código da função gerar_pdf aqui)
    

 # criando a lista tabela e colocando os valores iniciais
    tabela_padrao = []
    tag_tabela_padrao = []
    tabela_padrao.append(["Descrição","Valor","Data"])
    tag_tabela_padrao.append(["ok"])

    tabela_linear = []
    tag_tabela_linear = []
    tabela_linear.append(["Descrição","Valor","Data"])
    tag_tabela_linear.append(["ok"])

        # inserindo valores e suas respectivas tags nas listas
    for child in tabela_parcelas_padrao.get_children():
        tabela_padrao.append(tabela_parcelas_padrao.item(child)["values"])
        tag_tabela_padrao.append(tabela_parcelas_padrao.item(child)["tags"])

    for child in tabela_parcelas_linear.get_children():
        tabela_linear.append(tabela_parcelas_linear.item(child)["values"])
        tag_tabela_linear.append(tabela_parcelas_linear.item(child)["tags"])

        style = styles["Normal"]

        # criando uma table para o documento
        t1 = Table(np.array(tabela_padrao).tolist())
        t2 = Table(np.array(lista_cef_padrao).tolist())
        t3 = Table(np.array(tabela_linear).tolist())
        t4 = Table(np.array(lista_cef).tolist())
        index = 0

        # laço for para colocar a cor na tabela do documento com  base na tag da linha
        for row in range(len(tabela_padrao)):
            taglida =  str(tag_tabela_padrao[index])
            if taglida == "['limite']":
                GRID_STYLE.add('BACKGROUND', (0, row), (-1, row), colors.red)
            elif taglida == "['aviso']":
                GRID_STYLE.add('BACKGROUND', (0, row), (-1, row), colors.yellow)
            index += 1
            
        index = 0
        for row in range(len(tabela_linear)):
            taglida =  str(tag_tabela_linear[index])
            if taglida == "['limite']":
                GRID_STYLE3.add('BACKGROUND', (0, row), (-1, row), colors.red)
            elif taglida == "['aviso']":
                GRID_STYLE3.add('BACKGROUND', (0, row), (-1, row), colors.yellow)
            index += 1
        element = []
        # definido variaveis para texto no arquivo
        falta_text  = label_falta_pagar.cget("text") + " "
        soma_text  = label_soma_parcelas.cget("text") + " "
        usuario = getlogin()

        # defindo nome do arquivo como data e hora atual
        data = datetime.datetime.now()
        nome = str(data.strftime("%Y_%b_%d__%H_%M_%S")) + ".pdf"

        # criando documento
        doc = SimpleDocTemplate(nome, pagesize=letter, rightMargin=3 * cm, 
                                leftMargin=6.5 * cm, topMargin=2 * cm, bottomMargin=0)

        # inserindo dados da unidade no documento
        funcoes.inserir_elementos(element,style,"Vendedor(a): ", usuario)
        funcoes.inserir_elementos(element,style,"Empreendimento: ", dados_unidade.Empreendimento)
        funcoes.inserir_elementos(element,style,"Unidade: ", dados_unidade.Unidade)
        funcoes.inserir_elementos(element,style,"Renda do Cliente: ", funcoes.converter_real(renda))
        funcoes.inserir_elementos(element,style,"Capacidade de Pagto do Cliente: ", funcoes.converter_real(
            float(valor_capacidade)))
        funcoes.inserir_elementos(element,style,"Valor de Avaliação: ", dados_unidade.Valor_Avaliacao)
        funcoes.inserir_elementos(element,style,"Valor com Desconto: ", dados_unidade.Valor_Desconto)
        funcoes.inserir_elementos(element,style,"Valor Finaciado: ", dados_unidade.Financiamento)
        funcoes.inserir_elementos(element,style,"Pro Soluto: ", funcoes.converter_real(valor_pro_soluto))
        funcoes.inserir_elementos(element,style,"Data de Entrega: ", dados_unidade.Data_Entrega)
        t1.setStyle(GRID_STYLE)
        element.append(t1)
        element.append(Spacer(1,12))
        t2.setStyle(GRID_STYLE2)
        element.append(t2)
        element.append(Spacer(1,12))
        if tipo == "linear":
            t3.setStyle(GRID_STYLE3)
            element.append(t3)
            element.append(Spacer(1,12))
            t4.setStyle(GRID_STYLE2)
            element.append(t4)
            element.append(Spacer(1,12))
            funcoes.inserir_elementos(element,style, falta_text, entry_falta_pagar.get())
            element.append(Spacer(1,12))
            funcoes.inserir_elementos(element,style, soma_text, entry_soma_parcelas.get())
            element.append(Spacer(1,12))






    # Texto Exclusivo para o Jurídico
    texto_jurídico = '''
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute 
                    irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.***'''

    texto_jurídico_2 = '''
                    ***Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute 
                    irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.***'''

    element.append(Spacer(1, 12))
    funcoes.inserir_elementos(element, style, "\n\n***ESTE TEXTO É RESERVADO PARA O TEXTO DO JURÍDICO: \n\n", texto_jurídico)
    
    element.append(Spacer(1, 12))
    funcoes.inserir_elementos(element, style, " ", texto_jurídico_2)

    # Código para adicionar imagens ao PDF
    nome_pdf = "nome_do_seu_pdf.pdf"  # Substitua "nome_do_seu_pdf.pdf" pelo nome desejado para o PDF
    cnv = canvas.Canvas(nome_pdf, pagesize=letter, rightMargin=3 * cm, leftMargin=6.5 * cm, topMargin=2 * cm, bottomMargin=0)
    cnv.drawImage("caminho_da_sua_imagem1.png", 100, 100, width=100, height=50)  # Substitua "caminho_da_sua_imagem1.png" pelo caminho da sua primeira imagem
    cnv.drawImage("caminho_da_sua_imagem2.png", 200, 200, width=100, height=50)  # Substitua "caminho_da_sua_imagem2.png" pelo caminho da sua segunda imagem
    # Adicione quantas imagens desejar, ajustando as posições conforme necessário
    cnv.save()

# Exemplo de chamada da função
gerar_pdf("linear")
