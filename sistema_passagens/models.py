from django.db import models


class Aeroporto(models.Model):
    nome = models.CharField(max_length=150)
    codigo_iata = models.CharField(max_length=3, unique=True)
    cidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.codigo_iata} - {self.cidade}'

    class Meta:
        verbose_name = 'Aeroporto'
        verbose_name_plural = 'Aeroportos'


class Voo(models.Model):
    STATUS_CHOICES = [
        ('programado', 'Programado'),
        ('embarcando', 'Embarcando'),
        ('em_voo', 'Em Voo'),
        ('pousado', 'Pousado'),
        ('cancelado', 'Cancelado'),
    ]

    numero_voo = models.CharField(max_length=10, unique=True)
    origem = models.ForeignKey(Aeroporto, on_delete=models.PROTECT, related_name='voos_partida')
    destino = models.ForeignKey(Aeroporto, on_delete=models.PROTECT, related_name='voos_chegada')
    data_partida = models.DateTimeField()
    data_chegada = models.DateTimeField()
    capacidade = models.IntegerField()
    preco_base = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='programado')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Voo {self.numero_voo}: {self.origem.codigo_iata} -> {self.destino.codigo_iata}'

    class Meta:
        verbose_name = 'Voo'
        verbose_name_plural = 'Voos'


class Passagem(models.Model):
    CLASSE_CHOICES = [
        ('economica', 'Econômica'),
        ('executiva', 'Executiva'),
        ('primeira', 'Primeira Classe'),
    ]
    STATUS_CHOICES = [
        ('reservada', 'Reservada'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]

    voo = models.ForeignKey(Voo, on_delete=models.PROTECT, related_name='passagens')
    passageiro_nome = models.CharField(max_length=150)
    passageiro_cpf = models.CharField(max_length=14)
    assento = models.CharField(max_length=5)
    classe = models.CharField(max_length=20, choices=CLASSE_CHOICES, default='economica')
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='reservada')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Passagem {self.id} - {self.passageiro_nome} ({self.voo.numero_voo})'

    class Meta:
        verbose_name = 'Passagem'
        verbose_name_plural = 'Passagens'
