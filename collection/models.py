from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.fields import JSONField
import datetime
import hashlib
import traceback


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verbose = models.BooleanField(default=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Newsletter_subscriber(models.Model):
    email = models.EmailField(unique=True)
    userid = models.IntegerField(editable=False, unique=True)
    first_name = models.CharField(max_length=255)
    is_templar = models.BooleanField(default=False)
    is_alchemist = models.BooleanField(default=False)
    is_scholar = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    def save(self):
        # set the userid to be the md5-hash of the email
        email_string = self.email.encode('utf-8')
        self.userid = int(hashlib.sha1(email_string).hexdigest(), 16) % (10 ** 8)

        if not self.id:
            self.created = datetime.datetime.today()
        self.updated = datetime.datetime.today()
        super(Newsletter_subscriber, self).save()






class Uploaded_dataset(models.Model):
    # upload_data1
    file_name = models.CharField(max_length=255)
    file_path = models.TextField()
    sep = models.CharField(max_length=3, blank=True, null=True)
    encoding = models.CharField(max_length=10, blank=True, null=True)
    quotechar = models.CharField(max_length=1, blank=True, null=True)
    escapechar = models.CharField(max_length=1, blank=True, null=True)
    na_values = models.TextField(blank=True, null=True)
    skiprows = models.CharField(max_length=20, blank=True, null=True)
    header = models.CharField(max_length=10, blank=True, null=True)
    data_table_json = models.TextField()
    # upload_data2
    data_source = models.TextField(null=True)
    data_generation_date = models.DateField(null=True)
    correctness_of_data = models.IntegerField(null=True)
    # upload_data3
    object_type_name = models.TextField()
    object_type_id = models.TextField()
    entire_objectInfoHTMLString = models.TextField(null=True)
    # upload_data4
    meta_data_facts = models.TextField()
    # upload_data5
    attribute_selection = models.TextField()
    datetime_column = models.TextField(null=True)
    object_identifiers = models.TextField(null=True)
    # upload_data6
    list_of_matches = models.TextField()
    # upload_data7
    # valid_times = models.TextField()
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,)
    def save(self):
        if not self.id:
            self.created = datetime.datetime.today()
        self.updated = datetime.datetime.today()
        super(Uploaded_dataset, self).save()


class Data_point(models.Model):
    object_id = models.IntegerField()
    attribute_id = models.TextField()
    value_as_string = models.TextField()
    numeric_value = models.FloatField(null=True)
    string_value = models.TextField(null=True)
    boolean_value = models.NullBooleanField() 
    valid_time_start = models.IntegerField()
    valid_time_end = models.IntegerField()
    data_quality = models.IntegerField()



class Object_hierachy_tree_history(models.Model):
    object_hierachy_tree = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,)
    timestamp = models.DateTimeField(editable=False)
    def save(self):
        self.timestamp = datetime.datetime.today()
        super(Object_hierachy_tree_history, self).save()

class Object_types(models.Model):
    id = models.TextField(primary_key=True)
    parent = models.TextField()
    name = models.TextField()
    li_attr = models.TextField(null=True)
    a_attr = models.TextField(null=True)
    object_icon = models.TextField()


class Object(models.Model):
    object_type_id = models.TextField()


class Attribute(models.Model):
    name = models.TextField()
    data_type = models.TextField()
    expected_valid_period = models.IntegerField()
    description = models.TextField()
    format_specification = models.TextField()
    first_applicable_object = models.TextField()


class Rule(models.Model):
    name = models.TextField()
    attribute_id = models.IntegerField()
    number_of_times_used = models.IntegerField()
    used_attribute_ids = models.TextField()
    used_attribute_names = models.TextField()
    rule_text = models.TextField()
    executable = models.TextField()

    def run(self, input_values, timestep_size):
        to_be_executed_code = self.executable

        to_be_executed_code = to_be_executed_code.replace('delta_t', str(timestep_size))
        for attribute_id in input_values.keys():
            search_term = attribute_id.replace('simulated_','attr')
            to_be_executed_code = to_be_executed_code.replace(search_term, str(input_values[attribute_id]))

        try:
            print("<><><><><><><><><><><><><<><><><><><><>")
            print(to_be_executed_code)
            print("<><><><><><><><><><><><><<><><><><><><>")
            execution_results = {}
            exec(to_be_executed_code, globals(), execution_results)
            result = execution_results['result']
            return result
        except Exception as error:
            traceback.print_exc()
            return str(error)




class Simulation_model(models.Model):
    objects_dict = models.TextField()
    object_type_counts = models.TextField()
    total_object_count= models.IntegerField()
    number_of_additional_object_facts = models.IntegerField()
    simulation_start_time = models.IntegerField()
    simulation_end_time = models.IntegerField()
    timestep_size = models.IntegerField(null=True)
    timeline_visualisation_data = models.TextField(null=True)
    linegraph_data = models.TextField(null=True)
    attribute_errors = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    # is_private  = models.BooleanField(default=False)
    def save(self):
        if not self.id:
            self.created = datetime.datetime.today()
        self.updated = datetime.datetime.today()
        super(Simulation_model, self).save()


# class Meta_data_constaint(models.Model):
#     simulation_model = models.ForeignKey(Simulation_model, on_delete=models.SET_NULL, blank=True, null=True,)
#     attribute =  models.ForeignKey(Attribute, on_delete=models.SET_NULL, blank=True, null=True,)
#     operation = models.CharField(max_length=2)
#     value = models.TextField()


# class Object_properties(models.Model):
#     first_applicable_object = models.ForeignKey(Object_types, on_delete=models.SET_NULL, blank=True, null=True,)
#     attribute =  models.ForeignKey(Attribute, on_delete=models.SET_NULL, blank=True, null=True,)
#     operation = models.CharField(max_length=2)
#     value = models.TextField()






