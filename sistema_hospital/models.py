from django.db import models


class Especialidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'


class Medico(models.Model):
    nome = models.CharField(max_length=150)
    crm = models.CharField(max_length=20, unique=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.PROTECT, related_name='medicos')
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Dr(a). {self.nome}'

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'


class Paciente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    sus = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


class AgendamentoConsulta(models.Model):
    STATUS_CHOICES = [
        ('aguardando', 'Aguardando'),
        ('confirmado', 'Confirmado'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado'),
        ('falta', 'Falta'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='agendamentos')
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT, related_name='agendamentos')
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aguardando')
    motivo = models.TextField()
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.paciente.nome} - {self.medico.nome} em {self.data_hora}'

    class Meta:
        verbose_name = 'Agendamento de Consulta'
        verbose_name_plural = 'Agendamentos de Consultas'
