# Generated by Django 4.0.3 on 2022-03-24 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yingding', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admissions_data',
            name='annual_target',
            field=models.IntegerField(null=True, verbose_name='计划数'),
        ),
        migrations.AddField(
            model_name='admissions_data',
            name='college_property',
            field=models.CharField(default='', max_length=4, verbose_name='院校性质'),
        ),
        migrations.AddField(
            model_name='admissions_data',
            name='college_state',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='院校说明'),
        ),
        migrations.AddField(
            model_name='admissions_data',
            name='line_2019',
            field=models.IntegerField(blank=True, null=True, verbose_name='2019录取线'),
        ),
        migrations.AddField(
            model_name='admissions_data',
            name='line_2020',
            field=models.IntegerField(blank=True, null=True, verbose_name='2020录取线'),
        ),
        migrations.AddField(
            model_name='admissions_data',
            name='line_2021',
            field=models.IntegerField(blank=True, null=True, verbose_name='2021录取线'),
        ),
        migrations.AddField(
            model_name='admissions_data',
            name='major_group_name',
            field=models.CharField(default='', max_length=30, verbose_name='专业组名称'),
        ),
        migrations.AddField(
            model_name='admissions_data',
            name='plan_change',
            field=models.IntegerField(null=True, verbose_name='计划增减'),
        ),
        migrations.AddField(
            model_name='admissions_data',
            name='provinces',
            field=models.CharField(default='', max_length=10, verbose_name='所在省份'),
        ),
        migrations.AddField(
            model_name='admissions_data',
            name='ranking_2019',
            field=models.IntegerField(blank=True, null=True, verbose_name='2019位次'),
        ),
        migrations.AddField(
            model_name='admissions_data',
            name='ranking_2020',
            field=models.IntegerField(blank=True, null=True, verbose_name='2020位次'),
        ),
        migrations.AddField(
            model_name='admissions_data',
            name='ranking_2021',
            field=models.IntegerField(blank=True, null=True, verbose_name='2021位次'),
        ),
        migrations.AddField(
            model_name='admissions_data',
            name='region',
            field=models.CharField(default='', max_length=10, verbose_name='所在地区'),
        ),
        migrations.AddField(
            model_name='admissions_data',
            name='subject_demand',
            field=models.CharField(default='', max_length=20, verbose_name='选科要求'),
        ),
        migrations.AlterField(
            model_name='admissions_data',
            name='major_group_code',
            field=models.IntegerField(default='', verbose_name='专业组代码'),
        ),
    ]
