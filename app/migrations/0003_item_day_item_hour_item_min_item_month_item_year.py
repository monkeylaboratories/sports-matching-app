# Generated by Django 5.0.6 on 2024-05-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_item_sample_1_remove_item_sample_10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='day',
            field=models.IntegerField(blank=True, choices=[(1, '1日'), (2, '2日'), (3, '3日'), (4, '4日'), (5, '5日'), (6, '6日'), (7, '7日'), (8, '8日'), (9, '9日'), (10, '10日'), (11, '11日'), (12, '12日'), (13, '13日'), (14, '14日'), (15, '15日'), (16, '16日'), (17, '17日'), (18, '18日'), (19, '19日'), (20, '20日'), (21, '21日'), (22, '22日'), (23, '23日'), (24, '24日'), (25, '25日'), (26, '26日'), (27, '27日'), (28, '28日'), (29, '29日'), (30, '30日'), (31, '31日')], null=True, verbose_name='日'),
        ),
        migrations.AddField(
            model_name='item',
            name='hour',
            field=models.IntegerField(blank=True, choices=[(0, '0日'), (1, '1日'), (2, '2日'), (3, '3日'), (4, '4日'), (5, '5日'), (6, '6日'), (7, '7日'), (8, '8日'), (9, '9日'), (10, '10日'), (11, '11日'), (12, '12日'), (13, '13日'), (14, '14日'), (15, '15日'), (16, '16日'), (17, '17日'), (18, '18日'), (19, '19日'), (20, '20日'), (21, '21日'), (22, '22日'), (23, '23日'), (24, '24日')], null=True, verbose_name='時間'),
        ),
        migrations.AddField(
            model_name='item',
            name='min',
            field=models.IntegerField(blank=True, choices=[(0, '0分'), (15, '15分'), (30, '30分'), (45, '45分')], null=True, verbose_name='分'),
        ),
        migrations.AddField(
            model_name='item',
            name='month',
            field=models.IntegerField(blank=True, choices=[(1, '1月'), (2, '2月'), (3, '3月'), (4, '4月'), (5, '5月'), (6, '6月'), (7, '7月'), (8, '8月'), (9, '9月'), (10, '10月'), (11, '11月'), (12, '12月')], null=True, verbose_name='月'),
        ),
        migrations.AddField(
            model_name='item',
            name='year',
            field=models.IntegerField(blank=True, choices=[(2024, '2024年'), (2025, '2025年'), (2026, '2026年')], null=True, verbose_name='年'),
        ),
    ]
