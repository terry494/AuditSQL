# Generated by Django 2.1.7 on 2019-03-28 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_onlineversion_updated_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SysConfig',
        ),
        migrations.AlterModelOptions(
            name='orderstasks',
            options={'default_permissions': (), 'verbose_name': '工单子任务', 'verbose_name_plural': '工单子任务'},
        ),
        migrations.AlterField(
            model_name='orders',
            name='contents',
            field=models.TextField(default='', verbose_name='工单内容'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='envi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.SysEnvironment', verbose_name='环境'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='progress',
            field=models.CharField(choices=[('0', '待批准'), ('1', '未批准'), ('2', '已批准'), ('3', '处理中'), ('4', '已完成'), ('5', '已关闭'), ('6', '已复核'), ('7', '已勾住')], default='0', max_length=30, verbose_name='进度'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='version',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.OnlineVersion', verbose_name='上线版本号'),
        ),
        migrations.AlterField(
            model_name='orderstasks',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Orders', verbose_name='工单标题'),
        ),
        migrations.AlterField(
            model_name='orderstasks',
            name='sql',
            field=models.TextField(default='', verbose_name='SQL'),
        ),
    ]