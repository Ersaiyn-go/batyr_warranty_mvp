# Generated manually for MVP
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='ProductWarranty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=64, unique=True, verbose_name='Серийный номер')),
                ('model_name', models.CharField(default='Batyr Watch', max_length=120, verbose_name='Модель')),
                ('color', models.CharField(blank=True, max_length=60, verbose_name='Цвет')),
                ('status', models.CharField(choices=[('in_stock', 'На складе / не активирован'), ('sold', 'Продан / гарантия активирована'), ('returned', 'Возврат'), ('replaced', 'Заменён'), ('blocked', 'Заблокирован / спорный серийник')], default='in_stock', max_length=20, verbose_name='Статус')),
                ('sale_date', models.DateField(blank=True, null=True, verbose_name='Дата продажи')),
                ('warranty_months', models.PositiveIntegerField(default=12, verbose_name='Срок гарантии, месяцев')),
                ('buyer_name', models.CharField(blank=True, max_length=120, verbose_name='Имя покупателя')),
                ('buyer_phone', models.CharField(blank=True, max_length=40, verbose_name='Телефон покупателя')),
                ('channel', models.CharField(choices=[('kaspi', 'Kaspi'), ('instagram', 'Instagram'), ('whatsapp', 'WhatsApp'), ('store', 'Офлайн-магазин'), ('other', 'Другое')], default='kaspi', max_length=20, verbose_name='Канал продажи')),
                ('notes', models.TextField(blank=True, verbose_name='Заметки для админа')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name': 'Товар / гарантия',
                'verbose_name_plural': 'Товары / гарантии',
                'ordering': ['-created_at'],
            },
        ),
    ]
