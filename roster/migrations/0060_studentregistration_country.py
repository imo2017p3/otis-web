# Generated by Django 3.2.5 on 2021-07-27 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0059_auto_20210727_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentregistration',
            name='country',
            field=models.CharField(
                choices=[('AFG', 'Afghanistan (AFG)'), ('ALB', 'Albania (ALB)'),
                            ('ALG', 'Algeria (ALG)'), ('AGO', 'Angola (AGO)'),
                            ('ARG', 'Argentina (ARG)'), ('ARM', 'Armenia (ARM)'),
                            ('AUS', 'Australia (AUS)'), ('AUT', 'Austria (AUT)'),
                            ('AZE', 'Azerbaijan (AZE)'), ('BAH', 'Bahrain (BAH)'),
                            ('BGD', 'Bangladesh (BGD)'), ('BLR', 'Belarus (BLR)'),
                            ('BEL', 'Belgium (BEL)'), ('BEN', 'Benin (BEN)'),
                            ('BOL', 'Bolivia (BOL)'), ('BIH', 'Bosnia and Herzegovina (BIH)'),
                            ('BWA', 'Botswana (BWA)'), ('BRA', 'Brazil (BRA)'),
                            ('BRU', 'Brunei (BRU)'), ('BGR', 'Bulgaria (BGR)'),
                            ('BFA', 'Burkina Faso (BFA)'), ('KHM', 'Cambodia (KHM)'),
                            ('CAN', 'Canada (CAN)'), ('CHI', 'Chile (CHI)'),
                            ('CHN', "People's Republic of China (CHN)"),
                            ('COL', 'Colombia (COL)'),
                            ('CIS', 'Commonwealth of Independent States (CIS)'),
                            ('CRI', 'Costa Rica (CRI)'), ('HRV', 'Croatia (HRV)'),
                            ('CUB', 'Cuba (CUB)'), ('CYP', 'Cyprus (CYP)'),
                            ('CZE', 'Czech Republic (CZE)'), ('CZS', 'Czechoslovakia (CZS)'),
                            ('DEN', 'Denmark (DEN)'), ('DOM', 'Dominican Republic (DOM)'),
                            ('ECU', 'Ecuador (ECU)'), ('EGY', 'Egypt (EGY)'),
                            ('EST', 'Estonia (EST)'), ('FIN', 'Finland (FIN)'),
                            ('FRA', 'France (FRA)'), ('GMB', 'Gambia (GMB)'),
                            ('GEO', 'Georgia (GEO)'),
                            ('GDR', 'German Democratic Republic (GDR)'),
                            ('GER', 'Germany (GER)'), ('GHA', 'Ghana (GHA)'),
                            ('HEL', 'Greece (HEL)'), ('GTM', 'Guatemala (GTM)'),
                            ('HND', 'Honduras (HND)'), ('HKG', 'Hong Kong (HKG)'),
                            ('HUN', 'Hungary (HUN)'), ('ISL', 'Iceland (ISL)'),
                            ('IND', 'India (IND)'), ('IDN', 'Indonesia (IDN)'),
                            ('IRQ', 'Iraq (IRQ)'), ('IRN', 'Islamic Republic of Iran (IRN)'),
                            ('IRL', 'Ireland (IRL)'), ('ISR', 'Israel (ISR)'),
                            ('ITA', 'Italy (ITA)'), ('CIV', 'Ivory Coast (CIV)'),
                            ('JAM', 'Jamaica (JAM)'), ('JPN', 'Japan (JPN)'),
                            ('KAZ', 'Kazakhstan (KAZ)'), ('KEN', 'Kenya (KEN)'),
                            ('PRK', "Democratic People's Republic of Korea (PRK)"),
                            ('KOR', 'Republic of Korea (KOR)'), ('KSV', 'Kosovo (KSV)'),
                            ('KWT', 'Kuwait (KWT)'), ('KGZ', 'Kyrgyzstan (KGZ)'),
                            ('LAO', 'Laos (LAO)'), ('LVA', 'Latvia (LVA)'),
                            ('LIE', 'Liechtenstein (LIE)'), ('LTU', 'Lithuania (LTU)'),
                            ('LUX', 'Luxembourg (LUX)'), ('MAC', 'Macau (MAC)'),
                            ('MDG', 'Madagascar (MDG)'), ('MAS', 'Malaysia (MAS)'),
                            ('MRT', 'Mauritania (MRT)'), ('MEX', 'Mexico (MEX)'),
                            ('MDA', 'Republic of Moldova (MDA)'), ('MNG', 'Mongolia (MNG)'),
                            ('MNE', 'Montenegro (MNE)'), ('MAR', 'Morocco (MAR)'),
                            ('MOZ', 'Mozambique (MOZ)'), ('MMR', 'Myanmar (MMR)'),
                            ('NPL', 'Nepal (NPL)'), ('NLD', 'Netherlands (NLD)'),
                            ('NZL', 'New Zealand (NZL)'), ('NIC', 'Nicaragua (NIC)'),
                            ('NGA', 'Nigeria (NGA)'), ('MKD', 'North Macedonia (MKD)'),
                            ('NOR', 'Norway (NOR)'), ('OMN', 'Oman (OMN)'),
                            ('PAK', 'Pakistan (PAK)'), ('PAN', 'Panama (PAN)'),
                            ('PAR', 'Paraguay (PAR)'), ('PER', 'Peru (PER)'),
                            ('PHI', 'Philippines (PHI)'), ('POL', 'Poland (POL)'),
                            ('POR', 'Portugal (POR)'), ('PRI', 'Puerto Rico (PRI)'),
                            ('ROU', 'Romania (ROU)'), ('RUS', 'Russian Federation (RUS)'),
                            ('RWA', 'Rwanda (RWA)'), ('SLV', 'El Salvador (SLV)'),
                            ('SAU', 'Saudi Arabia (SAU)'), ('SEN', 'Senegal (SEN)'),
                            ('SRB', 'Serbia (SRB)'), ('SCG', 'Serbia and Montenegro (SCG)'),
                            ('SGP', 'Singapore (SGP)'), ('SVK', 'Slovakia (SVK)'),
                            ('SVN', 'Slovenia (SVN)'), ('SAF', 'South Africa (SAF)'),
                            ('ESP', 'Spain (ESP)'), ('LKA', 'Sri Lanka (LKA)'),
                            ('SWE', 'Sweden (SWE)'), ('SUI', 'Switzerland (SUI)'),
                            ('SYR', 'Syria (SYR)'), ('TWN', 'Taiwan (TWN)'),
                            ('TJK', 'Tajikistan (TJK)'), ('TZA', 'Tanzania (TZA)'),
                            ('THA', 'Thailand (THA)'), ('TTO', 'Trinidad and Tobago (TTO)'),
                            ('TUN', 'Tunisia (TUN)'), ('TUR', 'Turkey (TUR)'),
                            ('NCY', 'Turkish Republic of Northern Cyprus (NCY)'),
                            ('TKM', 'Turkmenistan (TKM)'), ('UGA', 'Uganda (UGA)'),
                            ('UKR', 'Ukraine (UKR)'), ('UAE', 'United Arab Emirates (UAE)'),
                            ('UNK', 'United Kingdom (UNK)'),
                            ('USA', 'United States of America (USA)'), ('URY', 'Uruguay (URY)'),
                            ('USS', 'Union of Soviet Socialist Republics (USS)'),
                            ('UZB', 'Uzbekistan (UZB)'), ('VEN', 'Venezuela (VEN)'),
                            ('VNM', 'Vietnam (VNM)'), ('YEM', 'Yemen (YEM)'),
                            ('YUG', 'Yugoslavia (YUG)'), ('ZWE', 'Zimbabwe (ZWE)')],
                default='USA',
                max_length=6),
        ),
    ]
