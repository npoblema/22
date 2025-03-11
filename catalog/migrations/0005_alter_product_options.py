from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_product_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "category"],
                "permissions": [
                    ("can_edit_product", "can edit product"),
                    ("can_edit_description", "can edit description"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
