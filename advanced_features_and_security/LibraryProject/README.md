
Custom Permissions and Groups
This application uses custom permissions to control access to model instances.

Permissions:
can_view: Can view instances
can_create: Can create instances
can_edit: Can edit instances
can_delete: Can delete instances

Groups:
Editors: Has can_view, can_create, can_edit permissions
Viewers: Has can_view permission
Admins: Has all permissions



                Security Measures Implemented
                    Settings
DEBUG = False:   Disables debug mode in production.
SECURE_BROWSER_XSS_FILTER:      Activates the browser's XSS filter.
X_FRAME_OPTIONS = DENY:         Prevents the application from being loaded in a frame.
SECURE_CONTENT_TYPE_NOSNIFF:    Prevents the browser from trying to guess the MIME type.
CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE: Ensure cookies are sent over HTTPS only.

                    CSRF Protection
CSRF tokens are included in all form templates to protect against CSRF attacks.
Data Access Security
Views use Django’s ORM to avoid SQL injection and handle user inputs safely.
