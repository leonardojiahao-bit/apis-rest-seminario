from django.db import models


class Medico(models.Model):
    nome = models.CharField(max_length=150)
    crm = models.CharField(max_length=20, unique=True)
    especialidade = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Dr(a). {self.nome} - {self.especialidade}'

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'


class Paciente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20)
    convenio = models.CharField(max_length=100, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'


class Consulta(models.Model):
    STATUS_CHOICES = [
        ('agendada', 'Agendada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT, related_name='consultas')
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='agendada')
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.paciente.nome} com {self.medico.nome} em {self.data_hora}'

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
