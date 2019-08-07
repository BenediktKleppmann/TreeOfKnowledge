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
    object_id = models.IntegerField(db_index=True)
    attribute_id = models.TextField(db_index=True)
    value_as_string = models.TextField(db_index=True)
    numeric_value = models.FloatField(null=True, db_index=True)
    string_value = models.TextField(null=True, db_index=True)
    boolean_value = models.NullBooleanField() 
    valid_time_start = models.IntegerField(db_index=True)
    valid_time_end = models.IntegerField(db_index=True)
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
    object_type_icon = models.TextField()




class Object(models.Model):
    object_type_id = models.TextField()




class Attribute(models.Model):
    name = models.TextField()
    data_type = models.TextField()
    expected_valid_period = models.IntegerField()
    description = models.TextField()
    format_specification = models.TextField()
    first_applicable_object_type = models.TextField()
    first_relation_object_type = models.TextField(null=True)




class Simulation_model(models.Model):
    is_timeseries_analysis = models.BooleanField()
    objects_dict = models.TextField()
    y_value_attributes = models.TextField()
    object_type_counts = models.TextField()
    total_object_count= models.IntegerField()
    number_of_additional_object_facts = models.IntegerField()
    simulation_start_time = models.IntegerField()
    simulation_end_time = models.IntegerField()
    timestep_size = models.IntegerField(null=True)
    just_learned_rules = models.TextField(null=True)
    rule_infos = models.TextField(null=True)
    triggered_rules = models.TextField(null=True)
    simulation_data = models.TextField(null=True)
    errors = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    # is_private  = models.BooleanField(default=False)
    def save(self):
        if not self.id:
            self.created = datetime.datetime.today()
        self.updated = datetime.datetime.today()
        super(Simulation_model, self).save()



class Rule(models.Model):
    changed_var_attribute_id = models.IntegerField()
    condition_text = models.TextField(null=True)
    condition_exec = models.TextField(null=True)
    effect_text = models.TextField()
    effect_exec = models.TextField()
    effect_is_calculation = models.NullBooleanField() # if False, then the effect is just a value and if the rule is triggered, then the column_to_change will be set to this value
    used_attribute_ids = models.TextField()
    is_conditionless = models.NullBooleanField()   #if true then this is a calculation rule i.e. the condition is 'True' and the effect is automatically triggered at every timestep
    has_probability_1 = models.NullBooleanField()  #if true, then the rule is a certain fact and there will be no beta-distribution coefficients in Posterior_distributions
    probability = models.FloatField(null=True)
    standard_dev = models.FloatField(null=True)

    


class Likelihood_fuction(models.Model):
    simulation_id = models.IntegerField()
    object_number = models.IntegerField()
    rule_id = models.IntegerField()
    list_of_probabilities = models.TextField()
    nb_of_simulations = models.IntegerField()
    nb_of_sim_in_which_rule_was_used = models.IntegerField()
    nb_of_values_in_posterior = models.IntegerField()






# ========================================================================================
# No Longer Used
# ========================================================================================

class Calculation_rule(models.Model):
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
            print(input_values)
            print(to_be_executed_code)
            print("<><><><><><><><><><><><><<><><><><><><>")
            execution_results = {}
            exec(to_be_executed_code, globals(), execution_results)
            result = execution_results['result']
            return result
        except Exception as error:
            traceback.print_exc()
            return str(error)



class Learned_rule(models.Model):
    overall_score = models.FloatField(null=True)
    object_type_id = models.TextField()
    object_type_name = models.TextField()
    attribute_id = models.IntegerField()
    attribute_name = models.TextField()
    object_filter_facts = models.TextField()
    specified_factors = models.TextField()
    sorted_factor_numbers = models.TextField()
    valid_times = models.TextField()
    min_score_contribution = models.FloatField()
    max_p_value = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)
    # is_private  = models.BooleanField(default=False)
    def save(self):
        if not self.id:
            self.created = datetime.datetime.today()
        self.updated = datetime.datetime.today()
        super(Learned_rule, self).save()







