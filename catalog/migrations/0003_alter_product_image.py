from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_alter_product_options_alter_category_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите фото продукта",
                null=True,
                upload_to="catalog/image/",
                verbose_name="Фото продукта",
            ),
        ),
    ]
