# PDF Editor Application

A full-featured web application for manipulating PDF files, including compression, merging, splitting, and more.

## Features

- PDF Compression with multiple quality options
- PDF Merging for combining multiple documents
- PDF Splitting for extracting specific pages
- Page Removal for removing unwanted pages
- PDF Protection/Encryption
- PDF Unlocking for password-protected files
- Add Watermarks to PDF documents
- Add Page Numbers to PDF documents
- PDF Rotation
- File Format Conversions (PDF to/from Word, PowerPoint, JPG)
- OCR for making scanned documents searchable
- Image to PDF conversion

## Component System

The application uses a modular component system to maintain a consistent user experience across all PDF operations. The following components are available:

### Core Components

1. **Feature Layout (`templates/pdf_tools/components/feature_layout.html`)**
   - Main layout component that includes all the reusable UI elements
   - Provides consistent structure for all PDF operation pages
   - Includes common elements like notifications, progress tracker, settings panel, etc.

2. **Notification System (`templates/pdf_tools/components/notification.html`)**
   - Displays success, error, warning and info messages
   - Can be shown with custom timeout durations
   - Accessible via JavaScript functions: `showSuccessNotification()`, `showErrorNotification()`, etc.

3. **Progress Tracker (`templates/pdf_tools/components/progress_tracker.html`)**
   - Shows real-time progress during PDF processing
   - Includes percentage indicator and detailed status messages
   - Can be controlled via JavaScript functions: `showProgress()`, `hideProgress()`, `updateProgress()`

4. **Settings Panel (`templates/pdf_tools/components/settings_panel.html`)**
   - Provides advanced options for PDF operations
   - Includes file naming, quality settings, and other preferences
   - Can be toggled open/closed and settings retrieved via JavaScript

## Using the Component System

### Integrating the Feature Layout

To use the feature layout component in your feature template:

1. Extend the base template
2. Include the feature layout component in your content block
3. Define your page-specific content in the page_content block

```html
{% extends 'base.html' %}
{% load static %}

{% block content %}
    {% with page_title="Your Feature Title" page_description="Description of your feature" operation_type="your_operation" show_help_button=True show_examples_button=True %}
        {% include "pdf_tools/components/feature_layout.html" with content=content %}
    {% endwith %}
{% endblock %}

{% block page_content %}
    {% with content=block.super %}
        <!-- Your feature-specific HTML goes here -->
    {% endwith %}
{% endblock %}
```

### Using the Notification System

```javascript
// Show a success notification
window.showSuccessNotification('Operation Complete', 'Your PDF has been successfully processed.', 3000);

// Show an error notification
window.showErrorNotification('Error', 'There was a problem processing your file.', 5000);

// Show a warning notification
window.showWarningNotification('Warning', 'This operation may take a while.', 4000);

// Show an info notification
window.showInfoNotification('Info', 'You can also access this feature from your dashboard.', 3000);
```

### Using the Progress Tracker

```javascript
// Show the progress tracker
window.showProgress();

// Update progress manually
window.updateProgress(50, 'Processing', 'Compressing images', '30 seconds remaining', 'Page 5 of 10');

// Simulate progress for demonstrations
window.simulateProgress();

// Hide the progress tracker
window.hideProgress();
```

### Using the Settings Panel

```javascript
// Get the current settings as an object
const settings = window.getSettings();
// Example result: { filename: 'custom-name.pdf', quality: 'high', preserveMetadata: true, ... }

// Toggle the settings panel
document.getElementById('settingsToggle').click();
```

## Development

### Prerequisites

- Python 3.8+
- Django 3.2+
- Required Python packages listed in requirements.txt

### Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`

### Adding a New Feature

1. Create a new template in `templates/pdf_tools/features/` using the component system
2. Add the necessary view function in `pdf_tools/views.py`
3. Add the URL pattern in `pdf_tools/urls.py`
4. Create any required JavaScript for client-side interactions

## License

This project is licensed under the MIT License - see the LICENSE file for details. 