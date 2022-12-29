from .models import Tutorial
from faker import Faker
def run():
    '''
        # https://faker.readthedocs.io/en/master/
        $ pip install faker # install faker module
        python manage.py flush # delete all exists data from db. dont forget: createsuperuser
        python manage.py shell
        from student_api.faker import run
        run()
        exit()
    '''
    fake = Faker(['tr-TR'])
    title = (
        "FullStack",
        "DataScience",
        "AwsDevops",
        "CyberSec",
    )
    description = (
        "FullStack",
        "DataScience",
        "AwsDevops",
        "CyberSec",
    )
    for i in range(50):
        title = Tutorial.objects.create(title = title, description = fake.description())
        # for _ in range(50):
        #     Tutorial.objects.create(title = new_title, description = fake.description())
    print('Finished')