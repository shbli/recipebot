from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


class Course(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Course, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']


class Cuisine(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Cuisine, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Recipe(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    cooking_instructions = models.TextField()
    slug = models.SlugField()
    preparation_time = models.IntegerField(help_text='Preparation time in minutes')
    cooking_time = models.IntegerField(help_text='Cooking time in minutes')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.PROTECT)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    version = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
            self.created = datetime.now()
            self.version = 1

        self.modified = datetime.now()
        self.version = self.version + 1

        super(Recipe, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        get_latest_by = 'created'


class Measurement(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Ingredient(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class RecipeIngredient(models.Model):
    amount = models.IntegerField()
    unit = models.ForeignKey(Measurement, on_delete=models.PROTECT)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.amount, self.unit, self.ingredient.name)

    class Meta:
        ordering = ['ingredient']
