from django.db import models

# Create your models here.
class Usuario (models.Model):
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.nome
    
class Objeto (models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    quantidade_disponivel = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
    
class Emprestimo( models.Model):
    STATUS_CHOICE = [('pendente', 'Pendente'), ('devolvido', 'Devolvido')]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    objeto = models.ForeignKey(Objeto, on_delete=models.CASCADE)

    data_emprestimo = models.DateTimeField(auto_now_add=True)

    data_devolucao = models.DateTimeField(null=True, blank=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='pendente')

    def __str__ (self):
        return f"{self.usuario.nome} - {self.objeto.nome}"
