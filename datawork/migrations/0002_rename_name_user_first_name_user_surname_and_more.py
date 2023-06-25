# Generated by Django 4.2.2 on 2023-06-25 08:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("datawork", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="name",
            new_name="first_name",
        ),
        migrations.AddField(
            model_name="user",
            name="surname",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="post_image",
            field=models.ImageField(blank=True, upload_to="post/"),
        ),
        migrations.AlterField(
            model_name="user",
            name="cover_image",
            field=models.ImageField(
                blank=True, default="cover/sample_cover.jpg", upload_to="cover/"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="dp",
            field=models.ImageField(
                blank=True, default="dp/sample_dp.jpg", upload_to="dp/"
            ),
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("m_id", models.AutoField(primary_key=True, serialize=False)),
                ("message", models.TextField()),
                ("date_time", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "receiver_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiver",
                        to="datawork.user",
                    ),
                ),
                (
                    "sender_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender",
                        to="datawork.user",
                    ),
                ),
            ],
        ),
    ]
