from django.db import models

class Prestador(models.Model):
    nome = models.CharField(max_length=225, null=False, blank=False)
    sobrenome = models.CharField(max_length=225, null=False, blank=False)
    # Deixei a foto comentada por enquanto
    # foto = models.ImageField(upload_to='fotos_prestadores/', null=False, blank=False)
    servicos = models.CharField(max_length=225, null=False, blank=False)
    avaliacao = models.DecimalField(max_digits=3, decimal_places=1, default=0.00)
    telefone_principal = models.CharField(max_length=15, null=False, blank=False)
    telefone_opcional = models.CharField(max_length=15, null=True, blank=True)
    descricao = models.CharField(max_length=300, null=False, blank=False)

    
    def __str__(self):
        return f"{self.nome} {self.sobrenome} - {self.servicos}"