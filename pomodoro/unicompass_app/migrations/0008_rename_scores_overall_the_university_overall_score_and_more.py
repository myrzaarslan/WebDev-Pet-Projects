# Generated by Django 5.1 on 2024-09-09 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unicompass_app', '0007_qs_university_score_nid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='the_university',
            old_name='scores_overall',
            new_name='overall_score',
        ),
        migrations.RenameField(
            model_name='the_university',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='qs_university',
            name='nid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_agriculture',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_anatomy',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_archaeology',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_architecture',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_art_design',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_art_history',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_arts',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_arts_humanities',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_bio_sci',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_chem_eng',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_chemistry',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_civil_eng',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_classics',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_comp_sci',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_data_sci',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_dentistry',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_earth_marine_sci',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_elec_eng',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_eng_tech',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_english',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_env_sci',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_geography',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_geology',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_geophysics',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_history',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_life_sci',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_linguistics',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_materials_sci',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_math',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_mech_eng',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_medicine',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_mining_eng',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_modern_languages',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_music',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_nat_sci',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_nursing',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_performing_arts',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_pet_eng',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_pharmacy',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_philosophy',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_physics_astronomy',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_psychology',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_theology',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='qs_university',
            name='rank_vet_sci',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='the_university',
            name='rank_arts',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='the_university',
            name='rank_bus',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='the_university',
            name='rank_clin',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='the_university',
            name='rank_comp',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='the_university',
            name='rank_edu',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='the_university',
            name='rank_eng',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='the_university',
            name='rank_law',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='the_university',
            name='rank_life',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='the_university',
            name='rank_phys',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='the_university',
            name='rank_psych',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
