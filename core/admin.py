from django.contrib import admin 
from .models import Portfolio, Resume,Project,SocialLink

# Register your models here.

class PortfolioAdmin(admin.ModelAdmin):
    model = Portfolio
    list_display = ['name', 'profession', 'bio','profile_image']  
    

class ResumeAdmin(admin.ModelAdmin):
     model = Resume
     list_display = ['file', 'uploaded_at']
     
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['title', 'description', 'image', 'link']
    
class SociaLinkAdmin(admin.ModelAdmin):
    model = SocialLink
    list_display = ['platform', 'url']
      
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Resume , ResumeAdmin)
admin.site.register(Project , ProjectAdmin)
admin.site.register(SocialLink, SociaLinkAdmin)
