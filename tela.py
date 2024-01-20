from tkinter import *
class App:
 def __init__(self):
  self.janela = Tk()
  self.tamanho = 1
  self.figura1Carregada = PhotoImage(file='tsi.png')
  self.figura1 = Label(self.janela)
  self.figura1['image']= self.figura1Carregada
  self.figura1.pack()
  self.botao1 = Button(self.janela,text='Muda Tamanho')
  self.botao1['command']=self.mudar
  self.botao1.pack()
  self.janela.mainloop()
 def mudar(self):
   if self.tamanho == 1:
      self.figura1Carregada = PhotoImage(file='tsi.png').subsample(2)
      self.tamanho = 2
   else:
      self.figura1Carregada = PhotoImage(file='tsi.png')
      self.tamanho = 1
      self.figura1['image']= self.figura1Carregada
aplicacao = App()
