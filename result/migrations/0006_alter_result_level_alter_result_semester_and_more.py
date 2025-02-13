# Generated by Django 4.2.7 on 2024-07-01 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("result", "0005_alter_result_id_alter_takencourse_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="result",
            name="level",
            field=models.CharField(
                choices=[
                    ("Бакалавр", "Степень бакалавра"),
                    ("Магистр", "Степень магистра"),
                ],
                max_length=25,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="result",
            name="semester",
            field=models.CharField(
                choices=[
                    ("Первый", "Первый"),
                    ("Второй", "Второй"),
                    ("Третий", "Третий"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="takencourse",
            name="comment",
            field=models.CharField(
                blank=True,
                choices=[("ПРОЙТИ", "ПРОЙТИ"), ("НЕУД", "НЕУД")],
                max_length=200,
            ),
        ),
    ]
