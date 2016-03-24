"""
Sample code to create a meal with various options.

Execute in ShellPlus: $ python manage.py shell_plus
"""

loc1 = Location.objects.create(lat=39.1086858, lng=-84.5150832)
img1 = Image.objects.create(
    url='http://imgsv.imaging.nikon.com/lineup/lens/zoom/normalzoom/af-s_dx_18-140mmf_35-56g_ed_vr/img/sample/sample1_l.jpg')
img2 = Image.objects.create(
    url='http://www.seriouseats.com/images/2014/02/20140227-chipotles-sofritas-tacos.jpg')
u = APIUser.objects.first()

meal = Meal.objects.create(
    name='meal1',
    portions=2,
    portions_available=2,
    available_from=timezone.now(),
    available_to=timezone.now() + timezone.timedelta(days=300),
    location=loc1,
    seller=u,
    preview_image=img1,
)
meal.images.add(img1, img2)
meal.allergens.add(Allergen.objects.get(name='soy'))
