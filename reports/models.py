from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.core.exceptions import ValidationError

class Report(models.Model):
  class Quarter(models.IntegerChoices):
    Q1 = 1, _('Q1 (January - March)')
    Q2 = 2, _('Q2 (April - June)')
    Q3 = 3, _('Q3 (July - September)')
    Q4 = 4, _('Q4 (October - December)')

  class Status(models.TextChoices):
    SUBMITTED = 'SUBM', _('Submitted')
    APPROVED = 'APPR', _('Approved')
    REJECTED = 'REJ', _('Rejected')

  class Sector(models.TextChoices):
    HEALTH = 'HEL', _('Health')
    EDUCATION = 'EDU', _('Education')
    GENDER = 'GEN', _('Gender')
    ENVIRONMENT = 'ENV', _('Environment')
    AGRICULTURE = 'AGR', _('Agriculture')
    WATER = 'WAT', _('Water and satitation')
    ECONOMIC = 'ECO', _('Economic empowerment')
    SOCIAL = 'SOC', _('Social Protection')
    GOVERNANCE = 'GOV', _('Governane')
    INFRASTRUCTURE = 'INF', _('Infrastructure')
    OTHER = 'OTH', _('Other')

  class WardChoices(models.TextChoices):
    NYAKATO = 'NYAKATO', _('Nyakato')
    BUSWELU = 'BUSWELU', _('Buswelu')
    ILEMELA = 'ILEMELA', _('Ilemela')
    PASIANSI = 'PASIANSI', _('Pasiansi')
    BUGOBWA = 'BUGOBWA', _('Bugogwa')  # Fixed typo (Bugogwa → BUGOBWA)
    SANGABUYE = 'SANGABUYE', _('Sangabuye')
    MECCO = 'MECCO', _('MECCO')
    BUZURUGA = 'BUZURUGA', _('Buzuruga')
    NYASAKA = 'NYASAKA', _('Nyasaka')
    KAHAMA = 'KAHAMA', _('Kahama')
    KISEKE = 'KISEKE', _('Kiseke')
    KAYENZE = 'KAYENZE', _('Kayenze')
    SHIBULA = 'SHIBULA', _('Shibula')
    KAWEEKAMO = 'KAWEEKAMO', _('Kawekamo')
    KITANGIRI = 'KITANGIRI', _('Kitangiri')
    KIRUMBA = 'KIRUMBA', _('Kirumba')
    NYAMANORO = 'NYAMANORO', _('Nyamanoro')
    IBUNGILO = 'IBUNGILO', _('Ibungilo')
    NYAMHONGOLO = 'NYAMHONGOLO', _('Nyamhongolo')

  class Indicators(models.TextChoices):
    PERFORMANCE = 'PER', _('Performance Indicators')
    MUNICIPALITY = 'MUN', _('Municipality Indicators')
    NATIONAL = 'NAT', _('National Indicators')
    SDG = 'SDG', _('SDG Indicators')

  class SDGChoices(models.TextChoices):
    SDG_1 = '1', _('No Poverty')
    SDG_2 = '2', _('Zero Hunger')
    SDG_3 = '3', _('Good Health and Well-being')
    SDG_4 = '4', _('Quality Education')
    SDG_5 = '5', _('Gender Equality')
    SDG_6 = '6', _('Clean Water and Sanitation')
    SDG_7 = '7', _('Affordable and Clean Energy')
    SDG_8 = '8', _('Decent Work and Economic Growth')
    SDG_9 = '9', _('Industry, Innovation and Infrastructure')
    SDG_10 = '10', _('Reduced Inequalities')
    SDG_11 = '11', _('Sustainable Cities and Communities')
    SDG_12 = '12', _('Responsible Consumption and Production')
    SDG_13 = '13', _('Climate Action')
    SDG_14 = '14', _('Life Below Water')
    SDG_15 = '15', _('Life on Land')
    SDG_16 = '16', _('Peace, Justice and Strong Institutions')
    SDG_17 = '17', _('Partnerships for the Goals')

  class SDGIndicatorChoices(models.TextChoices):
    CLIMATE_CHANGE_RESILIENCE = 'CLIMATE_CHANGE_RESILIENCE', _('Climate Change Resilience')
    ACCESS_TO_LAND_AND_CREDIT = 'ACCESS_TO_LAND_AND_CREDIT', _('Access to land and credit')
    CROP_YIELD_AGRICULTURAL_PRODUCTIVITY = 'CROP_YIELD_AGRICULTURAL_PRODUCTIVITY', _('Crop Yield & Agricultural Productivity')
    FOOD_SECURITY_MALNUTRITION_RATES = 'FOOD_SECURITY_MALNUTRITION_RATES', _('Food Security & Malnutrition Rates')
    REPRESENTATION_WOMEN_LEADERSHIP = 'REPRESENTATION_WOMEN_LEADERSHIP', _('Representation of women in leadership')
    GENDER_BASED_VIOLENCE_REDUCED = 'GENDER_BASED_VIOLENCE_REDUCED', _('Gender-Based Violence Reduced')

  organization = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='reports',on_delete=models.CASCADE)
  project = models.CharField(_("Project Title"), max_length=200)
  quarter = models.IntegerField(choices=Quarter.choices)
  year = models.PositiveIntegerField(validators=[MinValueValidator(2020),MaxValueValidator(2030)])
  title = models.CharField(_("Report Title"), max_length=200)
  status = models.CharField(max_length=5,choices=Status.choices,default=Status.SUBMITTED)
  approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,verbose_name=_('Approved/Rejected by'))
  sector = models.CharField(max_length=5,choices=Sector.choices)
  district = models.CharField(_("District"),max_length=20,default="Ilemela",editable=False)
  ward = models.CharField(_("Ward"),max_length=20,choices=WardChoices.choices)
  street = models.CharField(_("Street"), max_length=100)
  summary = models.TextField(_("Executive Summary"))
  activities = models.TextField(_("Activities Conducted"))
  amount_used = models.DecimalField( _("Amount Used (TZS)"),max_digits=14,decimal_places=2)
  indicators = models.CharField(max_length=5,choices=Indicators.choices)
  per_indicators = models.CharField(max_length=200)
  target = models.IntegerField(_("Target"), default=0)
  achieved = models.IntegerField(_("Achieved"), default=0)
  outcomes = models.TextField(_("Outcomes and Impact"))
  challenges = models.TextField(_("Challenges and Solutions"))
  men = models.IntegerField(_("Men Beneficiaries"), default=0)  
  women = models.IntegerField(_("Women Beneficiaries"), default=0)
  youth = models.IntegerField(_("Youth Beneficiaries"), default=0)
  sdg_alignment = models.CharField(max_length=2,choices=SDGChoices.choices,verbose_name=_('Sustainable Development Goal'))
  indicator = models.CharField(max_length=50, choices=SDGIndicatorChoices.choices, verbose_name=_('SDG Indicator'))
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def clean(self):
    # NEW: Validation for achieved <= target
    if self.achieved > self.target:
      raise ValidationError(_('Achieved value cannot exceed target'))
    
    # NEW: Validation for beneficiary numbers
    total_beneficiaries = self.men + self.women + self.youth
    if total_beneficiaries <= 0:
      raise ValidationError(_('Must have at least one beneficiary'))

  @property
  def total_beneficiaries(self):
    return self.men + self.women + self.youth

  class Meta:
    ordering = ['-year', '-quarter']

  def __str__(self):
    return f'{self.title}, {self.year}, {self.quarter}'
    
class ReportPhoto(models.Model):
  report = models.ForeignKey(Report,on_delete=models.CASCADE,related_name='photos')
  photo = models.ImageField(upload_to='reports/photos/%Y/%m/',validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])
  caption = models.CharField(max_length=200, blank=True)

