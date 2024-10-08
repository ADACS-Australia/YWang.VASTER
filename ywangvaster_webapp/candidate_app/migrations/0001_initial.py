# Generated by Django 4.2 on 2024-08-14 02:38

import candidate_app.models
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CandidateMinMaxStats",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("min_chi_square", models.FloatField(blank=True, null=True)),
                ("max_chi_square", models.FloatField(blank=True, null=True)),
                ("min_chi_square_sigma", models.FloatField(blank=True, null=True)),
                ("max_chi_square_sigma", models.FloatField(blank=True, null=True)),
                ("min_chi_square_log_sigma", models.FloatField(blank=True, null=True)),
                ("max_chi_square_log_sigma", models.FloatField(blank=True, null=True)),
                ("min_peak_map", models.FloatField(blank=True, null=True)),
                ("max_peak_map", models.FloatField(blank=True, null=True)),
                ("min_peak_map_sigma", models.FloatField(blank=True, null=True)),
                ("max_peak_map_sigma", models.FloatField(blank=True, null=True)),
                ("min_peak_map_log_sigma", models.FloatField(blank=True, null=True)),
                ("max_peak_map_log_sigma", models.FloatField(blank=True, null=True)),
                ("min_gaussian_map", models.FloatField(blank=True, null=True)),
                ("max_gaussian_map", models.FloatField(blank=True, null=True)),
                ("min_gaussian_map_sigma", models.FloatField(blank=True, null=True)),
                ("max_gaussian_map_sigma", models.FloatField(blank=True, null=True)),
                ("min_std_map", models.FloatField(blank=True, null=True)),
                ("max_std_map", models.FloatField(blank=True, null=True)),
                ("min_bright_sep_arcmin", models.FloatField(blank=True, null=True)),
                ("max_bright_sep_arcmin", models.FloatField(blank=True, null=True)),
                ("min_beam_sep_deg", models.FloatField(blank=True, null=True)),
                ("max_beam_sep_deg", models.FloatField(blank=True, null=True)),
                ("min_deep_int_flux", models.FloatField(blank=True, null=True)),
                ("max_deep_int_flux", models.FloatField(blank=True, null=True)),
                ("min_deep_peak_flux", models.FloatField(blank=True, null=True)),
                ("max_deep_peak_flux", models.FloatField(blank=True, null=True)),
                ("min_deep_sep_arcsec", models.FloatField(blank=True, null=True)),
                ("max_deep_sep_arcsec", models.FloatField(blank=True, null=True)),
                ("min_md_deep", models.FloatField(blank=True, null=True)),
                ("max_md_deep", models.FloatField(blank=True, null=True)),
            ],
            options={
                "db_table": "candidate_min_max_stats",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Beam",
            fields=[
                ("hash_id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("obs_id", models.CharField()),
                ("proj_id", models.CharField(max_length=64)),
                ("index", models.IntegerField()),
                ("description", models.CharField(blank=True, max_length=1024, null=True, verbose_name="Description")),
                ("total_file_count", models.IntegerField(blank=True, null=True)),
                ("total_file_size_bytes", models.BigIntegerField(blank=True, null=True)),
                (
                    "final_cand_csv",
                    models.FileField(
                        blank=True, max_length=1024, null=True, upload_to=candidate_app.models.beam_upload_path
                    ),
                ),
                (
                    "std_fits",
                    models.FileField(
                        blank=True, max_length=1024, null=True, upload_to=candidate_app.models.beam_upload_path
                    ),
                ),
                (
                    "chisquare_map1_png",
                    models.FileField(
                        blank=True, max_length=1024, null=True, upload_to=candidate_app.models.beam_upload_path
                    ),
                ),
                (
                    "chisquare_map2_png",
                    models.FileField(
                        blank=True, max_length=1024, null=True, upload_to=candidate_app.models.beam_upload_path
                    ),
                ),
                (
                    "chisquare_fits",
                    models.FileField(
                        blank=True, max_length=1024, null=True, upload_to=candidate_app.models.beam_upload_path
                    ),
                ),
                (
                    "peak_map1_png",
                    models.FileField(
                        blank=True, max_length=1024, null=True, upload_to=candidate_app.models.beam_upload_path
                    ),
                ),
                (
                    "peak_map2_png",
                    models.FileField(
                        blank=True, max_length=1024, null=True, upload_to=candidate_app.models.beam_upload_path
                    ),
                ),
                (
                    "peak_fits",
                    models.FileField(
                        blank=True, max_length=1024, null=True, upload_to=candidate_app.models.beam_upload_path
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Candidate",
            fields=[
                ("hash_id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("proj_id", models.CharField(max_length=64)),
                ("obs_id", models.CharField()),
                ("beam_index", models.IntegerField()),
                ("total_file_count", models.IntegerField(blank=True, null=True)),
                ("total_file_size_bytes", models.BigIntegerField(blank=True, null=True)),
                ("lightcurve_data", models.JSONField(blank=True, null=True)),
                (
                    "lightcurve_png",
                    models.FileField(blank=True, null=True, upload_to=candidate_app.models.cand_upload_path),
                ),
                (
                    "slices_gif",
                    models.FileField(blank=True, null=True, upload_to=candidate_app.models.cand_upload_path),
                ),
                (
                    "slices_fits",
                    models.FileField(blank=True, null=True, upload_to=candidate_app.models.cand_upload_path),
                ),
                (
                    "deepcutout_png",
                    models.FileField(blank=True, null=True, upload_to=candidate_app.models.cand_upload_path),
                ),
                (
                    "deepcutout_fits",
                    models.FileField(blank=True, null=True, upload_to=candidate_app.models.cand_upload_path),
                ),
                ("name", models.CharField(max_length=100)),
                ("ra_str", models.CharField(max_length=100)),
                ("dec_str", models.CharField(max_length=100)),
                ("ra", models.FloatField()),
                ("dec", models.FloatField()),
                ("chi_square", models.FloatField()),
                ("chi_square_log_sigma", models.FloatField()),
                ("chi_square_sigma", models.FloatField()),
                ("peak_map", models.FloatField()),
                ("peak_map_log_sigma", models.FloatField()),
                ("peak_map_sigma", models.FloatField()),
                ("gaussian_map", models.FloatField(blank=True, null=True)),
                ("gaussian_map_sigma", models.FloatField(blank=True, null=True)),
                ("std_map", models.FloatField()),
                ("bright_sep_arcmin", models.FloatField()),
                ("beam_ra", models.FloatField()),
                ("beam_dec", models.FloatField()),
                ("beam_sep_deg", models.FloatField()),
                ("deep_ra_deg", models.FloatField()),
                ("deep_dec_deg", models.FloatField()),
                ("deep_sep_arcsec", models.FloatField()),
                ("deep_name", models.CharField(max_length=100)),
                ("deep_num", models.IntegerField()),
                ("deep_peak_flux", models.FloatField()),
                ("deep_int_flux", models.FloatField()),
                ("md_deep", models.FloatField()),
                (
                    "beam",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cand_beams",
                        to="candidate_app.beam",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("hash_id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=256, null=True, unique=True, verbose_name="Classification tag"
                    ),
                ),
                ("description", models.CharField(blank=True, max_length=1024, null=True, verbose_name="Description")),
            ],
        ),
        migrations.CreateModel(
            name="Upload",
            fields=[
                ("hash_id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("date", models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="upload",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rating",
            fields=[
                ("hash_id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                (
                    "rating",
                    models.CharField(
                        choices=[("T", "true"), ("F", "false"), ("U", "unsure")], default=None, max_length=1
                    ),
                ),
                ("date", models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ("notes", models.CharField(max_length=1024)),
                (
                    "candidate",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rating",
                        to="candidate_app.candidate",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="rating",
                        to="candidate_app.tag",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="rating",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                ("hash_id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("id", models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name="id")),
                ("name", models.CharField(blank=True, max_length=64, null=True, verbose_name="Project name")),
                ("description", models.CharField(blank=True, max_length=256, null=True, verbose_name="Description")),
                (
                    "upload",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="proj_upload",
                        to="candidate_app.upload",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Observation",
            fields=[
                ("hash_id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("proj_id", models.CharField(max_length=64)),
                ("id", models.CharField()),
                ("obs_start", models.DateTimeField(blank=True, null=True)),
                (
                    "project",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="obs_proj",
                        to="candidate_app.project",
                    ),
                ),
                (
                    "upload",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="obs_upload",
                        to="candidate_app.upload",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="candidate",
            name="observation",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cand_obs",
                to="candidate_app.observation",
            ),
        ),
        migrations.AddField(
            model_name="candidate",
            name="project",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cand_proj",
                to="candidate_app.project",
            ),
        ),
        migrations.AddField(
            model_name="candidate",
            name="upload",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cand_upload",
                to="candidate_app.upload",
            ),
        ),
        migrations.AddField(
            model_name="beam",
            name="observation",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="beam_obs",
                to="candidate_app.observation",
            ),
        ),
        migrations.AddField(
            model_name="beam",
            name="project",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="beam_proj",
                to="candidate_app.project",
            ),
        ),
        migrations.AddField(
            model_name="beam",
            name="upload",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="beam_upload",
                to="candidate_app.upload",
            ),
        ),
    ]
