from faker import Faker

from django.contrib.auth.models import User

def set_user(fakegen=None):
    if fakegen is None:
        fakegen = Faker(['en_US'])

    f_name = fakegen.first_name()
    l_name = fakegen.last_name()
    u_name = f_name.lower() + '_' + l_name.lower()
    email = f'{u_name}@{fakegen.domain_name()}'

    user_check = User.objects.filter(username=u_name)
	##### BÖYLE BİR USERNAME VARSA HATA ALACAĞIZ BUNUN İÇİN BİR VALIDATION YAPIYORUZ
    while user_check.exists():
        print(f'Böyle bir kullanıcı var zaten: {u_name}')
        u_name = f_name + '_' + l_name + str(random.randrange(1, 999))
        user_check = User.objects.filter(username=u_name)


    user = User(
        username =  u_name,
        first_name =  f_name,
        last_name = l_name,
        email =  email,
    )

    user.set_password('testing123')
    user.save()

    user_check = User.objects.filter(username=u_name)[0]
    print(f'Kullanici {user_check.username}, {user_check.id} id numarası ile kaydedildi. ')