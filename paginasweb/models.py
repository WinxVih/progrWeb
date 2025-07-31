from django.db import models
# Criação das classes para o modelo


class Camera(models.Model):
    ip = models.PositiveSmallIntegerField(default=0)
    status = models.CharField(max_length=100)
    def __str__(self):
        return f"IP: {self.ip} - Status: {self.status}"

class Sistema_Seguranca(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nome} ({self.localizacao})"


class Processador_IA(models.Model):
    modelo = models.CharField(max_length=100)
    confiabilidade = models.BooleanField(default=True)  


class Dispositivo_Automacao(models.Model):
    tipo = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)


class Notificacao(models.Model):
    tipo = models.CharField(max_length=100)
    def __str__(self):
        return f"Notificação: {self.tipo}"
    
