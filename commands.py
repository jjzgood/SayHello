import click
from app import db,app,models
from faker import Faker


fake = Faker('zh_CN')


# @app.cli.command()
# @click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    """
    生成测试数据
    """
    db.drop_all()
    db.create_all()

    click.echo('Working...')
    for i in range(count):
        message = models.Message(
            name = fake.name(),
            body = fake.sentence(),
            timestamp = fake.date_time_this_year()
        )
        db.session.add(message)
    db.session.commit()
    click.echo('Created %d fake messages.' % count)


forge(count=5000)

