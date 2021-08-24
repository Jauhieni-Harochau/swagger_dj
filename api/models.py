from django.db import models

# Create your models here.
BLANK = {'null': True, 'blank': True}

# class ProcessFoci(models.CharField, models.Choices):
#     mobile = 'mobile' 'Moblie'
#     desktop = 'desktop' 'Desktop'

class Fab(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Lithography(models.Model):
    name = models.CharField(max_length=40)
    based_on = models.ForeignKey("self", on_delete=models.CASCADE, **BLANK)
    fab = models.ForeignKey(Fab, on_delete=models.CASCADE, related_name='processes')
    transistor_density = models.FloatField()
    focus = models.TextChoices('Mobile', 'Desktop')

    def __str__(self):
        return self.name


class GPUArchitecture(models.Model):
    name = models.CharField(max_length=40)
    # based_on = models.ManyToManyField("self", **BLANK)
    feature_support = models.CharField(max_length=40)
    lithography = models.ManyToManyField(Lithography)
    developer = models.ForeignKey('Chipmaker', on_delete=models.CASCADE, related_name='architectures')


    def __str__(self):
        return self.name

class GPU(models.Model):
    codename = models.CharField(max_length=40)
    architecture = models.ForeignKey(GPUArchitecture, on_delete=models.CASCADE, related_name='gpus')
    lithography = models.ForeignKey(Lithography, on_delete=models.CASCADE)
    diesize = models.FloatField(**BLANK)
    transistors = models.PositiveBigIntegerField(**BLANK)
    ALUs = models.SmallIntegerField()
    max_memory_bus = models.SmallIntegerField()
    release_date = models.DateField(**BLANK)
    end_of_life_date = models.DateField(**BLANK)
    developer = models.ForeignKey('Chipmaker', on_delete=models.CASCADE, related_name='gpus')

    def __str__(self):
        return self.codename


class Chipmaker(models.Model):
    name = models.CharField(max_length=40)
    founded_date = models.DateField()
    disbanded_date = models.DateField(**BLANK)
    sold_date = models.DateField(**BLANK)
    owned_by = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='subsidiaries')

    def __str__(self):
        return self.name


class GraphicsBoardSKU(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, **BLANK)
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE)
    alus = models.SmallIntegerField()
    max_memory_bus = models.SmallIntegerField()
    gpu_clock = models.SmallIntegerField()
    memory_clock = models.SmallIntegerField()
    msrp = models.SmallIntegerField()
    developer = models.ForeignKey(Chipmaker, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, **BLANK)
    is_branded = models.BooleanField(default=False)

    def __str__(self):
        return self.name if self.name is not None else 'NONAME'

class GraphicsBoard(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, **BLANK)
    sku = models.ForeignKey(GraphicsBoardSKU, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    gpu_clock = models.SmallIntegerField()
    memory_clock = models.SmallIntegerField()
    is_oc = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=100, **BLANK)
    img = models.ImageField()

