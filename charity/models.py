from django.contrib.auth import get_user_model
from django.db import models
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import truncatechars
from ckeditor.fields import RichTextField


class Tag(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='دسته بندی')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته بندی')
    status = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')
    positions = models.IntegerField(default=True, verbose_name='پوزیشن')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی'

    def get_absolute_url(self):
        # return reverse("blog_detail", kwargs={"pk":self.id})
        return reverse("category", args=[str(self.slug)])


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'غیر فعال'),
        ('published', 'فعال'),
    )
    title = models.CharField(max_length=100, verbose_name='تیتر')
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='نویسنده')
    body = RichTextField(verbose_name='متن')
    image = models.ImageField(upload_to="image/", verbose_name='انتخاب عکس')
    time = models.DateTimeField(verbose_name='زمان')
    daste = models.ManyToManyField(Tag, verbose_name="دسته بندی", related_name='articles')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published', verbose_name='وضعیت')

    class Meta:
        verbose_name = 'مقالات'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse("blog_detail", kwargs={"pk":self.id})
        return reverse("detail-news", args=[str(self.id)])

    def image_tag(self):
        return format_html("<img width=50 style='border-radius:5px;' src='{}'>".format(self.image.url))
    image_tag.short_description = 'عکس'


class Comment(models.Model): # new
    article = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')
