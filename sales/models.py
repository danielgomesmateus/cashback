from django.db import models


class Sale(models.Model):
    STATUS = [
        ('APROVADO', 'Aprovado'),
        ('EM_VALIDACAO', 'Em validação'),
    ]

    code = models.CharField(max_length=32)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    cpf_reseller = models.CharField(max_length=11)
    status = models.CharField(max_length=12, choices=STATUS)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

    def __str__(self):
        return self.code
