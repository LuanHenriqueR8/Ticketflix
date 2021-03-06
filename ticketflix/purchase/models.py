from django.db import models
from django.utils.translation import gettext as _
from django.core import validators
from ticketflix.users.models import User
from ticketflix.cart.models import Cart

class Purchase(models.Model):
    AGUARDANDO = 'Aguardando'
    CONFIRMADO = 'Confirmado'
    CANCELADO = 'Cancelado'

    STATUS_CHOICES = (
        (AGUARDANDO, AGUARDANDO),
        (CONFIRMADO, CONFIRMADO),
        (CANCELADO, CANCELADO),
    )

    total_price = models.FloatField(
        verbose_name=_("Preço Total"),
        help_text=_("Preço Total"),
        validators=[validators.MinValueValidator(0)],
        blank=False,
        default=0
    )

    rate = models.FloatField(
        verbose_name=_("Taxa"),
        help_text=_("Taxa"),
        default=0.1,
        blank=False
    )

    statusPayment = models.CharField(
        verbose_name=_('Status'),
        help_text=_('Status do Pagamento'),
        max_length=20,
        choices=STATUS_CHOICES,
        default=AGUARDANDO,
    )

    customer = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )
    
    cart = models.ForeignKey(
        Cart,
        on_delete=models.PROTECT
    )

    def update_status_payment(self, status_payment):
        self.statusPayment = status_payment
        self.save()

    def set_total_price(self):
        self.total_price = self.cart.parcial_price * (1.0 + self.rate)
        self.save()