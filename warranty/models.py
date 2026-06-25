import calendar
from datetime import date

from django.db import models
from django.utils import timezone


def add_months(source_date: date, months: int) -> date:
    month = source_date.month - 1 + months
    year = source_date.year + month // 12
    month = month % 12 + 1
    day = min(source_date.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)


class ProductWarranty(models.Model):
    class Status(models.TextChoices):
        IN_STOCK = 'in_stock', 'На складе / не активирован'
        SOLD = 'sold', 'Продан / гарантия активирована'
        RETURNED = 'returned', 'Возврат'
        REPLACED = 'replaced', 'Заменён'
        BLOCKED = 'blocked', 'Заблокирован / спорный серийник'

    class Channel(models.TextChoices):
        KASPI = 'kaspi', 'Kaspi'
        INSTAGRAM = 'instagram', 'Instagram'
        WHATSAPP = 'whatsapp', 'WhatsApp'
        STORE = 'store', 'Офлайн-магазин'
        OTHER = 'other', 'Другое'

    serial_number = models.CharField('Серийный номер', max_length=64, unique=True)
    model_name = models.CharField('Модель', max_length=120, default='Batyr Watch')
    color = models.CharField('Цвет', max_length=60, blank=True)

    status = models.CharField('Статус', max_length=20, choices=Status.choices, default=Status.IN_STOCK)
    sale_date = models.DateField('Дата продажи', null=True, blank=True)
    warranty_months = models.PositiveIntegerField('Срок гарантии, месяцев', default=12)

    buyer_name = models.CharField('Имя покупателя', max_length=120, blank=True)
    buyer_phone = models.CharField('Телефон покупателя', max_length=40, blank=True)
    channel = models.CharField('Канал продажи', max_length=20, choices=Channel.choices, default=Channel.KASPI)

    notes = models.TextField('Заметки для админа', blank=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Товар / гарантия'
        verbose_name_plural = 'Товары / гарантии'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.serial_number:
            self.serial_number = self.serial_number.strip().upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.serial_number} — {self.model_name}'

    @property
    def warranty_end_date(self):
        if not self.sale_date:
            return None
        return add_months(self.sale_date, self.warranty_months)

    @property
    def is_warranty_active(self):
        if self.status != self.Status.SOLD or not self.warranty_end_date:
            return False
        return timezone.localdate() <= self.warranty_end_date

    @property
    def days_left(self):
        if not self.is_warranty_active:
            return 0
        return (self.warranty_end_date - timezone.localdate()).days

    @property
    def masked_buyer(self):
        if not self.buyer_name:
            return ''
        parts = self.buyer_name.strip().split()
        if not parts:
            return ''
        first = parts[0]
        if len(parts) > 1:
            return f'{first} {parts[1][0]}.'
        return first

    @property
    def masked_phone(self):
        digits = ''.join(ch for ch in self.buyer_phone if ch.isdigit())
        if len(digits) < 4:
            return ''
        return f'****{digits[-4:]}'
