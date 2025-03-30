from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('organize/', views.organize, name='organize'),
    path('convert/', views.convert, name='convert'),
    path('edit/', views.edit, name='edit'),
    path('security/', views.security, name='security'),
    
    # User Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # User Document Management
    path('my-documents/', views.my_documents, name='my_documents'),
    path('document-history/', views.document_history, name='document_history'),
    path('profile/', views.profile_view, name='profile'),
    path('document/<int:document_id>/delete/', views.delete_document, name='delete_document'),
    path('document/<int:document_id>/toggle-favorite/', views.toggle_favorite, name='toggle_favorite'),
    
    # Individual feature URLs
    path('merge-pdf/', views.merge_pdf_view, name='merge_pdf_view'),
    path('split-pdf/', views.split_pdf_view, name='split_pdf_view'),
    path('compress-pdf/', views.compress_pdf_view, name='compress_pdf_view'),
    path('jpg-to-pdf/', views.jpg_to_pdf_view, name='jpg_to_pdf_view'),
    # New feature page URLs
    path('ocr-pdf/', views.ocr_pdf_view, name='ocr_pdf_view'),
    path('pdf-to-jpg/', views.pdf_to_jpg_view, name='pdf_to_jpg_view'),
    path('pdf-to-word/', views.pdf_to_word_view, name='pdf_to_word_view'),
    path('pdf-to-ppt/', views.pdf_to_ppt_view, name='pdf_to_ppt_view'),
    path('word-to-pdf/', views.word_to_pdf_view, name='word_to_pdf_view'), 
    path('ppt-to-pdf/', views.ppt_to_pdf_view, name='ppt_to_pdf_view'),
    path('rotate-pdf/', views.rotate_pdf_view, name='rotate_pdf_view'),
    path('add-page-numbers/', views.add_page_numbers_view, name='add_page_numbers_view'),
    path('add-watermark/', views.add_watermark_view, name='add_watermark_view'),
    path('protect-pdf/', views.protect_pdf_view, name='protect_pdf_view'),
    path('unlock-pdf/', views.unlock_pdf_view, name='unlock_pdf_view'),
    path('remove-pages/', views.remove_pages_view, name='remove_pages_view'),
    
    # API endpoints
    path('api/merge-pdf/', views.merge_pdf, name='merge_pdf'),
    path('api/split-pdf/', views.split_pdf, name='split_pdf'),
    path('api/compress-pdf/', views.compress_pdf, name='compress_pdf'),
    path('api/ocr-pdf/', views.ocr_pdf, name='ocr_pdf'),
    
    # Convert to PDF
    path('api/jpg-to-pdf/', views.jpg_to_pdf, name='jpg_to_pdf'),
    path('api/word-to-pdf/', views.word_to_pdf, name='word_to_pdf'),
    path('api/ppt-to-pdf/', views.ppt_to_pdf, name='ppt_to_pdf'),
    
    # Convert from PDF
    path('api/pdf-to-jpg/', views.pdf_to_jpg, name='pdf_to_jpg'),
    path('api/pdf-to-word/', views.pdf_to_word, name='pdf_to_word'),
    path('api/pdf-to-ppt/', views.pdf_to_ppt, name='pdf_to_ppt'),
    
    # Edit PDF
    path('api/rotate-pdf/', views.rotate_pdf, name='rotate_pdf'),
    path('api/add-page-numbers/', views.add_page_numbers, name='add_page_numbers'),
    path('api/add-watermark/', views.add_watermark, name='add_watermark'),
    path('api/remove-pages/', views.remove_pages, name='remove_pages'),
    
    # Security
    path('api/unlock-pdf/', views.unlock_pdf, name='unlock_pdf'),
    path('api/protect-pdf/', views.protect_pdf, name='protect_pdf'),
    path('api/sign-pdf/', views.sign_pdf, name='sign_pdf'),
] 