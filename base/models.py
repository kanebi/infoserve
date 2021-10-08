from django.db import models

class tobetest(nodels,class tobe(models.Model):

    name = models.CharField(, max_length=50)

    class Meta:
        verbose_name = _("tobe")
        verbose_name_plural = _("tobes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tobe_detail", kwargs={"pk": self.pk})
)
# Create your models here. tobe added this
