from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from warranty.models import ProductWarranty


class Command(BaseCommand):
    help = 'Создаёт демо-серийники для проверки сайта'

    def handle(self, *args, **options):
        today = timezone.localdate()
        items = [
            {
                'serial_number': 'BW-SUN-2026-000125',
                'model_name': 'Batyr Watch Sunqar Pro 44 mm',
                'color': 'Black',
                'status': ProductWarranty.Status.SOLD,
                'sale_date': today - timedelta(days=45),
                'warranty_months': 12,
                'buyer_name': 'Мадияр Болатбекулы',
                'buyer_phone': '+7 777 123 7755',
                'channel': ProductWarranty.Channel.KASPI,
            },
            {
                'serial_number': 'BW-TOM-2026-000088',
                'model_name': 'Batyr Watch Tomiris 41 mm',
                'color': 'Silver',
                'status': ProductWarranty.Status.IN_STOCK,
                'warranty_months': 12,
                'channel': ProductWarranty.Channel.OTHER,
            },
            {
                'serial_number': 'BW-SUN-2024-000001',
                'model_name': 'Batyr Watch Sunqar Pro 44 mm',
                'color': 'Black',
                'status': ProductWarranty.Status.SOLD,
                'sale_date': today - timedelta(days=500),
                'warranty_months': 12,
                'buyer_name': 'Айбек Нурланов',
                'buyer_phone': '+7 701 555 1122',
                'channel': ProductWarranty.Channel.INSTAGRAM,
            },
        ]

        created = 0
        for data in items:
            _, was_created = ProductWarranty.objects.update_or_create(
                serial_number=data['serial_number'],
                defaults=data,
            )
            created += int(was_created)

        self.stdout.write(self.style.SUCCESS(f'Готово. Демо-записи добавлены/обновлены: {len(items)}. Новых: {created}'))
