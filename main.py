import tkinter as tk
import sqlite3 as sq

connection = sq.connect('banco_cadastro.bd')
c = connection.cursor()

janela = tk.Tk()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS pessoa(nome varchar(80),cpf varchar(80))')
create_table()

def cria_janela_sucesso():
    janela2 = tk.Tk()
    janela2.geometry("50x50")
    janela2["bg"] = "green"
    tk.Label(janela2,text="Cadastrado.").pack()

def cria_janela_fracasso():
    janela3 = tk.Tk()
    janela3.geometry("50x50")
    janela3["bg"] = "red"
    tk.Label(janela3,text="Não cadastrado").pack()

def valores_invalidos():
    janela4 = tk.Tk()
    janela4.geometry("50x50")
    janela4["bg"] = "red"
    tk.Label(janela4,text="Valores inválidos.").pack()

def confirmar():
    sql = 'SELECT * FROM pessoa'
    nome = ed1.get()
    cpf = ed2.get()
    tem = False
    
    if len(nome) == 0 or len(cpf) == 0:
        valores_invalidos()
    else:
        for pessoa in c.execute(sql):
            if cpf == pessoa[1]:
                tem = True
        if tem:
            cria_janela_fracasso()
        else:
            c.execute('INSERT INTO pessoa (nome, cpf) VALUES (?,?)',
                      (nome,cpf))
            connection.commit()
            cria_janela_sucesso()

def ver_cadastros():
    janela5 = tk.Tk()
    janela5.title('Cadastros')
    cont = 1
    y = 5
    sql = 'SELECT * FROM pessoa'
    for pessoa in c.execute(sql):
        lb2 = tk.Label(janela5,text="")
        y+=20
        lb2.place(x = 5, y = y)
        lb2['text'] = str(cont)+'-Nome: '+pessoa[0] + ' Cpf: '+pessoa[1]
        cont+=1
    def ok():
        janela5.destroy()
    bt = tk.Button(janela5,width = 5,text='Ok',command=ok)
    bt.place(x = 70, y=y + 60)

def sair():
    janela.destroy()

lb1 = tk.Label(janela,text = "SISTEMA DE CADASTRO")
lb1.place(x=85, y = 20)

lb2 = tk.Label(janela,text="================")
lb2.place(x=85,y=35)

lb3 = tk.Label(janela,text = "NOME:")
lb3.place(x=35,y=80)

ed1 = tk.Entry(janela,width = 30)
ed1.place(x=80,y=80)

lb4 = tk.Label(janela,text="CPF:")
lb4.place(x=35,y=110)

ed2 = tk.Entry(janela,width=30)
ed2.place(x=65,y=110)

bt1 = tk.Button(janela,width = 10, text ="Confirmar",command=confirmar)
bt1.place(x=140, y = 150)
bt1.configure(bg='green')

bt2 = tk.Button(janela,width = 10, text="Ver cadastros",command=ver_cadastros)
bt2.place(x=50,y=150)
bt2.configure(bg = 'yellow')

bt3 = tk.Button(janela,width = 5, text = 'Sair',command=sair)
bt3.place(x = 230,y=150 )
bt3.configure(bg='red')

#Largura X Altura
janela.geometry("300x200")
janela.title('CADASTRO')
janela.mainloop()
