from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'


class Plano(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    valor_mensal = models.DecimalField(max_digits=8, decimal_places=2)
    duracao_meses = models.IntegerField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'


class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas')
    plano = models.ForeignKey(Plano, on_delete=models.PROTECT, related_name='matriculas')
    data_inicio = models.DateField()
    data_fim = models.DateField()
    ativa = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.aluno.nome} - {self.plano.nome}'

    class Meta:
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas'
