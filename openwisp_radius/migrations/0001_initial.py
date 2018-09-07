# Generated by Django 2.0.8 on 2018-09-06 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import openwisp_users.mixins
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('openwisp_users', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Nas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(db_column='nasname', db_index=True, help_text='NAS Name (or IP address)', max_length=128, verbose_name='name')),
                ('short_name', models.CharField(db_column='shortname', max_length=32, verbose_name='short name')),
                ('type', models.CharField(default='other', max_length=30, verbose_name='type')),
                ('ports', models.PositiveIntegerField(blank=True, null=True, verbose_name='ports')),
                ('secret', models.CharField(help_text='Shared Secret', max_length=60, verbose_name='secret')),
                ('server', models.CharField(blank=True, max_length=64, null=True, verbose_name='server')),
                ('community', models.CharField(blank=True, max_length=50, null=True, verbose_name='community')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='description')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openwisp_users.Organization', verbose_name='organization')),
            ],
            options={
                'verbose_name': 'NAS',
                'db_table': 'nas',
                'swappable': 'OPENWISP_RADIUS_NAS_MODEL',
                'verbose_name_plural': 'NAS',
                'abstract': False,
            },
            bases=(openwisp_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RadiusAccounting',
            fields=[
                ('id', models.BigAutoField(db_column='radacctid', primary_key=True, serialize=False)),
                ('session_id', models.CharField(db_column='acctsessionid', db_index=True, max_length=64, verbose_name='session ID')),
                ('unique_id', models.CharField(db_column='acctuniqueid', max_length=32, unique=True, verbose_name='accounting unique ID')),
                ('username', models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='username')),
                ('groupname', models.CharField(blank=True, max_length=64, null=True, verbose_name='group name')),
                ('realm', models.CharField(blank=True, max_length=64, null=True, verbose_name='realm')),
                ('nas_ip_address', models.GenericIPAddressField(db_column='nasipaddress', db_index=True, verbose_name='NAS IP address')),
                ('nas_port_id', models.CharField(blank=True, db_column='nasportid', max_length=15, null=True, verbose_name='NAS port ID')),
                ('nas_port_type', models.CharField(blank=True, db_column='nasporttype', max_length=32, null=True, verbose_name='NAS port type')),
                ('start_time', models.DateTimeField(blank=True, db_column='acctstarttime', db_index=True, null=True, verbose_name='start time')),
                ('update_time', models.DateTimeField(blank=True, db_column='acctupdatetime', null=True, verbose_name='update time')),
                ('stop_time', models.DateTimeField(blank=True, db_column='acctstoptime', db_index=True, null=True, verbose_name='stop time')),
                ('interval', models.IntegerField(blank=True, db_column='acctinterval', null=True, verbose_name='interval')),
                ('session_time', models.PositiveIntegerField(blank=True, db_column='acctsessiontime', null=True, verbose_name='session time')),
                ('authentication', models.CharField(blank=True, db_column='acctauthentic', max_length=32, null=True, verbose_name='authentication')),
                ('connection_info_start', models.CharField(blank=True, db_column='connectinfo_start', max_length=50, null=True, verbose_name='connection info start')),
                ('connection_info_stop', models.CharField(blank=True, db_column='connectinfo_stop', max_length=50, null=True, verbose_name='connection info stop')),
                ('input_octets', models.BigIntegerField(blank=True, db_column='acctinputoctets', null=True, verbose_name='input octets')),
                ('output_octets', models.BigIntegerField(blank=True, db_column='acctoutputoctets', null=True, verbose_name='output octets')),
                ('called_station_id', models.CharField(blank=True, db_column='calledstationid', db_index=True, max_length=50, null=True, verbose_name='called station ID')),
                ('calling_station_id', models.CharField(blank=True, db_column='callingstationid', db_index=True, max_length=50, null=True, verbose_name='calling station ID')),
                ('terminate_cause', models.CharField(blank=True, db_column='acctterminatecause', max_length=32, null=True, verbose_name='termination cause')),
                ('service_type', models.CharField(blank=True, db_column='servicetype', max_length=32, null=True, verbose_name='service type')),
                ('framed_protocol', models.CharField(blank=True, db_column='framedprotocol', max_length=32, null=True, verbose_name='framed protocol')),
                ('framed_ip_address', models.GenericIPAddressField(blank=True, db_column='framedipaddress', db_index=True, null=True, verbose_name='framed IP address')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openwisp_users.Organization', verbose_name='organization')),
            ],
            options={
                'verbose_name': 'accounting',
                'db_table': 'radacct',
                'swappable': 'OPENWISP_RADIUS_RADIUSACCOUNTING_MODEL',
                'verbose_name_plural': 'accountings',
                'abstract': False,
            },
            bases=(openwisp_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RadiusBatch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(db_index=True, help_text='A unique batch name', max_length=128, verbose_name='name')),
                ('strategy', models.CharField(choices=[('prefix', 'Generate from prefix'), ('csv', 'Import from CSV')], db_index=True, help_text='Import users from a CSV or generate using a prefix', max_length=16, verbose_name='strategy')),
                ('csvfile', models.FileField(blank=True, help_text='The csv file containing the user details to be uploaded', null=True, upload_to='', verbose_name='CSV')),
                ('prefix', models.CharField(blank=True, help_text='Usernames generated will be of the format [prefix][number]', max_length=20, null=True, verbose_name='prefix')),
                ('pdf', models.FileField(blank=True, help_text='The pdf file containing list of usernames and passwords', null=True, upload_to='', verbose_name='PDF')),
                ('expiration_date', models.DateField(blank=True, help_text='If left blank users will never expire', null=True, verbose_name='expiration date')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openwisp_users.Organization', verbose_name='organization')),
                ('users', models.ManyToManyField(blank=True, help_text='List of users uploaded in this batch', related_name='radius_batch', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'batch user creation',
                'db_table': 'radbatch',
                'swappable': 'OPENWISP_RADIUS_RADIUSBATCH_MODEL',
                'verbose_name_plural': 'batch user creation operations',
                'abstract': False,
                'unique_together': {('name', 'organization')}
            },
            bases=(openwisp_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RadiusCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('username', models.CharField(db_index=True, max_length=64, verbose_name='username')),
                ('value', models.CharField(max_length=253, verbose_name='value')),
                ('op', models.CharField(choices=[('=', '='), (':=', ':='), ('==', '=='), ('+=', '+='), ('!=', '!='), ('>', '>'), ('>=', '>='), ('<', '<'), ('<=', '<='), ('=~', '=~'), ('!~', '!~'), ('=*', '=*'), ('!*', '!*')], default=':=', max_length=2, verbose_name='operator')),
                ('attribute', models.CharField(choices=[('Max-Daily-Session', 'Max-Daily-Session'), ('Max-All-Session', 'Max-All-Session'), ('Max-Daily-Session-Traffic', 'Max-Daily-Session-Traffic'), ('Cleartext-Password', 'Cleartext-Password'), ('NT-Password', 'NT-Password'), ('LM-Password', 'LM-Password'), ('MD5-Password', 'MD5-Password'), ('SMD5-Password', 'SMD5-Password'), ('SHA-Password', 'SHA-Password'), ('SSHA-Password', 'SSHA-Password'), ('Crypt-Password', 'Crypt-Password')], default='NT-Password', max_length=64, verbose_name='attribute')),
                ('is_active', models.BooleanField(default=True)),
                ('valid_until', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openwisp_users.Organization', verbose_name='organization')),
            ],
            options={
                'verbose_name': 'check',
                'db_table': 'radcheck',
                'swappable': 'OPENWISP_RADIUS_RADIUSCHECK_MODEL',
                'verbose_name_plural': 'checks',
                'abstract': False,
            },
            bases=(openwisp_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RadiusGroupCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('groupname', models.CharField(db_index=True, max_length=64, verbose_name='group name')),
                ('attribute', models.CharField(max_length=64, verbose_name='attribute')),
                ('op', models.CharField(choices=[('=', '='), (':=', ':='), ('==', '=='), ('+=', '+='), ('!=', '!='), ('>', '>'), ('>=', '>='), ('<', '<'), ('<=', '<='), ('=~', '=~'), ('!~', '!~'), ('=*', '=*'), ('!*', '!*')], default=':=', max_length=2, verbose_name='operator')),
                ('value', models.CharField(max_length=253, verbose_name='value')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openwisp_users.Organization', verbose_name='organization')),
            ],
            options={
                'verbose_name': 'group check',
                'db_table': 'radgroupcheck',
                'swappable': 'OPENWISP_RADIUS_RADIUSGROUPCHECK_MODEL',
                'verbose_name_plural': 'group checks',
                'abstract': False,
            },
            bases=(openwisp_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RadiusGroupReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('groupname', models.CharField(db_index=True, max_length=64, verbose_name='group name')),
                ('attribute', models.CharField(max_length=64, verbose_name='attribute')),
                ('op', models.CharField(choices=[('=', '='), (':=', ':='), ('+=', '+=')], default='=', max_length=2, verbose_name='operator')),
                ('value', models.CharField(max_length=253, verbose_name='value')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openwisp_users.Organization', verbose_name='organization')),
            ],
            options={
                'verbose_name': 'group reply',
                'db_table': 'radgroupreply',
                'swappable': 'OPENWISP_RADIUS_RADIUSGROUPREPLY_MODEL',
                'verbose_name_plural': 'group replies',
                'abstract': False,
            },
            bases=(openwisp_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RadiusPostAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='username')),
                ('password', models.CharField(blank=True, db_column='pass', max_length=64, verbose_name='password')),
                ('reply', models.CharField(max_length=32, verbose_name='reply')),
                ('called_station_id', models.CharField(blank=True, db_column='calledstationid', max_length=50, null=True, verbose_name='called station ID')),
                ('calling_station_id', models.CharField(blank=True, db_column='callingstationid', max_length=50, null=True, verbose_name='calling station ID')),
                ('date', models.DateTimeField(auto_now_add=True, db_column='authdate', verbose_name='date')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openwisp_users.Organization', verbose_name='organization')),
            ],
            options={
                'verbose_name': 'post auth',
                'db_table': 'radpostauth',
                'swappable': 'OPENWISP_RADIUS_RADIUSPOSTAUTH_MODEL',
                'verbose_name_plural': 'post auth log',
                'abstract': False,
            },
            bases=(openwisp_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RadiusProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(db_index=True, help_text='A unique profile name', max_length=128, verbose_name='name')),
                ('daily_session_limit', models.BigIntegerField(blank=True, help_text='Hours', null=True, verbose_name='daily session limit')),
                ('daily_bandwidth_limit', models.BigIntegerField(blank=True, help_text='Megabytes (MB)', null=True, verbose_name='daily bandwidth limit')),
                ('max_all_time_limit', models.BigIntegerField(blank=True, help_text='Hours', null=True, verbose_name='maximum all time session limit')),
                ('default', models.BooleanField(default=False, verbose_name='Use this profile as the default profile')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openwisp_users.Organization', verbose_name='organization')),
            ],
            options={
                'verbose_name': 'limit profile',
                'abstract': False,
                'swappable': 'OPENWISP_RADIUS_RADIUSPROFILE_MODEL',
                'verbose_name_plural': 'limit profiles',
                'unique_together': {('name', 'organization')}
            },
            bases=(openwisp_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RadiusReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('username', models.CharField(db_index=True, max_length=64, verbose_name='username')),
                ('value', models.CharField(max_length=253, verbose_name='value')),
                ('op', models.CharField(choices=[('=', '='), (':=', ':='), ('+=', '+=')], default='=', max_length=2, verbose_name='operator')),
                ('attribute', models.CharField(max_length=64, verbose_name='attribute')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openwisp_users.Organization', verbose_name='organization')),
            ],
            options={
                'verbose_name': 'reply',
                'db_table': 'radreply',
                'swappable': 'OPENWISP_RADIUS_RADIUSREPLY_MODEL',
                'verbose_name_plural': 'replies',
                'abstract': False,
            },
            bases=(openwisp_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RadiusUserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('username', models.CharField(db_index=True, max_length=64, verbose_name='username')),
                ('groupname', models.CharField(max_length=64, verbose_name='group name')),
                ('priority', models.IntegerField(default=1, verbose_name='priority')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openwisp_users.Organization', verbose_name='organization')),
            ],
            options={
                'verbose_name': 'user group',
                'db_table': 'radusergroup',
                'swappable': 'OPENWISP_RADIUS_RADIUSUSERGROUP_MODEL',
                'verbose_name_plural': 'user groups',
                'abstract': False,
            },
            bases=(openwisp_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RadiusUserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='openwisp_users.Organization', verbose_name='organization')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.OPENWISP_RADIUS_RADIUSPROFILE_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='radius_user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user profile',
                'db_table': 'radiususerprofile',
                'swappable': 'OPENWISP_RADIUS_RADIUSUSERPROFILE_MODEL',
                'verbose_name_plural': 'user profiles',
                'abstract': False,
            },
            bases=(openwisp_users.mixins.ValidateOrgMixin, models.Model),
        ),
    ]
