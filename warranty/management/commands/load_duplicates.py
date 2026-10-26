from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from warranty.duplicates import apply_duplicates, parse_duplicate_rows, read_rows


class Command(BaseCommand):
    help = 'Загрузить серийные номера, выданные двум покупателям (файл .txt/.tsv/.csv/.xlsx)'

    def add_arguments(self, parser):
        parser.add_argument('path')
        parser.add_argument('--dry-run', action='store_true', help='Только показать, ничего не сохранять')

    def handle(self, path, dry_run=False, **options):
        file_path = Path(path)
        if not file_path.exists():
            raise CommandError(f'Файл не найден: {path}')

        with open(file_path, 'rb') as fh:
            rows = read_rows(fh, file_path.name)

        items, problems = parse_duplicate_rows(rows)
        stats, log = apply_duplicates(items, dry_run=dry_run)

        for line in log:
            self.stdout.write(line)
        for line in problems:
            self.stdout.write(self.style.WARNING(line))

        prefix = '[ПРОБНЫЙ ЗАПУСК] ' if dry_run else ''
        self.stdout.write(self.style.SUCCESS(
            f'{prefix}Серийников: {stats["serials"]}. '
            f'Обновлено записей: {stats["updated"]}. Создано: {stats["created"]}.'
        ))
