from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Veiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='veiculos')
    placa = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.CharField(max_length=50)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.placa} - {self.marca} {self.modelo}'

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'


class OrdemServico(models.Model):
    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('em_andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada'),
    ]

    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT, related_name='ordens')
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberta')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_entrada = models.DateField(auto_now_add=True)
    data_saida = models.DateField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'OS #{self.id} - {self.veiculo.placa}'

    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviço'
