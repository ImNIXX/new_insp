from django.db import models

# Create your models here.


class User(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=100, blank=True)
    dob = models.CharField(max_length=100, blank=True)
    role_id = models.IntegerField()
    status = models.IntegerField()
    register_date = models.DateTimeField(auto_now_add=True)
    user_directory = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = "insp_user"

    def __str__(self):
        return self.username


class Inspections(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    facility = models.CharField(max_length=100)
    stakeholders = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    operating_area = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100, blank=True)
    datetime = models.DateField(max_length=50, blank=True)
    draft_directory = models.CharField(max_length=100, blank=True)
    draft_name = models.CharField(max_length=100, blank=True)
    draft_slug = models.CharField(max_length=100, blank=True)
    status = models.IntegerField(null=True)
    approve = models.CharField(max_length=100, blank=True)
    user_id = models.IntegerField()

    class Meta:
        db_table = "insp_inspection"

    def __str__(self):
        return self.title


class Facility(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    facility = models.CharField(max_length=100)

    class Meta:
        db_table = "insp_facility"

    def __str__(self):
        return self.facility


class Type(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    type_slug = models.CharField(max_length=200, blank=True)
    draft_html = models.TextField()

    class Meta:
        db_table = "insp_type"

    def __str__(self):
        return self.type


class DraftTables(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    draft_name = models.CharField(max_length=100)
    table_name = models.CharField(max_length=100)

    class Meta:
        db_table = "insp_draft_tbl"

    def __str__(self):
        return self.draft_name

# DRAFTS DATABASE


class AccidentInvestigationRCAForm(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    job_title = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    date_occurrence = models.CharField(max_length=50, blank=True)
    lcoation = models.CharField(max_length=50, blank=True)
    date_reported = models.CharField(max_length=50, blank=True)
    to_whom = models.CharField(max_length=50, blank=True)
    incident = models.CharField(max_length=50, blank=True)
    des_happened = models.TextField(blank=True)
    des_nature = models.TextField(blank=True)
    body_injured = models.CharField(max_length=255, blank=True)
    type_accident = models.CharField(max_length=255, blank=True)
    wit_name_one = models.CharField(max_length=50, blank=True)
    wit_ph_one = models.CharField(max_length=50, blank=True)
    wit_addr_one = models.CharField(max_length=50, blank=True)
    wit_ph_two = models.CharField(max_length=50, blank=True)
    wit_name_two = models.CharField(max_length=50, blank=True)
    wit_ph_three = models.CharField(max_length=50, blank=True)
    wit_addr_two = models.CharField(max_length=50, blank=True)
    wit_ph_four = models.CharField(max_length=50, blank=True)
    wit_name_three = models.CharField(max_length=50, blank=True)
    wit_ph_five = models.CharField(max_length=50, blank=True)
    wit_addr_three = models.CharField(max_length=50, blank=True)
    wit_ph_six = models.CharField(max_length=50, blank=True)
    phy_name = models.CharField(max_length=50, blank=True)
    phy_ph_one = models.CharField(max_length=50, blank=True)
    phy_addr = models.CharField(max_length=50, blank=True)
    phy_ph_two = models.CharField(max_length=50, blank=True)
    causes = models.TextField(blank=True)
    des_exist = models.TextField(blank=True)
    corr_actions = models.TextField(blank=True)
    des_action = models.TextField(blank=True)
    invest_name = models.CharField(max_length=50, blank=True)
    invest_sign = models.CharField(max_length=50, blank=True)
    invest_date = models.CharField(max_length=50, blank=True)
    review_name = models.CharField(max_length=50, blank=True)
    review_sign = models.CharField(max_length=50, blank=True)
    review_date = models.CharField(max_length=50, blank=True)
    review_first_name = models.CharField(max_length=50, blank=True)
    review_job_title = models.CharField(max_length=50, blank=True)
    review_addr = models.CharField(max_length=50, blank=True)
    review_date_occurrence = models.CharField(max_length=50, blank=True)
    review_location = models.CharField(max_length=50, blank=True)
    review_date_report = models.CharField(max_length=50, blank=True)
    review_to_whom = models.CharField(max_length=50, blank=True)
    illness = models.CharField(max_length=255, blank=True)
    des_injury = models.CharField(max_length=50, blank=True)
    des_materials = models.CharField(max_length=50, blank=True)
    body_injured_second = models.CharField(max_length=255, blank=True)
    type_incident = models.CharField(max_length=255, blank=True)
    wit_two_name_one = models.CharField(max_length=50, blank=True)
    wit_two_ph_one = models.CharField(max_length=50, blank=True)
    wit_two_addr_one = models.CharField(max_length=50, blank=True)
    wit_two_ph_two = models.CharField(max_length=50, blank=True)
    wit_two_name_two = models.CharField(max_length=50, blank=True)
    wit_two_ph_three = models.CharField(max_length=50, blank=True)
    wit_two_addr_two = models.CharField(max_length=50, blank=True)
    wit_two_ph_four = models.CharField(max_length=50, blank=True)
    wit_two_name_three = models.CharField(max_length=50, blank=True)
    wit_two_ph_five = models.CharField(max_length=50, blank=True)
    wit_two_addr_three = models.CharField(max_length=50, blank=True)
    wit_two_ph_six = models.CharField(max_length=50, blank=True)
    wit_two_emp_sign = models.CharField(max_length=50, blank=True)
    wit_two_date = models.CharField(max_length=50, blank=True)
    wit_two_supervisor = models.CharField(max_length=50, blank=True)
    wit_two_supervisor_sign = models.CharField(max_length=50, blank=True)
    wit_two_name_four = models.CharField(max_length=50, blank=True)
    wit_two_job_title = models.CharField(max_length=50, blank=True)
    wit_two_addr_four = models.CharField(max_length=50, blank=True)
    wit_two_date_occurance = models.CharField(max_length=50, blank=True)
    wit_two_location = models.CharField(max_length=50, blank=True)
    wit_two_wit_name = models.CharField(max_length=50, blank=True)
    wit_two_wit_job = models.CharField(max_length=50, blank=True)
    wit_two_wit_addr = models.CharField(max_length=50, blank=True)
    wit_two_loc_accident = models.CharField(max_length=50, blank=True)
    wit_two_date_occ = models.CharField(max_length=50, blank=True)
    wit_two_time_occ = models.CharField(max_length=50, blank=True)
    des_incident = models.CharField(max_length=50, blank=True)
    body_injured_third = models.CharField(max_length=255, blank=True)
    type_occupation = models.CharField(max_length=255, blank=True)
    wit_sign = models.CharField(max_length=50, blank=True)
    date = models.CharField(max_length=50, blank=True)
    supervisor_name = models.CharField(max_length=50, blank=True)
    supervisor_sign = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_AccidentInvestigationRCAForm"

    def __str__(self):
        return self.plants_name


class AWPForm(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    date = models.CharField(max_length=50, blank=True)
    device_id = models.CharField(max_length=50, blank=True)
    unit_type = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=255, blank=True)
    brakes = models.CharField(max_length=5, blank=True)
    controls = models.CharField(max_length=5, blank=True)
    emergency = models.CharField(max_length=5, blank=True)
    lower = models.CharField(max_length=5, blank=True)
    both_controls = models.CharField(max_length=5, blank=True)
    defective = models.CharField(max_length=5, blank=True)
    hydraulic = models.CharField(max_length=5, blank=True)
    handrails = models.CharField(max_length=5, blank=True)
    basket = models.CharField(max_length=5, blank=True)
    exhaust = models.CharField(max_length=5, blank=True)
    outriggers = models.CharField(max_length=5, blank=True)
    tires = models.CharField(max_length=5, blank=True)
    landings = models.CharField(max_length=5, blank=True)
    coolant = models.CharField(max_length=5, blank=True)
    charged = models.CharField(max_length=5, blank=True)
    alarms = models.CharField(max_length=5, blank=True)
    Drive = models.CharField(max_length=5, blank=True)
    legible = models.CharField(max_length=5, blank=True)
    switches = models.CharField(max_length=5, blank=True)
    Operators = models.CharField(max_length=5, blank=True)
    first_name = models.CharField(max_length=5, blank=True)
    supervisor_name = models.CharField(max_length=50, blank=True)
    printed_name = models.CharField(max_length=50, blank=True)
    operat_name = models.CharField(max_length=50, blank=True)
    emp_by = models.CharField(max_length=50, blank=True)
    AWP = models.CharField(max_length=50, blank=True)
    comments = models.TextField(blank=True)
    representative_name = models.CharField(max_length=50, blank=True)
    emp_sign = models.CharField(max_length=50, blank=True)
    emp_date = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_AWPForm"

    def __str__(self):
        return self.plants_name


class CompressedGasCylinder(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    cylinder_colour = models.CharField(max_length=5, blank=True)
    cylinder_correct = models.CharField(max_length=5, blank=True)
    cylinder_hoses = models.CharField(max_length=5, blank=True)
    cylinder_upright = models.CharField(max_length=5, blank=True)
    cylinder_suitable = models.CharField(max_length=5, blank=True)
    cylinder_securing = models.CharField(max_length=5, blank=True)
    cylinder_lifting = models.CharField(max_length=5, blank=True)
    cylinder_appropriate = models.CharField(max_length=5, blank=True)
    cylinder_caps = models.CharField(max_length=5, blank=True)
    cylinder_trolley = models.CharField(max_length=5, blank=True)
    cylinder_restrictions = models.CharField(max_length=5, blank=True)
    cylinder_PPE = models.CharField(max_length=5, blank=True)
    cylinder_fire = models.CharField(max_length=5, blank=True)
    cylinder_emergency = models.CharField(max_length=5, blank=True)
    date = models.CharField(max_length=50, blank=True)
    cylinder_id = models.CharField(max_length=50, blank=True)
    isnp_name = models.CharField(max_length=50, blank=True)
    sign = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_CompressedGasCylinder"

    def __str__(self):
        return self.plants_name


class ConfinedSpaceAuthorization(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    area = models.CharField(max_length=50, blank=True)
    date_issue = models.CharField(max_length=50, blank=True)
    start_time = models.CharField(max_length=50, blank=True)
    expiry_time = models.CharField(max_length=50, blank=True)
    mastercard = models.CharField(max_length=50, blank=True)
    equipment_id = models.CharField(max_length=50, blank=True)
    equipment_name = models.CharField(max_length=50, blank=True)
    des_hazardous = models.TextField(blank=True)
    equip_hazrdous = models.CharField(max_length=100, blank=True)
    remove_hazrdous = models.CharField(max_length=100, blank=True)
    LEL = models.CharField(max_length=50, blank=True)
    oxygen = models.CharField(max_length=50, blank=True)
    H2S = models.CharField(max_length=50, blank=True)
    CO = models.CharField(max_length=50, blank=True)
    time_test_one = models.CharField(max_length=50, blank=True)
    person_conducting_test = models.CharField(max_length=50, blank=True)
    print_one = models.CharField(max_length=50, blank=True)
    sign_one = models.CharField(max_length=50, blank=True)
    hazardous_reading = models.CharField(max_length=50, blank=True)
    time_test_two = models.CharField(max_length=50, blank=True)
    print_two = models.CharField(max_length=50, blank=True)
    print_three = models.CharField(max_length=50, blank=True)
    atmos = models.CharField(max_length=50, blank=True)
    atmos_other = models.CharField(max_length=50, blank=True)
    detail_freq = models.CharField(max_length=50, blank=True)
    protection = models.CharField(max_length=50, blank=True)
    protection_detail = models.CharField(max_length=50, blank=True)
    harness = models.CharField(max_length=5, blank=True)
    harness_detail = models.CharField(max_length=50, blank=True)
    goggles = models.CharField(max_length=5, blank=True)
    goggles_detail = models.CharField(max_length=50, blank=True)
    clothing = models.CharField(max_length=5, blank=True)
    clothing_detail = models.CharField(max_length=50, blank=True)
    other = models.CharField(max_length=5, blank=True)
    other_detail = models.CharField(max_length=50, blank=True)
    purifying = models.CharField(max_length=5, blank=True)
    purifying_detail = models.CharField(max_length=50, blank=True)
    breathing = models.CharField(max_length=5, blank=True)
    breathing_detail = models.CharField(max_length=50, blank=True)
    developed = models.CharField(max_length=5, blank=True)
    developed_detail = models.CharField(max_length=50, blank=True)
    intrinsically = models.CharField(max_length=5, blank=True)
    intrinsically_detail = models.CharField(max_length=50, blank=True)
    lighting = models.CharField(max_length=5, blank=True)
    lighting_detail = models.CharField(max_length=50, blank=True)
    place = models.CharField(max_length=5, blank=True)
    place_detail = models.CharField(max_length=50, blank=True)
    isolation = models.CharField(max_length=5, blank=True)
    isolation_detail = models.CharField(max_length=50, blank=True)
    blinding = models.CharField(max_length=5, blank=True)
    blinding_detail = models.CharField(max_length=50, blank=True)
    agitators = models.CharField(max_length=5, blank=True)
    agitators_detail = models.CharField(max_length=50, blank=True)
    portable = models.CharField(max_length=5, blank=True)
    portable_detail = models.CharField(max_length=50, blank=True)
    temperature = models.CharField(max_length=5, blank=True)
    temperature_detail = models.CharField(max_length=50, blank=True)
    entry = models.CharField(max_length=5, blank=True)
    entry_detail = models.CharField(max_length=50, blank=True)
    personnel = models.CharField(max_length=5, blank=True)
    personnel_detail = models.CharField(max_length=50, blank=True)
    communication = models.CharField(max_length=50, blank=True)
    des_instruction = models.TextField(blank=True)
    CSE_issuer_name = models.CharField(max_length=50, blank=True)
    CSE_issuer_sign = models.CharField(max_length=50, blank=True)
    CSW_name = models.CharField(max_length=50, blank=True)
    CSW_sign = models.CharField(max_length=50, blank=True)
    CSE_receiver_name = models.CharField(max_length=50, blank=True)
    CSE_receiver_sign = models.CharField(max_length=50, blank=True)
    main_auth_name = models.CharField(max_length=50, blank=True)
    main_auth_sign = models.CharField(max_length=50, blank=True)
    ABSP_auth_name = models.CharField(max_length=50, blank=True)
    ABSP_auth_sign = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_ConfinedSpaceAuthorization"

    def __str__(self):
        return self.plants_name


class ConfinedSpaceEntry(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    entry_location_one = models.CharField(max_length=50, blank=True)
    confined_name_one = models.CharField(max_length=50, blank=True)
    initials_one = models.CharField(max_length=50, blank=True)
    time_in_one = models.CharField(max_length=50, blank=True)
    time_out_one = models.CharField(max_length=50, blank=True)
    entry_location_two = models.CharField(max_length=50, blank=True)
    confined_name_two = models.CharField(max_length=50, blank=True)
    initials_two = models.CharField(max_length=50, blank=True)
    time_in_two = models.CharField(max_length=50, blank=True)
    time_out_two = models.CharField(max_length=50, blank=True)
    entry_location_three = models.CharField(max_length=50, blank=True)
    confined_name_three = models.CharField(max_length=50, blank=True)
    initials_three = models.CharField(max_length=50, blank=True)
    time_in_three = models.CharField(max_length=50, blank=True)
    time_out_three = models.CharField(max_length=50, blank=True)
    entry_location_four = models.CharField(max_length=50, blank=True)
    confined_name_four = models.CharField(max_length=50, blank=True)
    initials_four = models.CharField(max_length=50, blank=True)
    time_in_four = models.CharField(max_length=50, blank=True)
    time_out_four = models.CharField(max_length=50, blank=True)
    entry_location_five = models.CharField(max_length=50, blank=True)
    confined_name_five = models.CharField(max_length=50, blank=True)
    initials_five = models.CharField(max_length=50, blank=True)
    time_in_five = models.CharField(max_length=50, blank=True)
    time_out_five = models.CharField(max_length=50, blank=True)
    entry_location_six = models.CharField(max_length=50, blank=True)
    confined_name_six = models.CharField(max_length=50, blank=True)
    initials_six = models.CharField(max_length=50, blank=True)
    time_in_six = models.CharField(max_length=50, blank=True)
    time_out_six = models.CharField(max_length=50, blank=True)
    entry_location_seven = models.CharField(max_length=50, blank=True)
    confined_name_seven = models.CharField(max_length=50, blank=True)
    initials_seven = models.CharField(max_length=50, blank=True)
    time_in_seven = models.CharField(max_length=50, blank=True)
    time_out_seven = models.CharField(max_length=50, blank=True)
    entry_location_eight = models.CharField(max_length=50, blank=True)
    confined_name_eight = models.CharField(max_length=50, blank=True)
    initials_eight = models.CharField(max_length=50, blank=True)
    time_in_eight = models.CharField(max_length=50, blank=True)
    time_out_eight = models.CharField(max_length=50, blank=True)
    entry_location_nine = models.CharField(max_length=50, blank=True)
    confined_name_nine = models.CharField(max_length=50, blank=True)
    initials_nine = models.CharField(max_length=50, blank=True)
    time_in_nine = models.CharField(max_length=50, blank=True)
    time_out_nine = models.CharField(max_length=50, blank=True)
    entry_location_ten = models.CharField(max_length=50, blank=True)
    confined_name_ten = models.CharField(max_length=50, blank=True)
    initials_ten = models.CharField(max_length=50, blank=True)
    time_in_ten = models.CharField(max_length=50, blank=True)
    time_out_ten = models.CharField(max_length=50, blank=True)
    entry_location_eleven = models.CharField(max_length=50, blank=True)
    confined_name_eleven = models.CharField(max_length=50, blank=True)
    initials_eleven = models.CharField(max_length=50, blank=True)
    time_in_eleven = models.CharField(max_length=50, blank=True)
    time_out_eleven = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_ConfinedSpaceEntry"

    def __str__(self):
        return self.plants_name


class DailyExcavation(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    date = models.CharField(max_length=50, blank=True)
    area = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    weather = models.CharField(max_length=50, blank=True)
    rainfall = models.CharField(max_length=50, blank=True)
    authorized = models.CharField(max_length=50, blank=True)
    additional_info = models.CharField(max_length=50, blank=True)
    spoil = models.CharField(max_length=5, blank=True)
    tension = models.CharField(max_length=5, blank=True)
    trench = models.CharField(max_length=5, blank=True)
    seepage = models.CharField(max_length=5, blank=True)
    bracing = models.CharField(max_length=5, blank=True)
    caving = models.CharField(max_length=5, blank=True)
    zones = models.CharField(max_length=5, blank=True)
    egress = models.CharField(max_length=5, blank=True)
    certified = models.CharField(max_length=5, blank=True)
    shoring = models.CharField(max_length=5, blank=True)
    correct = models.CharField(max_length=5, blank=True)
    hydraulic = models.CharField(max_length=5, blank=True)
    adequate = models.CharField(max_length=5, blank=True)
    barricades = models.CharField(max_length=5, blank=True)
    boulders = models.CharField(max_length=5, blank=True)
    vibrations = models.CharField(max_length=5, blank=True)
    safety = models.CharField(max_length=5, blank=True)
    space = models.CharField(max_length=5, blank=True)
    supervisor_name = models.CharField(max_length=50, blank=True)
    sign = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_DailyExcavation"

    def __str__(self):
        return self.plants_name


class DailyMaintenance(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    engine_condition = models.CharField(max_length=50, blank=True)
    engine_notes = models.CharField(max_length=50, blank=True)
    battery_condition = models.CharField(max_length=50, blank=True)
    battery_notes = models.CharField(max_length=50, blank=True)
    belts_condition = models.CharField(max_length=50, blank=True)
    belts_notes = models.CharField(max_length=50, blank=True)
    bolts_condition = models.CharField(max_length=50, blank=True)
    bolts_notes = models.CharField(max_length=50, blank=True)
    coolant_condition = models.CharField(max_length=50, blank=True)
    coolant_notes = models.CharField(max_length=50, blank=True)
    cleaner_condition = models.CharField(max_length=50, blank=True)
    cleaner_notes = models.CharField(max_length=50, blank=True)
    drain_condition = models.CharField(max_length=50, blank=True)
    drain_notes = models.CharField(max_length=50, blank=True)
    evidence_condition = models.CharField(max_length=50, blank=True)
    evidence_notes = models.CharField(max_length=50, blank=True)
    walkways_condition = models.CharField(max_length=50, blank=True)
    walkways_notes = models.CharField(max_length=50, blank=True)
    oil_pressure_condition = models.CharField(max_length=50, blank=True)
    oil_pressure_notes = models.CharField(max_length=50, blank=True)
    oil_level_condition = models.CharField(max_length=50, blank=True)
    oil_level_notes = models.CharField(max_length=50, blank=True)
    temp_condition = models.CharField(max_length=50, blank=True)
    temp_notes = models.CharField(max_length=50, blank=True)
    air_cleaner_condition = models.CharField(max_length=50, blank=True)
    air_cleaner_notes = models.CharField(max_length=50, blank=True)
    hydraulic_condition = models.CharField(max_length=50, blank=True)
    hydraulic_notes = models.CharField(max_length=50, blank=True)
    hoses_condition = models.CharField(max_length=50, blank=True)
    hoses_notes = models.CharField(max_length=50, blank=True)
    reservoir_condition = models.CharField(max_length=50, blank=True)
    reservoir_notes = models.CharField(max_length=50, blank=True)
    seals_condition = models.CharField(max_length=50, blank=True)
    seals_notes = models.CharField(max_length=50, blank=True)
    filter_condition = models.CharField(max_length=50, blank=True)
    filter_notes = models.CharField(max_length=50, blank=True)
    cuts_condition = models.CharField(max_length=50, blank=True)
    cuts_notes = models.CharField(max_length=50, blank=True)
    light_condition = models.CharField(max_length=50, blank=True)
    light_notes = models.CharField(max_length=50, blank=True)
    tracks_condition = models.CharField(max_length=50, blank=True)
    tracks_notes = models.CharField(max_length=50, blank=True)
    fasteners_condition = models.CharField(max_length=50, blank=True)
    fasteners_notes = models.CharField(max_length=50, blank=True)
    pins_condition = models.CharField(max_length=50, blank=True)
    pins_notes = models.CharField(max_length=50, blank=True)
    guards_condition = models.CharField(max_length=50, blank=True)
    guards_notes = models.CharField(max_length=50, blank=True)
    braking_condition = models.CharField(max_length=50, blank=True)
    braking_notes = models.CharField(max_length=50, blank=True)
    emergency_condition = models.CharField(max_length=50, blank=True)
    emergency_notes = models.CharField(max_length=50, blank=True)
    steering_condition = models.CharField(max_length=50, blank=True)
    steering_notes = models.CharField(max_length=50, blank=True)
    crawler_condition = models.CharField(max_length=50, blank=True)
    crawler_notes = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_DailyMaintenance"

    def __str__(self):
        return self.plants_name


class EarthmovingEquipment(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    equipment_name = models.CharField(max_length=50, blank=True)
    equipment = models.CharField(max_length=50, blank=True)
    other_specify = models.CharField(max_length=50, blank=True)
    equipment_id = models.CharField(max_length=50, blank=True)
    access_good = models.CharField(max_length=50, blank=True)
    access_rejected = models.CharField(max_length=50, blank=True)
    access_na = models.CharField(max_length=50, blank=True)
    access_remarks = models.CharField(max_length=50, blank=True)
    backup_good = models.CharField(max_length=50, blank=True)
    engine_condition = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_EarthmovingEquipment"

    def __str__(self):
        return self.plants_name


class EmergencyEvacuation(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    equipment_name = models.CharField(max_length=50, blank=True)
    date = models.CharField(max_length=50, blank=True)
    time_drill = models.CharField(max_length=50, blank=True)
    location_drill = models.TextField(blank=True)
    des_drill = models.TextField(blank=True)
    des_deficiencies = models.TextField(blank=True)
    work_one = models.CharField(max_length=50, blank=True)
    work_two = models.CharField(max_length=50, blank=True)
    work_three = models.CharField(max_length=50, blank=True)
    work_four = models.CharField(max_length=50, blank=True)
    work_five = models.CharField(max_length=50, blank=True)
    work_six = models.CharField(max_length=50, blank=True)
    work_seven = models.CharField(max_length=50, blank=True)
    work_eight = models.CharField(max_length=50, blank=True)
    work_nine = models.CharField(max_length=50, blank=True)
    work_ten = models.CharField(max_length=50, blank=True)
    work_eleven = models.CharField(max_length=50, blank=True)
    work_twelve = models.CharField(max_length=50, blank=True)
    work_thirteen = models.CharField(max_length=50, blank=True)
    work_fourteen = models.CharField(max_length=50, blank=True)
    work_fifteen = models.CharField(max_length=50, blank=True)
    date_last_drill = models.CharField(max_length=50, blank=True)
    noted_deficiencies = models.TextField(blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_EmergencyEvacuation"

    def __str__(self):
        return self.plants_name


class EmergencyRescue(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    permit = models.CharField(max_length=50, blank=True)
    area = models.CharField(max_length=50, blank=True)
    equipment = models.CharField(max_length=50, blank=True)
    date_develop = models.CharField(max_length=50, blank=True)
    developed_by = models.CharField(max_length=50, blank=True)
    des_location = models.TextField(blank=True)
    des_identify = models.TextField(blank=True)
    des_access = models.TextField(blank=True)
    access_info = models.CharField(max_length=50, blank=True)
    des_work = models.TextField(blank=True)
    des_hazards = models.TextField(blank=True)
    equipment_PPE = models.CharField(max_length=5, blank=True)
    equipment_horizontal = models.CharField(max_length=5, blank=True)
    equipment_self = models.CharField(max_length=5, blank=True)
    equipment_vertical = models.CharField(max_length=5, blank=True)
    equipment_supplied = models.CharField(max_length=5, blank=True)
    equipment_tripod = models.CharField(max_length=5, blank=True)
    equipment_ropes = models.CharField(max_length=5, blank=True)
    equipment_stokes = models.CharField(max_length=5, blank=True)
    equipment_protection = models.CharField(max_length=5, blank=True)
    equipment_monitor = models.CharField(max_length=5, blank=True)
    equipment_space = models.CharField(max_length=5, blank=True)
    other_equipment = models.CharField(max_length=50, blank=True)
    des_PPE = models.TextField(blank=True)
    des_emergency = models.TextField(blank=True)
    site_emergency = models.CharField(max_length=50, blank=True)
    auxiliary = models.CharField(max_length=50, blank=True)
    emergency = models.CharField(max_length=50, blank=True)
    contractor = models.CharField(max_length=50, blank=True)
    aid_support = models.CharField(max_length=50, blank=True)
    other_resources = models.CharField(max_length=50, blank=True)
    des_rescue = models.CharField(max_length=50, blank=True)
    supervisor_name = models.CharField(max_length=50, blank=True)
    supervisor_sign = models.CharField(max_length=50, blank=True)
    supervisor_date = models.CharField(max_length=50, blank=True)
    emer_representative_name = models.CharField(max_length=50, blank=True)
    emer_representative_sign = models.CharField(max_length=50, blank=True)
    emer_representative_date = models.CharField(max_length=50, blank=True)
    CSS_watch_name = models.CharField(max_length=50, blank=True)
    CSS_watch_sign = models.CharField(max_length=50, blank=True)
    CSS_watch_date = models.CharField(max_length=50, blank=True)
    HSE_representative_name = models.CharField(max_length=50, blank=True)
    HSE_representative_sign = models.CharField(max_length=50, blank=True)
    HSE_representative_date = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_EmergencyRescue"

    def __str__(self):
        return self.plants_name


class EnergizedElectrical(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    permit = models.CharField(max_length=50, blank=True)
    work_permit = models.CharField(max_length=50, blank=True)
    parmit_valid = models.CharField(max_length=50, blank=True)
    parmit_valid_two = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    cons_permit = models.CharField(max_length=50, blank=True)
    des_work = models.TextField(blank=True)
    des_energized = models.TextField(blank=True)
    req_name = models.CharField(max_length=50, blank=True)
    req_date = models.CharField(max_length=50, blank=True)
    check_list_scaffolding = models.CharField(max_length=5, blank=True)
    hazards_ana_one = models.CharField(max_length=50, blank=True)
    hazards_ana_two = models.CharField(max_length=50, blank=True)
    hazards_ana_three = models.CharField(max_length=50, blank=True)
    hazards_ana_four = models.CharField(max_length=50, blank=True)
    goggles = models.CharField(max_length=5, blank=True)
    Hardhat = models.CharField(max_length=5, blank=True)
    sleeve = models.CharField(max_length=5, blank=True)
    Insulated = models.CharField(max_length=5, blank=True)
    protection = models.CharField(max_length=5, blank=True)
    required = models.CharField(max_length=50, blank=True)
    other_one = models.CharField(max_length=50, blank=True)
    other_two = models.CharField(max_length=50, blank=True)
    other_three = models.CharField(max_length=50, blank=True)
    shock_haz = models.CharField(max_length=50, blank=True)
    flash_haz = models.CharField(max_length=50, blank=True)
    work_dis = models.CharField(max_length=50, blank=True)
    inci_energy = models.CharField(max_length=50, blank=True)
    arc_flash = models.CharField(max_length=50, blank=True)
    hazards_risk = models.CharField(max_length=50, blank=True)
    shock_hazard = models.CharField(max_length=50, blank=True)
    limited_boundry = models.CharField(max_length=50, blank=True)
    rest_boundry = models.CharField(max_length=50, blank=True)
    proh_boundry = models.CharField(max_length=50, blank=True)
    identify_area = models.CharField(max_length=50, blank=True)
    pre_job = models.CharField(max_length=5, blank=True)
    name_one = models.CharField(max_length=50, blank=True)
    sign_one = models.CharField(max_length=50, blank=True)
    position_one = models.CharField(max_length=50, blank=True)
    date_one = models.CharField(max_length=50, blank=True)
    name_two = models.CharField(max_length=50, blank=True)
    sign_two = models.CharField(max_length=50, blank=True)
    position_two = models.CharField(max_length=50, blank=True)
    date_two = models.CharField(max_length=50, blank=True)
    name_three = models.CharField(max_length=50, blank=True)
    sign_three = models.CharField(max_length=50, blank=True)
    position_three = models.CharField(max_length=50, blank=True)
    date_three = models.CharField(max_length=50, blank=True)
    name_four = models.CharField(max_length=50, blank=True)
    sign_four = models.CharField(max_length=50, blank=True)
    position_four = models.CharField(max_length=50, blank=True)
    date_four = models.CharField(max_length=50, blank=True)
    per_rec_name = models.CharField(max_length=50, blank=True)
    per_rec_sign = models.CharField(max_length=50, blank=True)
    per_rec_date = models.CharField(max_length=50, blank=True)
    per_issu_name = models.CharField(max_length=50, blank=True)
    per_issu_sign = models.CharField(max_length=50, blank=True)
    per_issu_date = models.CharField(max_length=50, blank=True)
    absp_lead_name = models.CharField(max_length=50, blank=True)
    absp_lead_sign = models.CharField(max_length=50, blank=True)
    absp_lead_date = models.CharField(max_length=50, blank=True)
    hse_rep_name = models.CharField(max_length=50, blank=True)
    hse_rep_sign = models.CharField(max_length=50, blank=True)
    hse_rep_date = models.CharField(max_length=50, blank=True)
    first_elect_name = models.CharField(max_length=50, blank=True)
    first_elect_sign = models.CharField(max_length=50, blank=True)
    first_elect_date = models.CharField(max_length=50, blank=True)
    second_elect_name = models.CharField(max_length=50, blank=True)
    second_elect_sign = models.CharField(max_length=50, blank=True)
    second_elect_date = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_EnergizedElectrical"

    def __str__(self):
        return self.plants_name


class EquipmentDeficiency(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    unit = models.CharField(max_length=50, blank=True)
    date = models.CharField(max_length=50, blank=True)
    des_tool = models.CharField(max_length=50, blank=True)
    des_deficiency = models.TextField(blank=True)
    required = models.CharField(max_length=5, blank=True)
    completed = models.CharField(max_length=5, blank=True)
    des_follow = models.TextField(blank=True)
    print = models.CharField(max_length=50, blank=True)
    sign = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_EquipmentDeficiency"

    def __str__(self):
        return self.plants_name


class PortableLadder(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    date = models.CharField(max_length=50, blank=True)
    vehicle = models.CharField(max_length=50, blank=True)
    odometer = models.CharField(max_length=50, blank=True)
    extcle_satis = models.CharField(max_length=50, blank=True)
    extcle_need_impro = models.CharField(max_length=50, blank=True)
    extcle_comment = models.CharField(max_length=50, blank=True)
    intcle_satis = models.CharField(max_length=50, blank=True)
    intcle_need_impro = models.CharField(max_length=50, blank=True)
    intcle_comment = models.CharField(max_length=50, blank=True)
    tracks_satis = models.CharField(max_length=50, blank=True)
    tracks_need_impro = models.CharField(max_length=50, blank=True)
    tracks_comment = models.CharField(max_length=50, blank=True)
    winds_satis = models.CharField(max_length=50, blank=True)
    winds_need_impro = models.CharField(max_length=50, blank=True)
    winds_comment = models.CharField(max_length=50, blank=True)
    wind_wiper_satis = models.CharField(max_length=50, blank=True)
    wind_wiper_need_impro = models.CharField(max_length=50, blank=True)
    wind_wiper_comment = models.CharField(max_length=50, blank=True)
    all_light_satis = models.CharField(max_length=50, blank=True)
    all_light_need_impro = models.CharField(max_length=50, blank=True)
    all_light_comment = models.CharField(max_length=50, blank=True)
    horn_satis = models.CharField(max_length=50, blank=True)
    horn_need_impro = models.CharField(max_length=50, blank=True)
    horn_comment = models.CharField(max_length=50, blank=True)
    fuel_satis = models.CharField(max_length=50, blank=True)
    fuel_need_impro = models.CharField(max_length=50, blank=True)
    fuel_comment = models.CharField(max_length=50, blank=True)
    oil_satis = models.CharField(max_length=50, blank=True)
    oil_need_impro = models.CharField(max_length=50, blank=True)
    oil_comment = models.CharField(max_length=50, blank=True)
    doc_satis = models.CharField(max_length=50, blank=True)
    doc_need_impro = models.CharField(max_length=50, blank=True)
    doc_comment = models.TextField(blank=True)
    des_comment = models.TextField(blank=True)
    insp_by = models.CharField(max_length=50, blank=True)
    sign = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_PortableLadder"

    def __str__(self):
        return self.plants_name


class EquipmentOperator(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    check_off = models.CharField(max_length=50, blank=True)
    equipments = models.CharField(max_length=100, blank=True)
    other_equip = models.CharField(max_length=50, blank=True)
    ope_name = models.CharField(max_length=50, blank=True)
    emp_name = models.CharField(max_length=50, blank=True)
    date_traning = models.CharField(max_length=50, blank=True)
    course_name = models.CharField(max_length=50, blank=True)
    equip_model = models.CharField(max_length=50, blank=True)
    emp_repres = models.CharField(max_length=50, blank=True)
    emp_date = models.CharField(max_length=50, blank=True)
    oper_sign = models.CharField(max_length=50, blank=True)
    oper_date = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_EquipmentOperator"

    def __str__(self):
        return self.plants_name


class EyewashStation(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    jan_def = models.CharField(max_length=50, blank=True)
    jan_insp_by = models.CharField(max_length=50, blank=True)
    jan_sign = models.CharField(max_length=50, blank=True)
    feb_def = models.CharField(max_length=50, blank=True)
    feb_insp_by = models.CharField(max_length=50, blank=True)
    feb_sign = models.CharField(max_length=50, blank=True)
    mar_def = models.CharField(max_length=50, blank=True)
    mar_insp_by = models.CharField(max_length=50, blank=True)
    mar_sign = models.CharField(max_length=50, blank=True)
    apr_def = models.CharField(max_length=50, blank=True)
    apr_insp_by = models.CharField(max_length=50, blank=True)
    apr_sign = models.CharField(max_length=50, blank=True)
    may_def = models.CharField(max_length=50, blank=True)
    may_insp_by = models.CharField(max_length=50, blank=True)
    may_sign = models.CharField(max_length=50, blank=True)
    jun_def = models.CharField(max_length=50, blank=True)
    jun_insp_by = models.CharField(max_length=50, blank=True)
    jun_sign = models.CharField(max_length=50, blank=True)
    jul_def = models.CharField(max_length=50, blank=True)
    jul_insp_by = models.CharField(max_length=50, blank=True)
    jul_sign = models.CharField(max_length=50, blank=True)
    aug_def = models.CharField(max_length=50, blank=True)
    aug_insp_by = models.CharField(max_length=50, blank=True)
    aug_sign = models.CharField(max_length=50, blank=True)
    sep_def = models.CharField(max_length=50, blank=True)
    sep_insp_by = models.CharField(max_length=50, blank=True)
    sep_sign = models.CharField(max_length=50, blank=True)
    oct_def = models.CharField(max_length=50, blank=True)
    oct_insp_by = models.CharField(max_length=50, blank=True)
    oct_sign = models.CharField(max_length=50, blank=True)
    nov_def = models.CharField(max_length=50, blank=True)
    nov_insp_by = models.CharField(max_length=50, blank=True)
    nov_sign = models.CharField(max_length=50, blank=True)
    dec_def = models.CharField(max_length=50, blank=True)
    dec_insp_by = models.CharField(max_length=50, blank=True)
    dec_sign = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_EyewashStation"

    def __str__(self):
        return self.plants_name


class FireExtinguisher(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    jan_def = models.CharField(max_length=50, blank=True)
    jan_insp_by = models.CharField(max_length=50, blank=True)
    jan_sign = models.CharField(max_length=50, blank=True)
    feb_def = models.CharField(max_length=50, blank=True)
    feb_insp_by = models.CharField(max_length=50, blank=True)
    feb_sign = models.CharField(max_length=50, blank=True)
    mar_def = models.CharField(max_length=50, blank=True)
    mar_insp_by = models.CharField(max_length=50, blank=True)
    mar_sign = models.CharField(max_length=50, blank=True)
    apr_def = models.CharField(max_length=50, blank=True)
    apr_insp_by = models.CharField(max_length=50, blank=True)
    apr_sign = models.CharField(max_length=50, blank=True)
    may_def = models.CharField(max_length=50, blank=True)
    may_insp_by = models.CharField(max_length=50, blank=True)
    may_sign = models.CharField(max_length=50, blank=True)
    jun_def = models.CharField(max_length=50, blank=True)
    jun_insp_by = models.CharField(max_length=50, blank=True)
    jun_sign = models.CharField(max_length=50, blank=True)
    jul_def = models.CharField(max_length=50, blank=True)
    jul_insp_by = models.CharField(max_length=50, blank=True)
    jul_sign = models.CharField(max_length=50, blank=True)
    aug_def = models.CharField(max_length=50, blank=True)
    aug_insp_by = models.CharField(max_length=50, blank=True)
    aug_sign = models.CharField(max_length=50, blank=True)
    sep_def = models.CharField(max_length=50, blank=True)
    sep_insp_by = models.CharField(max_length=50, blank=True)
    sep_sign = models.CharField(max_length=50, blank=True)
    oct_def = models.CharField(max_length=50, blank=True)
    oct_insp_by = models.CharField(max_length=50, blank=True)
    oct_sign = models.CharField(max_length=50, blank=True)
    nov_def = models.CharField(max_length=50, blank=True)
    nov_insp_by = models.CharField(max_length=50, blank=True)
    nov_sign = models.CharField(max_length=50, blank=True)
    dec_def = models.CharField(max_length=50, blank=True)
    dec_insp_by = models.CharField(max_length=50, blank=True)
    dec_sign = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_FireExtinguisher"

    def __str__(self):
        return self.plants_name


class FirstAid(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    jan_supply = models.CharField(max_length=50, blank=True)
    jan_insp_by = models.CharField(max_length=50, blank=True)
    jan_sign = models.CharField(max_length=50, blank=True)
    feb_supply = models.CharField(max_length=50, blank=True)
    feb_insp_by = models.CharField(max_length=50, blank=True)
    feb_sign = models.CharField(max_length=50, blank=True)
    mar_supply = models.CharField(max_length=50, blank=True)
    mar_insp_by = models.CharField(max_length=50, blank=True)
    mar_sign = models.CharField(max_length=50, blank=True)
    apr_supply = models.CharField(max_length=50, blank=True)
    apr_insp_by = models.CharField(max_length=50, blank=True)
    apr_sign = models.CharField(max_length=50, blank=True)
    may_supply = models.CharField(max_length=50, blank=True)
    may_insp_by = models.CharField(max_length=50, blank=True)
    may_sign = models.CharField(max_length=50, blank=True)
    jun_supply = models.CharField(max_length=50, blank=True)
    jun_insp_by = models.CharField(max_length=50, blank=True)
    jun_sign = models.CharField(max_length=50, blank=True)
    jul_supply = models.CharField(max_length=50, blank=True)
    jul_insp_by = models.CharField(max_length=50, blank=True)
    jul_sign = models.CharField(max_length=50, blank=True)
    aug_supply = models.CharField(max_length=50, blank=True)
    aug_insp_by = models.CharField(max_length=50, blank=True)
    aug_sign = models.CharField(max_length=50, blank=True)
    sep_supply = models.CharField(max_length=50, blank=True)
    sep_insp_by = models.CharField(max_length=50, blank=True)
    sep_sign = models.CharField(max_length=50, blank=True)
    oct_supply = models.CharField(max_length=50, blank=True)
    oct_insp_by = models.CharField(max_length=50, blank=True)
    oct_sign = models.CharField(max_length=50, blank=True)
    nov_supply = models.CharField(max_length=50, blank=True)
    nov_insp_by = models.CharField(max_length=50, blank=True)
    nov_sign = models.CharField(max_length=50, blank=True)
    dec_supply = models.CharField(max_length=50, blank=True)
    dec_insp_by = models.CharField(max_length=50, blank=True)
    dec_sign = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_FirstAid"

    def __str__(self):
        return self.plants_name


class FormalSite(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    des_comment = models.TextField(blank=True)
    insp_one = models.CharField(max_length=50, blank=True)
    sign_one = models.CharField(max_length=50, blank=True)
    date_one = models.CharField(max_length=50, blank=True)
    insp_two = models.CharField(max_length=50, blank=True)
    sign_two = models.CharField(max_length=50, blank=True)
    date_two = models.CharField(max_length=50, blank=True)
    insp_three = models.CharField(max_length=50, blank=True)
    sign_three = models.CharField(max_length=50, blank=True)
    date_three = models.CharField(max_length=50, blank=True)
    insp_four = models.CharField(max_length=50, blank=True)
    sign_four = models.CharField(max_length=50, blank=True)
    date_four = models.CharField(max_length=50, blank=True)
    insp_five = models.CharField(max_length=50, blank=True)
    sign_five = models.CharField(max_length=50, blank=True)
    date_five = models.CharField(max_length=50, blank=True)
    sign = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=50, blank=True)
    date = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_FormalSite"

    def __str__(self):
        return self.plants_name


class GasMonitor(models.Model):
    id = models.AutoField(primary_key=True)
    plants_name = models.CharField(max_length=50, blank=True)
    date_cali_one = models.CharField(max_length=50, blank=True)
    location_one = models.CharField(max_length=50, blank=True)
    date_cali_exp_one = models.CharField(max_length=50, blank=True)
    date_cali_two = models.CharField(max_length=50, blank=True)
    location_two = models.CharField(max_length=50, blank=True)
    date_cali_exp_two = models.CharField(max_length=50, blank=True)
    date_cali_three = models.CharField(max_length=50, blank=True)
    location_three = models.CharField(max_length=50, blank=True)
    date_cali_exp_three = models.CharField(max_length=50, blank=True)
    date_cali_four = models.CharField(max_length=50, blank=True)
    location_four = models.CharField(max_length=50, blank=True)
    date_cali_exp_four = models.CharField(max_length=50, blank=True)
    date_cali_five = models.CharField(max_length=50, blank=True)
    location_five = models.CharField(max_length=50, blank=True)
    date_cali_exp_five = models.CharField(max_length=50, blank=True)
    date_cali_six = models.CharField(max_length=50, blank=True)
    location_six = models.CharField(max_length=50, blank=True)
    date_cali_exp_six = models.CharField(max_length=50, blank=True)
    date_cali_seven = models.CharField(max_length=50, blank=True)
    location_seven = models.CharField(max_length=50, blank=True)
    date_cali_exp_seven = models.CharField(max_length=50, blank=True)
    date_cali_eight = models.CharField(max_length=50, blank=True)
    location_eight = models.CharField(max_length=50, blank=True)
    date_cali_exp_eight = models.CharField(max_length=50, blank=True)
    date_cali_nine = models.CharField(max_length=50, blank=True)
    location_nine = models.CharField(max_length=50, blank=True)
    date_cali_exp_nine = models.CharField(max_length=50, blank=True)
    date_cali_ten = models.CharField(max_length=50, blank=True)
    location_ten = models.CharField(max_length=50, blank=True)
    date_cali_exp_ten = models.CharField(max_length=50, blank=True)
    date_cali_eleven = models.CharField(max_length=50, blank=True)
    location_eleven = models.CharField(max_length=50, blank=True)
    date_cali_exp_eleven = models.CharField(max_length=50, blank=True)
    date_cali_twelve = models.CharField(max_length=50, blank=True)
    location_twelve = models.CharField(max_length=50, blank=True)
    date_cali_exp_twelve = models.CharField(max_length=50, blank=True)
    inspection_id = models.IntegerField(max_length=10)

    class Meta:
        db_table = "insp_GasMonitor"

    def __str__(self):
        return self.plants_name