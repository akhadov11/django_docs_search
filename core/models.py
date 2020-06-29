from django.db import models


class DocumentType(models.Model):
    name = models.CharField(max_length=255)
    has_validity = models.BooleanField()
    has_series = models.BooleanField()


class LostDocuments(models.Model):
    identifier = models.CharField(max_length=255, unique=True)  # y not builtin id
    series = models.CharField("Document series", max_length=255)
    doc_num = models.CharField("Document number", max_length=255)
    type = models.ForeignKey(DocumentType, on_delete=models.CASCADE)
    status = models.BooleanField()
    loss_date = models.DateTimeField("Date of loss")
    reg_date = models.DateTimeField("Date of registration")
    authority = models.CharField(max_length=255)
