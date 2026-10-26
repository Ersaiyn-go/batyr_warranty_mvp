from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warranty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productwarranty',
            name='serial_number',
            field=models.CharField(db_index=True, max_length=64, verbose_name='Серийный номер'),
        ),
    ]
